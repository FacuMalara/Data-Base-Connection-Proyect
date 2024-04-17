from logger_base import log


class User:
    def __init__(self, user_id=None, username=None, password=None):
        self._user_id = user_id
        self._username = username
        self._password = password

    def __str__(self):
        return f'''
            Id User: {self._user_id}, Username: {self._username}, Password: {self._password}
        '''

    @property
    def id_user(self):
        return self._user_id

    @id_user.setter
    def id_user(self, user_id):
        self._user_id = user_id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password


if __name__ == '__main__':
    user1 = User(1, 'facu123', '123')
    log.debug(user1)
    #Simular un insert
    user1 = User(username='facu123', password='123')
    log.debug(user1)
