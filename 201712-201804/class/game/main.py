import random
class Game:
    def __init__(self, user, hp, at_name):
        self.user = user
        self.hp = hp

    def attack(self):
        for i in range(10):
            hero_cnt = random.randint(1, 5)
            enemy_cnt = random.randint(1, 5)
            print(hero_cnt)


user1 = Game('自分', 50, '必殺技')

user1.attack()