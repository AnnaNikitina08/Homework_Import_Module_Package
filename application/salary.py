class Salary:
    def __init__(self, rate, bonus):
        self.rate = rate
        self.bonus = bonus

        pass

    def calculate_salary(self):
        print(f'Заработная плата директора - {self.rate*self.bonus}')

