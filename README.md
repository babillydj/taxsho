### Installation
Tax Calculator requires [Docker](https://www.docker.com/), [Python](https://www.python.org/), and [PostgreSQL](https://www.postgresql.org/) to run.

open terminal and start Docker. you can access https://www.localhost:8000/ after process finished but without data

```sh
$ cd taxCalculator
$ docker-compose up
```

Access docker web container to run all commands for Django requirements (run this commands in new terminal, docker need to keep running to run this).

```sh
$ docker exec -it taxcalculator_web_1 /bin/bash
```

### Manage Data
Initial migrate and load data.

```sh
$ python manage.py migrate
$ python manage.py loaddata product.json
```

Create super user for user data requirements or for login https://www.localhost:8000/admin content management system 

```sh
$ python manage.py createsuperuser
```

### Automated Test
Unit test for API
```
python manage.py test
```

### API Documentation
open https://www.localhost:8000/doc after all above process