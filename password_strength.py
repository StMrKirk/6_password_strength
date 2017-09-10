import re
import sys


'''Господи боже мой скок я разбирался с этим regex я надеюсь что-то я запомнил: соотвествие или строчной или заглавной 
или цифре, цифре и строчной и заглавной, цифре и строчной и заглавной и спец.знаку, двум цифрам и двум заглавным и двум
строчным и двум спец.знакам'''
password_patterns_list = list(['^(\d|[A-Z]|[a-z]|[!@#$&*%,./:;^_=?\(\)\{\}\[\]])$',
                               '^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]+$',
                               '^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[!@#$&*%,./:;^_=?\(\)\{\}\[\]])'
                               '[A-Za-z\d!@#$&*%,./:;^_=?\(\)\{\}\[\]]+$',
                               '^(?=.*?\d.*\d)(?=.*?[A-Z].*[A-Z])(?=.*?[a-z].*[a-z])'
                               '(?=.*?[!@#$&*%,./:;^_=?\(\)\{\}\[\]]'
                               '.*[!@#$&*%,./:;^_=?\(\)\{\}\[\]])[A-Za-z\d!@#$&*%,./:;^_=?\(\)\{\}\[\]]+$'])


def get_password_strength(password):
    """Функция проверяет наличие пароля в файле с самыми популярными паролями и выводит его сложность согласно
    условию(паттерну)"""
    strength = 1
    with open('10_million_password_list_top_10000.txt', 'r', encoding='UTF-8') as password_list:
        for password_list_line in password_list:
            if password_list_line.rstrip() == password:
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

