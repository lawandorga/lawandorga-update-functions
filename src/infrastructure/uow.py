from src.infrastructure.repository import PostgresRepository
from src.domain.uow import AbstractUnitOfWork
from typing import Optional
import psycopg2


class PostgresUnitOfWork(AbstractUnitOfWork):
    def __get_connection(self):
        return psycopg2.connect(
            user=self.__pguser,
            host=self.__pghost,
            database=self.__pgdatabase,
            password=self.__pgpassword,
            port=self.__pgport
        )
    
    def __init__(self, pghost, pguser, pgdatabase, pgpassword, pgport):
        self.__pghost = pghost
        self.__pguser = pguser
        self.__pgdatabase = pgdatabase
        self.__pgpassword = pgpassword
        self.__pgport = pgport
        self.connection: Optional[psycopg2.connection] = None

    def __enter__(self):
        self.connection = self.__get_connection()
        self.repository = PostgresRepository(self.connection)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()
