from fastapi import FastAPI
import cowsay

app = FastAPI()


@app.get("/")
async def root():
    msg = "Hello Pants and FastAPI!"
    print(cowsay.get_output_string("cow", msg))
    return {"message": msg}


@app.get("/hello/{name}")
async def say_hello(name: str):
    msg = f"Hello {name}!"
    print(cowsay.get_output_string("cow", msg))
    return {"message": msg}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("api.main:app", reload=True)
