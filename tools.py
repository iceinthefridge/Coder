class Binary:
    def __init__(self, string):
        self.number = [self.__get_binary(ord(i)) for i in string]


    def __get_binary(self, number):
        result = []
        while number != 1 and number != 0:
            result.append(number%2)
            number = number // 2
        result.append(number)
        return tuple(result[::-1])

