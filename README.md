# Example Dockerized FastAPI project built with Pants

## Goals

This is a simple demo of a dockerized Python API service (using [FastAPI](https://fastapi.tiangolo.com/)) that's built 
with [Pants](https://www.pantsbuild.org/). The design goals include:

- to have a docker image with layers for the infrequently changing 3rd party dependencies and the frequently changing 1st party source to improve image build performance.
- to not compile the pex into .pyc since the small performance benefit in my case doesn't seem worth the cost of not having a deterministic, reproducible build. But if it's easy to set the project up so it's trivial to switch between compiled and uncompiled pex, that's great and I'll gladly document it.
- to be ready to run as a container on AWS Fargate with a load balancer handling scaling at the container level so I'd like the container to run plain uvicorn without gunicorn. I think this would be similar for folks deploying FastAPI on Kubernetes.

## Notes

- To run: `docker run -p 80:8000 hello-api`
