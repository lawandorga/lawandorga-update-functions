from src.domain.repository import AbstractRepository
import abc


class AbstractUnitOfWork(abc.ABC):
    repository: AbstractRepository

    def __enter__(self) -> "AbstractUnitOfWork":
        return self

    def __exit__(self, *args):
        self.rollback()

    @abc.abstractmethod
    def commit(self, exc_type, exc_value, traceback):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
