# Dokcer-Django Starter
This repository has been created to easily start dockerizing Django projects

### Server Dependencies
| # | Dependency | Version | Image Type |
|---|------------|---------|------------|
| Language | Python | v3.12.2 | slim |
| Framework | Django | v4.2.9 | |
| Database | Postgres | v16.1 | alpine3.19 |
| Database Driver | psycopg | v3.1.18 | |
| WSGI Server | Gunicorn | 21.2.0 | |
| Web Server | nginx | v1.25.3 | |

### Start Development Containers
```
docker compose up [--build]
```

### Create The Database Secret File
```shell
echo THE_DATABASE_PASSWORD > ./secrets/db/password.txt
```
> **Note:** always remember to remove the secret files on production

<br/>

## Production Setup
1. Migrate The Database
```shell
docker compose -f compose.prod.yaml exec <CONTAINER_NAME> python manage.py migrate
```

2. Create a Superuser
```shell
docker compose -f compose.prod.yaml exec <CONTAINER_NAME> python manage.py createsuperuser
```

3. Collect Static Files
```shell
docker compose -f compose.prod.yaml exec <CONTAINER_NAME> python manage.py collectstatic
```

## Start Production Containers
```
docker compose -f compose.prod.yaml up [--build] [-d]
```