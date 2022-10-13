from src.domain.uow import AbstractUnitOfWork
from src.config import config
import psycopg2


class PostgresUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.connection = psycopg2.connect(
            user=config.PGUSER,
            host=config.PGHOST,
            database=config.PGDATABASE,
            password=config.PGPASSWORD,
            port=config.PGPORT
        )

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()
