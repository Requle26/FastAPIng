class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"안녕하세요. 저는 {self.name}이고 {self.age}살입니다."

person = Person("김성일", 17)

print(person.name)
print(person.age)
print(person.introduce())

# --------------------------

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def show_score(self):
        print(f"{self.name} 학생의 점수는 {self.score}점입니다.")

student = Student("김성일", 95)
student.show_score()

# --------------------------

class Account:
    def __init__(self, amount):
        self.amount = amount
    def deposit(self, money):
        self.amount += money
    def withdraw(self, money):
        self.amount -= money
    def show_balance(self):
        print(f"현재 잔액: {self.amount}원")
    
account = Account(10000)
account.deposit(5000)
account.withdraw(3000)
account.show_balance()

# --------------------------

class Car:
    def __init__(self, speed = 0):
        self.speed = speed
    def accelerate(self):
        self.speed += 10
    def brake(self):
        if self.speed > 0:
            self.speed -= 10
    def show_speed(self):
        print(f"현재 속도: {self.speed}")

car = Car()
car.accelerate()
car.brake()
car.show_speed()