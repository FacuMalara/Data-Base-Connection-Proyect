from logger_base import log
from cursor_pool import CursorPool
from user import User


class UserDao:
    '''
    DAO - Data Access Object for table user1
    CRUD - Create - Read - Update - Delete for table user1  #there was an error in the authentication process within the table name, so I had to make a new table, that is why the '1' in user.
    '''
    _SELECT = 'SELECT * FROM user1 ORDER BY user_id'
    _INSERT = 'INSERT INTO user1(username, password) VALUES(%s,%s)'
    _UPDATE = 'UPDATE user1 SET username=%s, password=%s WHERE user_id=%s'
    _DELETE = 'DELETE FROM user1 WHERE user_id=%s'

    @classmethod
    def select(cls):
        with CursorPool() as cursor:
            log.debug('Executing code')
            cursor.execute(cls._SELECT)
            recordings = cursor.fetchall()
            users = []
            for record in recordings:
                user = User(record[0], record[1], record[2])
                users.append(user)
            return users

    @classmethod
    def insert(cls, user):
        with CursorPool() as cursor:
            log.debug('Executing the code')
            values = (user.username, user.password)
            cursor.execute(cls._INSERT, values)
            log.debug(f'User added: {user}')
            return cursor.rowcount

    @classmethod
    def update(cls, user):
        with CursorPool() as cursor:
            log.debug('Executing the code')
            values = (user.username, user.password, user.id_user)
            cursor.execute(cls._UPDATE, values)
            log.debug(f'User updated: {user}')
            return cursor.rowcount

    @classmethod
    def delete(cls, user):
        with CursorPool() as cursor:
            log.debug('Executing the code')
            values = (user.id_user,)    #para que sea una tupla
            cursor.execute(cls._DELETE, values)
            log.debug(f'User deleted: {user}')
            return cursor.rowcount


if __name__ == '__main__':

    #Delete
    # user1 = User(user_id=4)
    # user2= User(user_id=5)
    # deleted = UserDao.delete(user2)
    # log.debug(deleted)

    #Update
    # user1 = User(1, 'pep','msan')
    # updated= UserDao.update(user1)
    # log.debug(updated)

    #Insert
    # user1 = User(username='santi', password='321')
    # record = UserDao.insert(user1)
    # log.debug(record)

    #Select
    users = UserDao.select()
    for user in users:
        log.debug(user)

