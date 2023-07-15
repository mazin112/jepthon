try:
    from . import BASE, SESSION
except ImportError as e:
    raise Exception("Hello!") from e
from sqlalchemy import Column, String, select


class Mute(BASE):
    __tablename__ = "mute"
    sender = Column(String(14), primary_key=True)
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, sender, chat_id):
        self.sender = str(sender)
        self.chat_id = str(chat_id)


Mute.__table__.create(checkfirst=True)


def is_muted(sender, chat_id):
    with SESSION() as session:
        user = session.query(Mute).get((str(sender), str(chat_id)))
        return bool(user)


def mute(sender, chat_id):
    with SESSION() as session:
        adder = Mute(str(sender), str(chat_id))
        session.add(adder)
        session.commit()


def unmute(sender, chat_id):
    with SESSION() as session:
        if rem := session.query(Mute).get((str(sender), str(chat_id))):
            session.delete(rem)
            session.commit()


def get_muted_users():
    with SESSION() as session:
        query = select(Mute)
        muted_users = session.execute(query).scalars().all()
        return muted_users