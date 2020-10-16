# Simple Portfolio
Practices django application is built with postgres, docker and nginx

This project is considered finish, However there are some enhancements like Web UI, User login, etc. that is nice to be implemented as well later. Please take a look at [TODO.md](./TODO.md) document for details.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes.

### Prerequisites

1. Clone repository: `git clone https://github.com/rojekapp/django-postgres-simple-portfolio.git`
2. Install Postgresql: [Postgresql](https://www.postgresql.org/download/)
3. Run database migrations: refer below
4. Install Docker Desktop: [Docker Desktop](https://www.docker.com/products/docker-desktop)

### Run Project

Running project:

```$xslt
docker-compose up -d --build
```
### Migrations

When running in Local, you need to run the db-migrations to setup the app's database for your local machine.

1. Run `docker-compose exec web python manage.py migrate`
2. Run `docker-compose exec web python manage.py collectstatic`

### Create Super User

Run `docker-compose exec web python manage.py createsuperuser --username USERNAME`

### Docker Stop 

Run `docker-compose down -v`

### Production 

1. Run `docker-compose -f docker-compose.prod.yml up -d --build`
2. Run `docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput`
3. Run `docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear`

## Directory Structure

This repository is organized in the following directory structure.

```
djang-postgres-simple-portfolio
|-- app                                    # Contains static-files, UI etc.
|   |-- env                                # Development Environment (Django)
|   |-- jobs                               # Delivery layer of the app
|   |   |-- migrations                     # Migrations log 
|   |   |-- static                         # Static files for jobs application
|   |   |   |-- jobs                        
|   |   |-- templates                      # UI related code
|   |   |-- <other_entities>.py            # Other python func 
|   |-- mediafiles                         # Contains Images
|   |-- simple_portfolio                   # Use Case of application
|   |-- Dockerfile                         # Development Docker File
|   |-- Dockerfile.prod                    # Production App Docker File
|   |-- entrypoint.prod.sh                 # Command when docker-compose run 
|   |-- Dockerfile.prod                    # Command production for docker-compose run
|   |-- manage.py                          # Django default file system
|   |-- requirements.txt                   # Applications requirements
|-- .env.dev                               # Environment Variables for development
|-- .env.prod                              # Environment Variables for production
|-- .env.prod.db                           # Environment Variables for db production
|-- docker-compose.yml                     # 
|-- docker-compose.prod.yml                # 
```
## Contributing

Your contributions are welcome!

Please take a look at [CONTRIBUTING.md](./CONTRIBUTING.md) document for details.

## Tech Stacks

- Django
- Postgresql
- Nginx
- Docker