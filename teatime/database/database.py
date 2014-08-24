from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DatabaseConnection:
    connection_str_template = ('postgresql+psycopg2://{user}:{password}@'
                               '/{database}')

    def __init__(self, user, password, database):
        self.user = user
        self.password = password
        self.database = database

    @classmethod
    def from_teetee_config(cls, teetee_config):
        user = teetee_config['database']['username']
        password = teetee_config['database']['password']
        database = teetee_config['database']['database']
        return cls(user, password, database)

    def connect(self, Base, *args, **kwargs):
        connection_str = self.connection_str_template.format(
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.engine = create_engine(connection_str, *args, **kwargs)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def new_session(self):
        return self.Session()


Base = declarative_base()
