FROM python:3.11-slim-bookworm as deps
COPY src.python/api-binary-deps.pex /api-binary-deps.pex
RUN PEX_TOOLS=1 /usr/local/bin/python3.11 /api-binary-deps.pex venv --scope=deps /app

FROM python:3.11-slim-bookworm as srcs
COPY src.python/api-binary-srcs.pex /api-binary-srcs.pex
RUN PEX_TOOLS=1 /usr/local/bin/python3.11 api-binary-srcs.pex venv --scope=srcs /app

ENTRYPOINT ["/app/pex"]
EXPOSE 80
