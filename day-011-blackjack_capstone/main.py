from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

house_hand = []
player_hand = []

# def deal_card():
#     if len(house_hand) == 0:
#           house_hand.extend(random.sample(cards, 2))
#     if len(player_hand) == 0:
#           player_hand.extend(random.sample(cards, 2))
#     else:
#           house_hand.append(random.choice(cards))
#           player_hand.append(random.choice(cards))

def deal_card(input_list):
      return input_list.append(random.choice(cards))
      

def calculate_score(player, house):
      player_check = sum(player)
      house_check = sum(house)
      if player_check == 21:
            print("Player win")
      if house_check == 21:
            print("House win")
      return player_check, house_check

def play_game():
      if sum(house_hand) < 17:
          deal_card(house_hand)
      else:
          print(house_hand)
      if sum(player_hand) < 21:
          deal_card(player_hand)
      else:
          print(player_hand)


play_game()

def display_the_game():
          print(f'house hand - [{house_hand[0]}, X]')
          print(player_hand)
          if sum(house_hand) > 21:
                print(f"House Busted {house_hand}")
          if sum(player_hand) > 21:
                print("Player Busted")
          if sum(player_hand) > sum(house_hand):
                print("Player Won")
# display_the_game()
end_game = False

while len(player_hand) < 21 and end_game == False:
      hit = input('hit me y|n :')
      if hit == 'y':
            play_game()
            display_the_game()
      else:
            end_game = True          
# deal_card()
# print(f"house cards: [{house_hand[0]}, X]")
# print(f'players cards: {player_hand}')
# # print(len(house_hand))
# print(calculate_score(player=player_hand, house=house_hand))




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
