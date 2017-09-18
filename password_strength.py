import re
import sys


password_patterns_list = list(['^(\d|[A-Z]|[a-z]|[!@#$&*%,./:;^_=?\(\)\{\}\[\]])$',
                               # наличие либо заглавной либо строчной либо спецсимвола либо цифры
                               '^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]+$',
                               # наличие цифры и заглавной и строчной
                               '^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[!@#$&*%,./:;^_=?\(\)\{\}\[\]])'
                               '[A-Za-z\d!@#$&*%,./:;^_=?\(\)\{\}\[\]]+$',
                               # наличие цифры и заглавной и строчной и спецсимвола
                               '^(?=.*?\d.*\d)(?=.*?[A-Z].*[A-Z])(?=.*?[a-z].*[a-z])'
                               '(?=.*?[!@#$&*%,./:;^_=?\(\)\{\}\[\]]'
                               '.*[!@#$&*%,./:;^_=?\(\)\{\}\[\]])[A-Za-z\d!@#$&*%,./:;^_=?\(\)\{\}\[\]]+$'])
                               # наличие 2 цифр и 2 заглавных и 2 строчных и 2 спецсимволов


def load_password_top_list():
    password_list = []
    with open('10_million_password_list_top_10000.txt', 'r', encoding='UTF-8') as password_file:
        for password_file_line in password_file:
            password_list.append(password_file_line.rstrip())
        return password_list


def check_password_in_top_list(password):
    password_list = load_password_top_list()
    for password_list_item in password_list:
        if password_list_item == password:
            return True


def get_password_strength(password):
    strength = 1
    if check_password_in_top_list(password):
        return strength
    for password_pattern in password_patterns_list:
        if re.search(password_pattern, password):
            strength = password_patterns_list.index(password_pattern)+1
    if len(password) >= 8 and strength != 1 and strength != 2:
        strength += 6
    elif strength not in (1, 2, 3):
        strength += len(password)
    return strength


if __name__ == '__main__':
    print('Сложность вашего пароля: {}'.format(get_password_strength(sys.argv[1])))

