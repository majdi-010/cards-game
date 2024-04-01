import random

suits = ['♠', '♥', '♦', '♣']

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
cards = list(map(str, cards))

deck = []
for i in cards: 
    for suit in suits: 
        deck.append(suit + i) 

lives = 3
score = 0
random.shuffle(deck) 
for i in range(len(deck) + 1): 
    while lives != 0: 
        print()
        print(f"Remaining lives: {lives}\n")
        print("Current card: ",deck[i], "\n")
        answer = input("Is the next card higher, lower, or equal?\n")
        print("Next card is: ",deck[i+1]) 
        if cards.index(deck[i+1][1:]) > cards.index(deck[i][1:]):
            if answer.lower()[0] == "h": #Lenient on spelling mistakes
                print("You guessed right!") 
                score += 1
            else: 
                print("You guessed wrong!") 
                lives -= 1 
        elif cards.index(deck[i+1][1:]) < cards.index(deck[i][1:]):
            if answer.lower()[0] == "l": #Lenient on spelling mistakes
                print("You guessed right!")
                score += 1
            else: 
                print("You guessed wrong!")
                lives -= 1
        else:
            if answer.lower()[0] == "e": #Lenient on spelling mistakes
                print("You guessed right!") 
                score += 1
            else: 
                print("You guessed wrong!")
                lives -= 1
        break;
print()
print(f"You have no more lives. Your score is {score}.")  
                      
                      
    




