import enum

class Experience(enum.Enum):
    none = 0
    levies = 1
    regular = 2
    veteran = 3
    elite = 4
    superelite = 5

class Equipment(enum.Enum):
    none = 0
    light = 1
    medium = 2
    heavy = 3
    superheavy = 4

class Type(enum.Enum):
    none = 0
    aerial = 1
    artillery = 2
    cavalry = 3
    infantry = 4

class Ancestry(enum.Enum):
    none = 0
    barbeddevil = 1
    bugbear = 2
    construct = 3
    dragonborn = 4
    drow = 5
    dwarf = 6
    elf = 7
    ghoul = 8
    gnoll = 9
    gnome = 10
    goblin = 11
    goliath = 12
    halfling = 13
    hobgoblin = 14
    human = 15
    kenku = 16
    kobold = 17
    lizardfolk = 18
    ogre = 19
    orc = 20
    skeleton = 21
    tortle = 22
    triton = 23
    troll = 24
    wight = 25
    wraith = 26
    yuanti = 27
    zombie = 28

class Trait(enum.Enum):
    none = 0
    AAAUUUGH = 1
    Adaptable = 2
    AerialBombardment = 3
    Amphibious = 4
    Arcadian = 5
    Archers = 6
    ArmoredCarapace = 7
    Barbs = 8
    BattleHymn = 9
    BetterthanOne = 10
    Big = 11
    BlanketFire = 12
    Blinding = 13
    Burning = 14
    Burrow = 15
    ChaosVulnerability = 16
    Charge = 17
    ChourusofVictory = 18
    CloseRange= 19
    CloudofDarkness = 20
    CollateralDamage = 21
    Consume = 22
    Corrode = 23
    CorrosiveBreath = 24
    CreateDead = 25
    DamageResistant = 26
    DaylightWeakness = 27
    Dead = 28
    Dig = 29
    DireHyenaMounts = 30
    Distruptive = 31
    DraconicAncestry = 32
    Dragonkin = 33
    Drone = 34
    ElfShot = 35
    Embiggen = 36
    Eternal = 37
    Ethereal = 38
    Fade = 39
    FastSiegeWeapon = 40
    FastSiegeWeaponHeavy = 41
    Fearless = 42
    Fearsome = 43
    Feast = 44
    FireBlast = 45
    FireBreath = 46
    FireImmunity = 47
    FlamingWeapons = 48
    FollowtheStandart = 49
    Guerrillas = 50
    Gulp = 51
    HallucinatorySpores = 52
    HardHats = 53
    Harriers = 54
    Harrowing = 55
    HeroesoftheMyriadWorlds = 56
    Holy = 57
    Hop = 58
    Implacable = 59
    Indistinct = 60
    Inexorable = 61
    InspireFear = 62
    IntotheBreach = 63
    Invisibility = 64
    Jaunt = 65
    LightningBreath = 66
    LoadtheBones = 67
    MagicResistant = 68
    MagicalAdepts = 69
    ManeuverDetonate = 70
    ManeuverEvasiveManeuvers = 71
    ManeuverFire = 72
    ManeuverHoldtheLine = 73
    ManeuverLancersFlankThem = 74
    ManeuverLandandCharge = 75
    ManeuverOutflank = 76
    ManeuverPreyontheWeak = 77
    ManeuverRamThem = 78
    ManeuverRepair = 79
    ManeuverSpitUponTheirHorns = 80
    ManeuverStrafe = 81
    ManeuverTestudo = 82
    MassProtectionAgainstEvil = 83
    Meld = 84
    Mobile = 85
    NaturesBond = 86
    NoxiousFog = 87
    PackPactics = 88
    PikeTraining = 89
    PointBlank = 90
    Poisonous = 91
    PoolofSoulsBlood = 92
    Quadruped = 93
    RamRiders = 94
    Reckless = 95
    Reflector = 96
    Regenerate = 97
    Relentless = 98
    Resolute = 99
    Rime = 100
    Rock = 101
    Rockbreaker = 102
    RollingThunder = 103
    Rush = 104
    Savage = 105
    ScourgeoftheWild = 106
    Scouts = 107
    Screech = 108
    ShockTroups = 109
    SiegeEngine = 110
    SiegeWeapon = 111
    Slam = 112
    SmokeScreen = 113
    SolarFlare = 114
    SoporificSpores = 115
    SowChaos = 116
    SpikeShot = 117
    Split = 118
    Spores = 119
    Stalwart = 120
    Stinky = 121
    Stone = 122
    Stoneskin = 123
    StrengthinNumbers = 124
    Stupid = 125
    SwordsoftheDragonLord = 126
    TotheDeath = 127
    VeteransofaThousandWars = 128
    Wail = 129
    Warbred = 130
    Wave = 131
    Whirlwind = 132
    YouFollow = 133
    

class Upgrade(enum.Enum):
    none = 0
    hawk = 1
    pegasus = 2
    direwasp = 3
    wyvern = 4
    orccatapult = 5
    catapult = 6
    ballista = 7
    crossbow = 8
    longbow = 9
    boltthrower = 10
    bonebow = 11
    undeadcatapult = 12
    cannon = 13
    riffle = 14
    smoker = 15
    horse = 16
    ram = 17
    elk = 18
    nightmare = 19
    worg = 20
    direhyena = 21
    lance = 22
    engineer = 23
    pike = 24
    shield = 25
    grenade = 26
    sapper = 27
    miner = 28
    wounded = 29
    artisan = 30
    extraatk = 31
    extradef = 32
    extrapow = 33
    extratou = 34
    extramor = 35
    
    
types = {
    Type.aerial: (5, 0, 3, -2, 0, 0),
    Type.artillery: (3, 0, 2, -2, 0, 0),
    Type.cavalry: (3, 2, 3, 0, 0, 1),
    Type.infantry: (3, 2, 2, 2, 2, 0)
    }

experiences = {
    (Type.infantry, Experience.levies): (0, -1, -2, -2, -1),
    (Type.infantry, Experience.regular): (0, 0, 0, 0, 0),
    (Type.infantry, Experience.veteran): (0, 1, 2, 2, 0),
    (Type.infantry, Experience.elite): (1, 2, 4, 4, 1),
    (Type.infantry, Experience.superelite): (1, 3, 6, 6, 1),
    (Type.cavalry, Experience.regular): (0, 0, 0, 0, 0),
    (Type.cavalry, Experience.veteran): (0, 1, 1, 1, 2),
    (Type.cavalry, Experience.elite): (1, 2, 2, 2, 4),
    (Type.cavalry, Experience.superelite): (1, 3, 3, 3, 6),
    (Type.aerial, Experience.regular): (0, 0, 0, 0, 0),
    (Type.aerial, Experience.veteran): (0, 1, 1, 1, 2),
    (Type.aerial, Experience.elite): (1, 2, 2, 2, 4),
    (Type.aerial, Experience.superelite): (1, 3, 3, 3, 6),
    (Type.artillery, Experience.regular): (0, 0, 0, 0, 0),
    (Type.artillery, Experience.veteran): (1, 2, 1, 1, 1),
    (Type.artillery, Experience.elite): (1, 4, 2, 2, 2),
    (Type.artillery, Experience.superelite): (1, 6, 3, 3, 3)
    }

equipments = {
    (Type.infantry, Equipment.light): (0, 0, 0),
    (Type.infantry, Equipment.medium): (2, 2, 0),
    (Type.infantry, Equipment.heavy): (4, 4, 0),
    (Type.infantry, Equipment.superheavy): (6, 6, 1),
    (Type.cavalry, Equipment.light): (0, 0, 0),
    (Type.cavalry, Equipment.medium): (1, 1, 0),
    (Type.cavalry, Equipment.heavy): (2, 2, 0),
    (Type.cavalry, Equipment.superheavy): (3, 3, 1),
    (Type.aerial, Equipment.light): (0, 0, 0),
    (Type.aerial, Equipment.medium): (1, 1, 0),
    (Type.aerial, Equipment.heavy): (2, 2, 0),
    (Type.aerial, Equipment.superheavy): (3, 3, 1),
    (Type.artillery, Equipment.light): (0, 0, 0),
    (Type.artillery, Equipment.medium): (1, 1, 0),
    (Type.artillery, Equipment.heavy): (2, 2, 0),
    (Type.artillery, Equipment.superheavy): (3, 3, 0)
    }

ancestries = {
    Ancestry.barbeddevil : (),
    Ancestry.bugbear : (1, 0, 0, 0, 1, 0, 0, 0, [Trait.InspireFear]),
    Ancestry.construct : (2, 1, 5, 3, -1, 0, 1, 0, [Trait.DamageResistant, Trait.MagicResistant, Trait.Dead]),
    Ancestry.dragonborn : (0, 0, 0, 0, 1, 0, 0, 0, [Trait.DraconicAncestry]),
    Ancestry.drow : (1, 0, 0, 0, 0, 0, 0, 0, [Trait.DaylightWeakness, Trait.MagicResistant, Trait.Poisonous, Trait.Mobile, Trait.Eternal]),
    Ancestry.dwarf : (0, 0, 0, 0, 0, 0, 0, 0, [Trait.Stalwart]),
    Ancestry.elf : (1, 0, 0, 0, 0, 0, 0, 0, [Trait.Mobile, Trait.Eternal]),
    Ancestry.ghoul : (2, -1, 3, 2, 0, 1, 0, 0, [Trait.Dead, Trait.Harrowing, Trait.Feast]),
    Ancestry.gnoll : (1, -1, 1, -1, 0, -1, 0, 0, [Trait.Savage, Trait.Harrowing, Trait.Feast]),
    Ancestry.gnome : (-1, -1, -1, -1, -1, -1, 0, -2, [Trait.MagicResistant]),
    Ancestry.goblin : (-1, -1, -1, -1, -1, -1, 0, -2, [Trait.AAAUUUGH]),
    Ancestry.goliath : (1, 0, 0, 0, 1, 0, 0, 0, [Trait.Warbred]),
    Ancestry.halfling : (-1, -1, -1, -1, -1, -1, 0, -2, [Trait.Adaptable]),
    Ancestry.hobgoblin : (1, 0, 0, 0, 1, 0, 0, 0,[Trait.Warbred]),
    Ancestry.human : (0, 0, 0, 0, 1, 1, 0, 0, [Trait.Adaptable]),
    Ancestry.kenku : (-1, -1, -1, -1, -1, -1, 0, -2, [Trait.SowChaos]),
    Ancestry.kobold : (-1, -1, -1, -1, -1, -1, 0, -2, [Trait.AAAUUUGH, Trait.Dragonkin]),
    Ancestry.lizardfolk : (0, 0, 0, 0, 0, 1, 0, 0, [Trait.Amphibious, Trait.Guerrillas]),
    Ancestry.ogre : (2, 1, 3, 2, -1, -1, 0, 2, [Trait.Big, Trait.Slam]),
    Ancestry.orc : (1, 0, 0, 1, 0, 0, 0, 0, [Trait.Relentless]),
    Ancestry.skeleton : (0, -1, -1, 0, 0, 0, 0, -2, [Trait.Dead, Trait.Harrowing]),
    Ancestry.tortle : (0, 0, 0, 0, 0, 0, 0, 0, [Trait.Amphibious, Trait.Stoneskin]),
    Ancestry.triton : (0, 0, 0, 0, 0, 1, 0, 0, [Trait.Amphibious, Trait.Warbred]),
    Ancestry.troll : (2, 1, 3, 2, -1, -1, 0, 2, [Trait.Regenerate]),
    Ancestry.wight : (2, 2, 1, 1, 3, 3, 0, 0, [Trait.Dead, Trait.Harrowing, Trait.Warbred]),
    Ancestry.wraith : (0, -1, 1, 2, 0, 0, 0, 0, [Trait.Dead, Trait.Harrowing, Trait.Ethereal, Trait.CreateDead]),
    Ancestry.yuanti : (1, 0, 0, 0, 0, 0, 0, 0, [Trait.Eternal, Trait.Fearsome]),
    Ancestry.zombie : (-1, -1, -1, 1, 0, 0, 0, 0, [Trait.Dead, Trait.Harrowing, Trait.Relentless])
    }

upgrades = {
    Upgrade.hawk : (0, 0, 0, 0, 0, 0, 0, 1, [Trait.AerialBombardment]),
    Upgrade.pegasus : (0, 0, 0, 0, 0, 0, 0, 1, [Trait.ManeuverLandandCharge]),
    Upgrade.direwasp : (0, 0, 0, 0, 0, 0, 0, 1, [Trait.Poisonous]),
    Upgrade.wyvern : (0, 0, 2, 0, 0, 0, 0, 2, [Trait.Poisonous]),
    Upgrade.orccatapult : (0, 0, 0, 0, 0, -1, 2, 1, [Trait.SiegeWeapon]),
    Upgrade.catapult : (0, 0, 0, 0, 0, -1, 2, 1, [Trait.SiegeEngine]),
    Upgrade.ballista : (0, 0, 0, 0, 0, -1, 0, 1, [Trait.FastSiegeWeapon]),
    Upgrade.crossbow : (0, 0, 0, 0, 0, 0, 0, 1, [Trait.CloseRange]),
    Upgrade.longbow : (0, 0, 0, 0, 0, 0, 0, 0, []),
    Upgrade.boltthrower : (0, 0, 0, 0, 0, 0, 0, 2, [Trait.CollateralDamage, Trait.PointBlank]),
    Upgrade.bonebow : (0, 0, 0, 0, 0, 0, 0, 0, [Trait.PointBlank]),
    Upgrade.undeadcatapult : (0, 0, 0, 0, 0, -1, 2, 1, [Trait.LoadtheBones, Trait.SiegeEngine]),
    Upgrade.cannon : (0, 0, 0, 0, 0, -1, 2, 3, [Trait.SiegeEngine, Trait.Rockbreaker]), 
    Upgrade.riffle : (0, 0, 0, 0, 0, -1, 0, 2, [Trait.CollateralDamage, Trait.PointBlank]),
    Upgrade.smoker : (0, 0, 0, 0, 0, 0, 0, 1, [Trait.SmokeScreen]),
    Upgrade.horse : (0, 0, 0, 0, 0, 0, 0, 0, []),
    Upgrade.ram : (0, 0, 0, 0, 0, 0, 0, 1, [Trait.RamRiders]),
    Upgrade.elk : (0, 0, 0, 0, 0, 0, 0, 1, [Trait.ManeuverSpitUponTheirHorns]),
    Upgrade.nightmare : (0, 0, 0, 0, 0, 0, 0, 3, [Trait.Harrowing, Trait.Jaunt]),
    Upgrade.worg : (0, 0, 0, 0, 0, 0, 0, 1, [Trait.ManeuverPreyontheWeak]),
    Upgrade.direhyena : (0, 0, 0, 0, 0, 0, 0, 1, [Trait.DireHyenaMounts]),
    Upgrade.lance : (0, 0, 0, 0, 0, 0, 0, 1, [Trait.ManeuverLancersFlankThem]),
    Upgrade.engineer : (0, 0, 0, 0, 0, 0, 0, 1, [Trait.ManeuverDetonate, Trait.ManeuverRepair]),
    Upgrade.pike : (0, 0, 0, 0, 0, 0, 0, 1, [Trait.PikeTraining]),
    Upgrade.shield : (0, 0, 0, 0, 0, 0, 0, 1, [Trait.ManeuverTestudo]),
    Upgrade.grenade : (0, 0, 0, 0, 0, 0, 0, 2, [Trait.FireBlast]),
    Upgrade.sapper : (0, 0, 0, 0, 0, 0, 0, 1, [Trait.Dig]),
    Upgrade.miner : (0, 0, 0, 0, 0, 0, 0, 0, [Trait.HardHats]),
    Upgrade.wounded : (0, 0, 0, 0, 0, 0, 0, 0, [Trait.TotheDeath]),
    Upgrade.artisan : (0, 0, 0, 0, 0, 0, 0, 0, [Trait.ManeuverRepair]),
    Upgrade.extraatk : (1, 0, 0, 0, 0, 0, 0, 1, []),
    Upgrade.extradef : (0, 1, 0, 0, 0, 0, 0, 1, []),
    Upgrade.extrapow : (0, 0, 1, 0, 0, 0, 0, 1, []),
    Upgrade.extratou : (0, 0, 0, 1, 0, 0, 0, 1, []),
    Upgrade.extramor : (0, 0, 0, 0, 1, 0, 0, 2, []),
    }

class Unit:
    experience = Experience.none
    equipment = Equipment.none
    unittype = Type.none
    ancestry = Ancestry.none
    traits = []
    upgrades = []
    statatk = 0
    statdef = 10
    statpow = 0
    stattou = 10
    statmor = 0
    statcom = 0
    statnoatk = 1
    statdmg = 1
    statsize = 6
    stattier = 1
    name = ""
    
    def __init__(self, name = "", experience = Experience.none, equipment = Equipment.none, ancestry = Ancestry.none, unittype = Type.none, upgrades = [], traits = [] ):
        self.name = name
        self.experience = experience
        self.equipment = equipment
        self.unittype = unittype
        self.ancestry = ancestry
        self.traits += traits
        self.upgrades += upgrades
        self.addType(self.unittype)
        self.addExperience(self.unittype, self.experience)
        self.addEquipment(self.unittype, self.equipment)
        self.addAncestry(self.ancestry, self.unittype)
        for upgrade in self.upgrades:
            addUpgrade(upgrade)

    def addType(self, unitType):
        global types
        self.statatk += types[unitType][0]
        self.statdef += types[unitType][1]
        self.statpow += types[unitType][2]
        self.stattou += types[unitType][3]
        self.statcom += types[unitType][4]
        self.statdmg += types[unitType][5]

    def addExperience(self, unitType, experience):
        global experiences
        self.statnoatk += experiences[(unitType, experience)][0]
        self.statatk += experiences[(unitType, experience)][1]
        self.statdef += experiences[(unitType, experience)][2]
        self.statmor += experiences[(unitType, experience)][3]
        self.statcom += experiences[(unitType, experience)][4]

    def addEquipment(self, unitType, equipment):
        global equipments
        self.statpow += equipments[(unitType, equipment)][0]
        self.stattou += equipments[(unitType, equipment)][1]
        self.statdmg += equipments[(unitType, equipment)][2]
        
    def addAncestry(self, ancestry, unitType):
        global ancestries
        self.statatk += ancestries[ancestry][0]
        self.statdef += ancestries[ancestry][1]
        self.statpow += ancestries[ancestry][2]
        self.stattou += ancestries[ancestry][3]
        self.statmor += ancestries[ancestry][4]
        self.statcom += ancestries[ancestry][5]
        self.statdmg += ancestries[ancestry][6]
        self.statsize += ancestries[ancestry][7]
        self.traits += ancestries[ancestry][8]
        if(ancestry == Ancestry.dwarf and unitType == Type.artillery):
            stattou += 2

    def addUpgrade(self, upgrade):
        global upgrades
        self.statatk += upgrades[upgrade][0]
        self.statdef += upgrades[upgrade][1]
        self.statpow += upgrades[upgrade][2]
        self.stattou += upgrades[upgrade][3]
        self.statmor += upgrades[upgrade][4]
        self.statnoatk += upgrades[upgrade][5]
        self.statdmg += upgrades[upgrade][6]
        self.stattier += upgrades[upgrade][7]
        self.traits += upgrades[upgrade][8]
        

    def printUnitCard(self):
        print(self.name)
        print(self.experience.name.capitalize(), self.equipment.name.capitalize(), self.ancestry.name.capitalize(), self.unittype.name.capitalize())
        print("Size:", self.statsize, "| ATK No:", self.statnoatk, "| DMG:", self.statdmg, "| Tier:", self.stattier)
        print("ATK:",self.statatk, "| DEF:", self.statdef, "| POW:", self.statpow, "| TOU:", self.stattou, "| MOR:", self.statmor, "| COM:", self.statcom)
        for trait in self.traits:
            print(trait.name)
    
                 
