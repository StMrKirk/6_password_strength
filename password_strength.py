import re
import sys


password_patterns_list = list(['^(\d|[A-Z]|[a-z]|[!@#$&*%,./:;^_=?\(\)\{\}\[\]])$',
                               '^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]+$',
                               '^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[!@#$&*%,./:;^_=?\(\)\{\}\[\]])'
                               '[A-Za-z\d!@#$&*%,./:;^_=?\(\)\{\}\[\]]+$',
                               '^(?=.*?\d.*\d)(?=.*?[A-Z].*[A-Z])(?=.*?[a-z].*[a-z])'
                               '(?=.*?[!@#$&*%,./:;^_=?\(\)\{\}\[\]]'
                               '.*[!@#$&*%,./:;^_=?\(\)\{\}\[\]])[A-Za-z\d!@#$&*%,./:;^_=?\(\)\{\}\[\]]+$'])


def check_password_in_top_list(password):
    """Функция проверяет наличие пароля в самых популярных"""
    with open('10_million_password_list_top_10000.txt', 'r', encoding='UTF-8') as password_list:
        for password_list_line in password_list:
            if password_list_line.rstrip() == password:
                return True


def get_password_strength(password):
    """Функция выводит сложность пароля согласно условию(паттерну)"""
    strength = 1
    if check_password_in_top_list(password):
        return strength
    for password_pattern in password_patterns_list:
        if re.search(password_pattern, password):
            strength = password_patterns_list.index(password_pattern)+1
    if len(password) >= 8 and strength != 1 and strength != 2:
        strength += 6
    elif strength != 1 and strength != 2 and strength != 3:
        strength += len(password)
    return strength


if __name__ == '__main__':
    print('Сложность вашего пароля: {}'.format(get_password_strength(sys.argv[1])))

