from random import randint

_hidden_number = []
_results = {'bulls': 0, 'cow': 0}
_quon_steps = 0

def generate_number():
    global _hidden_number
    _hidden_number = []
    while len(_hidden_number) < 4:
        j = str(randint(1, 9))
        if j not in _hidden_number:
            _hidden_number.append(str(j))

    return print(_hidden_number)


def check_number(user_answer):
    global _results, _quon_steps
    _results = {'bulls': 0, 'cow': 0}
    _quon_steps += 1
    user_answer_list = list(user_answer)

    for i, symbol in enumerate(user_answer_list):
        if symbol == _hidden_number[i]:
            _results['bulls'] += 1
        elif symbol in _hidden_number:
            _results['cow'] += 1

    print(_results)


def game_over():
    if _results['bulls'] == 4:
        print('Победа! с ', _quon_steps, 'хода!')
        return False
    else:
        return True


