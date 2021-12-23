from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def db_session(db_url):
    """ Creates a context with an open SQLAlchemy session.
    """
    engine = create_engine(db_url, convert_unicode=True)
    Session = sessionmaker(engine)

    return Session
