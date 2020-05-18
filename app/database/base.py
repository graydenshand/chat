from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
import re

engine = create_engine(os.environ.get("DATABASE_URL"), convert_unicode=True)
db_session = scoped_session(
	sessionmaker(
		autocommit=False, 
		autoflush=False, 
		bind=engine
	)
)
Base = declarative_base()
Base.query = db_session.query_property()

class SerializerMixin():
	"""
	Extending inhereted Table interface with serialization functions
	"""
	def to_dict(self):
		data = {}
		for column in self.__table__.columns:
			column_name = re.sub(f"{self.__tablename__}.", "", str(column))
			data[column_name] = getattr(self, column_name)
		return data