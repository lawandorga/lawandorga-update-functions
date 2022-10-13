from pydantic import BaseSettings


class Config(BaseSettings):
    PGHOST: str
    PGUSER: str
    PGDATABASE: str
    PGPASSWORD: str
    PGPORT: int

    class Config:
        env_file = ".env"

    @property
    def DEFAULT_UNIT_OF_WORK(self):
        from src.infrastructure.uow import PostgresUnitOfWork
        
        return PostgresUnitOfWork()

    @property
    def DEFAULT_REPOSITORY(self):
        from src.infrastructure.repository import PostgresRepository

        return PostgresRepository(self.DEFAULT_UNIT_OF_WORK.connection)


config = Config()
