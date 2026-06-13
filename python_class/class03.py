class Dog:
    def __init(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name}가 짖습니다!")
        
dog1 = Dog("멍멍이")
dog2 = Dog("초코")

dog1.bark()
dog2.bark()

# 출력 : 멍멍이가 짖습니다!
# 출력 : 초코가 짖습니다!

#--------------------------------

class Dog:
    def __init__(self, name):
        self.name = name

dog = Dog("초코")

print(dog.name)

# 출력 : 초코
# 설명 : 모르겠음

#--------------------------------

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    
    def attack(self, target):
        target.hp -= 10

hero = Character("전사", 100)
monster = Character("슬라임", 50)

hero.attack(monster)

print(hero.hp)
print(monster.hp)

# 출력 : 100
# 출력 : 40