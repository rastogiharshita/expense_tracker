from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from utils import Utils

Base = declarative_base()


class DatabaseUtils:

    @classmethod
    def initialize_db(cls):
        db_config = Utils.get_config()['database']
        db_uri = f"{db_config['driver']}://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['db_name']}"
        cls.__engine = create_engine(db_uri, echo=True)
        cls.__session = sessionmaker(bind=cls.__engine)
        # todo: auto-create all tables
        Base.metadata.create_all(cls.__engine)
        # session = sessionmaker(autocommit=False, autoflush=False, bind=self.__engine)

    @classmethod
    def get_session(cls):
        if cls.__session is None:
            cls.initialize_db()
        return cls.__session()

    @classmethod
    @contextmanager
    def session_scope(cls):
        """Provide a transactional scope around a series of operations."""
        session = cls.get_session()
        try:
            yield session  # give session to caller
            session.commit()  # commit if everything went fine
        except Exception:
            session.rollback()  # rollback on error
            raise
        finally:
            session.close()  # always close the session