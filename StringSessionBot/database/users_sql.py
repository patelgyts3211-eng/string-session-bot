# Asad ALI

from sqlalchemy import Column, BigInteger
from StringSessionBot.database import BASE, SESSION


class Users(BASE):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    user_id = Column(BigInteger, primary_key=True)

    def __init__(self, user_id):
        self.user_id = user_id


async def num_users():
    try:
        return SESSION.query(Users).count()
    finally:
        SESSION.remove()
