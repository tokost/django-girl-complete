# Complete Django Girls Tutorial

This repository contains the code that one would eventually have were they to go through the [Django Girls tutorial](https://tutorial.djangogirls.org/en/).

[![CircleCI](https://circleci.com/gh/NdagiStanley/django_girls_complete.svg?style=svg)](https://circleci.com/gh/NdagiStanley/django_girls_complete)

## Differences

Expressing my authorial rights, some things are a bit different from the tutorial:

- A `Log in` and `Log out` links on the page header
- A `Back` link within the *blog-detail* and *blog-edit* pages
- A more extensive `.gitignore` file
- A `.editorconfig` file
- An additional python package in the requirements.txt: `pycodestyle`

- Within `mysite/settings.py`,

  - Use of `Africa/Nairobi` as my *TIME_ZONE*
  - Use of `en-us` as my *LANGUAGE_CODE*
  - Addition of `0.0.0.0` and `.herokuapp.com` to the *ALLOWED_HOSTS* list

<<<<<<< HEAD
https://www.postgresql.org/download/

## Setup

$ python -m venv myvenv
$ . myvenv/scripts/activate
$ python.exe -m pip install --upgrade pip
$ python manage.py migrate
$ pip freeze
$ python manage.py createsuperuser
$ python manage.py runserver

In a python virtual environment, run:

$ pip install -r requirements.txt
$ pip install django-allauth
$ pip install psycopg2
$ python manage.py migrate blog
$ python manage.py createsuperuser (to create user that you'll use to log in)
=======
## Setup

In a python virtual environment, run:

- `pip install -r requirements.txt`
- `python manage.py migrate blog`
- `python manage.py createsuperuser` (to create user that you'll use to log in)
>>>>>>> adacb8cb4b7e3a474ad28ffe9bc5d5b391f378eb

### Run the application

```bash
python manage.py runserver
```

Now, you are good to go. Your blog is ready.

### Test

```bash
python manage.py test
```

### Docker
NB: The app instance will run off the a preset admin user as set in [init.sh](/init.sh).

To spin up the application using docker, ensure that Docker is installed. Then run:

```bash
docker-compose up
```

Or in detached mode:

```bash
docker-compose up -d
```

The application will be live at [0.0.0.0:8000](0.0.0.0:8000)

### Log in/ out

- Click on `Log in` (you'll be redirected to the Admin page)
- On the admin page, fill in the credentials of the superuser created in [Setup](#setup)
- Click on the *Log in* button (You'll be redirected back to the page)
- Click on `Log out` to log out.

### Blog entry

- Log in
- Click on the `+` button, enter the _**title**_ and _**text**_
- Finally hit the `Save` button

Django SQLite to PostgreSQL database migration
https://medium.com/djangotube/django-sqlite-to-postgresql-database-migration-e3c1f76711e1 

<<<<<<< HEAD
1. Vytvoríme si zálohu celej databázy dumpdata zariadenia SQLite.
najprv musíte urobiť zálohu celej SQLiteDB do form=atu JSON pomocou nižšie uvedeného príkazu
~~~
python manage.py dumpdata > whole.json
~~~

2. Nainštalujeme PostgreSQL z tejto adresy:

https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

3. Pomocou PostgreSQL Shell-u (psql) ktorý sa nachádza pri inštalácii PostgreSQL vytvoríme DB **my_db** a prístupové údaje:
~~~
Server [localhost]:
Database [postgres]:
Port [5432]:
Username [postgres]:
Password for user postgres:

psql (16.2)
WARNING: Console code page (852) differs from Windows code page (1250)
         8-bit characters might not work correctly. See psql reference
         page "Notes for Windows users" for details.
Type "help" for help.

postgres=# 
~~~
 
4. Zadáme údaje pre konektivitu na PostgreSQL DB do setting.py :
~~~
=======
1. Vezmite si zálohu celej databázy dumpdata zariadenia SQLite.
najprv musíte urobiť zálohu celej DB pomocou nižšie uvedeného príkazu
~~~
python manage.py dumpdata > whole.json
~~~
2. Vytvorte Postgres DB pomocou používateľa a hesla.

settings.py
>>>>>>> adacb8cb4b7e3a474ad28ffe9bc5d5b391f378eb
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'my_db',
        'USER' : 'postgres',
        'PASSWORD' : '03091953-Tomo',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}
<<<<<<< HEAD
~~~
 
4. Nainštaluje konektor PostgreSQL DB pre Python

Psycopg je najpopulárnejší databázový adaptér PostgreSQL pre programovací jazyk Python . Jeho hlavnými vlastnosťami sú úplná implementácia špecifikácie Python DB API 2.0 a bezpečnosť vlákien (viacero vlákien môže zdieľať rovnaké pripojenie). https://docs.yugabyte.com/preview/reference/drivers/python/postgres-psycopg2-reference/ 
~~~
$ pip install psycopg2
~~~
5. Odstráňte všetky súbory migrácie napr. manualne, pretože nepotrebujeme všetky staré migrácie.

6. Namiesto toho vytvoríme jeden súbor migrácie na aplikáciu.
~~~
$ python manage.py makemigrations
$ python manage.py migrovať
~~~
7. Teraz odstráňte typy obsahu (povinné kroky), inak budete mať krásne miliardy chýb
~~~
$ python manage.py shell

>>> from django.contrib.contenttypes.models import ContentType
>>> ContentType.objects.all().delete()
>>> ^Z
=======

Psycopg je najpopulárnejší databázový adaptér PostgreSQL pre programovací jazyk Python . Jeho hlavnými vlastnosťami sú úplná implementácia špecifikácie Python DB API 2.0 a bezpečnosť vlákien (viacero vlákien môže zdieľať rovnaké pripojenie). https://docs.yugabyte.com/preview/reference/drivers/python/postgres-psycopg2-reference/ 
~~~
pip install psycopg2
~~~
3. Odstráňte všetky súbory migrácie napr. manualne, pretože nepotrebujeme všetky staré migrácie.

4. Namiesto toho vytvoríme jeden súbor migrácie na aplikáciu.
~~~
python manage.py makemigrations
python manage.py migrovať
~~~
5. Teraz odstráňte typy obsahu (povinné kroky), inak budete mať krásne miliardy chýb
~~~
shell python manage.py
z django.contrib.contenttypes.models importujte ContentType
ContentType.objects.all().delete()
>>>>>>> adacb8cb4b7e3a474ad28ffe9bc5d5b391f378eb
~~~

6. Importujte prípravok pomocou údajov o zaťažení.
Jedným z hlavných krokov je deaktivácia všetkých signálov v projektoch, inak získate jedinečné obmedzenie alebo už vytvorený objekt.
~~~
<<<<<<< HEAD
$ python manage.py loaddata whole.json
~~~
To je všetko, napriek varovaniu, že adresár so statickými súbormi neexistuje. Toto upozornenie nás len informuje, že zadaný adresár pre statické súbory neexistuje, čo môže, ale nemusí byť relevantné pre našu aktuálnu operáciu.

Údaje z SQLite sa úspešne presunuli do PostgreSQL, čo si môžeme overiť v phAdmin4 alebo nainštalovaním rozšírenia PostgreSQL od Chris Kolkman-a do VS-Code.

GIT - GITHUB

$ git init
$ git branch -m master main
$ git remote add origin https://github.com/tokost/django-girl-complete.git
$ 
$ git pull origin main --allow-unrelated-historiesgit remote add dgc-gh https://github.com/tokost/django-girl-complete.git
$ git push -u origin main

$ git status
$ git add .
$ git commit -m "Popis vykonanej cinnosti"

Po vyriešení konfliktov musíte dokončiť zlúčenie potvrdením zmien. Nasleduj tieto kroky:

1. Pridajte konfliktné súbory do pracovnej oblasti:
~~~
git add README.md blog/migrations/0001_initial.py
~~~

2. Odovzdajte zmeny na dokončenie zlúčenia:
~~~
git commit -m "Merge conflicting changes from remote repository"
~~~
3. Ak správa o odovzdaní vyzerá dobre, môžete svoje zmeny vložiť:
~~~
git push origin main
~~~
Toto presunie zlúčené zmeny do main vetvy na vzdialenom úložisku.

Po vyriešení konfliktov a potvrdení zlúčenia by vaša lokálna pobočka mala byť synchronizovaná so vzdialenou mainpobočkou a mali by ste byť schopní bez problémov preniesť svoje zmeny. 

=======
python manage.py loaddata whole.json
~~~
to je všetko, úspešne ste presunuli údaje z SQLite do Postgres pomocou zariadení
použite nižšie uvedený príkaz na načítanie údajov do DB z príslušenstva
>>>>>>> adacb8cb4b7e3a474ad28ffe9bc5d5b391f378eb

IMPLEMENTACIA all-auth

1. Nainštalovať
~~~
pip install django-allauth
~~~
2. Urobiť úpravy v settings.py
~~~
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
~~~

~~~
# Specify the context processors as follows:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Already defined Django-related contexts here

                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    ...
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
    ...
]

INSTALLED_APPS = [
    ...
    # The following apps are required:
    'django.contrib.auth',
    'django.contrib.messages',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.agave',
    'allauth.socialaccount.providers.amazon',
    'allauth.socialaccount.providers.amazon_cognito',
    'allauth.socialaccount.providers.angellist',
    'allauth.socialaccount.providers.apple',
    'allauth.socialaccount.providers.asana',
    'allauth.socialaccount.providers.auth0',
    'allauth.socialaccount.providers.authentiq',
    'allauth.socialaccount.providers.baidu',
    'allauth.socialaccount.providers.basecamp',
    'allauth.socialaccount.providers.battlenet',
    'allauth.socialaccount.providers.bitbucket_oauth2',
    'allauth.socialaccount.providers.bitly',
    'allauth.socialaccount.providers.box',
    'allauth.socialaccount.providers.cilogon',
    'allauth.socialaccount.providers.clever',
    'allauth.socialaccount.providers.coinbase',
    'allauth.socialaccount.providers.dataporten',
    'allauth.socialaccount.providers.daum',
    'allauth.socialaccount.providers.digitalocean',
    'allauth.socialaccount.providers.dingtalk',
    'allauth.socialaccount.providers.discord',
    'allauth.socialaccount.providers.disqus',
    'allauth.socialaccount.providers.douban',
    'allauth.socialaccount.providers.doximity',
    'allauth.socialaccount.providers.draugiem',
    'allauth.socialaccount.providers.drip',
    'allauth.socialaccount.providers.dropbox',
    'allauth.socialaccount.providers.dwolla',
    'allauth.socialaccount.providers.edmodo',
    'allauth.socialaccount.providers.edx',
    'allauth.socialaccount.providers.eventbrite',
    'allauth.socialaccount.providers.eveonline',
    'allauth.socialaccount.providers.evernote',
    'allauth.socialaccount.providers.exist',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.feedly',
    'allauth.socialaccount.providers.figma',
    'allauth.socialaccount.providers.fivehundredpx',
    'allauth.socialaccount.providers.flickr',
    'allauth.socialaccount.providers.foursquare',
    'allauth.socialaccount.providers.frontier',
    'allauth.socialaccount.providers.fxa',
    'allauth.socialaccount.providers.gitea',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.gitlab',
    'allauth.socialaccount.providers.globus',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.gumroad',
    'allauth.socialaccount.providers.hubic',
    'allauth.socialaccount.providers.instagram',
    'allauth.socialaccount.providers.jupyterhub',
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.lemonldap',
    'allauth.socialaccount.providers.line',
    'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.linkedin_oauth2',
    'allauth.socialaccount.providers.mailchimp',
    'allauth.socialaccount.providers.mailru',
    'allauth.socialaccount.providers.mediawiki',
    'allauth.socialaccount.providers.meetup',
    'allauth.socialaccount.providers.miro',
    'allauth.socialaccount.providers.microsoft',
    'allauth.socialaccount.providers.naver',
    'allauth.socialaccount.providers.nextcloud',
    'allauth.socialaccount.providers.notion',
    'allauth.socialaccount.providers.odnoklassniki',
    'allauth.socialaccount.providers.openid',
    'allauth.socialaccount.providers.openid_connect',
    'allauth.socialaccount.providers.openstreetmap',
    'allauth.socialaccount.providers.orcid',
    'allauth.socialaccount.providers.patreon',
    'allauth.socialaccount.providers.paypal',
    'allauth.socialaccount.providers.persona',
    'allauth.socialaccount.providers.pinterest',
    'allauth.socialaccount.providers.pocket',
    "allauth.socialaccount.providers.questrade",
    'allauth.socialaccount.providers.quickbooks',
    'allauth.socialaccount.providers.reddit',
    'allauth.socialaccount.providers.robinhood',
    'allauth.socialaccount.providers.salesforce',
    'allauth.socialaccount.providers.sharefile',
    'allauth.socialaccount.providers.shopify',
    'allauth.socialaccount.providers.slack',
    'allauth.socialaccount.providers.snapchat',
    'allauth.socialaccount.providers.soundcloud',
    'allauth.socialaccount.providers.spotify',
    'allauth.socialaccount.providers.stackexchange',
    'allauth.socialaccount.providers.steam',
    'allauth.socialaccount.providers.stocktwits',
    'allauth.socialaccount.providers.strava',
    'allauth.socialaccount.providers.stripe',
    'allauth.socialaccount.providers.telegram',
    'allauth.socialaccount.providers.trainingpeaks',
    'allauth.socialaccount.providers.trello',
    'allauth.socialaccount.providers.tumblr',
    'allauth.socialaccount.providers.twentythreeandme',
    'allauth.socialaccount.providers.twitch',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.twitter_oauth2',
    'allauth.socialaccount.providers.untappd',
    'allauth.socialaccount.providers.vimeo',
    'allauth.socialaccount.providers.vimeo_oauth2',
    'allauth.socialaccount.providers.vk',
    'allauth.socialaccount.providers.wahoo',
    'allauth.socialaccount.providers.weibo',
    'allauth.socialaccount.providers.weixin',
    'allauth.socialaccount.providers.windowslive',
    'allauth.socialaccount.providers.xing',
    'allauth.socialaccount.providers.yahoo',
    'allauth.socialaccount.providers.yandex',
    'allauth.socialaccount.providers.ynab',
    'allauth.socialaccount.providers.zoho',
    'allauth.socialaccount.providers.zoom',
    'allauth.socialaccount.providers.okta',
    'allauth.socialaccount.providers.feishu',
    ...
]

MIDDLEWARE = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",

    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
)

SITE_ID = 1

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}
~~~

3. Doplnit do urls.py projektu t.j. v adresári mysite
~~~
urlpatterns = [
    ...
    path('accounts/', include('allauth.urls')),
    ...
]
~~~

4. Vykonť migráciu modelu DB
~~~
python manage.py migrate
~~~

5. Ošetrenie poskytovateľa socialných sietí

Pre každého poskytovateľa založeného na protokole **OAuth** buď pridajte SocialApp( socialaccount aplikáciu) obsahujúcu požadované poverenia klienta, alebo sa uistite, že sú nakonfigurované prostredníctvom nastavenia SOCIALACCOUNT_PROVIDERS[<provider>]['APP'](pozri príklad vyššie). Ak ho nepoužívame tak poskytovatelov účtov na socialiných sieťách netreba uviesť ani v settings.py v časti INSTALED_APPS

6. Po inštalácii a doplnkoch

V koreňovom adresári Django vykonajte príkaz uvedený nižšie a vytvorte databázové tabuľky:
~~~
python manage.py migrate
~~~

7. Download zip z django-allaut na adrese https://github.com/pennersr/django-allauth  

Po rozbalení zip-u otvoriť priečinok allauth, následne templates a account.
Celý priečinok account nakopírujeme a vložíme ho do adresára templates v našej aplikácii blog

8. Uskutočníme test funkčnosti zadaním adresresy do URL
~~~
http://127.0.0.1:8000/accounts/login/
~~~
Ak zadame naše prihlasovacie údaje dostaneme síce chybu a v URL sa nám to prestaví na /profile
ale o to teraz nejde. Skúšame manuálne funkciu inštalcie a tak miesto profile môžeme zadať /logout t.j. URL http://127.0.0.1:8000/accounts/logout/
Po stlačení tlačítka **Sign Out** sa dostaneme na našu domovskú stránku.

9. Ďalšia ev. úprava v settings.py

Ak sme mali v settings.py LOGIN_URL = '/admin/' tak ho teraz okomentujeme a miesto neho napíšeme
~~~
LOGIN_REDIRECT_URL = '/posts'
~~~

MANUALNE VOLANIE ŠABLÓN all-auth
http://127.0.0.1:8000/accounts/logout/
http://127.0.0.1:8000/accounts/login/
http://127.0.0.1:8000/accounts/password/reset/
http://127.0.0.1:8000/accounts/signup/

Ak nepoužijeme pri prihlasovaní sa meno ale mailovú adresu, tak musím do **settings.py**
 toto pridat:
# Pridane kvoli prihlasovaniu sa miesto mena mailom
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_UNIQUE = True
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory' lebo to suvisi s overenim na mail serveri

Ošetrenie registracie ak by by bol zapnutý DEBAG alebo ak by bol použitý mailový server
# Pokial nastane pri registracii pomocou mailu chyba moy eto suvisiet
# s pouzivanim mailoveho servera. Osetri sa to pridanim tohoto v pripade
# osetrenia DEBUGU:
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

Čsato používanou technologiou pri registrácii je okrem overovania (verifikovnia) mailovej adresy
aj odoslanie oznamu či je mailová adresa v poriadku a pod. Použivajú sa na to najmä súbory 
/account/email/email_confirmation_message.txt a /account/email_confirm.html

ZÁVEROM:
* knižnica all-auth ponúka ešte aj ďalšie nástroje na autentifikáciu a zabezpečenie ochrany pri manipulácii s citlivými údajmi ako je mailová adresa, uživatelské meno, prihlasovacie heslo a pod
* v tejto aplikácii boli na prihlsovanie a odhlasovanie použité okrem šablón all-auth ešte dialógy admina volané cez http://127.0.0.1:8000/admin/ . Bolo to urobené kvôli názornosti že prostriedky admina ponúkajú na rozdiel od all-auth veľmi obmedzené možnosti
* v cielovej verzii webovej aplikácii by preto bolo žiaduce použiť na prihlasovanie a odhlasovanie ktoré je zabudované do banera v hornom pravom rohu tiež prostriedky ktoré nám ponúka all-auth a ktoré môžeme vidieť ak manuálne zadáme URL http://127.0.0.1:8000/accounts/logout resp. http://127.0.0.1:8000/accounts/login

Nahradenie admin s all-auth pre login a logout urobíme zámenou týchto riadkov
v súbore base.html:

pre login
<h3> <a href="/admin/login/?next=/">Log in</a> </h3>
za
<h3> <a href="ccounts/login/">Log in</a> </h3>

pre logout
<h3> {{ request.user }} | <a href="/admin/logout?next=/">Log out</a> </h3>
za
<h3> {{ request.user }} | <a href="accounts/logout/">Log out</a> </h3>