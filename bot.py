import os

import discord
import numpy as np
import responses
from dotenv import load_dotenv


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


intents = discord.Intents.default()
intents.message_content = True


servers = [None]


class coupGame:
    def __init__(self, gaming, playerList, playerList2, startcount, forcestart, turn, deck, vote, challengeWon, temparr, server, greenfn):
        self.gaming = gaming
        self.playerList = playerList
        self.playerList2 = playerList2
        self.startcount = startcount
        self.forcestart = forcestart
        self.turn = turn
        self.deck = deck
        self.vote = vote
        self.challengeWon = challengeWon
        self.temparr = temparr
        self.server = server
        self.greenfn = greenfn




def run_discord_bot():
    
    load_dotenv()
    TOKEN = os.getenv('BOT_KEY')
    
    
    
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')



    @client.event
    async def on_message(message):
        global servers

        server = None


        for i in range(0,len(servers)):
            if servers[i] == None:
                servers[i] = coupGame(False, [], [], 0, 0, 0,
                             ['🥷', '🤵‍♂️', '💃', '🧑‍✈️', '🦹‍♂️', '🥷', '🤵‍♂️', '💃', '🧑‍✈️', '🦹‍♂️', '🥷', '🤵‍♂️', '💃',
                              '🧑‍✈️', '🦹‍♂️'], 0, False, [], message.guild, False)
                server = servers[i]
                servers.append(None)
                break
            elif servers[i].server == message.guild:
                server = servers[i]
                break



        # global gaming, playerList, playerList2, startcount, forcestart, turn, deck, vote, challengeWon
        if message.author == client.user:
            if responses.handle_response2(message.content) == 1:
                await message.add_reaction('✅')
                await message.add_reaction('💣')
            elif responses.handle_response2(message.content) == 2:
                await message.add_reaction('🪙')
                await message.add_reaction('💵')
                await message.add_reaction('💰')
                await message.add_reaction('😈')
                await message.add_reaction('🔪')
                await message.add_reaction('🎲')
                await message.add_reaction('⚔️')
            elif responses.handle_response2(message.content) == 3 or responses.handle_response2(message.content) == 4:
                await message.add_reaction('👊')
                await message.add_reaction('👌')
            elif responses.handle_response2(message.content) == 5:
                await message.add_reaction('1️⃣')
                await message.add_reaction('2️⃣')
            elif responses.handle_response2(message.content) == 6 or responses.handle_response2(
                    message.content) == 7 or responses.handle_response2(message.content) == 12:
                arr = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣']
                for i in server.playerList2:
                    if i.health > 0 and message.content.find(i.discord_tag) != 0:
                        await message.add_reaction(arr.pop(0))
            elif responses.handle_response2(message.content) == 8:
                if server.challengeWon == False:
                    await message.add_reaction('👊')
                await message.add_reaction('💃')
                await message.add_reaction('👌')
            elif responses.handle_response2(message.content) == 9:
                if server.challengeWon == False:
                    await message.add_reaction('👊')
                await message.add_reaction('🧑‍✈️')
                await message.add_reaction('🦹‍♂️')
                await message.add_reaction('👌')
            elif responses.handle_response2(message.content) == 10:
                await message.add_reaction('1️⃣')
                await message.add_reaction('2️⃣')
                await message.add_reaction('3️⃣')
                await message.add_reaction('4️⃣')
            elif responses.handle_response2(message.content) == 11:
                await message.add_reaction('1️⃣')
                await message.add_reaction('2️⃣')
                await message.add_reaction('3️⃣')
            elif responses.handle_response2(message.content) == 13:
                server.gaming = False
                server.playerList = []
                server.playerList2 = []
                server.startcount = 0
                server.forcestart = 0
                server.turn = 0
                server.deck = ['🥷', '🤵‍♂️', '💃', '🧑‍✈️', '🦹‍♂️', '🥷', '🤵‍♂️', '💃', '🧑‍✈️', '🦹‍♂️', '🥷', '🤵‍♂️', '💃', '🧑‍✈️',
                        '🦹‍♂️']
                server.vote = 0
                server.challengeWon = False


            return
        else:
            if responses.handle_response2(message.content) == 13:
                server.gaming = False
                server.playerList = []
                server.playerList2 = []
                server.startcount = 0
                server.forcestart = 0
                server.turn = 0
                server.deck = ['🥷', '🤵‍♂️', '💃', '🧑‍✈️', '🦹‍♂️', '🥷', '🤵‍♂️', '💃', '🧑‍✈️', '🦹‍♂️', '🥷', '🤵‍♂️', '💃', '🧑‍✈️',
                        '🦹‍♂️']
                server.vote = 0
                server.challengeWon = False


                await message.channel.send("Game reset, type !start to start a new game.")

            elif responses.handle_response2(message.content) == 14:
                await message.channel.purge(limit=50)
            elif responses.handle_response2(message.content) == 15:
                if server.gaming:
                    player = None
                    for i in server.playerList2:
                        if i.discord_tag == message.author.mention:
                            player = i

                    msg = ''
                    for i in player.cards:
                        msg += i
                    await message.author.send(msg)
            elif responses.handle_response2(message.content) == 16:
                if server.gaming == False:
                    await message.channel.send("Starting a game of Coup, react with :white_check_mark: to join. React with :bomb: to start without 6 players.")
                else:
                    await message.channel.send(f"Game is in progress in {server.server}")
            elif responses.handle_response2(message.content) == 17:
                server.greenfn = not server.greenfn
                if server.greenfn:
                    await message.channel.send("Green FN is now active")
                else:
                    await message.channel.send("Green FN is not active")



        for i in range(len(servers)):
            if servers[i] != None:
                if servers[i].server == message.guild:
                    servers[i] = server



        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)



    @client.event
    async def on_reaction_add(reaction, user):


        # global gaming, startcount, forcestart, playerList, vote, playerList2, challengeWon, temparr, deck
        message = reaction.message
        user_message = str(reaction.emoji)
        channel = str(message.channel)

        global servers

        server = None

        for i in range(0, len(servers)):
            if servers[i] == None:
                servers[i] = coupGame(False, [], [], 0, 0, 0,
                                      ['🥷', '🤵‍♂️', '💃', '🧑‍✈️', '🦹‍♂️', '🥷', '🤵‍♂️', '💃', '🧑‍✈️', '🦹‍♂️', '🥷', '🤵‍♂️',
                                       '💃',
                                       '🧑‍✈️', '🦹‍♂️'], 0, False, [], message.guild, False)
                server = servers[i]
                servers.append(None)
                break
            elif servers[i].server == message.guild:
                server = servers[i]
                break

        print(server.server)
        print(server.gaming)


        if reaction.message.author == client.user:
            print(f"{user} reacted with: '{user_message}' ({channel})")
            if responses.handle_response2(message.content) == 1 and server.gaming == False:
                if reaction.emoji == '✅':
                    server.startcount += 1
                    if server.startcount >= 2:
                        server.playerList.append(user)
                elif reaction.emoji == '💣':
                    server.forcestart += 1
                print(server.startcount)
                print(server.forcestart)
                if server.startcount == 7 or (reaction.emoji == '💣' and server.startcount >= 3 and server.startcount < 7 and server.forcestart >= 2):
                    await Game(server.playerList, message, server)
                    server.gaming = True
            elif responses.handle_response2(message.content) == 2:
                if user.mention in message.content:
                    await Game2(user, reaction.emoji, message, server)
            elif responses.handle_response2(message.content) == 3:
                aliveCount = 0
                player1 = None
                for i in server.playerList2:
                    if i.health >= 1:
                        aliveCount += 1
                if reaction.emoji == '👊':
                    for i in server.playerList2:
                        if i.discord_tag == user.mention and i.health > 0 and (user.mention not in message.content):
                            await claim(i, '🤵‍♂️', message, server)
                elif reaction.emoji == '👌':
                    for i in server.playerList2:
                        if i.health >= 1:
                            if user.mention == i.discord_tag:
                                server.vote += 1
                    if server.vote == aliveCount:
                        server.vote = 0
                        await newTurn(message, server)

            elif responses.handle_response2(message.content) == 4:
                aliveCount = 0
                player1 = None
                for i in server.playerList2:
                    if i.discord_tag in message.content:
                        player1 = i
                    if i.health >= 1:
                        aliveCount += 1

                char = '🤵'
                char2 = 'duke'
                if 'duke' in message.content:
                    char = '🤵‍♂️'
                    char2 = 'duke'
                elif 'assassin' in message.content:
                    char = '🥷'
                    char2 = 'assassin'
                elif 'captain' in message.content:
                    char = '🦹‍♂️'
                    char2 = 'captain'
                elif 'ambassador' in message.content:
                    char = '🧑‍✈️'
                    char2 = 'ambassador'
                elif 'contessa' in message.content:
                    char = '💃'
                    char2 = 'contessa'

                if reaction.emoji == '👊':
                    for i in server.playerList2:
                        if i.discord_tag == user.mention and i.health > 0 and i != player1:
                            await challenge(player1, i, char, message, server)
                            if server.challengeWon == True:
                                if i.health > 0:
                                    await server.playerList[server.playerList2.index(player1)].send(' '.join(player1.cards))
                                    await message.channel.send(
                                        player1.discord_tag + ' did have a(n) ' + char2 + ' and won the challenge, their card has been replaced.' + i.discord_tag + ' must reveal and lose one of their cards.')

                                    await message.delete()
                                else:
                                    if char == '🥷':
                                        if server.challengeWon == True:
                                            await pickTarget(player1, char, message, server)
                                    elif char == '🦹‍♂️':
                                        if server.challengeWon == True:
                                            if player1.potmoney >= 0:
                                                await pickTarget(player1, char, message, server)
                                            else:
                                                server.challengeWon = False
                                                for i in server.playerList2:
                                                    i.potmoney = 0
                                                await newTurn(message, server)
                                    elif char == '🧑‍✈️':
                                        if server.challengeWon == True:
                                            server.challengeWon = False
                                            if player1.potmoney < 0:
                                                for i in server.playerList2:
                                                    i.potmoney = 0
                                                await newTurn(message, server)
                                            else:
                                                await swap(player1, message, server)
                                    else:
                                        server.challengeWon = False
                                        await newTurn(message, server)
                            else:
                                if player1.health > 0:
                                    await message.channel.send(
                                        player1.discord_tag + ' did NOT have a(n) ' + char2 + ' and lost the challenge, they must reveal and lose one of their cards.')
                                    await message.delete()
                                else:
                                    await newTurn(message, server)



                elif reaction.emoji == '👌':
                    for i in server.playerList2:
                        if i.health >= 1:
                            if user.mention == i.discord_tag and user.mention != player1.discord_tag:
                                server.vote += 1

                    if server.vote == aliveCount-1:
                        server.vote = 0
                        if char == '🤵‍♂️' or char == '💃':
                            for i in server.playerList2:
                                i.potdeath = False
                            await newTurn(message, server)
                        elif char == '🥷':
                            await pickTarget(player1, char, message, server)
                        elif char == '🦹‍♂️':
                            if player1.potmoney >= 0:
                                await pickTarget(player1, char, message, server)
                            else:
                                for i in server.playerList2:
                                    i.potmoney = 0
                                await newTurn(message, server)
                        elif char == '🧑‍✈️':
                            if player1.potmoney >= 0:
                                await swap(player1, message, server)
                            else:
                                server.challengeWon = False
                                for i in server.playerList2:
                                    i.potmoney = 0
                                await newTurn(message, server)



            elif responses.handle_response2(message.content) == 5:
                choppingBlock = 0
                player1 = None
                for i in server.playerList2:
                    if i.health == 1 and i.visible_cards == '? ?':
                        choppingBlock = server.playerList2.index(i)
                    if server.challengeWon == True and message.content.find(i.discord_tag) == 0:
                        player1 = i

                if (user == server.playerList[choppingBlock]):
                    if reaction.emoji == '1️⃣':
                        server.playerList2[choppingBlock].visible_cards = server.playerList2[choppingBlock].cards[0] + ' ?'
                        server.playerList2[choppingBlock].cards = [server.playerList2[choppingBlock].cards[1]]
                    elif reaction.emoji == '2️⃣':
                        server.playerList2[choppingBlock].visible_cards = '? ' + server.playerList2[choppingBlock].cards[1]
                        server.playerList2[choppingBlock].cards = [server.playerList2[choppingBlock].cards[0]]


                    if server.challengeWon:
                        if 'assassin' in message.content:
                            if server.challengeWon == True:
                                await pickTarget(player1, '🥷', message, server)
                        elif 'captain' in message.content:
                            if server.challengeWon == True:
                                if player1.potmoney >= 0:
                                    await pickTarget(player1, '🦹‍♂️', message, server)
                                else:
                                    server.challengeWon = False
                                    for i in server.playerList2:
                                        i.potmoney = 0
                                    await newTurn(message, server)
                        elif 'ambassador' in message.content:
                            if server.challengeWon == True:
                                server.challengeWon = False
                                if player1.potmoney >= 0:
                                    await swap(player1, message, server)
                                else:
                                    server.challengeWon = False
                                    for i in server.playerList2:
                                        i.potmoney = 0
                                    await newTurn(message, server)
                        else:
                            await newTurn(message, server)
                    else:
                        await newTurn(message, server)



            elif responses.handle_response2(message.content) == 6:
                attacker = None

                for i in server.playerList2:
                    if message.content.find(i.discord_tag) == 0:
                        attacker = i

                arr = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣']
                arr2 = []
                for i in server.playerList2:
                    if i.health > 0 and i.discord_tag != attacker.discord_tag:
                        arr2.append(i)

                for i in arr:
                    if reaction.emoji == i and message.content.find(user.mention) == 0:
                        target = arr2[arr.index(i)]
                        await assasination(target, attacker, message, server)
            elif responses.handle_response2(message.content) == 7:
                attacker = None

                for i in server.playerList2:
                    if message.content.find(i.discord_tag) == 0:
                        attacker = i

                arr = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣']
                arr2 = []
                for i in server.playerList2:
                    if i.health > 0 and i.discord_tag != attacker.discord_tag:
                        arr2.append(i)

                for i in arr:
                    if reaction.emoji == i and message.content.find(user.mention) == 0:
                        target = arr2[arr.index(i)]
                        await steal(target, attacker, message, server)
            elif responses.handle_response2(message.content) == 8:
                defender = None
                for i in server.playerList2:
                    if message.content.find(i.discord_tag) == 0:
                        defender = i
                attacker = None
                for i in server.playerList2:
                    if message.content.find(i.discord_tag) == message.content.find(', ') + 2:
                        attacker = i

                if user.mention == defender.discord_tag:
                    if reaction.emoji == '👊' and server.challengeWon == False:
                        server.challengeWon = False
                        defender.potdeath = True
                        await challenge(attacker, defender, '🥷', message, server)
                        if server.challengeWon == True:
                            server.challengeWon = False
                            if defender.health > 0:
                                await server.playerList[server.playerList2.index(attacker)].send(' '.join(attacker.cards))
                                await message.channel.send(
                                    attacker.discord_tag + ' did have a(n) ' + 'assassin' + ' and won the challenge, their card has been replaced.' + defender.discord_tag + ' must reveal and lose one of their cards.')
                                await message.delete()
                            else:
                                server.challengeWon = False
                                await newTurn(message, server)
                        else:
                            if attacker.health > 0:
                                await message.channel.send(
                                    attacker.discord_tag + ' did NOT have a(n) ' + 'assassin' + ' and lost the challenge, they must reveal and lose one of their cards.')
                                await message.delete()
                            else:
                                await newTurn(message, server)
                    elif reaction.emoji == '💃':
                        server.challengeWon = False
                        await claim(defender, '💃', message, server)
                    elif reaction.emoji == '👌':
                        server.challengeWon = False
                        defender.health -= 1
                        await message.channel.send(defender.discord_tag + ' must reveal and lose one of their cards.')
                        await message.delete()
            elif responses.handle_response2(message.content) == 9:
                defender = None
                for i in server.playerList2:
                    if message.content.find(i.discord_tag) == 0:
                        defender = i
                attacker = None
                for i in server.playerList2:
                    if message.content.find(i.discord_tag) == message.content.find(', ') + 2:
                        attacker = i



                if user.mention == defender.discord_tag:
                    if reaction.emoji == '👊' and server.challengeWon == False:
                        server.challengeWon = False
                        await challenge(attacker, defender, '🦹‍♂️', message, server)
                        if server.challengeWon == True:
                            server.challengeWon = False
                            if defender.health > 0:
                                await server.playerList[server.playerList2.index(attacker)].send(' '.join(attacker.cards))
                                await message.channel.send(
                                    attacker.discord_tag + ' did have a(n) ' + 'captain' + ' and won the challenge, their card has been replaced.' + defender.discord_tag + ' must reveal and lose one of their cards.')
                                await message.delete()
                            else:
                                server.challengeWon = False
                                await newTurn(message, server)
                        else:
                            for i in server.playerList2:
                                i.potmoney = 0
                            if attacker.health > 0:
                                await message.channel.send(
                                    attacker.discord_tag + ' did NOT have a(n) ' + 'captain' + ' and lost the challenge, they must reveal and lose one of their cards.')
                                await message.delete()
                            else:
                                await newTurn(message, server)

                    elif reaction.emoji == '🦹‍♂️':
                        server.challengeWon = False
                        await claim(defender, '🦹‍♂️', message, server)
                    elif reaction.emoji == '🧑‍✈️':
                        server.challengeWon = False
                        await claim(defender, '🧑‍✈️', message, server)
                    elif reaction.emoji == '👌':
                        server.challengeWon = False
                        await newTurn(message, server)
            elif responses.handle_response2(message.content) == 10:
                player = None
                for i in server.playerList2:
                    if i.discord_tag == user.mention:
                        player = i
                if player.discord_tag in message.content:
                    if len(player.cards) == 0:
                        if reaction.emoji == '1️⃣':
                            player.cards.append(server.temparr[0])
                            server.vote = 1
                        elif reaction.emoji == '2️⃣':
                            player.cards.append(server.temparr[1])
                            server.vote = 2
                        elif reaction.emoji == '3️⃣':
                            player.cards.append(server.temparr[2])
                            server.vote = 3
                        elif reaction.emoji == '4️⃣':
                            player.cards.append(server.temparr[3])
                            server.vote = 4
                    else:
                        if reaction.emoji == '1️⃣' and server.vote != 1:
                            player.cards.append(server.temparr[0])
                        elif reaction.emoji == '2️⃣' and server.vote != 2:
                            player.cards.append(server.temparr[1])
                        elif reaction.emoji == '3️⃣' and server.vote != 3:
                            player.cards.append(server.temparr[2])
                        elif reaction.emoji == '4️⃣' and server.vote != 4:
                            player.cards.append(server.temparr[3])
                        server.deck.append(server.temparr.pop(0))
                        server.deck.append(server.temparr.pop(0))
                        server.vote = 0
                        await newTurn(message, server)
            elif responses.handle_response2(message.content) == 11:
                if user.mention in message.content:
                    if reaction.emoji == '1️⃣':
                        user.cards.append(server.temparr[0])
                    elif reaction.emoji == '2️⃣':
                        user.cards.append(server.temparr[1])
                    elif reaction.emoji == '3️⃣':
                        user.cards.append(server.temparr[2])
                    server.deck.append(server.temparr.pop(0))
                    server.deck.append(server.temparr.pop(0))
                    await newTurn(message, server)
            elif responses.handle_response2(message.content) == 12:
                attacker = None

                for i in server.playerList2:
                    if message.content.index(i.discord_tag) == 0:
                        attacker = i

                arr = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣']
                arr2 = []
                for i in server.playerList2:
                    if i.health > 0 and i.discord_tag != user.mention:
                        arr2.append(i)

                for i in arr:
                    if reaction.emoji == i and user.mention in message.content:
                        target = arr2[arr.index(i)]
                        target.health -= 1
                        if (target.health == 1):
                            await message.channel.send(target.discord_tag + ' must reveal and lose one of their cards.')
                            await message.delete()
                        else:
                            await newTurn(message, server)

        for i in range(len(servers)):
            if servers[i] != None:
                if servers[i].server == message.guild:
                    servers[i] = server

    @client.event
    async def on_reaction_remove(reaction, user):
        global servers

        message = reaction.message

        server = None

        for i in range(0, len(servers)):
            if servers[i] == None:
                servers[i] = coupGame(False, [], [], 0, 0, 0,
                                      ['🥷', '🤵‍♂️', '💃', '🧑‍✈️', '🦹‍♂️', '🥷', '🤵‍♂️', '💃', '🧑‍✈️', '🦹‍♂️', '🥷', '🤵‍♂️',
                                       '💃',
                                       '🧑‍✈️', '🦹‍♂️'], 0, False, [], message.guild, False)
                server = servers[i]
                servers.append(None)
                break
            elif servers[i].server == message.guild:
                server = servers[i]
                break

        if reaction.message.author == client.user:
            if reaction.emoji == '✅':
                server.startcount -=1

        for i in range(len(servers)):
            if servers[i] != None:
                if servers[i].server == message.guild:
                    servers[i] = server

    client.run(TOKEN)


async def Game(playerList, message, server):
    deck = np.array(server.deck)
    np.random.shuffle(deck)
    server.deck = deck.tolist()

    for i in range(len(playerList)):
        server.playerList2.append(Player(playerList[i].mention, '? ?', [server.deck.pop(0), server.deck.pop(0)], 2, 0, False, 2))

    gameMessage = ""

    if server.gaming == False:
        gameMessage += "Playing COUP, review rules by typing !rules\n"
        for i in range(len(playerList)):
            await playerList[i].send(' '.join(server.playerList2[i].cards))

    for i in server.playerList2:
        gameMessage += '\n' + i.discord_tag + ': \nCards: ' + i.visible_cards + ', Money: ' + str(i.money) + '\n'

    await message.channel.send(gameMessage)
    await message.channel.send(server.playerList2[0].discord_tag + ", it's your turn. What would you like to do?")
    await message.delete()


async def Game2(user, reaction, message, server):

    player = None
    for i in range(len(server.playerList)):
        if user == server.playerList[i]:
            player = server.playerList2[i]
            break

    if reaction == '🪙':
        player.money += 1
        await newTurn(message, server)
    elif reaction == '💵':
        player.potmoney = 2
        await message.channel.send(
            player.discord_tag + " is attempting to claim foreign aid. Would anyone like to claim Duke and block this?")
        await message.delete()
    elif reaction == '💰':
        player.potmoney = 3
        await claim(player, '🤵‍♂️', message, server)
    elif reaction == '😈':
        await claim(player, '🦹‍♂️', message, server)
    elif reaction == '🔪':
        if player.money >= 3:
            player.money -= 3
            await claim(player, '🥷', message, server)
    elif reaction == '🎲':
        await claim(player, '🧑‍✈️', message, server)
    elif reaction == '⚔️':
        if player.money >= 7:
            player.money -= 7
            await pickTarget(player, '⚔️', message, server)


async def claim(user, reaction, message, server):
    if reaction == '🤵‍♂️':
        await message.channel.send(user.discord_tag + " is attempting to claim duke. Would anyone like to challenge?")
        await message.delete()
    elif reaction == '💃':
        user.potdeath = True
        await message.channel.send(
            user.discord_tag + " is attempting to claim contessa. Would anyone like to challenge?")
        await message.delete()
    elif reaction == '🦹‍♂️':
        await message.channel.send(
            user.discord_tag + " is attempting to claim captain. Would anyone like to challenge?")
        await message.delete()
    elif reaction == '🧑‍✈️':
        await message.channel.send(
            user.discord_tag + " is attempting to claim ambassador. Would anyone like to challenge?")
        await message.delete()
    elif reaction == '🥷':
        await message.channel.send(
            user.discord_tag + " is attempting to claim assassin. Would anyone like to challenge?")
        await message.delete()


async def challenge(user1, user2, char, message, server):
    if char in user1.cards:
        server.deck.append(char)
        user1.cards[user1.cards.index(char)] = server.deck.pop(0)
        print(type(user1.cards))

        if user2.potdeath:
            user2.health -= 2
        else:
            user2.health -= 1

        user1.potdeath = False
        user2.potdeath = False

        server.challengeWon = True


    else:
        if user1.potdeath:
            user1.health -= 2
        else:
            user1.health -= 1
        
        user1.potmoney = 0

        user1.potdeath = False
        user2.potdeath = False


async def pickTarget(user, char, message, server):
    playerWon = server.playerList2[0]
    checkAlive = 0
    for i in server.playerList2:
        if i.health >= 1:
            checkAlive += 1
            playerWon = i

    if checkAlive == 1:
        server.gaming = False
        await message.channel.send(playerWon.discord_tag + " has won the game")
        if server.greenfn:
            await message.channel.send('https://tenor.com/view/green-fn-peter-griffin-green-gif-1521709978489846232')
        return

    arr = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣']

    players = ''
    if char == '🥷':
        count = 0
        for i in server.playerList2:
            if i.health > 0 and i.discord_tag not in message.content:
                players += arr[count] + ': ' + i.discord_tag + '\n'
                count += 1
        players2 = ', Choose a player to assassinate out of these ' + str(count) + ':\n'
        await(message.channel.send(user.discord_tag + players2 + players))
        await message.delete()
    elif char == '🦹‍♂️':
        count = 0
        for i in server.playerList2:
            if i.health > 0 and i.discord_tag not in message.content:
                players += arr[count] + ': ' + i.discord_tag + '\n'
                count += 1
        players2 = ', Choose a player to steal from out of these ' + str(count) + ':\n'
        await(message.channel.send(user.discord_tag + players2 + players))
        await message.delete()
    elif char == '⚔️':
        count = 0
        for i in server.playerList2:
            if i.health > 0 and i.discord_tag not in message.content:
                players += arr[count] + ': ' + i.discord_tag + '\n'
                count += 1
        players2 = ', Choose a player to coup out of these ' + str(count) + ':\n'
        await(message.channel.send(user.discord_tag + players2 + players))
        await message.delete()


async def assasination(target, attacker, message, server):
    await message.channel.send(
        (target.discord_tag + ', ' + attacker.discord_tag + ' is attempting to assassinate you. What do you do?'))
    await message.delete()


async def steal(target, attacker, message, server):
    if target.money >= 2:
        target.potmoney = -2
        attacker.potmoney += 2
    else:
        target.potmoney = -1 * target.money
        attacker.potmoney = target.money

    await message.channel.send(
        (target.discord_tag + ', ' + attacker.discord_tag + ' is attempting to steal from you. What do you do?'))
    await message.delete()


async def swap(player, message, server):

    playerWon = server.playerList2[0]
    checkAlive = 0
    for i in server.playerList2:
        if i.health >= 1:
            checkAlive += 1
            playerWon = i

    if checkAlive == 1:
        server.gaming = False
        await message.channel.send(playerWon.discord_tag + " has won the game")
        if server.greenfn:
            await message.channel.send('https://tenor.com/view/green-fn-peter-griffin-green-gif-1521709978489846232')
        return


    user = None
    for i in server.playerList:
        if i.mention == player.discord_tag:
            user = i

    server.temparr.append(server.deck.pop(0))
    server.temparr.append(server.deck.pop(0))

    if player.health == 2:
        server.temparr.append(player.cards[0])
        server.temparr.append(player.cards[1])
        player.cards = []
        await user.send(server.temparr[0] + server.temparr[1] + server.temparr[2] + server.temparr[3])
        await message.channel.send(
            player.discord_tag + ', Pick which 2 cards you would like out of the ones dmed to you')
        await message.delete()
    elif player.health == 1:
        server.temparr.append(player.cards[0])
        player.cards = []
        await user.send(server.temparr[0] + server.temparr[1] + server.temparr[2])
        await message.channel.send(player.discord_tag + ', Pick which card you would like out of the ones dmed to you')
        await message.delete()


async def newTurn(message, server):

    playerWon = server.playerList2[0]
    checkAlive = 0
    for i in server.playerList2:
        if i.health >= 1:
            checkAlive += 1
            playerWon = i

    if checkAlive == 1:
        server.gaming = False
        await message.channel.send(playerWon.discord_tag + " has won the game")
        if server.greenfn:
            await message.channel.send('https://tenor.com/view/green-fn-peter-griffin-green-gif-1521709978489846232')
        return


    for i in server.playerList2:
        i.money += i.potmoney
        i.potmoney = 0
        if i.money < 0:
            i.money = 0

    gameMessage = "------------------------------------------"
    for i in server.playerList2:
        if i.health == 0 and i.visible_cards != '? ?':
            i.visible_cards.replace('?', i.cards[0])
        elif i.health == 0:
            i.visible_cards = ' '.join(i.cards)
        gameMessage += '\n' + i.discord_tag + ': \nCards: ' + i.visible_cards + ', Money: ' + str(i.money)
        if (i.health == 0):
            gameMessage += '** (DEAD)**'
    await message.channel.send('\n' + gameMessage + '\n------------------------------------------')

    server.turn += 1
    if server.turn == len(server.playerList2):
        server.turn = 0
    if server.playerList2[server.turn].health == 0:
        server.turn += 1
        if server.turn == len(server.playerList2):
            server.turn = 0

    if server.playerList2[server.turn].money >= 10:
        server.playerList2[server.turn].money -= 7
        await pickTarget(server.playerList2[server.turn], '⚔️', message, server)
    else:
        await message.channel.send(server.playerList2[server.turn].discord_tag + ", it's your turn. What would you like to do?")
        await message.delete()


class Player:
    def __init__(self, discord_tag, visible_cards, cards, money, potmoney, potdeath, health):
        self.discord_tag = discord_tag
        self.visible_cards = visible_cards
        self.cards = cards
        self.money = money
        self.potmoney = potmoney
        self.potdeath = potdeath
        self.health = health
