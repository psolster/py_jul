from random import randint
_hidden_number = []


def generate_number():
    global _hidden_number
    _hidden_number = []
    while len(_hidden_number) < 4:
        j = randint(1, 9)
        if j not in _hidden_number:
            _hidden_number.append(str(j))

    return print(_hidden_number)


def check_number(user_answer):
    bull = 0
    cow = 0
    user_answer_list = list(user_answer)
    # print(user_answer_list)
    for i, symbol in enumerate(user_answer_list):

        if symbol == _hidden_number:
            bull += 1
        elif symbol in _hidden_number:
            cow += 1
    return print(bull, cow)


# generate_number()
# check_number('5478')





