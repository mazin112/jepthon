try:
    from . import BASE, SESSION
except ImportError as e:
    raise AttributeError from e
from sqlalchemy import Column, String, UnicodeText, Table

if 'globals' in BASE.metadata.tables:
    globals_table = Table('globals', BASE.metadata, autoload=True, autoload_with=SESSION.bind)
else:
    globals_table = Table(
        'globals', BASE.metadata,
        Column('variable', String, primary_key=True, nullable=False),
        Column('value', UnicodeText, primary_key=True, nullable=False)
    )

class Globals:
    def __init__(self, variable, value):
        self.variable = str(variable)
        self.value = value

def addgvar(variable, value):
    if SESSION.query(globals_table).filter(globals_table.c.variable == str(variable)).one_or_none():
        delgvar(variable)
    ins = globals_table.insert().values(variable=str(variable), value=value)
    SESSION.execute(ins)
    SESSION.commit()

def delgvar(variable):
    dele = globals_table.delete().where(globals_table.c.variable == str(variable))
    SESSION.execute(dele)
    SESSION.commit()
