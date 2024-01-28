from passKeyСipher import charToNum
from math import fabs
from classesOfExceptions import PasswordError
from random import choice


class Password:
    @staticmethod
    def matrix(charlist: str) -> str:
        if len(charlist) == 9 and charlist.isalpha():
            det_matrix = (charToNum[charlist[0]] * charToNum[charlist[4]] * charToNum[charlist[8]] +
                          charToNum[charlist[3]] * charToNum[charlist[7]] * charToNum[charlist[2]] + charToNum[
                              charlist[1]]
                          * charToNum[charlist[5]] * charToNum[charlist[6]] - charToNum[charlist[6]] *
                          charToNum[charlist[4]] * charToNum[charlist[2]] - charToNum[charlist[0]] * charToNum[
                              charlist[7]]
                          * charToNum[charlist[5]] - charToNum[charlist[1]] * charToNum[charlist[3]] *
                          charToNum[charlist[8]])
            return str(fabs(det_matrix))[0]
        else:
            raise PasswordError("Invalid characters")

    @staticmethod
    def actor(name: str) -> str:
        if name.isalpha():
            return choice(list(name)).upper()
        else:
            raise PasswordError("It is not name)")
