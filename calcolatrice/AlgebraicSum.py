from typing import Tuple, List


class AlgebraicSum:
    @staticmethod
    def check_sign(n1: float, n2: float) -> List[str]:
        pp, pm, mp, mm = ['plus', 'plus'], ['plus', 'minus'], ['minus', 'plus'], ['minus', 'minus']
        # first sign: plus -> the operation will be sum, minus-> the operation will be subtraction
        # second sign: the sign of the result
        signs = {'TrueTrueTrue': pp, 'TrueTrueFalse': pp, 'FalseFalseFalse': pm, 'FalseFalseTrue': pm, 'TrueFalseTrue':
                 mp, 'TrueFalseFalse': mm, 'FalseTrueTrue': mm, 'FalseTrueFalse': mp}
        return signs[str(n1 > 0) + str(n2 > 0) + str(n1 > n2)]

    @staticmethod
    def check_length(n1: float, n2: float) -> Tuple[str, str]:
        #in order to sum them column by column the 2 numbers and their integer_part must have the same numbers of digits
        max_ = max(n1, n2)
        min_ = min(n1, n2)
        int_n1_len = len(str(int(max_)))
        int_n2_len = len(str(int(min_)))
        n1 = str(max_)
        n2 = str(min_)
        while int_n1_len < int_n2_len:
            n1 = '0' + n1
            int_n1_len += 1
        while int_n2_len < int_n1_len:
            n2 = '0' + n2
            int_n2_len += 1
        while len(n1) < len(n2):
            n1 += '0'
        while len(n2) < len(n1):
            n2 += '0'
        return n1, n2

    def __init__(self, n1: float, n2: float):
        self.sign = AlgebraicSum.check_sign(n1, n2)
        self.n1, self.n2 = AlgebraicSum.check_length(abs(n1), abs(n2))

    def Sum(self) -> str:
        result = ''
        remainder = 0
        for digit_1, digit_2 in zip(self.n1[::-1], self.n2[::-1]):
            if digit_1 != '.':
                digit_result = int(digit_1) + int(digit_2) + remainder
                if digit_result > 9:
                    remainder = 1
                    digit_result -= 10
                else:
                    remainder = 0
            else:
                digit_result = '.'
            result = str(digit_result) + result
        return result

    def subtraction(self) -> str:
        result = ''
        remainder = 0
        for digit_1, digit_2 in zip(self.n1[::-1], self.n2[::-1]):
            if digit_1 != '.':
                digit_result = int(digit_1) - int(digit_2) - remainder
                if digit_result < 0:
                    digit_result += 10
                    remainder = 1
                else:
                    remainder = 0
            else:
                digit_result = '.'
            result = str(digit_result) + result
        return result

    def get_result(self):
        if self.sign[0] == 'minus':
            result = AlgebraicSum.subtraction(self)
        else:
            result = AlgebraicSum.Sum(self)
        if self.sign[1] == 'minus':
            return -float(result)
        return float(result)

    def print_info(self, n1, n2):
        result = AlgebraicSum.get_result(self)
        if all((n1 > 0, n2 > 0)):
            string = f'{n1} + {n2}'
        elif n1 < 0:
            string = f'{n1} + {n2}'
        else:
            string = f'{n1} {n2}'
        print(f'{string} = {result}')


op = AlgebraicSum(21.21, 0.223)
op.print_info(21.21, 0.223)
