# Dokcer-Django Starter
This repository has been created to easily start dockerizing Django projects

  ## Server Dependencies
  - Python: v3.12.2 slim
  - Database: Postgres v16.1 alpine3.19
  - Django: v4.2.9
  - psycopg: v3.1.18

## Start Development Containers
```
docker compose up [--build]
```

### Create The Database Secret File
```shell
echo THE_DATABASE_PASSWORD > ./secrets/db/password.txt
```
> **Note:** always remember to remove the secret files on production
