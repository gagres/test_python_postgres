# Python, Excel and Postgres

This repository was created to test a [python](https://www.python.org/) to read some data of an excel file using [xlrd](http://xlrd.readthedocs.io/en/latest/api.html) and compare the result with a [postgres](https://www.postgresql.org/) database records

## Getting Started

Clone the repository

```
git clone https://github.com/gagres/test_python_postgres
```

Inside the root project folder, run the command

```
./config.sh
```

**OBS:** When you run the configuration file, the postgres server container will already be up-to-date

## Container initialization

1. **Postgres Container:** `docker run --name pos-server -d postgres-image`
	
    1. If you want to enter in postgres cli, before start postgres container run `docker run --rm -it --link pos-server:server postgres psql -h server -U admin -d admin`
	
    2. Put the password (default: **admin**)

2. **Python Container:** `docker run --rm -it --link pos-server:server python-image`
	
    1. This will just read an excel file, compare with values saved on postgre database initialized before and add the new ones that aren't there yet.