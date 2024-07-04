import random

def coin_toss():
    return "Heads" if random.randint(0, 1) == 0 else "Tails"

def heads_or_tails_game():
    name = input("Who are you?\n> ")
    print(f"Hello, {name}!")
    
    print("Tossing a coin...")

    results = [coin_toss() for _ in range(3)]

    for i, result in enumerate(results):
        print(f"Round {i + 1}: {result}")

    heads_count = results.count("Heads")
    tails_count = results.count("Tails")

    print(f"Heads: {heads_count}, Tails: {tails_count}")

heads_or_tails_game()
