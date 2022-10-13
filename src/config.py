from src.infrastructure.repository import PostgresRepository
from src.infrastructure.uow import PostgresUnitOfWork
from src.domain.repository import AbstractRepository
from src.domain.uow import AbstractUnitOfWork
from pydantic import BaseSettings
from typing import Optional


class EnvConfig(BaseSettings):
    PGHOST: Optional[str]
    PGUSER: Optional[str]
    PGDATABASE: Optional[str]
    PGPASSWORD: Optional[str]
    PGPORT: Optional[int]

    class Config:
        env_file = ".env"


env_config = EnvConfig()


POSTGRES_UNIT_OF_WORK = PostgresUnitOfWork(env_config.PGHOST, env_config.PGUSER, env_config.PGDATABASE, env_config.PGPASSWORD, env_config.PGPORT)
POSTGRES_REPOSITORY = PostgresRepository(POSTGRES_UNIT_OF_WORK.connection)


class Config:
    UNIT_OF_WORK: AbstractUnitOfWork = POSTGRES_UNIT_OF_WORK
    REPOSITORY: AbstractRepository = POSTGRES_REPOSITORY


config = Config()
