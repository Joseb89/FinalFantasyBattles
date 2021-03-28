from Character import *
import time

hero = Hero()
hero_dictionary = hero.get_dictionary(hero.get_heroes())


def call_hero_functions():
    hero.display_selections(hero_dictionary)
    hero.select_character(hero_dictionary, prompt=hero.hero_prompt)


villain = Villain()
villain_dictionary = villain.get_dictionary(villain.get_villains())


def call_villain_functions():
    villain.display_selections(villain_dictionary)
    villain.select_character(villain_dictionary, prompt=villain.villain_prompt)


call_hero_functions()
call_villain_functions()

time_delay = 1

if hero.stats is not None:
    hero.display_stats()

else:
    call_hero_functions()

if villain.stats is not None:
    villain.display_stats()

else:
    call_villain_functions()

confirm = input("Do you wish to proceed? (Y/N): ")

if confirm.upper() == "Y":
    pass

elif confirm.upper() == "N":
    call_hero_functions()
    call_villain_functions()

# stats[1] = HP
while hero.stats[1] > 0 and villain.stats[1] > 0:
    hero.attack_character(villain.stats, min_multiplier=6, max_multiplier=9)
    time.sleep(time_delay)
    villain.attack_character(hero.stats, min_multiplier=2, max_multiplier=5)
    time.sleep(time_delay)
