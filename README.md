# Rimornesia Billing Backend

> Rimornesia mountain system

## Build Setup

``` bash
# install dependencies
$ pip install -r requirements.txt

# create uploads directory on app
$ mkdir uploads

# run flask
$ flask run 

# or run scripts
$ . bin/run.sh

# db migration
$ python -m app.migrations.db_migration

# or run scripts
$ . bin/migrate.sh

# update pip package
$ pip freeze > requirements.txt
```
