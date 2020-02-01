import json
from typing import List

from bson import json_util
from bson.objectid import ObjectId
from mongoengine import connect
from mongoengine.connection import disconnect

from config import APP_CONFIG


class DBEngine:

    def __init__(self, db_name: str = APP_CONFIG.DB_NAME):
        self.db_name = db_name
        self._connection = None

    def __enter__(self) -> 'DBEngine':
        return self._connect()

    def __exit__(self, *args) -> None:
        disconnect(alias=self.db_name)
        del self._connection

    def _connect(self) -> 'DBEngine':
        self._connection = connect(db=self.db_name,
                                   alias=self.db_name,
                                   host='{prefix}://{login}:{password}@{host}:{port}/?authSource=admin' \
                                        .format(prefix='mongodb', login=APP_CONFIG.DB_USERNAME,
                                                password=APP_CONFIG.DB_PASSWORD,
                                                host='mongodb', port=27017)) \
                            .get_database(self.db_name)

        return self

    def insert(self, table: str, data: list) -> List[ObjectId]:
        return self._connection[table].insert_many(data).inserted_ids

    def get(self, table: str, query: dict = {}, dump: bool = True) -> list:
        data = list(self._connection[table].find(query))
        if dump:
            return [json.loads(json_util.dumps(_dict)) for _dict in data]
        return data

    def update(self, data: dict, table: str, query: dict) -> 'DBEngine':
        current_data = self.get(table, query, dump=False)[0]
        self._connection[table].update(query, {**current_data, **data})
        return self

    def remove(self, table: str, query: dict) -> 'DBEngine':
        if query and table:
            self._connection[table].delete_many(query)
        return self
