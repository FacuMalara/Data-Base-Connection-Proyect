import sys

from psycopg2 import pool
from logger_base import log


class Connection:
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _DB_NAME = 'test_db'
    _MAX_CONN = 5
    _MIN_CONN = 1
    _pool = None

    @classmethod
    def getPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CONN, cls._MAX_CONN,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      database=cls._DB_NAME,
                                                      port=cls._DB_PORT
                                                      )
                log.debug('Pool connection succed')
                return cls._pool
            except Exception as e:
                log.error(f'An error occured when trying to get pool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def getConnection(cls):
        connection = cls.getPool().getconn()
        log.debug(f'Connection stablished from pool: {connection}')
        return connection

    @classmethod
    def freeConnection(cls, connection):
        cls.getPool().putconn(connection)
        log.debug(f'Connection object has been set free: {connection}')

    @classmethod
    def closeAllConn(cls):
        cls.getPool().closeall()


if __name__ == '__main__':
    connection1 = Connection.getConnection()
    connection2 = Connection.getConnection()
    Connection.freeConnection(connection2)
    connection3 = Connection.getConnection()
    connection4 = Connection.getConnection()
    Connection.freeConnection(connection4)
    connection5 = Connection.getConnection()
    connection6 = Connection.getConnection()
    connection7 = Connection.getConnection()
