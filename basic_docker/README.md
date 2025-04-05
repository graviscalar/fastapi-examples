# Quickstart

Simple FastAPI app with Docker

Exploring routes:

* default
* with GET and JSON return
* with POST and JSON data
* with GET, POST and JSON data

To build the Docker image, run the following command in the same directory as the Dockerfile
``` shell
 docker build -t fastapi_basic_docker .
```

To run the Docker container, run the following command:

``` shell
 docker run --name fastapi_basic_docker -p 8000:8000 fastapi_basic_docker
```

Enter the container to verify the saved images:
``` shell
 docker exec -ti fastapi_basic_docker sh
```


Test functionality by running the test.py
