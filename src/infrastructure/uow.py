from src.domain.uow import AbstractUnitOfWork
import psycopg2


class PostgresUnitOfWork(AbstractUnitOfWork):
    def __init__(self, pghost, pguser, pgdatabase, pgpassword, pgport):
        self.connection = psycopg2.connect(
            user=pguser,
            host=pghost,
            database=pgdatabase,
            password=pgpassword,
            port=pgport
        )

    def commit(self):
        self.connection.commit()
        print('commit')

    def rollback(self):
        self.connection.rollback()
        print('rollback')
