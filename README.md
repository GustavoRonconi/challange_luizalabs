<br />
<p align="center">
  <a href="https://medium.com/luizalabs">
    <img src="https://cdn-images-1.medium.com/max/1200/1*IVax5__p6o5n1YPgugiqGQ.png" alt="Logo" width="300" height="300">
  </a>


  <h3 align="center">LuizaLabs - Challange</h3>

  <p align="center">
    API developed for test purposes.
  </p>
  <p align="left">
    Você pode acessar a documentação da API neste <a href="https://challangeluizalabs.herokuapp.com/api/docs/">LINK</a>. 👈
  </p>
  <p align="left">
    Você pode obter a collection do postman neste <a href="https://www.getpostman.com/collections/679aefc1251a12f9c4f2">LINK</a>. 👈
  </p>
</p>



### Construído a partir de:

* [Django](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)
* [Postgrees](https://postgrees.org)

## Features Extras
- CI/CD completo utilizando Github Actions 💥.

## Iniciando

Crie um ambiente python-3.9 e instale as dependências, presume-se neste ponto que você já tenha o Postgres instalado no seu ambiente.

### Pré-requisitos
* django==3.1.5
* djangorestframework==3.12.2
* djangorestframework_simplejwt==4.6.0
* pytest-django==4.1.0
* pytest-cov==2.8.1
* pytest==5.4.0
* django-heroku==0.3.1
* requests==2.25.1
* gunicorn==20.1.0
* pyyaml==5.4.1
* uritemplate==3.0.1
* django-rest-swagger==2.2.0

### Instalação
1. Clone o projeto e na pasta raiz execute:
   ```bash
   pip install -r requirements.txt
   ```

2. Rode o seguinte comando na pasta raiz:
    ```bash
    make install
    ```


## Utilização
1. Para iniciar a API no ambiente de desenvolvimento execute:
   ```python
   python manage.py runserver 
   ```
2. Credenciais para autenticação:
   - username: gustavoronconi
   - password: gustavo_luizalabs

