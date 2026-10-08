from sqlalchemy import Column, Integer, String

from database import Base


class Password(Base):
    __tablename__ = "passwords"

    id = Column(Integer, primary_key=True)
    service = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    category = Column(String)