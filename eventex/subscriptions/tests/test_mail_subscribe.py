from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Leandro Silva', cpf='12345678911',
                    email='ldfsilva@gmail.com', phone='8179031476')
        self.resp = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = '[Eventex] Confirmação de Inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'ldfsilva@gmail.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['ldfsilva@gmail.com', 'ldfsilva@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Leandro Silva',
            '12345678911',
            'ldfsilva@gmail.com',
            '8179031476'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
