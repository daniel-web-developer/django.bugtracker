# Bugtracker - Full-stack CRUD app

## Introduction

Welcome to BugTracker, a safe open-source CRUD app complete with authentication.


## Features

### Sign up/in/out

Users can create an account and log in/out.


### Create, read, update, and delete (CRUD) operations

A user can create projects and tickets that will be associated to the user's profile, meaning only the user can edit and delete the projects/tickets, or even view them if they are set to private.


### Security

I've extensively tested the app and everything you can do with it.

- Only the user can create a project/ticket as that user.
- Only the owner of a project/ticket set to private can see, edit, and delete them.
- Authentication system provided by Django;
- Unauthorised users (who try to access something they can't, like a private project/ticket, etc.) will be redirected to a [403 page](https://en.wikipedia.org/wiki/HTTP_403);


### Search functionality

Users can use the search bar in order to filter tickets according to their titles.


## How to run it

To run it on your machine or deploy it to production on the cloud, you're gonna need to install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/).

**This teaches you to run the development build. If you want to use the production environment, always type `-f docker-compose.prod.yml` after `compose`, e.g. `$ docker compose -f docker-compose.prod.yml...`**

### Building the containers

1. Clone the repository to a folder;
2. Type `$ docker compose up -d --build` to build and run the containers.
3. If you find an error, `$ docker compose logs -f` will show you the logs.
4. To execute any Django command, type `$ docker compose exec web ${COMMAND HERE}`. Basically, `exec` is a Docker command to execute a command inside a running container, and `web` is the container you're executing the command in. To see the name of each container just open one of the `docker-compose.yml` files on the root folder of the project.
5. To bring the containers down, type `$ docker compose down -v`. **The -v flag also removes the volumes.**

### Additional configurations for production

- You'll need to run the migrations the first time you start them with `$ docker compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput`.
- You'll also have to `collectstatic` so your static files (CSS, JS, images, etc.) will be accessible to Nginx (so it can serve them to the user). Type `$ docker compose -f docker-compose.p^Cd.yml exec web python manage.py collectstatic --noinput`.


## Further reading:
I'll add some blog articles here when I post them.

