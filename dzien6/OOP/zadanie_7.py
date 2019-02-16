from zad_2 import Employee


class PremiumEmployee(Employee):

    def __init__(self, name, last_name, rate_per_hour):
        super().__init__(name, last_name, rate_per_hour)
        self.bonus = 0

    def give_bonus(self, amount):
        self.bonus += amount

    def pay_salary(self):
        to_pay = super().pay_salary() + self.bonus
        self.bonus = 0
        return to_pay

def test_premium_employee_give_bonus():
    employee = PremiumEmployee("Jan", "Słodowy", 100)
    employee.register_time(5)
    employee.give_bonus(1000)
    assert employee.pay_salary() == 1500
    assert employee.pay_salary() == 0
