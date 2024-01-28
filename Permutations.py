from passKeyСipher import charToNum
from math import fabs
from classesOfExceptions import PasswordError

class Password:
    @staticmethod
    def matrix(charlist: str) -> str:
        if len(charlist) == 9:
            det_matrix = (charToNum[charlist[0]] * charToNum[charlist[4]] * charToNum[charlist[8]] +
                          charToNum[charlist[3]] * charToNum[charlist[7]] * charToNum[charlist[2]] + charToNum[charlist[1]]
                          * charToNum[charlist[5]] * charToNum[charlist[6]] - charToNum[charlist[6]] *
                          charToNum[charlist[4]] * charToNum[charlist[2]] - charToNum[charlist[0]] * charToNum[charlist[7]]
                          * charToNum[charlist[5]] - charToNum[charlist[1]] * charToNum[charlist[3]] *
                          charToNum[charlist[8]])
            return str(fabs(det_matrix))[0]
        else:
            raise PasswordError("Too few characters")
    @staticmethod
    def srt(nums: int) -> str:
        pass