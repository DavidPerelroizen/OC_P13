## Résumé

Site web d'Orange County Lettings.

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

### Explication générale

Le déploiement est le résultat d'une succession d'étapes permettant la mise en service d'une application.
Principales étapes:
1. Compilation du code
2. Tests
3. Création de l'artefact
4. Mise en service finale

Le principe est de mettre en place de manière continue les différentes modifications, améliorations, nouveautés du code
tout en en assurant la qualité: chaque étape est dépendante de la validation de la précédente.

Ici nous utilisons CircleCi pour gérer cette succession d'étapes (pipeline), Docker pour la création de l'artefact, 
et Heroku pour la mise en service de l'application.

### Configuration Docker

1. Créer un compte docker sur hub.docker.com
2. Installer docker desktop et connecter l'application à votre compte docker hub

### Configuration CircleCi

1. Copier le code de l'application dans votre repository Github ou Bitbucket
2. Se connecter à CircleCi avec son compte Github ou Bitbucket
3. Une fois connecté à CircleCi, cliquer sur "Projects" dans le menu de la barre de gauche
4. Sélectionner le repository contenant le code de l'application
5. Cliquer sur `Set-up project`
6. Sélectionner l'option `Fastest` de la pop-up, cela permettra d'utiliser le fichier config.yml déjà présent dans le repository
7. Aller dans projects settings et ajouter les deux variables d'environnement suivantes:
   a. DOCKERHUB_PASSWORD: votre mot de passe dockerhub 
   b. DOCKERHUB_USERNAME: votre username dockerhub

### Configuration Heroku

1. Créer un compte sur Heroku
2. Créer une nouvelle application
3. Dans le fichier `settings.py` remplacer oc-lettings-111 par le nom de votre app heroku dans le code ci-dessous:
    ```bash
   if IS_HEROKU:
    ALLOWED_HOSTS = ['oc-lettings-111.herokuapp.com']
    ```
4. Sur Heroku, aller dans Accounts settings>API Key> Reveal
5. Copier cette clé puis aller dans les variables d'environnement de CircleCi
6. Créer une nouvelle variable d'environnement `HEROKU_API_KEY`
7. Coller la clé copiée
8. Créer également dans Circleci une variable d'environnement `HEROKU_APP_NAME` et renseigner le nom de votre application heroku

### Heroku postgresql configuration

1. Dans votre application sur Heroku, cliquer sur `Ressources`
2. Sélectionner la base de donnée postgresql
3. Cliquer sur `Settings`
4. Cliquer sur `View credentials`
5. Reporter les différentes valeurs dans le fichier `settings.py` de l'application django dans le code ci-dessous:
   ```bash
   else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'heroku db name',
            'USER': 'herok db user',
            'PASSWORD': 'heroku db password',
            'HOST': 'heroku db host',
            'PORT': 'herolu db port',
        }
    }
    ```
### Migration des données vers la base heroku

1. Dans `settings.py` commenter les lignes ci-dessous:
   ```bash
   if not IS_HEROKU:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'oc-lettings-site.sqlite3'),
        }
    }
    else:
   ```
2. Exécuter successivement les commandes ci-dessous dans le terminal:
   `python manage.py makemigrations`
   `python manage.py makemigrations`
   `python manage.py loaddata user.json`
   `python manage.py loaddata profiles.json`
   `python manage.py loaddata address.json`
   `python manage.py loaddata lettings.json`
3. Décommenter les lignes commentées à l'étape 1

La base Postgresql Heroku est prête à l'usage. 

## Lancer le site

### En local

Dans le terminal, exécuter la commande `python manage.py runserver` et se connecter à l'URL http://127.0.0.1:8000/

### Sur Heroku

Se connecter à son compte Heroku, ouvrir la page de l'application, cliquer sur `Open app`

### Via docker desktop

1. Ouvrir docker desktop
2. Sélectionner l'image de l'application et effectuer un pull pour en avoir la dernière version
3. Cliquer sur `Run`
4. Dans les "Optional settings", renseigner 8000 en tant que "Host Port"
5. Cliquer sur `Run`
6. Une fois le container lancé, aller dans les "Action" et cliquer sur "Open with browser"

## Surveillance de l'application via Sentry

### Configuration

1. Créer un compte sur Sentry
2. Créer un projet
3. Récupérer la clé DSN du projet
4. Dans `settings.py` coller la clé dsn du projet dans le code ci-dessous:
    ```bash
   sentry_sdk.init(
    dsn="la clé DSN de votre projet",
   # ...
   )
    ```

### Test

1. Exécuter l'application via heroku
2. Rentrer l'URL `https://<votre application>.herokuapp.com/sentry-debug/` dans le navigateur
3. Une erreur 500 se produit
4. Une issue apparaît dans votre projet sentry