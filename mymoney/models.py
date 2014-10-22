from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    VARCHAR,
    Unicode,
    UnicodeText,
    DateTime,
    ForeignKey,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


def foreign_key_column(name, type_, target, nullable=False):
    """Construct a foreign key column for a table.

    ``name`` is the column name. Pass ``None`` to omit this arg in the
    ``Column`` call; i.e., in Declarative classes.

    ``type_`` is the column type.

    ``target`` is the other column this column references.

    ``nullable``: pass True to allow null values. The default is False
    (the opposite of SQLAlchemy's default, but useful for foreign keys).
    """
    fk = ForeignKey(target)
    if name:
        return Column(name, type_, fk, nullable=nullable)
    else:
        return Column(type_, fk, nullable=nullable)

class LabelList(Base):
    __tablename__ = 'label_list'
    # userid = Column(VARCHAR(50), primary_key=True)
    # userid = Column(Integer)
    id = Column(Integer, primary_key=True)
    userid = foreign_key_column(None, Integer, 'users.id')
    plus_list = Column(UnicodeText, nullable=False)
    minus_list = Column(UnicodeText, nullable=False)

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    # userid = Column(VARCHAR(50))
    userid = foreign_key_column(None, Integer, 'users.id')
    label = Column(Unicode(100), nullable=False)
    datetime = Column(DateTime, nullable = False)
    value = Column(Integer, nullable = False)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    userid = Column(Unicode(100), unique=True)
    name = Column(Unicode(50), nullable=False)
    password = Column(VARCHAR(255), nullable=False)

