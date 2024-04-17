from logger_base import log
from connection import Connection


class CursorPool:
    def __init__(self):
        self._connection = None
        self._cursor = None

    def __enter__(self):
        log.debug('Beggining of with\'s method __enter__')
        self._connection = Connection.getConnection()
        self._cursor = self._connection.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('Beggining of with\'s method __exit__')
        if exc_val:
            self._connection.rollback()
            log.error(f'Exception occured: {exc_type} {exc_val} {exc_tb}')
        else:
            self._connection.commit()
            log.debug('Commit made')
        self._cursor.close()
        Connection.freeConnection(self._connection)


if __name__ == '__main__':
    with CursorPool() as cursor:
        log.debug('Inside with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())
