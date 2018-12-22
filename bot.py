#IMPORTS
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random


#GLOBAL VARIABLES
# token of the bot and ID of the admin(change to you ID)
token = "NTI0OTY3MDE3NzgzMDk5NDEy.Dvv17g.BxXD5GhVA1eTSxIhuKLD1cFmrgU"
adminID = <yourID> (no brackets)
dmID = 0
data = []
data.append(dmID)

Client = discord.Client()  # Initialise Client
client = commands.Bot(command_prefix="?")  # Initialise client bot

# AUX FUNCTIONS


def GetData(id, data):
    for info in data:
        if info == id:
            return data.index(info)


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='-help'))
    # This will be called when the bot connects to the server


@client.event
async def on_message(message):

    
    # HELP GUIDE
    if message.content.lower().startswith('-help'):  # set help event
        await client.send_message(message.channel, "```Quick Guide To DnD 5e Dice Roller \n\nSetting data(remember to use only backspace, no comma or hifen): -sd \nFormat[level] [attribute modifier for meelee attacks+additional bonus] [attribute modifier for ranged attacks+additonal bonus] [meelee weapon damage roll] [range weapon damage roll] [attribute modifier for spell attacks] [max hp] [hit dice(only the size)] [constitution mod] [money(in cp)] \nE.g.: \n-sd 1 4 3 6 0 3 20 6 2 100  \n\nRandom Rolls: \n-sr to simple roll \n-ar to advantage roll \n-dr to disavantage roll \nExemple: \n-ra 2d6+3 = 10 [1,4,3,2] \n\nSpecific Rolls(need data to be setted): n-ma to Meelee Attack Rolls \n-ra to Ranged Attack Rolls \n-sa to Spell Attack Rolls \n-md to Meelee Damage Rolls\n-rd to Ranged Damage Roll \n-hd [amount used] to Hit Dice roll \nds-to death save \n\nOther Features: \n-hit ro decrase HP \n-lr to long rest \n-ul to upgrade level \n -ss to show current stats to player \n-sm to spend Money(always in CP. Remember: 1PP = 10 GP = 20 EP = 100SP = 1000CP) \n\nAdmin Features: \n\n-dm <ID> to set DM \n-si to show all info of each players (privatly)to DM```")

    # SETS

    if message.content.lower().startswith('-sd'):  # set data of each character
        await client.send_message(message.channel, " ```Lucky man... Remember the DM is watching... ```")
        userID = message.author.id
        # first info is id for the purpose of finding the data specific to that user
        data.append(userID)
        args = message.content.lower().split(' ')
        level = int(args[1])  # level of the character
        data.append(level)
        try:
            if level >= 1 and level < 5:
                prof = 2
            if level >= 5 and level < 9:
                prof = 3
            if level >= 9 and level < 13:
                prof = 4
            if level >= 13 and level < 17:
                prof = 5
            if level >= 17 and level <= 20:
                prof = 6

        except level < 0 or level > 20:

            await client.send_message(message.channel, "```Level is not between 1 and 20```")

        data.append(prof)  # proficiency of the character based on its level
        meelee_mod = int(args[2])  # meelee attack modifier
        data.append(meelee_mod)
        range_mod = int(args[3])
        data.append(range_mod)
        # damage dice type of the character's meelee weapon
        meelee_damage = int(args[4])
        data.append(meelee_damage)
        # damage dice type of the character's range weapon
        range_damage = int(args[5])
        data.append(range_damage)
        spell_mod = int(args[6])
        data.append(spell_mod)
        spell_save = 8 + prof + spell_mod
        data.append(spell_save)
        hp_max = int(args[7])
        data.append(hp_max)
        hp = hp_max
        data.append(hp)
        qtd_hd_max = level
        data.append(qtd_hd_max)
        qtd_hd = qtd_hd_max
        data.append(qtd_hd)
        hit_dice = int(args[8])
        data.append(hit_dice)
        con = int(args[9])
        data.append(con)
        death_roll_fail = 0  # Say if the last death save was a succes or a fail
        death_roll_succes = 0  # save the amount of succesfull death saves
        data.append(death_roll_fail)
        data.append(death_roll_succes)
        money = int(args[10])
        data.append(money)
    # ROLLS
    if message.content.lower().startswith('-ar'):  # set advantage roll event

        adv_roll = True
        args = message.content.split(" ")
        # args[0] = -ra
        # args[1] = 1d6
        dice_mod = args[len(args)-1]
        try:
            dice = dice_mod.split('+')[0]
        except ValueError:
            dice = dice_mod
        # dice[0] = 1
        # dice[2] = 6
        qtd, size_mod = dice_mod.split('d')
        qtd = int(qtd)
        qtd = 2*qtd
        # advantage grants the double of dices in the roll

        try:
            size, mod = size_mod.split('+')

        except ValueError:
            size = size_mod
            mod = 0

        size = int(size)
        mod = int(mod)
        rolls = []
        for i in range(qtd):
            roll = random.randint(1, size)
            rolls.append(roll)
        sum = 0
        rolls_clone = []
        for i in range(len(rolls)):  # clone to analyse get the highest amounts
            rolls_clone.append(rolls[i])

        for i in range(int(qtd/2)):
            higher = max(rolls_clone)
            rolls_clone.remove(higher)
            sum += higher



        rolls = str(rolls)

        if mod != 0:
            await client.send_message(message.channel, " ``` %s + %i = %i. %s```" % (dice, mod, sum, rolls))
        else:
            await client.send_message(message.channel, " ``` %s = %i. %s```" % (dice, sum, rolls))

    if message.content.lower().startswith('-dr'):

        dis_roll = True
        args = message.content.split(" ")
        # args[0] = -rd
        # args[1] = 1d6
        dice_mod = args[len(args)-1]
        try:
            dice = dice_mod.split('+')[0]
        except ValueError:
            dice = dice_mod
        # dice[0] = 1
        # dice[2] = 6
        qtd, size_mod = dice_mod.split('d')
        qtd = int(qtd)
        qtd = 2*qtd
        # advantage grants the double of dices in the roll

        try:
            size, mod = size_mod.split('+')

        except ValueError:
            size = size_mod
            mod = 0

        size = int(size)
        mod = int(mod)
        rolls = []
        for i in range(qtd):
            roll = random.randint(1, size)
            rolls.append(roll)
        sum = 0
        rolls_clone = []
        for i in range(len(rolls)):  # clone to analyse get the lowest amounts
            rolls_clone.append(rolls[i])

        for i in range(int(qtd/2)):
            lower = min(rolls_clone)
            rolls_clone.remove(lower)
            sum += lower



        rolls = str(rolls)

        if mod != 0:
            await client.send_message(message.channel, " ``` %s + %i = %i. %s```" % (dice, mod, sum, rolls))
        else:
            await client.send_message(message.channel, " ``` %s = %i. %s```" % (dice, sum, rolls))

    if message.content.lower().startswith('-sr'):  # simple roll

        args = message.content.split(" ")
        # args[0] = -r
        # args[1] = 1d6
        dice_mod = args[len(args)-1]
        try:
            dice = dice_mod.split('+')[0]
        except ValueError:
            dice = dice_mod
        # dice[0] = 1
        # dice[2] = 6
        qtd, size_mod = dice_mod.split('d')
        qtd = int(qtd)
        try:
            size, mod = size_mod.split('+')

        except ValueError:
            size = size_mod
            mod = 0

        size = int(size)
        mod = int(mod)
        rolls = []
        sum = 0
        for i in range(qtd):
            roll = random.randint(1, size)
            rolls.append(roll)
            sum += roll
        sum += mod
        rolls = str(rolls)
        if mod != 0:
            await client.send_message(message.channel, " ``` %s + %i = %i. %s```" % (dice, mod, sum, rolls))
        else:
            await client.send_message(message.channel, " ``` %s = %i. %s```" % (dice, sum, rolls))

    # AUTOMATIC ROLLS AND FUNCTIONS
    if message.content.lower().startswith('-ma'):  # meelee attack roll
        if data:
            roll = random.randint(1, 20)

            # get the id of the user that calls the event for the purpose of finding his data in the list
            userID = message.author.id
            prof = data[GetData(userID, data)+2]
            mod = data[GetData(userID, data)+3]
            await client.send_message(message.channel, "``` 1d20+%i = %i.[%i]```" % (mod+prof, roll+mod+prof, roll))
        else:
            await client.send_message(message.channel, "```Error!Data not setted```")

    if message.content.lower().startswith('-ra'):  # ranged attack roll
        if data:
            roll = random.randint(1, 20)
            userID = message.author.id
            prof = data[GetData(userID, data)+2]
            mod = data[GetData(userID, data)+4]
            await client.send_message(message.channel, "``` 1d20+%i = %i.[%i]```" % (mod+prof, roll+mod+prof, roll))
        else:
            await client.send_message(message.channel, "```Error!Data not setted```")

    if message.content.lower().startswith('-md'):  # meelee damage roll
        if data:
            userID = message.author.id
            damage = data[GetData(userID, data)+5]
            mod = data[GetData(userID, data)+3]
            roll = random.randint(1, damage)
            await client.send_message(message.channel, "``` 1d%i + %i = %i.[%i]```" % (damage, mod, roll+mod, roll))
        else:
            await client.send_message(message.channel, "```Error!Data not setted```")

    if message.content.lower().startswith('-rd'):  # ranged damage roll
        userID = message.author.id
        damage = data[GetData(userID, data)+6]
        if damage == 0:
            await client.send_message(message.channel, "```No damage!```")
        if data:
            mod = data[GetData(userID, data)+4]
            roll = random.randint(1, damage)
            await client.send_message(message.channel, "``` 1d%i + %i = %i.[%i]```" % (damage, mod, roll+mod, roll))
        else:
            await client.send_message(message.channel, "```Error!Data not setted```")

    if message.content.lower().startswith('-sa'):  # spell attack roll
        if data:
            roll = random.randint(1, 20)
            userID = message.author.id
            prof = data[GetData(userID, data)+2]
            mod = data[GetData(userID, data)+7]
            await client.send_message(message.channel, "``` 1d20+%i = %i.[%i]```" % (mod, roll, roll))
        else:
            await client.send_message(message.channel, "```Error!Data not setted```")

    if message.content.lower().startswith('-hd'):  # hit dice roll
        if data:
            args = message.content.lower().split(' ')
            userID = message.author.id
            qtd_hd = data[GetData(userID, data)+12]
            amount = int(args[1])#amount of dices used
            if amount > qtd_hd: #avoid of using more hit dices than the amount available
                amount = qtd_hd

            qtd_hd = data[GetData(userID, data)+12])
            hit_dice = data[GetData(userID, data)+13])
            hp = 10
            hp_max = data[GetData(userID, data)+9])
            con = data[GetData(userID, data)+14])
            s = 0
            hd_rolls = []
            for i in range(amount):
                if qtd_hd == 0:
                    await client.send_message(message.channel, "```No hit dices left```")
                else:
                    roll = random.randint(1, hit_dice)  # compute hit point gained
                    hd_rolls.append(roll)
                    roll += con
                    hp += roll
                    s += roll
                    if hp > hp_max:
                        s -= hp - hp_max
                        hp = hp_max
                        await client.send_message(message.channel, "```Max HP reachead```")
                        break
                    data[GetData(userID, data)+7] = hp
            
            hd_rolls = str(hd_rolls)
            await client.send_message(message.channel, "```%id%i + %i = %i %s```" %(amount,hit_dice,con*amount,s,hd_rolls))
            qtd_hd -= amount  # consume n hit dices
            data[GetData(userID, data)+12] = qtd_hd
        else:
            await client.send_message(message.channel, "```Error!Data not setted```")

    if message.content.lower().startswith('-ds'):  # death save, 3 succes = stable, 3 fails = 
        userID = message.author.id
        succes = data[GetData(userID, data)+16]
        fail = data[GetData(userID, data)+15]
        roll = random.randint(1, 20)
        if roll < 11 and fail == 2:
            succes = 0
            fail = 0
            await client.send_message(message.channel, "```You're Dead. Valar Morghulis")
        if roll < 11 and fail < 2:
            fail += 1
            await client.send_message(message.channel, "```You failed. One more fail and you are gone!")
        else:
            succes += 1
            if succes == 3:
                succes = 0
                fail = 0
                await client.send_message(message.channel, "```You're back ad stabilized. Take care!")

            await client.send_message(message.channel, "```You got a succes! Now you have %i successes and %i fails. Pray for the gods!."%(succes,fail))
        data[GetData(userID, data)+15] = succes
        data[GetData(userID, data)+14] = fail
    

    # OTHERS FEATURES
    if message.content.lower().startswith('-hit'):  # damage suffered
        if data:
            userID = message.author.id
            args = message.content.lower().split(' ')
            damage = int(args[1])
            hp = data[GetData(userID, data)+10]
            hp -= damage#take damage
            await client.send_message(message.channel, "```You took %i hit points. Don't you have a shield?```" %(damage))
            if hp <= 0:#unconcious
                hp = 0 
                await client.send_message(message.channel, "```You are unconcious. Roll a death save in the next turn.```")

            data[GetData(userID, data)+7] = hp

        else:
            await client.send_message(message.channel, "```Error!Data not setted```")
    if message.content.lower().startswith('-lr'):  # long rest]
        if data:
            userID = message.author.id
            hp = data[GetData(userID, data)+10]
            hp_max = data[GetData(userID, data)+9]
            qtd_hd = data[GetData(userID, data)+12]
            qtd_hd_max = data[GetData(userID, data)+11]
            hd = int(qtd_hd_max/2)
            if hd == 0: #to a minimum of 1
                hd = 1  # hit dice regained after finishing a long rest
            hp = hp_max #restore all hp
            qtd_hd += hd #add regained hit dices
            if qtd_hd > qtd_hd_max:
                qtd_hd = qtd_hd_max
            data[GetData(userID, data)+12] = qtd_hd
            await client.send_message(message.channel, "```All HP restored and you. And you regained %i hit dices, so now you have %i hit dices. Now you can charge into an elemental again, son! ```" % (hd, qtd_hd))
        else:
            await client.send_message(message.channel, "```Error!Data not setted```")

    if message.content.lower().startswith('-ul'):  # upgrade level
        if data:
            userID = message.author.id
            level = data[GetData(userID, data)+1]
            hp_max = data[GetData(userID, data)+9]
            qtd_hd_max = data[GetData(userID, data)+1
            hit_dice = data[GetData(userID, data)+13 
            con = data[GetData(userID, data)+14
            roll = random.randint(1,hit_dice) + con
            hp_max += roll
            level += 1 con
            qtd_hd_max += 1
            if level > 20:
                level = 20
            data[GetData(userID, data)+1] = level
            data[GetData(userID, data)+9] = hp_max
            data[GetData(userID, data)+11] = qtd_hd_max
            data[GetData(userID, data)+13] = hit_dice
            await client.send_message(message.channel, "```Level up! Great news Dovakhin!You gained %i hit points, so you´re new max HP is %i```"%(roll,hp_max))
        else:
            await client.send_message(message.channel, "```Error!Data not setted```")

    if message.content.lower().startswith('-ss'):  # show stats of a player
        userID = message.author.id
        hp = data[GetData(userID, data)+10]
        qtd_hd = data[GetData(userID, data)+12]
        await client.send_message(message.author, "```HP: %i \nHit dices left: %i```"%(hp,qtd_hd))
    
    if message.content.lower().startswith('-sm'):#spend money
        userID = message.author.id
        money_before = data[GetData(userID, data)+17]#Current amount of money
        money_after = money_before
        args = message.content.lower().split(' ')
        spent = int(args[1])#Amount that will be spent
        money_after -= spent
        data[GetData(userID, data)+17] = money_after

        await client.send_message(message.channel, "```You had %i, spent %i now you have %i``"%(money_before,spent, money_after))
    

    # ADMIN FEATURES

    if message.content.lower().startswith('-dm'):
        args = message.content.lower().split(' ')
        userID = message.author.id
        userID = int(userID)
        dmID = int(args[1])
        data[0] = dmID
        if userID != adminID:
            await client.send_message(message.channel, "```YOU SHALL NOT PASS```")
        else: 
            dmID_string = '<@' + str(dmID)+'>'
    
            await client.send_message(message.channel, "Congratulations %s ! You are the Dungeon Master. Shall the blood spill over your dices!"%(dmID_string))
    if message.content.lower().startswith('-si'):
        
        if data[0] != 0:
            userID = message.author.id
            userID = int(userID)
            if userID != data[0]:
                await client.send_message(message.channel, "```'A master cannot be mistaken for his students'-Someone Somewhere Somewhen```")
            else:
                await client.send_message(message.author, "DM. The stats are: ")
                i =  1 #just to help in the iteration, the element data[0] is the dm user
                while i < len(data) - 1: #Get groups of 18 elements for each player
                    user = data[i]
                    user = '<@'+str(user)+'>' 
                    level = data[i+1]
                    prof = data[i+2]
                    m_mod= data[i+3]
                    r_mod = data[i+4]
                    m_d = data[i+5]
                    r_d = data[i+6]
                    s_m = data[i+7]
                    s_s= data[i+8]
                    hp_m = data[i+9]
                    hp = data[i+10]
                    qtd_hd_m = data[i+11]
                    qtd_hd = data[i+12]
                    hd = data[i+13]
                    dr_fail = data[i+15]
                    dr_suc = data[i+16]
                    mon =  data[i+17]

                    await client.send_message(message.author, "Player: %s. \nLevel: %i, Proficiency: %i, Meelee Mod: %i, Meelee Damage: %i, Ranged Mod: %i, Ranged Damage: %i, Spell Mod: %i,Spell Save: %i, HP Max: %i, Current HP: %i, Max Hit dices: %i, Current Hit dices: %i, Money: %i \n"%(user,level,prof,m_mod,m_d,r_mod,r_d,s_m,s_s,hp_m,hp,qtd_hd_m,qtd_hd,mon))
                
                    i += 18
        else: 
            
            await client.send_message(message.channel, "```DM has not been selected, please type -dm + user id```")

client.run(token)