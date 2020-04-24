# Cargo App


## Installation

We use docker to run the project.

[Download Docker](https://www.docker.com/community-edition)

Docker can't help for some devices. If the project does not work with Docker, Docker Toolbox will help you.

[Download Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/#step-2-install-docker-toolbox)


## How to Run?

To build the project:
```
docker-compose -p cargo -f docker/docker-compose.yml -f docker/docker-compose.dev.yml build
```

To run the project:
```
docker-compose -p cargo -f docker/docker-compose.yml -f docker/docker-compose.dev.yml up -d
```

To restart the project:
```
docker-compose -p cargo -f docker/docker-compose.yml -f docker/docker-compose.dev.yml restart
```

To stop the project:
```
docker-compose -p cargo -f docker/docker-compose.yml -f docker/docker-compose.dev.yml stop
```

To see logs:
```
docker-compose -p cargo -f docker/docker-compose.yml -f docker/docker-compose.dev.yml logs -f --tail 50
```

To status docker containers:
```
docker-compose -p cargo -f docker/docker-compose.yml -f docker/docker-compose.dev.yml ps
```


## Technologies

This is a list of mostly used awesome technologies and libraries that are used in Cargo Project:

- [Python](https://www.python.org/): Python is an interpreted high-level programming language for general-purpose programming.

- [Flask](https://palletsprojects.com/p/flask/): Flask is a lightweight WSGI web application framework.

- [Mongodb](https://www.mongodb.com/): MongoDB is an open-source document-based database management tool that stores data in JSON-like formats.


## Maintainers

* **Kenan Subaşı**  - *kenansubasiceng@gmail.com*

