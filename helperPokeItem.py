import helperBasic

TMListAll = (
    ("01A", "Dynamic Punch"),
    ("01B", "Focus Punch"),
    ("01C", "Hone Claws"),
    ("01D", "Mega Punch"),
    ("01E", "Work Up"),
    ("02A", "Dragon Claw"),
    ("02B", "Headbutt"),
    ("02C", "Razor Wind"),
    ("03A", "Curse"),
    ("03B", "Psyshock"),
    ("03C", "Water Pulse"),
    ("04A", "Calm Mind"),
    ("04B", "Rollout"),
    ("04C", "Whirlwind"),
    ("05A", "Mega Kick"),
    ("05B", "Roar"),
    ("06A", "Toxic"),
    ("07A", "Hail"),
    ("07B", "Horn Drill"),
    ("07C", "Zap Cannon"),
    ("08A", "Body Slam"),
    ("08B", "Bulk Up"),
    ("09A", "Bullet Seed"),
    ("09B", "Take Down"),
    ("09C", "Venoshock"),
    ("10A", "Double-Edge"),
    ("10B", "Hidden Power"),
    ("11A", "Bubble Beam"),
    ("11B", "Sunny Day"),
    ("12A", "Sweet Scent"),
    ("12B", "Taunt"),
    ("12C", "Water Gun"),
    ("13A", "Ice Beam"),
    ("13B", "Snore"),
    ("14A", "Blizzard"),
    ("15A", "Hyper Beam"),
    ("16A", "Icy Wind"),
    ("16B", "Light Screen"),
    ("16C", "Pay Day"),
    ("17A", "Protect"),
    ("17B", "Submission"),
    ("18A", "Counter"),
    ("18B", "Rain Dance"),
    ("19A", "Giga Drain"),
    ("19B", "Roost"),
    ("19C", "Seismic Toss"),
    ("19D", "Telekinesis"),
    ("20A", "Rage"),
    ("20B", "Safeguard"),
    ("21A", "Frustration"),
    ("21B", "Mega Drain"),
    ("22A", "Solar Beam"),
    ("23A", "Dragon Rage"),
    ("23B", "Iron Tail"),
    ("23C", "Smack Down"),
    ("24A", "Dragon Breath"),
    ("24B", "Thunderbolt"),
    ("25A", "Thunder"),
    ("26A", "Earthquake"),
    ("27A", "Fissure"),
    ("27B", "Return"),
    ("28A", "Dig"),
    ("28B", "Leech Life"),
    ("29A", "Psychic"),
    ("30A", "Shadow Ball"),
    ("30B", "Teleport"),
    ("31A", "Brick Break"),
    ("31B", "Mimic"),
    ("31C", "Mud-Slap"),
    ("32A", "Double Team"),
    ("33A", "Ice Punch"),
    ("33B", "Reflect"),
    ("34A", "Bide"),
    ("34B", "Shock Wave"),
    ("34C", "Sludge Wave"),
    ("35A", "Flamethrower"),
    ("35B", "Metronome"),
    ("36A", "Selfdestruct"),
    ("36B", "Sludge Bomb"),
    ("37A", "Egg Bomb"),
    ("37B", "Sandstorm"),
    ("38A", "Fire Blast"),
    ("39A", "Rock Tomb"),
    ("39B", "Swift"),
    ("40A", "Aerial Ace"),
    ("40B", "Defense Curl"),
    ("40C", "Skull Bash"),
    ("41A", "Softboiled"),
    ("41B", "Thunder Punch"),
    ("41C", "Torment"),
    ("42A", "Dream Eater"),
    ("42B", "Facade"),
    ("43A", "Detect"),
    ("43B", "Flame Charge"),
    ("43C", "Secret Power"),
    ("43D", "Sky Attack"),
    ("44A", "Rest"),
    ("45A", "Attract"),
    ("46A", "Psywave"),
    ("46B", "Thief"),
    ("47A", "Low Sweep"),
    ("47B", "Steel Wing"),
    ("48A", "Fire Punch"),
    ("48B", "Round"),
    ("48C", "Skill Swap"),
    ("49A", "Echoed Voice"),
    ("49B", "Fury Cutter"),
    ("49C", "Snatch"),
    ("49D", "Tri Attack"),
    ("50A", "Nightmare"),
    ("50B", "Overheat"),
    ("51A", "Ally Switch"),
    ("52A", "Focus Blast"),
    ("53A", "Energy Ball"),
    ("54A", "False Swipe"),
    ("55A", "Brine"),
    ("55B", "Scald"),
    ("56A", "Fling"),
    ("57A", "Charge Beam"),
    ("58A", "Endure"),
    ("58B", "Sky Drop"),
    ("59A", "Brutal Swing"),
    ("59B", "Dragon Pulse"),
    ("59C", "Incinerate"),
    ("60A", "Drain Punch"),
    ("60B", "Quash"),
    ("61A", "Will-O-Wisp"),
    ("62A", "Acrobatics"),
    ("62B", "Silver Wind"),
    ("63A", "Embargo"),
    ("64A", "Explosion"),
    ("65A", "Shadow Claw"),
    ("66A", "Payback"),
    ("67A", "Recycle"),
    ("67B", "Retaliate"),
    ("67C", "Smart Strike"),
    ("68A", "Giga Impact"),
    ("69A", "Rock Polish"),
    ("70A", "Aurora Veil"),
    ("70B", "Flash"),
    ("71A", "Stone Edge"),
    ("72A", "Avalanche"),
    ("72B", "Volt Switch"),
    ("73A", "Thunder Wave"),
    ("74A", "Gyro Ball"),
    ("75A", "Swords Dance"),
    ("76A", "Fly"),
    ("76B", "Stealth Rock"),
    ("76C", "Struggle Bug"),
    ("77A", "Psych Up"),
    ("78A", "Bulldoze"),
    ("78B", "Captivate"),
    ("79A", "Frost Breath"),
    ("80A", "Rock Slide"),
    ("81A", "X-Scissor"),
    ("82A", "Dragon Tail"),
    ("83A", "Infestation"),
    ("83B", "Natural Gift"),
    ("84A", "Poison Jab"),
    ("85A", "Dream Eater"),
    ("86A", "Grass Knot"),
    ("87A", "Swagger"),
    ("88A", "Pluck"),
    ("88B", "Sleep Talk"),
    ("89A", "U-turn"),
    ("90A", "Substitute"),
    ("91A", "Flash Cannon"),
    ("92A", "Trick Room"),
    ("93A", "Wild Charge"),
    ("94A", "Rock Smash"),
    ("94B", "Surf"),
    ("95A", "Snarl"),
    ("96A", "Nature Power"),
    ("97A", "Dark Pulse"),
    ("98A", "Power-Up Punch"),
    ("98B", "Waterfall"),
    ("99A", "Dazzling Gleam"),
    ("100A", "Confide"))

TMListSale = (
    ("01A", "Dynamic Punch", 1500),
    ("01B", "Focus Punch", 1500),
    ("01C", "Hone Claws", 1000),
    ("01D", "Mega Punch", 1500),
    ("02A", "Dragon Claw", 1500),
    ("02B", "Headbutt", 1000),
    ("02C", "Razor Wind", 1000),
    ("03A", "Curse", 1500),
    ("03C", "Water Pulse", 1500),
    ("04A", "Calm Mind", 1000),
    ("04B", "Rollout", 1000),
    ("04C", "Whirlwind", 500),
    ("05A", "Mega Kick", 1500),
    ("05B", "Roar", 750),
    ("06A", "Toxic", 750),
    ("07A", "Hail", 5000),
    ("07B", "Horn Drill", 1000),
    ("07C", "Zap Cannon", 1000),
    ("08A", "Body Slam", 2000),
    ("08B", "Bulk Up", 1000),
    ("09A", "Bullet Seed", 1000),
    ("09B", "Take Down", 1500),
    ("09C", "Venoshock", 1000),
    ("10A", "Double-Edge", 2000),
    ("10B", "Hidden Power", 1000),
    ("11A", "Bubble Beam", 1000),
    ("11B", "Sunny Day", 5000),
    ("12A", "Sweet Scent", 500),
    ("12B", "Taunt", 750),
    ("12C", "Water Gun", 500),
    ("13A", "Ice Beam", 1500),
    ("13B", "Snore", 500),
    ("14A", "Blizzard", 3000),
    ("15A", "Hyper Beam", 5000),
    ("16A", "Icy Wind", 1500),
    ("16B", "Light Screen", 1000),
    ("16C", "Pay Day", 2500),
    ("17A", "Protect", 1000),
    ("17B", "Submission", 1500),
    ("18A", "Counter", 1000),
    ("18B", "Rain Dance", 5000),
    ("19A", "Giga Drain", 1500),
    ("19B", "Roost", 1000),
    ("19C", "Seismic Toss", 1500),
    ("20A", "Rage", 1000),
    ("20B", "Safeguard", 1000),
    ("21A", "Frustration", 1000),
    ("21B", "Mega Drain", 2500),
    ("22A", "Solar Beam", 1000),
    ("23A", "Dragon Rage", 2500),
    ("23B", "Iron Tail", 1500),
    ("23C", "Smack Down", 1000),
    ("24A", "Dragon Breath", 1500),
    ("24B", "Thunderbolt", 1500),
    ("25A", "Thunder", 3000),
    ("26A", "Earthquake", 2000),
    ("27A", "Fissure", 2500),
    ("27B", "Return", 1000),
    ("28A", "Dig", 1000),
    ("29A", "Psychic", 1500),
    ("30A", "Shadow Ball", 1500),
    ("30B", "Teleport", 500),
    ("31A", "Brick Break", 1000),
    ("31B", "Mimic", 1000),
    ("31C", "Mud-Slap", 1500),
    ("32A", "Double Team", 1000),
    ("33A", "Ice Punch", 1500),
    ("33B", "Reflect", 1000),
    ("34A", "Bide", 1000),
    ("34B", "Shock Wave", 1500),
    ("34C", "Sludge Wave", 1000),
    ("35A", "Flamethrower", 1500),
    ("35B", "Metronome", 2000),
    ("36A", "Selfdestruct", 1000),
    ("36B", "Sludge Bomb", 2000),
    ("37A", "Egg Bomb", 1000),
    ("37B", "Sandstorm", 5000),
    ("38A", "Fire Blast", 3000),
    ("39A", "Rock Tomb", 1000),
    ("39B", "Swift", 1000),
    ("40A", "Aerial Ace", 1000),
    ("40B", "Defense Curl", 500),
    ("40C", "Skull Bash", 2000),
    ("41A", "Softboiled", 1000),
    ("41B", "Thunder Punch", 1500),
    ("41C", "Torment", 750),
    ("42A", "Dream Eater", 1500),
    ("42B", "Facade", 1000),
    ("43A", "Detect", 500),
    ("43C", "Secret Power", 1000),
    ("43D", "Sky Attack", 2500),
    ("44A", "Rest", 1500),
    ("45A", "Attract", 750),
    ("46A", "Psywave", 2000),
    ("46B", "Thief", 1000),
    ("47A", "Low Sweep", 1000),
    ("47B", "Steel Wing", 1000),
    ("48A", "Fire Punch", 1500),
    ("48B", "Round", 500),
    ("48C", "Skill Swap", 1500),
    ("49B", "Fury Cutter", 1500),
    ("49C", "Snatch", 750),
    ("49D", "Tri Attack", 2000),
    ("50A", "Nightmare", 1000),
    ("50B", "Overheat", 3500),
    ("51A", "Ally Switch", 1000),
    ("52A", "Focus Blast", 3000),
    ("53A", "Energy Ball", 1500),
    ("54A", "False Swipe", 1000),
    ("55A", "Brine", 1500),
    ("56A", "Fling", 1000),
    ("57A", "Charge Beam", 1000),
    ("58A", "Endure", 1000),
    ("59B", "Dragon Pulse", 2000),
    ("59C", "Incinerate", 500),
    ("60A", "Drain Punch", 1500),
    ("60B", "Quash", 750),
    ("61A", "Will-O-Wisp", 750),
    ("62B", "Silver Wind", 1500),
    ("63A", "Embargo", 1000),
    ("64A", "Explosion", 1500),
    ("65A", "Shadow Claw", 1000),
    ("66A", "Payback", 1000),
    ("67A", "Recycle", 500),
    ("67B", "Retaliate", 1500),
    ("68A", "Giga Impact", 5000),
    ("69A", "Rock Polish", 1000),
    ("70A", "Aurora Veil", 3000),
    ("70B", "Flash", 500),
    ("71A", "Stone Edge", 3000),
    ("72A", "Avalanche", 1500),
    ("72B", "Volt Switch", 1000),
    ("73A", "Thunder Wave", 500),
    ("74A", "Gyro Ball", 1000),
    ("75A", "Swords Dance", 1000),
    ("76B", "Stealth Rock", 1000),
    ("76C", "Struggle Bug", 1000),
    ("77A", "Psych Up", 1000),
    ("78A", "Bulldoze", 1000),
    ("78B", "Captivate", 750),
    ("79A", "Frost Breath", 1000),
    ("80A", "Rock Slide", 1500),
    ("81A", "X-Scissor", 1500),
    ("82A", "Dragon Tail", 1000),
    ("83B", "Natural Gift", 1000),
    ("84A", "Poison Jab", 1000),
    ("85A", "Dream Eater", 1500),
    ("86A", "Grass Knot", 1500),
    ("87A", "Swagger", 750),
    ("88A", "Pluck", 750),
    ("88B", "Sleep Talk", 500),
    ("89A", "U-turn", 1000),
    ("90A", "Substitute", 1000),
    ("91A", "Flash Cannon", 1500),
    ("92A", "Trick Room", 2750),
    ("93A", "Wild Charge", 5000),
    ("94A", "Rock Smash", 500),
    ("96A", "Nature Power", 1000),
    ("97A", "Dark Pulse", 1500),
    ("98A", "Power-Up Punch", 1000),
    ("98B", "Waterfall", 1500),
    ("100A", "Confide", 1000))

types = (
    ("Bug", "Silver Powder", "Insect Plate", "Bug Gem"),
    ("Dark", "Black Glasses", "Dread Plate", "Dark Gem"),
    ("Dragon", "Dragon Fang", "Draco Pltae", "Dragon Gem"),
    ("Electric", "Magnet", "Zap Plate", "Electric Gem"),
    ("Fairy", "Pink Candy", "Pixie Plate", "Fairy Gem"),
    ("Fighting", "Black Belt", "Fist Plate", "Fighting Gem"),
    ("Fire", "Charcoal", "Flame Plate", "Fire Gem"),
    ("Flying", "Sharp Beak", "Sky Plate", "Flying Gem"),
    ("Ghost", "Spell Tag", "Spooky Plate", "Ghost Gem"),
    ("Grass", "Miracle Seed", "Meadow Plate", "Grass Gem"),
    ("Ground", "Soft Sand", "Earth Plate", "Ground Gem"),
    ("Ice", "Never-Melt Ice", "Icicle Plate", "Ice Gem"),
    ("Normal", "Silk Scarf", "Regular Plate", "Normal Gem"),
    ("Poison", "Poison Barb", "Toxic Plate", "Poison Gem"),
    ("Psychic", "Twisted Spoon", "Mind Plate", "Psychic Gem"),
    ("Rock", "Hard Stone", "Stone Plate", "Rock Gem"),
    ("Steel", "Metal Coat", "Iron Plate", "Steel Gem"),
    ("Water", "Mystic Water", "Splash Plate", "Water Gem"))


pokeballs = ((5, "Basic Ball"),
             (2, "Great Ball"),
             (1, "Ultra Ball"),
             (1, "Level Ball"),
             (1, "Lure Ball"),
             (1, "Moon Ball"),
             (1, "Friend Ball"),
             (1, "Love Ball"),
             (1, "Love Ball"),
             (1, "Heavy Ball"),
             (1, "Fast Ball"),
             (1, "Sport Ball"),
             (1, "Premier Ball"),
             (1, "Repeat Ball"),
             (1, "Timer Ball"),
             (1, "Nest Ball"),
             (1, "Net Ball"),
             (1, "Dive Ball"),
             (1, "Luxury Ball"),
             (1, "Heal Ball"),
             (1, "Quick Ball"),
             (1, "Dusk Ball"))

enhancers = ((2, "X Attack"),
             (2, "X Defend"),
             (2, "X Special"),
             (2, "X Sp. Def"),
             (2, "X Speed"),
             (2, "X Accuracy"),
             (2, "Dire Hit"),
             (2, "Guard Spec."),
             (1, "Herbal Booster"),
             (1, "Endurance Root"),
             (1, "Quick Weed"))

vitamins = ((2, "HP Up"),
            (2, "Protein"),
            (2, "Iron"),
            (2, "Calcium"),
            (2, "Zinc"),
            (2, "Carbos"),
            (1, "PP Up"))

healing = ((3, "Potion"),
           (2, "Super Potion"),
           (1, "Hyper Potion"),
           (1, "MooMoo Milk"),
           (3, "Antidote"),
           (3, "Paralyze Heal"),
           (3, "Awakening"),
           (3, "Burn Heal"),
           (3, "Ice Heal"),
           (1, "Full Heal"),
           (2, "Revive"),
           (2, "Ether"),
           (1, "Elixer"),
           (2, "Energy Powder"),
           (1, "Energy Root"),
           (2, "Heal Powder"),
           (3, "Revival Herb"))


effectlessBerry = ("Razz Berry",
                   "Bluk Berry",
                   "Nanab Berry",
                   "Wepear Berry",
                   "Pinap Berry",
                   "Cornn Berry",
                   "Magost Berry",
                   "Rabuta Berry",
                   "Nomel Berry",
                   "Spelon Berry",
                   "Pamtre Berry",
                   "Watmel Berry",
                   "Durin Berry",
                   "Belue Berry")

one8Berry = ("Figy Berry",
             "Wiki Berry",
             "Mago Berry",
             "Aguav Berry",
             "Iapapa Berry")

healingBerry = ("Cheri Berry",
                "Chesto Berry",
                "Pecha Berry",
                "Rawst Berry",
                "Aspear Berry",
                "Leppa Berry",
                "Oran Berry",
                "Persim Berry",
                "Lum Berry",
                "Sitrus Berry")

superEffectBerry = ("Occa Berry",
                    "Passho Berry",
                    "Wacan Berry",
                    "Rindo Berry",
                    "Yache Berry",
                    "Chople Berry",
                    "Kebia Berry",
                    "Shuca Berry",
                    "Coba Berry",
                    "Payapa Berry",
                    "Tanga Berry",
                    "Charti Berry",
                    "Kasib Berry",
                    "Haban Berry",
                    "Colbur Berry",
                    "Babiri Berry",
                    "Chilan Berry",
                    "Roseli Berry")
        
loweringBerry = ("Pomeg Berry",
                 "Kelpsy Berry",
                 "Qualot Berry",
                 "Hondew Berry",
                 "Grepa Berry",
                 "Tamoto Berry")

per50Berry = ("Liechi Berry",
              "Ganlon Berry",
              "Salac Berry",
              "Petaya Berry",
              "Apicot Berry",
              "Kansat Berry",
              "Starf Berry")

damageBerry = ("Enigma Berry",
               "Micle Berry",
               "Custab Berry",
               "Jaboca Berry",
               "Rowab Berry",
               "Kee Berry",
               "Maranga Berry")

def Helper():
    returnVal = ""
    returnVal += "FUNCTION\n"
    returnVal += "\t Helper()\n"
    returnVal += "\t GenerateTM()\n"
    returnVal += "\t GenerateTMShopItem()\n"
    returnVal += "\t GenerateTMShop(size = 1)\n"
    returnVal += "\t GenerateBerry(roll = -1)\n"
    returnVal += "\t GenerateHealing()\n"
    returnVal += "\t GenerateBall()\n"
    returnVal += "\t GenerateEnhancer()\n"
    returnVal += "\t GenerateVitamin()\n"
    returnVal += "\t Pickup(roll = -1)\n"
    returnVal += "\t GenerateType()\n"
    returnVal += "\t GenerateTypeItem()\n"
    returnVal += "\t GenerateTypePlate()\n"
    returnVal += "\t GenerateTypeGem()\n"
    returnVal += "TABLE\n"
    retrunVal += "\t TMListAll\n"
    retrunVal += "\t TMListSale\n"
    retrunVal += "\t types\n"
    retrunVal += "\t pokeballs\n"
    retrunVal += "\t enhancers\n"
    retrunVal += "\t vitamins\n"
    retrunVal += "\t healing\n"
    retrunVal += "\t effectlessBerry\n"
    retrunVal += "\t one8Berry\n"
    retrunVal += "\t healingBerry\n"
    retrunVal += "\t superEffectBerry\n"
    retrunVal += "\t loweringBerry\n"
    retrunVal += "\t per50Berry\n"
    retrunVal += "\t damageBerry\n"
    return returnVal

def GenerateTM():
    global TMListAll
    return helperBasic.RandomList(TMListAll)

def GenerateTMShopItem():
    global TMListSale
    baseItem = helperBasic.RandomList(TMListSale)
    costMultiplier = (float(helperBasic.RollFull(2, 6, 0)) * 0.05) + 0.5
    return [baseItem[0], baseItem[1], int(float(baseItem[2]) * costMultiplier)]

def GenerateTMShop(size = 1):
    returnVal = []
    attemptCount = helperBasic.RollFull(1, 4, size)
    print(attemptCount)
    if(size == 1):
        for x in range(0, attemptCount):
            amount = helperBasic.RollFull(1, 4, -2)
            if(amount > 0):
                item = GenerateTMShopItem()
                item.append(amount)
                returnVal.append(item)
    elif(size == 2):
         for x in range(0, attemptCount):
            amount = helperBasic.RollFull(1, 6, -2)
            if(amount > 0):
                item = GenerateTMShopItem()
                item.append(amount)
                returnVal.append(item)
    elif(size == 3):
         for x in range(0, attemptCount):
            amount = helperBasic.RollFull(1, 8, -2)
            if(amount > 0):
                item = GenerateTMShopItem()
                item.append(amount)
                returnVal.append(item)

    return returnVal

def GenerateBerry(roll = -1):
    global effectlessBerry
    global one8Berry
    global healingBerry
    global superEffectBerry
    global loweringBerry
    global per50Berry
    global damageBerry

    if(roll == -1):
        roll = helperBasic.Roll(1, 20)
    
    if(roll <= 5):
        return helperBasic.RandomList(effectlessBerry)
    elif(roll <= 9):
        return helperBasic.RandomList(one8Berry)
    elif(roll <= 12):
        return helperBasic.RandomList(healingBerry)
    elif(roll <= 15):
        return helperBasic.RandomList(superEffectBerry)
    elif(roll <= 17):
        return helperBasic.RandomList(loweringBerry)
    elif(roll <= 19):
        return helperBasic.RandomList(per50Berry)
    else:
        return helperBasic.RandomList(damageBerry)

def GenerateHealing():
    global healing
    return helperBasic.RandomWeightedList(healing)[0]

def GenerateBall():
    global pokeballs
    return helperBasic.RandomWeightedList(pokeballs)[0]

def GenerateEnhancer():
    global enhancers
    return helperBasic.RandomWeightedList(enhancers)[0]

def GenerateVitamin():
    global vitamins
    return helperBasic.RandomWeightedList(vitamins)

def Pickup(roll = -1):
    
    if(roll == -1):
        roll = helperBasic.Roll(1, 20)
    
    if(roll <= 5):
        return "Nothing"
    elif(roll <= 8):
        return GenerateEnhancer()
    elif(roll <= 10):
        return GenerateBerry()
    elif(roll <= 12):
        return GenerateHealing()
    elif(roll <= 16):
        return GenerateBall()
    elif(roll == 17):
        return "Stone"
    elif(roll == 18):
        return GenerateVitamin()
    elif(roll == 19):
        return "Held Item"
    elif(roll == 20):
        return GenerateTM()

def GenerateType():
    global types
    return helperBasic.RandomList(types)[0]

def GenerateTypeItem():
    global types
    return helperBasic.RandomList(types)[1]

def GenerateTypePlate():
    global types
    return helperBasic.RandomList(types)[2]

def GenerateTypeGem():
    global types
    return helperBasic.RandomList(types)[3]
