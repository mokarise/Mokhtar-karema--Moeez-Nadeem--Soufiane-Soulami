import random 

def guess_number():
    number = random.randint(1, 100) 
    attempts = 0 

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")

    while True:
        try:
            guess = int(input("Enter your guess: ")) 
            attempts += 1  

            if guess < number:
                print("Too low! Try again.\n")
            elif guess > number:
                print("Too high! Try again.\n")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break  
        except ValueError:
            print("Invalid input! Please enter an integer.\n")

if __name__ == "__main__":
    guess_number()  
