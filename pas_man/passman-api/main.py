from fastapi import FastAPI

from routers.passwords import router as password_router


app = FastAPI(
    title="PassMan API"
)


app.include_router(password_router)


@app.get("/")
def root():
    return {"message": "PassMan API is running"}