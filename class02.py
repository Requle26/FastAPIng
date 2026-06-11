class Character:
    def __init__(self, character, health):
        self.character = character
        self.health = health
    def take_damage(self, damage):
        self.health -= damage
    def show_status(self):
        print(f"{self.character}의 체력: {self.health}")
    def attack(self, monster):
        monster.health -= 10
        print(f"{self.character}가 {monster.character}을/를 공격했습니다.")



hero = Character("전사", 100)
hero.take_damage(30)
hero.show_status()

monster = Character("슬라임", 50)
hero.attack(monster)

#------------------------------
