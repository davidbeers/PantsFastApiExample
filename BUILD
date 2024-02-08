python_requirements(
    name="reqs",
    source="requirements.txt",
)

# A `local_environment` runs without containerization on localhost (which is also the
# default if no environment targets are defined).
local_environment(
  name="local_linux",
  compatible_platforms=["linux_x86_64"],
)

# A `docker_environment` runs in a cached container using the specified Docker image
# using a local installation of Docker. If the image does not already exist locally,
# it will be pulled.
docker_environment(
    name="docker_linux",
    platform="linux_x86_64",
    image="python:3.11-slim-bookworm",
    python_bootstrap_search_path=["<PATH>"]  # [python-bootstrap].search_path` is configured to use local discovery tools, which do not work in DockerEnvironmentTarget runtime environments.
)

# Default all environment-aware targets to the docker environment
__defaults__(all=dict(environment="docker_linux"))
