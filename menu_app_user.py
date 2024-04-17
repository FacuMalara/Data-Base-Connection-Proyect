from user_dao import UserDao
from user import User


def main():
    while True:
        option = None

        print(f'''
            Choose an option:
            
            1. Select all users.
            2. Insert new user.
            3. Update an user.
            4. Delete an user.
            5. Close programm.
        ''')

        option = input('Enter the option: ')
        match option:
            case '1':

                users = UserDao.select()
                for user in users:
                    print(user)

            case '2':

                user1 = User(username=input('Enter username: '), password=input('Enter password: '))
                inserted = UserDao.insert(user1)
                print(inserted)

            case '3':

                user1 = User(input('Please, provide a valid id: '), input('Enter new username: '), input('Enter new password: '))
                updated = UserDao.update(user1)
                print(updated)

            case '4':

                user1 = User(user_id=input('Enter a valid user id: '))
                deleted = UserDao.delete(user1)
                print(deleted)

            case '5':

                print('Ending process...')
                return

            case _:

                print('Incorrect income')


if __name__ == '__main__':
    main()
