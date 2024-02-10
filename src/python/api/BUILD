python_sources(
    name="lib"
)

# 3rd party deps
pex_binary(
    name="api-binary-deps",
    environment="docker_linux",
    dependencies=[
        ":lib",
        "//:reqs#uvicorn",
        # "//:reqs#gunicorn",  # if using gunicorn
    ],
    layout="packed",
    execution_mode="venv",
    include_sources=False,
    include_tools=True,
)

# 1st party srcs
pex_binary(
    name="api-binary-srcs",
    entry_point="api.main",
    environment="docker_linux",
    dependencies=[
        ":lib"
    ],
    layout="packed",
    execution_mode="venv",
    include_requirements=False,
    include_tools=True,
)
