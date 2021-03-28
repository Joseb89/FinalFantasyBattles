from abc import ABC
from random import randint


class Character(ABC):

    def __init__(self):

        self.name = None
        self.hp = None
        self.attack = None
        self.defense = None
        self.stats = None

        # List of hero characters: [Name, HP, Attack, Defense]
        self.__heroes = {1: ["Tidus", 2000, 15, 25], 2: ["Squall Leonhart", 3000, 20, 30],
                         3: ["Zidaine", 2500, 18, 27], 4: ["Cloud", 2000, 22, 24], 5: ["Vaan", 2700, 18, 24]}

        # List of villain characters: [Name, HP, Attack, Defense]
        self.__villains = {1: ["Bahamut", 4000, 15, 30], 2: ["Gilgamesh", 4500, 18, 32],
                           3: ["Ultima", 5500, 20, 35], 4: ["Omega", 6000, 23, 37], 5: ["Yiazmat", 7500, 30, 40]}

    def get_heroes(self):
        return self.__heroes

    def get_villains(self):
        return self.__villains

    @staticmethod
    def get_dictionary(dictionary):
        return dictionary

    @staticmethod
    def display_selections(dictionary):
        for key in dict(dictionary).keys():
            print(f'{key}: {dictionary[key][0]}')

    def select_character(self, dictionary, prompt):

        print(prompt)

        try:
            x = int(input())
            if x <= 0 or x > len(self.__heroes) or x > len(self.__villains):
                print("Invalid entry")

            else:
                self.name = dictionary[x][0]
                self.hp = dictionary[x][1]
                self.attack = dictionary[x][2]
                self.defense = dictionary[x][3]
                self.stats = [self.name, self.hp, self.attack, self.defense]

        except ValueError:
            print("x must be an integer")

    def display_stats(self):
        print(f'You selected {self.name}\n\nHP: {str(self.hp)}\n\n'
              f'Attack: {str(self.attack)}\n\nDefense: {str(self.defense)}\n\n')

    def attack_character(self, opponent_stats, min_multiplier, max_multiplier):

        opponent_name = opponent_stats[0]
        opponent_hp = opponent_stats[1]
        opponent_defense = opponent_stats[3]

        attk_multiplier = randint(min_multiplier, max_multiplier)

        total_attk = self.attack * attk_multiplier
        total_damage = total_attk - opponent_defense
        reduced_hp = opponent_hp - total_damage

        print(f'{self.name} did {str(total_damage)} damage to {opponent_name}.')

        if reduced_hp <= 0:
            print(f'{self.name} has defeated {opponent_name}.')
            exit(0)

        else:
            opponent_stats[1] = reduced_hp  # Opponent's new HP
            print(f'{opponent_name}\'s HP: {reduced_hp}')


class Hero(Character):
    hero_prompt = "Select your hero: "


class Villain(Character):
    villain_prompt = "Select your opponent: "
