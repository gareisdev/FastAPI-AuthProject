# FastAPI Auth Project

## Introduction

This is a little project to investigate how to create a service to Authenticate users.

## How works?
This project has 3 endpoints:

+ \[POST\] `/users`:  Create a new user
+ \[GET\] `/token`: Receive the credentials of a user and return the access Token (JWT)
+ \[GET\] `/current_user` : Return the current user based on the JWT in the Authorization Header.

## How run this project?

### With local resources:

1. Install all the dependencies:

```bash
pip install -r requirements.txt
```

2. Run the project

```bash
uvicorn main:app
```

### With Docker

1. Build the image

```bash
docker-compose build
```

2. Spin up the containers

```bash
docker-compose up
```

