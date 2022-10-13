from src.domain.repository import AbstractRepository
from typing_extensions import TYPE_CHECKING
from src.domain.model import Update


if TYPE_CHECKING:
    from psycopg2 import connection as Connection


class PostgresRepository(AbstractRepository):
    def __init__(self, connection: "Connection"):
        super().__init__()
        self.connection: "Connection" = connection

    def get_update_count(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from main;")
        data = cursor.fetchall()
        cursor.close()
        return data

    def add_update(self, update: Update):
        assert type(update.identifier) is str
        
        cursor = self.connection.cursor()
        cursor.execute("insert into main values ('{}');".format(update.identifier))
        cursor.close()

    def remove_update(self, identifier: str):
        assert type(identifier) is str

        cursor = self.connection.cursor()
        cursor.execute("delete from main where identifier = '{}';".format(identifier))
        cursor.close()
