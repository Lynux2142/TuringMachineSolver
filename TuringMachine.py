def get_triangle(n):
    return n // 100 % 10

def get_square(n):
    return n // 10 % 10

def get_circle(n):
    return n % 10

class Card:
    def __init__(self, n, case):
        self._triangle = get_triangle(n)
        self._square = get_square(n)
        self._circle = get_circle(n)
        self._value = False
        self._case = case
        self._case_name = ""
        self._case_list = []

    def get_result(self):
        self._case_list[self._case]()
        return self._value

    def get_case_name(self):
        self._case_list[self._case]()
        return self._case_name

    def get_case_number(self):
        return self._case

    def next_case(self):
        if self._case >= len(self._case_list) - 1:
            return False
        self._case += 1
        return True

    def reset_case(self):
        self._case = 0

class Card2(Card):
    def __init__(self, n, case=0):
        super().__init__(n, case)
        self._case_list = [self._case1, self._case2, self._case3]

    def _case1(self):
        self._case_name = "Triangle < 3"
        self._value = self._triangle < 3

    def _case2(self):
        self._case_name = "Triangle = 3"
        self._value = self._triangle == 3

    def _case3(self):
        self._case_name = "Triangle > 3"
        self._value = self._triangle > 3

class Card4(Card):
    def __init__(self, n, case=0):
        super().__init__(n, case)
        self._case_list = [self._case1, self._case2, self._case3]

    def _case1(self):
        self._case_name = "Square < 4"
        self._value = self._square < 4

    def _case2(self):
        self._case_name = "Square = 4"
        self._value = self._square == 4

    def _case3(self):
        self._case_name = "Square > 4"
        self._value = self._square > 4

class Card5(Card):
    def __init__(self, n, case=0):
        super().__init__(n, case)
        self._case_list = [self._case1, self._case2]

    def _case1(self):
        self._case_name = "Triangle is even"
        self._value = self._triangle % 2 == 0

    def _case2(self):
        self._case_name = "Triangle is odd"
        self._value = self._triangle % 2 == 1

class Card15(Card):
    def __init__(self, n, case=0):
        super().__init__(n, case)
        self._case_list = [self._case1, self._case2, self._case3]

    def _case1(self):
        self._case_name = "Triangle > (Square and Circle)"
        self._value = self._triangle > max(self._square, self._circle)

    def _case2(self):
        self._case_name = "Square > (Triangle and Circle)"
        self._value = self._square > max(self._triangle, self._circle)

    def _case3(self):
        self._case_name = "Circle > (Triangle and Square)"
        self._value = self._circle > max(self._triangle, self._square)

class Card16(Card):
    def __init__(self, n, case=0):
        super().__init__(n, case)
        self._case_list = [self._case1, self._case2]
        self._sum_odd_number = self._triangle % 2 + self._square % 2 + self._circle % 2

    def _case1(self):
        self._case_name = "Even > Odd"
        self._value = self._sum_odd_number <= 1

    def _case2(self):
        self._case_name = "Even < Odd"
        self._value = self._sum_odd_number > 1

class CardSet:
    def __init__(self, n, card_list):
        self._card_list = [card(n) for card in card_list]

    def test_number(self):
        for card in self._card_list:
            if not card.get_result():
                return False
        return True

    def next_case_config(self):
        for card in self._card_list:
            if card.next_case():
                return True
            else:
                card.reset_case()
        return False

    def get_config_set(self):
        return "".join([str(card._case) for card in self._card_list])

    def print_config(self):
        print(self.get_config_set())
        for card in self._card_list:
            print(card.get_case_name())

def main():
    solution = {}
    for triangle in range(1, 6):
        for square in range(1, 6):
            for circle in range(1, 6):
                n = triangle * 100 + square * 10 + circle
                test = CardSet(n, [Card4, Card5, Card15, Card16])
                if test.test_number():
                    config_set = test.get_config_set()
                    if config_set in solution:
                        solution[config_set][1].append(n)
                    else:
                        solution[config_set] = (1, [n])
                while test.next_case_config():
                    if test.test_number():
                        config_set = test.get_config_set()
                        if config_set in solution:
                            solution[config_set][1].append(n)
                        else:
                            solution[config_set] = (1, [n])
    for elem in solution:
        print(f"{elem}: {solution[elem]}")

if __name__ == "__main__":
    main()
