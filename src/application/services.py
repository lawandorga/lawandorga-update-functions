from src.domain.model import Update
from src.domain.uow import AbstractUnitOfWork


def add_update(uow: AbstractUnitOfWork, identifier: str):
    assert type(identifier) == str

    update = Update(identifier)
    with uow:
        uow.repository.add_update(update)
        uow.commit()


def remove_update(uow: AbstractUnitOfWork, identifier: str):
    assert type(identifier) == str
    
    with uow:
        uow.repository.remove_update(identifier)
        uow.commit()
