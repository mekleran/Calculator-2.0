import random
import time

def ask_math_problem():
    """Function to generate a random math problem and return its solution."""
    x = random.randint(1, 100)
    y = random.randint(1, 25)
    operator = random.choice(['+', '-', '*', '/'])

    if operator == '+':
        solution = x + y
    elif operator == '-':
        solution = x - y
    elif operator == '*':
        solution = x * y
    elif operator == '/':
        # Ensuring division results in an integer.
        solution = x // y
        x = solution * y

    return x, y, operator, solution

def main():
    """Main function to run the math problem game."""
    correct_count = 0

    while True:
        x, y, operator, solution = ask_math_problem()

        while True:
            try:
                user_answer = int(input(f"What is {x} {operator} {y}? "))

                if user_answer == solution:
                    if correct_count == 0:
                        print("You are correct, I'm declaring my retirement.")
                    elif correct_count == 1:
                        print("Smart, I will get going then.")
                    elif correct_count == 2:
                        print("I said, I will be going...")
                        print("Exiting in 5 seconds...")
                    elif correct_count == 3:
                        print("you are good at this, I will leave now.")
                        print("Exiting in 2 seconds...")
                        time.sleep(2)
                        return

                    correct_count += 1

                    play_again = input("Wanna go again? (yes/no): ").strip().lower()
                    if play_again == 'yes':
                        break
                    else:
                        print("Goodbye!")
                        return
                else:
                    print("Try again.")
            except ValueError:
                print("Please enter a valid number.")

if __name__ == "__main__":
    main()
