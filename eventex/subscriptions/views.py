from django.conf import settings
from django.core import mail
from django.core import signing
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'subscriptions/subscription_form.html',
                  {'form' : SubscriptionForm()})


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
         return render(request, 'subscriptions/subscription_form.html',
                      {'form': form})

    subscription = Subscription.objects.create(**form.cleaned_data)

    _send_mail('[Eventex] Confirmação de Inscrição',
               settings.DEFAULT_FROM_EMAIL,
               subscription.email,
               'subscriptions/subscription_email.txt',
               {'subscription': subscription})

    signer = signing.Signer()
    pk_signed = signer.sign(subscription.pk)

    return HttpResponseRedirect(r('subscriptions:detail', pk_signed))


def detail(request, pk):
    try:
        signer = signing.Signer()
        try:
            pk_unsigned = signer.unsign(pk)
        except signing.BadSignature:
            raise Http404
        subscription = Subscription.objects.get(pk=pk_unsigned)

    except Subscription.DoesNotExist:
        raise Http404

    return render(request, 'subscriptions/subscription_detail.html',
                  {'subscription': subscription})


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])