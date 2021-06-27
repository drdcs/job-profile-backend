# Backend for the Job Board

The job board has an admin page and a user page.
The admin has the right to publish the Job Profiles.
The User add users Info and the Job they are applying for.

# How to start ?

Make sure docker installed and connected to Docker Hub.

```sh
docker-compose up -d --build

docker-compose up # otherwise

docker-compose down # stop all containers

docker-compose down -v # stop with volume removed.

```

# Docs

```
http://localhost:8002/docs
http://localhost:8001/docs
```

# Git command:

```sh
git remote add origin git_repo_link
git branch -M main
git push -u origin main
```

# Access Database

Refer the docker-compose.yml file.
ports are different : 5432 and 5433 respectively
