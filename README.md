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

