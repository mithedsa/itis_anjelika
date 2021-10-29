import time

class Tomogucci:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.satiety = 100

pet = Tomogucci("pet")

while pet.health > 0:
    pet.satiety -= 5
    time.sleep(2)
    def check_health():
        if pet.health == 0:
            del pet
        return pet.health

    def check_satiety():
        if pet.satiety == 0:
            pet.health -= 1
        return pet.satiety

    def feed_the_pet():
        command = input("если хотите накормить питомца, отправьте '+'")
        if command == "+":
            pet.satiety += 1
            print("здоровье: ", pet.satiety, "единиц")
        return pet.satiety
    print("Имя питомца:", pet.name, "Здоровье питомца:", pet.health, "Сытость питомца:", pet.satiety)
    feed_the_pet()
    print("сытость сейчас:", check_satiety())
    print("здоровье сейчас:", check_health())