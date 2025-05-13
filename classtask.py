class MoringaEmployee:
    def __init__(self, first_name, last_name, salary, gender, dob, employment_date):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f"{first_name.lower()}{last_name.lower()}@moringaschool.com"
        self.salary = salary
        self.gender = gender
        self.dob = dob
        self.age = 2025 - self.dob 
        self.employment_date = employment_date

    def years_of_employment(self):
        current_year = 2025 
        years = current_year - self.employment_date
        return f"You've been employed for {years} years"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def age_message(self):
        if self.age > 50:
            return "Need to call it quits Old timer and retire"
        elif self.age > 40:
            return "It's about time to consider retiring"
        elif self.age > 30:
            return "It's about time to think about having kids"
        elif self.age > 25:
            return "It's about time to consider marriage"
        else:
            return "You're still young!"
        
#Example 
employee = MoringaEmployee("Adrian", "Maduafokwa",120000,"Male",2002,2017)
print(f"Full Name: {employee.full_name()}")
print(f"Email: {employee.email}")
print(f"Age: {employee.age}")
print(f"Salary: Ksh {employee.salary}")
print(f"Years of Employment: {employee.years_of_employment()}")
print(f"Feedback: {employee.age_message()}")