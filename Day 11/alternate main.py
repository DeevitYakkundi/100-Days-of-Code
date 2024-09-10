from turtledemo.penrose import start

import art
import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def drawCards(dealer_Cards_sum,player_Cards_sum):
    dealer_Card3 = random.choice(cards)
    dealer_Cards_sum += dealer_Card3
    player_Card3 = random.choice(cards)
    player_Cards_sum += player_Card3
    print("Your cards: [",player_Card1,",",player_Card2,",",player_Card3,"], Total value:", player_Cards_sum)

start = True

while start is True:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
    if play == "y":
        print("\n"*10)
        print(art.logo)

        dealer_Card1 = random.choice(cards)
        dealer_Card2 = random.choice(cards)
        dealer_Cards_sum = dealer_Card1 + dealer_Card2
        player_Card1 = random.choice(cards)
        player_Card2 = random.choice(cards)
        player_Cards_sum = player_Card1 + player_Card2
        print("Your cards: [",player_Card1,",",player_Card2,"], Total value:", player_Cards_sum)
        print("Dealer card [",dealer_Card1,"], Total value:", dealer_Card2)

        if(player_Cards_sum > 21):
            if (player_Card1 or player_Card2 == 11):
                player_Cards_sum -= 10
            elif (dealer_Card1 or dealer_Card2 == 11):
                dealer_Cards_sum -= 10
            else:
                print("Bust, you went over 21")
                print("Your cards: [",player_Card1,",",player_Card2,"], Total value:", player_Cards_sum)

        if(dealer_Cards_sum == 21):
            print("You lost buddy, Dealer has blackjack")
            print("Your cards: [", player_Card1, ",", player_Card2, "], Total value:", player_Cards_sum)
            print("Dealer card [", dealer_Card1, ",", dealer_Card2, "], Total value:", dealer_Cards_sum)
        elif(player_Cards_sum == 21):
            if(dealer_Cards_sum == 21):
                print("Draw, Dealer also has blackjack")
                print("Your cards: [", player_Card1, ",", player_Card2, "], Total value:", player_Cards_sum)
                print("Dealer card [", dealer_Card1, ",", dealer_Card2, "], Total value:", dealer_Cards_sum)
            print("Black jack you won")
            print("Your cards: [", player_Card1, ",", player_Card2, "], Total value:", player_Cards_sum)
            print("Dealer card [", dealer_Card1, ",", dealer_Card2, "], Total value:", dealer_Cards_sum)
            # after this control should ask if do you want to play black jack
            continue

        draw = input("Type 'y' to get another card, type 'n' to pass:").lower()
        while draw == "y":
            drawCards(dealer_Cards_sum,player_Cards_sum)


        print("endofthesegement")
    else:
        start = False


