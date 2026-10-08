from pydantic import BaseModel


class PasswordResponse(BaseModel):
    id: int
    service: str
    username: str
    password: str
    category: str | None = None

    class Config:
        from_attributes = True