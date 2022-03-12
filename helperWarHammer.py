import helperBasic

def WarDict(stats):
    return {'WS':stats[0],'BS':stats[1],'S':stats[2],'T':stats[3],'Ag':stats[4],'Int':stats[5],'WP':stats[6],'Fel':stats[7],'A':stats[8],'W':stats[9],'SB':stats[10],'TB':stats[11],'M':stats[12],'Mag':stats[13],'IP':stats[14],'FP':stats[15],'Race':stats[16]}

def WarRaceMod(stats,race):
    human = [20,20,20,20,20,20,20,20]
    elf = [20,30,20,20,30,20,20,20]
    half = [10,30,10,10,30,20,20,30]
    dwarf = [30,20,20,30,10,20,20,10]
    stats.append(1)
    
    if('human'==race):
        for x in range(0,8):
            stats[x]=stats[x]+human[x]

        w = helperBasic.Roll(1,10)
        if(1<=w<=3):
            stats.append(10)
        elif(4<=w<=6):
            stats.append(11)
        elif(7<=w<=9):
            stats.append(12)
        elif(w==10):
            stats.append(13)

        stats.append(stats[2]-(stats[2]%10))
        stats.append(stats[3]-(stats[3]%10))
        stats.append(4)
        stats.append(0)
        stats.append(0)

        w = helperBasic.Roll(1,10)
        if(1<=w<=4):
            stats.append(2)
        elif(5<=w<=7):
            stats.append(3)
        elif(8<=w<=10):
            stats.append(3)

        stats.append('Human')
        
    elif('elf'==race):
        for x in range(0,8):
            stats[x]=stats[x]+elf[x]

        w = helperBasic.Roll(1,10)
        if(1<=w<=3):
            stats.append(9)
        elif(4<=w<=6):
            stats.append(10)
        elif(7<=w<=9):
            stats.append(11)
        elif(w==10):
            stats.append(12)

        stats.append(stats[2]-(stats[2]%10))
        stats.append(stats[3]-(stats[3]%10))
        stats.append(5)
        stats.append(0)
        stats.append(0)

        w = helperBasic.Roll(1,10)
        if(1<=w<=4):
            stats.append(1)
        elif(5<=w<=7):
            stats.append(2)
        elif(8<=w<=10):
            stats.append(2)
            
        stats.append('Elf')
        
    elif('half'==race):
        for x in range(0,8):
            stats[x]=stats[x]+half[x]

        w = helperBasic.Roll(1,10)
        if(1<=w<=3):
            stats.append(8)
        elif(4<=w<=6):
            stats.append(9)
        elif(7<=w<=9):
            stats.append(10)
        elif(w==10):
            stats.append(11)

        stats.append(stats[2]-(stats[2]%10))
        stats.append(stats[3]-(stats[3]%10))
        stats.append(4)
        stats.append(0)
        stats.append(0)

        w = helperBasic.Roll(1,10)
        if(1<=w<=4):
            stats.append(2)
        elif(5<=w<=7):
            stats.append(2)
        elif(8<=w<=10):
            stats.append(3)
            
        stats.append('Halfling')
        
    elif('dwarf'==race):
        for x in range(0,8):
            stats[x]=stats[x]+dwarf[x]

        w = helperBasic.Roll(1,10)
        if(1<=w<=3):
            stats.append(11)
        elif(4<=w<=6):
            stats.append(12)
        elif(7<=w<=9):
            stats.append(13)
        elif(w==10):
            stats.append(14)

        stats.append(stats[2]-(stats[2]%10))
        stats.append(stats[3]-(stats[3]%10))
        stats.append(3)
        stats.append(0)
        stats.append(0)

        w = helperBasic.Roll(1,10)
        if(1<=w<=4):
            stats.append(1)
        elif(5<=w<=7):
            stats.append(2)
        elif(8<=w<=10):
            stats.append(3)
            
        stats.append('Dwarf')

    return WarDict(stats)

def WarStarTal(stats):
    if(stats['Race']=='Human'):
        roll = helperBasic.Roll(1,100)
        if(1<=roll<=4):
            stats['Talent1']='Acute Hearing'
        elif(5<=roll<=9):
            stats['Talent1']='Ambidextrous'
        elif(10<=roll<=13):
            stats['Talent1']='Coolheaded'
            stats['WP']=(stats['WP']+5)
        elif(14<=roll<=18):
            stats['Talent1']='Excellent Vision'
        elif(19<=roll<=22):
            stats['Talent1']='Fleet Footed'
            stats['M']=(stats['M']+5)
        elif(23<=roll<=27):
            stats['Talent1']='Hardy'
            stats['W']=(stats['W']+5)
        elif(28<=roll<=31):
            stats['Talent1']='Lightning Reflexes'
            stats['Ag']=(stats['Ag']+5)
        elif(32<=roll<=35):
            stats['Talent1']='Luck'
        elif(36<=roll<=40):
            stats['Talent1']='Marksman'
            stats['BS']=(stats['BS']+5)
        elif(41<=roll<=44):
            stats['Talent1']='Mimic'
        elif(45<=roll<=49):
            stats['Talent1']='Night Vision'
        elif(50<=roll<=53):
            stats['Talent1']='Resistance to Disease'
        elif(54<=roll<=57):
            stats['Talent1']='Resistance to Magic'
        elif(58<=roll<=61):
            stats['Talent1']='Resistance to Poison'
        elif(62<=roll<=66):
            stats['Talent1']='Savvy'
            stats['Int']=(stats['Int']+5)
        elif(67<=roll<=71):
            stats['Talent1']='Sixth Sense'
        elif(72<=roll<=75):
            stats['Talent1']='Strong-minded'
        elif(76<=roll<=79):
            stats['Talent1']='Sturdy'
        elif(80<=roll<=83):
            stats['Talent1']='Suave'
            stats['Fel']=(stats['Fel']+5)
        elif(84<=roll<=87):
            stats['Talent1']='Super Numerate'
        elif(88<=roll<=91):
            stats['Talent1']='Very Resilient'
            stats['T']=(stats['T']+5)
        elif(92<=roll<=95):
            stats['Talent1']='Very Strong'
            stats['S']=(stats['S']+5)
        elif(96<=roll<=100):
            stats['Talent1']='Warrior Born'
            stats['WS']=(stats['WS']+5)

        same = True
        while(same):
            roll = helperBasic.Roll(1,100)
            if(1<=roll<=4):
                stats['Talent2']='Acute Hearing'
            elif(5<=roll<=9):
                stats['Talent2']='Ambidextrous'
            elif(10<=roll<=13):
                stats['Talent2']='Coolheaded'
                stats['WP']=(stats['WP']+5)
            elif(14<=roll<=18):
                stats['Talent2']='Excellent Vision'
            elif(19<=roll<=22):
                stats['Talent2']='Fleet Footed'
                stats['M']=(stats['M']+5)
            elif(23<=roll<=27):
                stats['Talent2']='Hardy'
                stats['W']=(stats['W']+5)
            elif(28<=roll<=31):
                stats['Talent2']='Lightning Reflexes'
                stats['Ag']=(stats['Ag']+5)
            elif(32<=roll<=35):
                stats['Talent2']='Luck'
            elif(36<=roll<=40):
                stats['Talent2']='Marksman'
                stats['BS']=(stats['BS']+5)
            elif(41<=roll<=44):
                stats['Talent2']='Mimic'
            elif(45<=roll<=49):
                stats['Talent2']='Night Vision'
            elif(50<=roll<=53):
                stats['Talent2']='Resistance to Disease'
            elif(54<=roll<=57):
                stats['Talent2']='Resistance to Magic'
            elif(58<=roll<=61):
                stats['Talent2']='Resistance to Poison'
            elif(62<=roll<=66):
                stats['Talent2']='Savvy'
                stats['Int']=(stats['Int']+5)
            elif(67<=roll<=71):
                stats['Talent2']='Sixth Sense'
            elif(72<=roll<=75):
                stats['Talent2']='Strong-minded'
            elif(76<=roll<=79):
                stats['Talent2']='Sturdy'
            elif(80<=roll<=83):
                stats['Talent2']='Suave'
                stats['Fel']=(stats['Fel']+5)
            elif(84<=roll<=87):
                stats['Talent2']='Super Numerate'
            elif(88<=roll<=91):
                stats['Talent2']='Very Resilient'
                stats['T']=(stats['T']+5)
            elif(92<=roll<=95):
                stats['Talent2']='Very Strong'
                stats['S']=(stats['S']+5)
            elif(96<=roll<=100):
                stats['Talent2']='Warrior Born'
                stats['WS']=(stats['WS']+5)

            if(stats['Talent1']==stats['Talent2']):
                same = True
            else:
                same = False

    elif(stats['Race']=='Halfling'):
        roll = helperBasic.Roll(1,100)
        if(1<=roll<=5):
            stats['Talent1']='Acute Hearing'
        elif(6<=roll<=10):
            stats['Talent1']='Ambidextrous'
        elif(11<=roll<=15):
            stats['Talent1']='Coolheaded'
            stats['WP']=(stats['WP']+5)
        elif(16<=roll<=20):
            stats['Talent1']='Excellent Vision'
        elif(21<=roll<=25):
            stats['Talent1']='Fleet Footed'
            stats['M']=(stats['M']+5)
        elif(26<=roll<=29):
            stats['Talent1']='Hardy'
            stats['W']=(stats['W']+5)
        elif(30<=roll<=33):
            stats['Talent1']='Lightning Reflexes'
            stats['Ag']=(stats['Ag']+5)
        elif(34<=roll<=38):
            stats['Talent1']='Luck'
        elif(39<=roll<=42):
            stats['Talent1']='Marksman'
            stats['BS']=(stats['BS']+5)
        elif(43<=roll<=47):
            stats['Talent1']='Mimic'
        elif(48<=roll<=51):
            stats['Talent1']='Resistance to Disease'
        elif(52<=roll<=53):
            stats['Talent1']='Resistance to Magic'
        elif(54<=roll<=57):
            stats['Talent1']='Resistance to Poison'
        elif(58<=roll<=62):
            stats['Talent1']='Savvy'
            stats['Int']=(stats['Int']+5)
        elif(63<=roll<=67):
            stats['Talent1']='Sixth Sense'
        elif(68<=roll<=72):
            stats['Talent1']='Strong-minded'
        elif(73<=roll<=77):
            stats['Talent1']='Sturdy'
        elif(78<=roll<=82):
            stats['Talent1']='Suave'
            stats['Fel']=(stats['Fel']+5)
        elif(83<=roll<=87):
            stats['Talent1']='Super Numerate'
        elif(88<=roll<=91):
            stats['Talent1']='Very Resilient'
            stats['T']=(stats['T']+5)
        elif(92<=roll<=95):
            stats['Talent1']='Very Strong'
            stats['S']=(stats['S']+5)
        elif(96<=roll<=100):
            stats['Talent1']='Warrior Born'
            stats['WS']=(stats['WS']+5)

        stats['Talent2']='Night Vision'
        stats['Talent3']='Resistance to Chaos'
        stats['Talent4']='Specialist Weapon Group(Sling)'

    elif(stats['Race']=='Elf'):
        roll = helperBasic.Roll(1,2)
        if(roll == 1):
            stats['Talent1']='Aethyric Attunement'
        else:
            stats['Talent1']='Specialist Weapon Group(Longbow)'

        roll = helperBasic.Roll(1,2)
        if(roll==1):
            stats['Talent2']='Coolheaded'
        else:
            stats['Talent2']='Savvy'

        stats['Talent3']='Excellent Vision'
        stats['Talent4']='Night Vision'
        
    elif(stats['Race']=='Dwarf'):
        stats['Talent1']='Dwarfcraft'
        stats['Talent2']='Grudge-born Fury'
        stats['Talent3']='Night Vision'
        stats['Talent4']='Resistance to Magic'
        stats['Talent5']='Stout-hearted'
        stats['Talent6']='Sturdy'

    return stats
    

def War(List):
    stats = []
    for x in range(0,8):
        stats.append(helperBasic.Roll(2,10))
    
    if('human' in List):
        stats = WarRaceMod(stats,'human')
    elif('elf' in List):
        stats = WarRaceMod(stats,'elf')
    elif('half' in List):
        stats = WarRaceMod(stats,'half')
    elif('dwarf' in List):
        stats = WarRaceMod(stats,'dwarf')
    else:
        race = helperBasic.Roll(1,4)
        if (race==1):
            stats = WarRaceMod(stats,'dwarf')
        elif (race==2):
            stats = WarRaceMod(stats,'elf')
        elif (race==3):
            stats = WarRaceMod(stats,'half')
        elif (race==4):
            stats = WarRaceMod(stats,'human')

    if('t' in List):
        stats = WarStarTal(stats)
    return stats
