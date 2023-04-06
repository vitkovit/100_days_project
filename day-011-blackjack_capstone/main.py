from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

house_hand = []
player_hand = []

def deal_card():
    if len(house_hand) == 0:
          house_hand.extend(random.sample(cards, 2))
    if len(player_hand) == 0:
          player_hand.extend(random.sample(cards, 2))
    else:
          house_hand.append(random.choice(cards))
          player_hand.append(random.choice(cards))

def calculate_score(player, house):
      player_check = sum(player)
      house_check = sum(house)
      if player_check == 21:
            print("Player win")
      if house_check == 21:
            print("House win")
      return player_check, house_check
      
deal_card()
print(f'house cards: {house_hand}')
print(f'players cards: {player_hand}')
# print(len(house_hand))
print(calculate_score(player=player_hand, house=house_hand))

# deal_card()
# print(house_hand)
# print(player_hand)
# deal_card()
# print(house_hand)
# print(player_hand)
# deal_card()
# print(house_hand)
# print(player_hand)

# print(calculate_score(player=player_hand, house=house_hand))
