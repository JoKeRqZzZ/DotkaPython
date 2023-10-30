import random
heroes = {
    'Abaddon': {"Primary Attribute": "Universal", "Role": ["pos4", "pos5"], "Health": 604},
    'Alchemist': {"Primary Attribute": "Strength", "Role": ["pos1", "pos2", "pos3"], "Health": 625},
    "Ancient Apparition":{"Primary Attribute": "Intelligence", "Role": ["pos4", "pos5"], "Health": 560},
    'Anti-Mage':{"Primary Attribute": "Agility", "Role": ["pos1"], "Health": 538},
    'Arc Warden':{"Primary Attribute": "Agility", "Role": ["pos1","pos2"], "Health": 604},
    "Axe":{"Primary Attribute": "Strength", "Role": ["pos3"], "Health": 670},
    'Bane':{"Primary Attribute": "Universal", "Role": ["pos4", "pos5"],"Health": 626},
    'Batrider':{"Primary Attribute": "Universal", "Role": ["pos2","pos3","pos4"],"Health": 736},
    'Beastmaster':{"Primary Attribute": "Universal", "Role": ["pos3"], "Health": 670},
    'Bloodseeker':{"Primary Attribute": "Agility", "Role": ["pos1"], "Health": 648},
    'Bounty Hunter':{"Primary Attribute": "Agility", "Role": ["pos4","pos5"], "Health": 538},
    'Brewmaster':{"Primary Attribute": "Universal", "Role": ["pos3"], "Health": 626},
    'Bristleback':{"Primary Attribute": "Strength", "Role": ["pos3"], "Health": 604},
    'Broodmother':{"Primary Attribute": "Universal", "Role": ["pos2", "pos3"], "Health":538},
    'Centaur Warrunner':{"Primary Attribute": "Strength", "Role": ["pos3"], "Health": 714},
    'Chaos Knight':{"Primary Attribute": "Strength", "Role": ["pos1", "pos3"], "Health": 648},
    'Chen':{"Primary Attribute": "Universal", "Role": ["pos4","pos5"], "Health": 626},
    'Clinkz':{"Primary Attribute": "Agility", "Role": ["pos4","pos5"], "Health": 494},
    'Clockwerk':{"Primary Attribute": "Universal", "Role": ["pos4","pos5"], "Health": 714},
    'Crystal Maiden':{"Primary Attribute": "Intelligence", "Role": ["pos4","pos5"], "Health": 494},
    'Dawnbreaker': {"Primary Attribute": "Strength", "Role": ["pos3"], "Health": 604},
    'Dark Seer': {"Primary Attribute": "Universal", "Role": ["pos3"], "Health": 560},
    'Dark Willow': {"Primary Attribute": "Universal", "Role": ["pos4","pos5"], "Health": 670},
    'Dazzle': {"Primary Attribute": "Universal", "Role": ["pos2", "pos4","pos5"], "Health": 516},
    "Death Prophet": {"Primary Attribute": "Intelligence", "Role": ["pos2","pos3"], "Health": 582},
    "Disruptor": {"Primary Attribute": "Intelligence", "Role": ["pos4","pos5"], "Health": 582},
    "Doom": {"Primary Attribute": "Strength", "Role": ["pos2","pos3"], "Health": 648},
    "Dragon Knight": {"Primary Attribute": "Strength", "Role": ["pos2", "pos3"], "Health": 582},
    'Drow Ranger': {"Primary Attribute": "Agility", "Role": ["pos1"], "Health": 472},
    'Earth Spirit': {"Primary Attribute": "Strength", "Role": ["pos2", "pos4"], "Health": 604},
    'Earthshaker': {"Primary Attribute": "Strength", "Role": ["pos2", "pos4"], "Health": 604},
    'Elder Titan': {"Primary Attribute": "Strength", "Role": ["pos3", "pos4","pos5"], "Health": 692},
    'Ember Spirit': {"Primary Attribute": "Agility", "Role": ["pos2"], "Health": 604},
    'Enchantress': {"Primary Attribute": "Intelligence", "Role": ["pos4","pos5"], "Health": 494},
    'Enigma': {"Primary Attribute": "Universal", "Role": ["pos3"], "Health": 582},
    'Faceless Void': {"Primary Attribute": "Agility", "Role": ["pos1"], "Health": 560},
    'Grimstroke': {"Primary Attribute": "Intelligence", "Role": ["pos4","pos5"], "Health": 582},
    'Gyrocopter': {"Primary Attribute": "Agility", "Role": ["pos1","pos4"], "Health": 604},
    "Hoodwink": {"Primary Attribute": "Agility", "Role": ["pos4","pos5"], "Health": 494},
    'Huskar': {"Primary Attribute": "Strength", "Role": ["pos2"], "Health": 626},
    'Invoker': {"Primary Attribute": "Universal", "Role": ["pos2"], "Health": 538},
    'Io': {"Primary Attribute": "Universal", "Role": ["pos2", "pos4","pos5"], "Health": 494},
    'Jakiro': {"Primary Attribute": "Intelligence", "Role": ["pos4","pos5"], "Health": 670},
    'Juggernaut': {"Primary Attribute": "Agility", "Role": ["pos1"], "Health": 560},
    'Keeper of the Light': {"Primary Attribute": "Intelligence", "Role": ["pos2","pos4","pos5"], "Health": 516},
    'Kunkka': {"Primary Attribute": "Strength", "Role": ["pos2", "pos3"], "Health": 648},
    'Legion Commander': {"Primary Attribute": "Strength", "Role": ["pos3"], "Health": 626},
    'Leshrac': {"Primary Attribute": "Intelligence", "Role": ["pos2"], "Health": 560},
    'Lich': {"Primary Attribute": "Intelligence", "Role": ["pos4","pos5"], "Health": 560},
    'Lifestealer': {"Primary Attribute": "Strength", "Role": ["pos1"], "Health": 670},
    'Lina': {"Primary Attribute": "Intelligence", "Role": ["pos2"], "Health": 560},
    'Lion': {"Primary Attribute": "Intelligence", "Role": ["pos4","pos5"], "Health": 516},
    'Lone Druid': {"Primary Attribute": "Universal", "Role": ["pos1","pos2","pos3"], "Health": 560},
    'Luna': {"Primary Attribute": "Intelligence", "Role": ["pos1"], "Health": 582},
    'Lycan': {"Primary Attribute": "Universal", "Role": ["pos2","pos3"], "Health": 692},
    'Magnus': {"Primary Attribute": "Universal", "Role": ["pos3"], "Health": 670},
    'Mars': {"Primary Attribute": "Strength", "Role": ["pos3"], "Health": 626},
    'Marsi': {"Primary Attribute": "Universal", "Role": ["pos1","pos4","pos5"], "Health": 626},
    'Medusa': {"Primary Attribute": "Agility", "Role": ["pos1"], "Health": 120+375},
    'Meepo': {"Primary Attribute": "Agility", "Role": ["pos2"], "Health": 648},
    'Mirana': {"Primary Attribute": "Universal", "Role": ["pos4","pos5"], "Health": 560},
    'Muerta': {"Primary Attribute": "Intelligence", "Role": ["pos1"], "Health": 516},
    'Monkey King': {"Primary Attribute": "Agility", "Role": ["pos1", "pos2"], "Health": 626},
    'Morphling': {"Primary Attribute": "Agility", "Role": ["pos1", "pos2"], "Health": 538},
    'Naga Siren': {"Primary Attribute": "Agility", "Role": ["pos1"], "Health": 582},
    'Natures Prophet': {"Primary Attribute": "Intelligence", "Role": ["pos3","pos4","pos5"], "Health": 538},
    'Necrophos': {"Primary Attribute": "Intelligence", "Role": ["pos2","pos3"], "Health": 516},
    'Night Stalker': {"Primary Attribute": "Strength", "Role": ["pos3"], "Health": 626},
    'Nyx Assassin': {"Primary Attribute": "Universal", "Role": ["pos4"], "Health": 494},
    'Ogre Magi': {"Primary Attribute": "Strength", "Role": ["pos4","pos5"], "Health": 626},
    'Omniknight': {"Primary Attribute": "Strength", "Role": ["pos3","pos5"], "Health": 626},
    'Oracle': {"Primary Attribute": "Intelligence", "Role": ["pos4","pos5"], "Health": 560},
    'Outworld Destroyer': {"Primary Attribute": "Intelligence", "Role": ["pos2"], "Health": 582},
    'Pangolier': {"Primary Attribute": "Universal", "Role": ["pos2","pos3"], "Health": 538},
    'Phantom Assassin': {"Primary Attribute": "Agility", "Role": ["pos1"], "Health": 538},
    'Phantom Lancer': {"Primary Attribute": "Agility", "Role": ["pos1"], "Health": 538},
    'Phoenix': {"Primary Attribute": "Universal", "Role": ["pos3","pos4","pos5"], "Health": 626},
    'Puck': {"Primary Attribute": "Intelligence", "Role": ["pos2"], "Health": 692},
    "Primal Beast" : {"Primary Attribute": "Strength", "Role": ["pos2","pos3"], "Health": 494},
    'Pudge': {"Primary Attribute": "Strength", "Role": ["pos3","pos4","pos5"], "Health": 670},
    'Pugna': {"Primary Attribute": "Intelligence", "Role": ["pos2","pos4","pos5"], "Health": 538},
    'Queen of Pain': {"Primary Attribute": "Intelligence", "Role": ["pos2"], "Health": 516},
    'Razor': {"Primary Attribute": "Agility", "Role": ["pos1","pos3"], "Health": 604},
    'Riki': {"Primary Attribute": "Agility", "Role": ["pos1"], "Health": 516},
    'Rubick': {"Primary Attribute": "Intelligence", "Role": ["pos4","pos5"], "Health": 582},
    'Sand King': {"Primary Attribute": "Universal", "Role": ["pos3"], "Health": 604},
    'Shadow Demon': {"Primary Attribute": "Intelligence", "Role": ["pos4","pos5"], "Health": 626},
    'Shadow Fiend': {"Primary Attribute": "Agility", "Role": ["pos1", "pos2"], "Health": 538},
    'Shadow Shaman': {"Primary Attribute": "Intelligence", "Role": ["pos4","pos5"], "Health": 626},
    'Silencer': {"Primary Attribute": "Intelligence", "Role": ["pos4","pos5"], "Health": 538},
    'Skywrath Mage': {"Primary Attribute": "Intelligence", "Role": ["pos4","pos5"], "Health": 582},
    'Slardar': {"Primary Attribute": "Strength", "Role": ["pos3"], "Health": 582},
    'Slark': {"Primary Attribute": "Agility", "Role": ["pos1"], "Health": 560},
    'Snapfire': {"Primary Attribute": "Universal", "Role": ["pos4","pos5"], "Health": 582},
    'Sniper': {"Primary Attribute": "Agility", "Role": ["pos1","pos2"], "Health": 538},
    'Spectre': {"Primary Attribute": "Agility", "Role": ["pos1"], "Health": 582},
    'Spirit Breaker': {"Primary Attribute": "Strength", "Role": ["pos3","pos4","pos5"], "Health": 736},
    'Storm Spirit': {"Primary Attribute": "Intelligence", "Role": ["pos2"], "Health": 582},
    'Sven': {"Primary Attribute": "Strength", "Role": ["pos1"], "Health": 604},
    'Techies': {"Primary Attribute": "Universal", "Role": ["pos4","pos5"], "Health": 538},
    'Templar Assassin': {"Primary Attribute": "Agility", "Role": ["pos1", "pos2"], "Health": 626},
    'Terrorblade': {"Primary Attribute": "Agility", "Role": ["pos1"], "Health": 472},
    'Tidehunter': {"Primary Attribute": "Strength", "Role": ["pos3"], "Health": 714},
    'Timbersaw': {"Primary Attribute": "Universal", "Role": ["pos3"], "Health": 670},
    'Tinker': {"Primary Attribute": "Intelligence", "Role": ["pos2"], "Health": 538},
    'Tiny': {"Primary Attribute": "Strength", "Role": ["pos2","pos4","pos5"], "Health": 780},
    'Treant Protector': {"Primary Attribute": "Strength", "Role": ["pos4","pos5"], "Health": 670},
    'Troll Warlord': {"Primary Attribute": "Agility", "Role": ["pos1"], "Health": 582},
    'Tusk': {"Primary Attribute": "Strength", "Role": ["pos4","pos5"], "Health": 626},
    'Underlord': {"Primary Attribute": "Strength", "Role": ["pos3"], "Health": 670},
    'Undying': {"Primary Attribute": "Strength", "Role": ["pos5"], "Health": 604},
    'Ursa': {"Primary Attribute": "Agility", "Role": ["pos1"], "Health": 670},
    'Vengeful Spirit': {"Primary Attribute": "Universal", "Role": ["pos3", "pos4", "pos5"], "Health": 560},
    'Venomancer': {"Primary Attribute": "Universal", "Role": ["pos3","pos4","pos5"], "Health": 538},
    'Viper': {"Primary Attribute": "Agility", "Role": ["pos2","pos3"], "Health": 582},
    'Visage': {"Primary Attribute": "Universal", "Role": ["pos2","pos3"], "Health": 604},
    'Void Spirit': {"Primary Attribute": "Universal", "Role": ["pos2"], "Health": 582},
    'Warlock': {"Primary Attribute": "Intelligence", "Role": ["pos5"], "Health": 648},
    'Weaver': {"Primary Attribute": "Agility", "Role": ["pos1","pos4","pos5"], "Health": 472},
    'Windranger': {"Primary Attribute": "Universal", "Role": ["pos1","pos2","pos3"], "Health": 516},
    'Winter Wyvern': {"Primary Attribute": "Universal", "Role": ["pos5", "pos4", "pos3"], "Health": 560},
    'Witch Doctor': {"Primary Attribute": "Intelligence", "Role": ["pos5", "pos4"], "Health": 560},
    'Wraith King': {"Primary Attribute": "Strength", "Role": ["pos1"], "Health": 604},
    'Zeus': {"Primary Attribute": "Intelligence", "Role": ["pos2","pos4"], "Health": 538}
}

items = {
    'Blink Dagger': {"Price": 200},
    'Black King Bar': {"Price": 400},
    'Butterfly': {"Price": 300},
    'Desolator': {"Price": 350},
    'Eye of Skadi': {"Price": 500},
    'Heart of Tarrasque': {"Price": 600},
    'Monkey King Bar': {"Price": 450},
    'Radiance': {"Price": 550},
    'Sange and Yasha': {"Price": 350},
    'Scythe of Vyse': {"Price": 400}
}

lanes = {
    "Top",
    "Middlane",
    "Bottom"
}
def choose_hero():
    print("Choose a hero:")
    for hero in heroes:
        print(hero)
    hero_name = input("Enter the name of the hero: ")
    return hero_name


def choose_items(hero):
    hero_coins = 600
    chosen_items = []
    while hero_coins > 0:
        print(f"Current coins: {hero_coins}")
        print("Choose an item:")
        for item, data in items.items():
            if data["Price"] <= hero_coins:
                print(f"{item} - {data['Price']} coins")
        item_name = input("Enter the name of the item (leave blank to end): ")
        if item_name == "":
            break
        if item_name not in items.keys():
            print("Invalid item name. Please try again.")
            continue
        item_price = items[item_name]["Price"]
        if item_price > hero_coins:
            print("You don't have enough coins for this item. Please choose another one.")
            continue
        chosen_items.append(item_name)
        hero_coins -= item_price
    return chosen_items

def battle(hero, enemy,):
    hero_health = heroes[hero]["Health"]
    enemy_health = heroes[enemy]["Health"]
    print(f"начинается сражение между  {hero} и {enemy}")
    print(f"{hero}: {hero_health} HP")
    print(f"{enemy}: {enemy_health} HP")
    while hero_health > 0 and enemy_health > 0:
        print("выберите че делать:")
        print("1.атака")
        print("2.защита")
        action = input("Enter your choice: ")
        if action == "1":
            enemy_health -= random.randint(40, 60)
        elif action == "2":
            hero_health += random.randint(40, 60)
        else:
            print("нет такой команды.")
            continue
        hero_health -= random.randint(30, 60)
        print(f"{hero}: {hero_health} HP")
        print(f"{enemy}: {enemy_health} HP")
    if hero_health <= 0:
        print(f"{enemy} победил!")
    else:
        print(f"{hero} победил!")


def Game():
    hero_name = choose_hero()
    hero = heroes.get(hero_name)
    if hero is None:
        print("Invalid hero name. Exiting...")
        return
    chosen_items = choose_items(hero)
    print(f"Chosen items: {chosen_items}")

    for i in range(5):
        enemy = random.choice(list(heroes.keys()))
        battle(hero_name, enemy)


Game()






