try:
    from . import BASE, SESSION
except ImportError as e:
    raise AttributeError from e
from sqlalchemy import Column, String, UnicodeText

class kickname(BASE):
    __tablename__ = "kickname"
    variable = Column(String, primary_key=True, nullable=False)
    value = Column(UnicodeText, primary_key=True, nullable=False)

    def __init__(self, variable, value):
        self.variable = str(variable)
        self.value = value


kickname.__table__.create(checkfirst=True)


def gvarstatus(variable):
    try:
        return (
            SESSION.query(kickname)
            .filter(kickname.variable == str(variable))
            .first()
            .value
        )
    except BaseException:
        return None
    finally:
        SESSION.close()


def addgvar(variable, value):
    if SESSION.query(kickname).filter(kickname.variable == str(variable)).one_or_none():
        delgvar(variable)
    value_str = ",".join(value)  # تحويل القيمة إلى سلسلة نصية
    adder = kickname(str(variable), value_str)
    SESSION.add(adder)
    SESSION.commit()

def delgvar(variable):
    rem = (
        SESSION.query(kickname)
        .filter(kickname.variable == str(variable))
        .delete(synchronize_session="fetch")
    )
    if rem:
        SESSION.commit()
