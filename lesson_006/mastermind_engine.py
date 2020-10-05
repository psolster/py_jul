from random import randint

_hidden_number = []
# _results = {'bulls': 0, 'cow': 0}


def generate_number():
    global _hidden_number
    _hidden_number = []
    while len(_hidden_number) < 4:
        j = str(randint(1, 9))
        if j not in _hidden_number:
            _hidden_number.append(str(j))

    return print(_hidden_number)


def check_number(user_answer):
    results = {'bulls': 0, 'cow': 0}
    quon_steps = 0
    # _results = {'bulls': 0, 'cow': 0}
    user_answer_list = list(user_answer)
    while results['bulls'] < 4:
        quon_steps += 1
        for i, symbol in enumerate(user_answer_list):
            if symbol == _hidden_number[i]:
                results['bulls'] += 1
            elif symbol in _hidden_number:
                results['cow'] += 1

        print(results)
    # return print('молодец, угадад с ', _quon_steps, 'раза')


# def game_over():
#     if _results['bulls'] == 4:
#         print('Победа! с ', _quon_steps, 'хода!')
#         return True
#     else:
#         return False

# generate_number()
# check_number('5478')
