FROM python:3.11-slim-bookworm as deps
COPY src.python.api/api-binary-deps.pex /api-binary-deps.pex
RUN PEX_TOOLS=1 /usr/local/bin/python3.11 /api-binary-deps.pex venv --scope=deps /bin/app

FROM python:3.11-slim-bookworm as srcs
COPY src.python.api/api-binary-srcs.pex /api-binary-srcs.pex
RUN PEX_TOOLS=1 /usr/local/bin/python3.11 api-binary-srcs.pex venv --scope=srcs /bin/app

FROM python:3.11-slim-bookworm
COPY --from=deps /bin/app /bin/app
COPY --from=srcs /bin/app /bin/app

# Use this entry point if you want to run the service on uvicorn alone, often appropriate for deployment
# scenarios where the scaling and concurrency are handled at the container level and by a load balancer:
# AWS ECS/Fargate or Kubernetes.
ENTRYPOINT ["/bin/app/bin/uvicorn", "api.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
# Instead use this entry point if you want to use gunicorn as a process manager to improve concurrency
# and therefore performance using worker processes. See: https://fastapi.tiangolo.com/deployment/server-workers/
#ENTRYPOINT ["/bin/app/bin/gunicorn", "api.main:app", "--bind=0.0.0.0", "--timeout", "600", "--forwarded-allow-ips=*", "-k", "uvicorn.workers.UvicornWorker", "-w", "1"]
EXPOSE 8000
