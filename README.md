# Bugtracker - Full-stack CRUD app

## Introduction

Welcome to BugTracker, a safe open-source CRUD app complete with authentication.

## Features

### Sign up/in/out

Users can create an account (I've disabled it on the website I'm hosting since I don't have how to moderate what users post and, most importantly, I don't have enough storage to release it as an actual app), and log in/out. This is safely handled by Django so you don't need to worry about hashing and salting passwords, or worse, storing them in plain-text **(NEVER DO THIS)**.


### Create, Read, Update, Delete functionality

A user can create projects and tickets that will be associated to the user's profile, meaning only the user can edit and delete the projects/tickets, or even view them if they are set to private.


### Security

I've extensively tested the app and everything you can do with it.

- Only the user can create a project/ticket as that user.
- You can set tickets to private, and only you will be able to access them if set as private.
- Authentication system provided by Django;
- Unauthorised users (who try to access something they can't, like a private project/ticket, etc.) will be redirected to a [403 page](https://en.wikipedia.org/wiki/HTTP_403);

