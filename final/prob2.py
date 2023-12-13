import random
list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_pick = random.sample(list, 2)
dealer_pick = random.sample(list, 2)
dealer_show_card = random.choice(dealer_pick)

print(f"{my_pick}")
print("dealer card:", dealer_pick)
print(f"dealer card show 1 : {dealer_pick}")

def score_sum(card_pick):
    sum = 0
    for card in card_pick:
        sum += card
    return sum
    
my_score = score_sum(my_pick)
dealer_score = score_sum(dealer_pick)
print(f"my score: {my_score}")
print("dealer score:", {dealer_score})

if dealer_score < 17:
    a = True
    while a:
        one_more_card = random.sample(list, 1)
        dealer_pick.extend(one_more_card)
        dealer_score = score_sum(dealer_pick)
        print("new dealer card:", dealer_pick)
        print("new dealer score:", dealer_score)
        if dealer_score > 16:
            a = False
            
def winner(my_score, dealer_score):
    if my_score > dealer_score:
        print("win!")
    elif my_score == dealer_score:
        print("draw")
    else:
        print("Lose")

def decision(my_score, dealer_score):
    stand_hit = input("stand? of hit?")
    Keep_going = True
    while Keep_going:
        if stand_hit == "stand":
            if dealer_score > 21:
                print("win!")
                Keep_going = False
            else:
                winner(my_score, dealer_score)
                Keep_going = False
        elif stand_hit == "hit":
            one_more_card = random.sample(list, 1)
            my_pick.extend(one_more_card)
            my_score = score_sum(my_pick)
            print(f"my card list: {my_pick}")
            print(f"mt score: {my_score}")
            if my_score > 21:
                print("Lose")
                Keep_going = False
            else:
                stand_hit = input("stand? or hit?")
                
decision(my_score, dealer_score)

game_start = True
while game_start:
    want_game = input("/t Welcom to Blackjeck! /t")
