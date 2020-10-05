from random import randint
_hidden_number = []


def generate_number():
    global _hidden_number
    _hidden_number = []
    # was_digits = []
    # list_of_acceptable_digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    i = 0
    while len(_hidden_number) < 4:
        j = randint(1, 9)
        if j not in _hidden_number:
            _hidden_number.append(j)




    return _hidden_number

# generate_number()



def check_number(user_answer):
    pass

