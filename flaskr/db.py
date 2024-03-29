"""Module Database."""
# Disable all the no-member violations in this function
# pylint: disable=no-member

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base


# engine = create_engine("sqlite:////tmp/test.db")
engine_str = "postgresql+psycopg://myuser:mypass@localhost:5432/flask"
engine = create_engine(engine_str)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    """DocType"""
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import th
    # import flaskr.models

    Base.metadata.create_all(bind=engine)
