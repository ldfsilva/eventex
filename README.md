# Eventex

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/ldfsilva/eventex.svg?branch=master)](https://travis-ci.org/ldfsilva/eventex)
[![Code Health](https://landscape.io/github/ldfsilva/eventex/master/landscape.svg?style=flat)](https://landscape.io/github/ldfsilva/eventex/master)


## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env.
6. Execute os testes.

```console
git clone https://github.com/ldfsilva/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy no heroku?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False.
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
#configurar email
git push heroku master --force
```

## Como testar o ambiente de desenvolvimento no docker?

1. Clone o repositório.
2. Acesse o repositório wttd.
3. Crie uma imagem docker.
4. Execute o container da imagem wttd.

Após este passo você poderá acessar a página no endereço IP da sua docker-machine na porta 8000.

```console
git clone git@github.com:ldfsilva/eventex.git wttd
cd wttd
docker build -t wttd .
docker run --rm --name wttd_app -it --publish=8000:8000 wttd bash
```

Presume-se que você ja tenha docker instalado, a versão testada foi a seguinte:

```console
$ docker -v
Docker version 1.10.3, build 20f81dd
$
$ docker-machine -v
docker-machine version 0.6.0, build e27fb87
$
```