
# Eventex  
Sistema de Eventos desenvolvido no curso Welcome to the Django

[![Build Status](https://travis-ci.org/paulo-romano/eventex.svg?branch=master)](https://travis-ci.org/paulo-romano/eventex)  [![Code Climate](https://codeclimate.com/github/paulo-romano/eventex/badges/gpa.svg)](https://codeclimate.com/github/paulo-romano/eventex)


Exemplo: http://eventex-pauloromano.herokuapp.com/

 
## Como desenvolver? 
1. Clone o repositório; 
2. Crie um virtualenv com Python 3.5; 
3. Ative o virtualenv; 
4. Instale dependências (requirementes.txt); 
5. Configure a instancia com um arquivo .env; 
6. Execute os teste. 
 
```console 
git clone https://github.com/paulo-romano/eventex.git wttd 
cd wttd 
python -m venv .wttd 
source ./wttd/bin/activate 
pip install -r requirements.txt 
cp contrib/env-sample .env 
python manage.py test 
``` 
 
## Como fazer o deploy no Heroku 
1. Crie uma instância no heroku 
2. Envie as configurações para o Heroku 
3. Defina uma SECRET_KEY segura para a instancia. 
4. Defina DEBUG = False 
5. Configure o serviço de e-mail 
 
```Console 
heroku create minhainstancia 
heroku config:push 
heroku config:set SECRET_KEY=python contrib/secret_gen.py 
heroku config:set DEBUG=False 
#configura variáveis para o e-mail 
git push heroku master --force
```
