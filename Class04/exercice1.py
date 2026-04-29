class Employee:
    bonus = 0.25
    base_salary = 500
    company_name = "Tech Solutions"

    def __init__(self, name, sales_count):
        self.name = name
        self.sales_count = sales_count
    def employee_salary(self):
        if(self.sales_count > 10):
             bonus_amount = self.base_salary * self.bonus * self.sales_count
             return self.base_salary + bonus_amount
        else:
            return self.base_salary
employee1 = Employee("John Doe", 12)
employee2 = Employee("Jane Smith", 8)
print(employee1.employee_salary()) # Output: 2000
print(employee2.employee_salary()) # Output: 500
