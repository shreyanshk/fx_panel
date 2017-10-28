from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///:memory:')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class FirearmType(Base):
	__tablename__ = 'firearmtypes'

	id = Column(Integer, primary_key=True)
	model = Column(String)
	odm = Column(String)
	type = Column(String)


class Owner(Base):
	__tablename__ = 'owners'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	mobile = Column(Integer)
	address = Column(String)
	city = Column(String)
	aadhar = Column(Integer)


class FirearmTxn(Base):
	__tablename__ = 'txns'

	id = Column(Integer, primary_key=True)
	origowner = relationship('Owner', ForeignKey(Owner.id))
	newowner = relationship('Owner', ForeignKey(Owner.id))


class Users(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	username = Column(String)
	password = Column(String)
