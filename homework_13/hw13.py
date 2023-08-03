"""
Доработаем задачи 3 и 4. Создайте класс Project, содержащий атрибуты - список пользователей проекта и админ проекта.
Класс имеет следующие методы:
- классовый метод загрузки данных из JSON файла
- метод входа в систему - требует указать имя и id пользователя. Далее метод создает пользователя и проверяет, есть
ли он в списке пользователей проекта. Если в списке его нет, то вызывается исключение доступа. Если пользователь
присутствует в списке проекта, то пользователь, который входит, получает его уровень доступа и становится администратором.
- метод добавления пользователя в список пользователей. Если уровень пользователя меньше, чем уровень админа, вызывается
исключение уровня доступа.
 * метод удаления пользователя из списка пользователей
 * метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера

Доработать класс Project
Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках. Передавайте необходимые данные из
основного кода проекта.
"""


from sem34 import User as User
from sem34 import BaseError as RunTimeException
from sem34 import LevelError as LevelError
from sem34 import AccessError as AccessError
from pathlib import Path
import json


class Project:
    path = Path(Path.cwd(), 'users.json')
    admin = None
    JSON_data = {}
    users_lst = []

    def __init__(self, u_id, name, *args):
        self.level = None
        self.u_id = u_id
        self.name = name
        self.load_file()
        self.login()

    @classmethod
    def load_file(cls):
        try:
            with open(cls.path, 'r', encoding='utf-8') as f:
                cls.JSON_data = json.load(f)
        except FileNotFoundError:
            raise RunTimeException('File not found!')

        for level, users in cls.JSON_data.items():
            for u_id, name in users.items():
                try:
                    user = User(int(u_id), name, int(level))
                except ValueError:
                    raise RunTimeException('u_id and level must be of type INT')
                except:
                    raise RunTimeException()
                else:
                    cls.users_lst.append(user)

    def login(self):
        curr_user = User(self.u_id, self.name, self.level)
        if curr_user not in self.users_lst:
            raise AccessError('There is no such user in the list')
        for u in self.users_lst:
            if u.id == curr_user.id:
                self.level = u.level
                Project.admin = self
                print(f'{curr_user.name} successfully logged in!')
                break

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('users1.json', 'w', encoding='utf-8') as f:
            json.dump(self.users_lst, f, indent=2, sort_keys=True)

    def add_user(self, u_id, name, level):
        new_user = User(u_id, name, level)
        if new_user.level >= self.level:
            Project.users_lst.append(new_user)
            return f'User {new_user.name} was successfully added!'
        else:
            raise LevelError('Error access level!')


    def del_user(self, u_id, name, level):
        unnecessary = User(u_id, name, level)
        if level > self.level:
            try:
                Project.users_lst.remove(unnecessary)
            except ValueError:
                raise AccessError('There is no such user in the list')
            else:
                return f'User {unnecessary.name} was successfully deleted!'


if __name__ == '__main__':
    a = Project(6543, 'Ginn')
    print(a.__dict__)
    print('Admin:  ', Project.admin.name)
    print(a.add_user(4667, 'Andrey', 5))
    print(a.del_user(4667, 'Andrey', 5))
