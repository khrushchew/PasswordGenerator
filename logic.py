import Permutations
from appWindow import entry_for_password, label_for_password, label_for_result

mass = []
counter = 0


def get_text():
    global counter
    mass.append(entry_for_password.get())
    if counter == 0:
        label_for_password['text'] = 'fwefwefwefwef'
        label_for_result['text'] = Permutations.Password.matrix(mass[self.__counter])
        counter += 1
    elif counter == 1:
        label_for_password['text'] = 'fwefw'
        counter += 1
