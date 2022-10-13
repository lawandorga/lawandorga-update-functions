from src.domain.model import Update
from src.domain.uow import AbstractUnitOfWork
from src.domain.repository import AbstractRepository


def add_update(uow: AbstractUnitOfWork, repository: AbstractRepository, identifier: str):
    assert type(identifier) == str

    update = Update(identifier)
    with uow:
        repository.add_update(update)
        uow.commit()


def remove_update(uow: AbstractUnitOfWork, repository: AbstractRepository, identifier: str):
    assert type(identifier) == str
    
    with uow:
        repository.remove_update(identifier)
        uow.commit()
