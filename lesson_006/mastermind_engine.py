from random import randint

_hidden_number = []
_results = {'bulls': 0, 'cow': 0}
_quantity_steps = 0
_user_answer_set = None


def generate_number():
    global _hidden_number
    _hidden_number = []
    while len(_hidden_number) < 4:
        j = str(randint(1, 9))
        if j not in _hidden_number:
            _hidden_number.append(str(j))

    return _hidden_number


def check_number(user_answer):
    global _results, _quantity_steps, _user_answer_set
    _results = {'bulls': 0, 'cow': 0}
    _quantity_steps += 1

    user_answer_list = list(user_answer)
    user_answer_set = set(user_answer_list)
    if len(user_answer_set) != 4:
        _user_answer_set = len(user_answer_set)
        return _user_answer_set

    for i, symbol in enumerate(user_answer_list):
        if symbol == _hidden_number[i]:
            _results['bulls'] += 1
        elif symbol in _hidden_number:
            _results['cow'] += 1
    return _results, _result_len_set
    # print('Быки->', _results['bulls'], 'Коровы->', _results['cow'])


def game_over():
    if _results['bulls'] == 4:
        print('Победа! с ', _quantity_steps, 'хода!')
        print('Хотите еще партию?')
        return False
    else:
        return True


