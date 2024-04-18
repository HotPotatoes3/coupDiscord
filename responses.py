def handle_response(message) -> str:
    p_message = message.lower()

    # if p_message == '!start':
    #     if gameinProgress:
    #         return "Game is in progress"
    #     else:
    #         gameinProgress = True
    #         return "Starting a game of Coup, react with :white_check_mark: to join. React with :bomb: to start without 6 players."

    if p_message == '!rules' or '!help':
        return "Type !start to initialize a game. Refer to https://boardgame.bg/coup%20rules%20pdf.pdf to learn coup game rules\nAt the beginning of the game, you will recieve a direct message of your 2 starting cards which are 2 emojis.\nThe 5 possible cards you may recieve are:\nDuke: 🤵\nAmbassador: 🧑‍✈️\nCaptain: 🦹‍♂️\nAssassin: 🥷\nContessa: 💃\n\nIn addition to this, at the start of each turn, you may do one of the following actions:\n🪙: Gain one coin\n💵: Gain 2 coins (can be blocked by someone claiming duke)\n💰: Claim duke to earn 3 coins\n😈: Claim captain to steal 2 coins from another player\n🔪: Claim assassin to pay 3 coins to assassinate another player\n🎲: Claim ambassador to swap your cards\n⚔️: Pay 7 coins to coup another player (You will automatically be forced to coup if you have 10 or more coins)\n\nWhenever there is a card claim, all players must unanimously vote to allow the claim by reacting with 👌\nOtherwise, the player who first presses 👊 will be the one to challenge the claim."
    if p_message == '!green fn':
        return 'https://tenor.com/view/green-fn-peter-griffin-green-gif-1521709978489846232'

def handle_response2(message):
    if message == "Starting a game of Coup, react with :white_check_mark: to join. React with :bomb: to start without 6 players.":
        return 1
    if ", it's your turn. What would you like to do?" in message:
        return 2
    if "Would anyone like to claim Duke and block this?" in message:
        return 3
    if "Would anyone like to challenge?" in message:
        return 4
    if ' must reveal and lose one of their cards.' in message:
        return 5
    if ', Choose a player to assassinate out of these ' in message:
        return 6
    if ', Choose a player to steal from out of these ' in message:
        return 7
    if ' is attempting to assassinate you. What do you do?' in message:
        return 8
    if ' is attempting to steal from you. What do you do?' in message:
        return 9
    if ', Pick which 2 cards you would like out of the ones dmed to you' in message:
        return 10
    if ', Pick which card you would like out of the ones dmed to you' in message:
        return 11
    if ', Choose a player to coup out of these ' in message:
        return 12
    if ' has won the game' in message:
        return 13
    if '!reset' == message:
        return 13
    if '!purge' == message:
        return 14
    if '!cards' == message:
        return 15
    if '!start' == message:
        return 16
    if '!togglegfn' == message:
        return 17
