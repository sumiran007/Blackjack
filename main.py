import random
#set card value of ace to 11 unless cardvaluesum is 11
card_value = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

money = 50

def draw_card():
    return random.choice(cards)

def calculate_hand_value(hand):
    value = sum(card_value[card] for card in hand)
    num_aces = hand.count("A")
    
    while value > 21 and num_aces:
        value = value - 10
        num_aces = num_aces - 1
    
    return value
#get money will allow a bet
def get_bet(money):
    while True:
        print('welcome to blackjack")
        print('thanks for the money')
        bet = input("Enter your bet: ")
        if not bet.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        bet = int(bet)
        if bet > money:
            print("You don't have enough money")
        else:
            return bet

def play_game(money, card_value, cards):
    bet = get_bet(money)
    money = money - bet
    
    player_hand = [draw_card(), draw_card()]
    print(f"Your hand: {player_hand}")
    
    while True:
        hand_value = calculate_hand_value(player_hand)
        print(f"Hand value: {hand_value}")
        
        if hand_value > 21:
            print("You bust!")
            return money, hand_value, player_hand
        
        action = input("Do you want to hit or stand? type h or s: ")
        if action == 'h':
            player_hand = player_hand + [draw_card()]
            print(f"Your hand: {player_hand}")
        elif action == 's':
            break
        else:
            print("Invalid input. Please enter 'h' to hit or 's' to stand.")
    
    dealer_hand = [draw_card(), draw_card()]
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand = dealer_hand + [draw_card()]
    
    dealer_hand_value = calculate_hand_value(dealer_hand)
    print(f"Dealer's hand: {dealer_hand}")
    print(f"Dealer's hand value: {dealer_hand_value}")
    
    if dealer_hand_value > 21 or hand_value > dealer_hand_value:
        print("You win how did that happen the house is meant to win")
#TODO: need to fix ace card being drawn if cardvaluesum is 11 or greater
        money = money + bet * 2
        return money, hand_value, player_hand
    elif hand_value < dealer_hand_value:
        print("You lose!")
        return money, hand_value, player_hand
    else:
        print("you lose thanks for your mkney!")
# works even for a draw since a draw means loss for the player
        money = money - bet
        return money, hand_value, player_hand

def main():
    global money
    playing = True
    while playing and money > 0:
        money, hand_value, player_hand = play_game(money, card_value, cards)
        print(f"Your final hand: {player_hand}")
        print(f"Final hand value: {hand_value}")
        print(f"Remaining money: {money}")
        if money <= 0:
            print("You are out of money! Game over.")
            playing = False
        else:
            play_again = input("Do you want to play another round? type y or n for yes or nk: ")
            if play_again.lower() != 'y':
                save = open("save.txt", "a")
                name = input("Enter your name that can be saved in the text file for the money you made ")
                save.write(f"{name} {money}\n")
                save.close()
                playing = False

if __name__ == "__main__":
    main()