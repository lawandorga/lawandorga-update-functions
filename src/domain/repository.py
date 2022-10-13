from src.domain.model import Update
import abc


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def get_update_count(self):
        raise NotImplementedError

    @abc.abstractmethod
    def add_update(self, update: Update):
        raise NotImplementedError
    
    @abc.abstractmethod
    def remove_update(self, identifier: str):
        raise NotImplementedError
