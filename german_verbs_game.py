import csv
import random
import readline  # To fix backspace issue
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Load verbs from the CSV file
verbs = []

with open('german_verbs.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        verbs.append(row)

# Initialize score counters (optional)
correct_count = 0
total_count = 0

# Start the game loop
while True:
    total_count += 1

    # Randomly select a verb
    verb = random.choice(verbs)

    # Get the English translation
    english = verb['English']

    # Display the English translation
    print(f"\n{Style.BRIGHT}English: {english}")

    # Prompt for user input
    infinitive = input("Infinitive: ").strip()
    prateritum = input("Präteritum: ").strip()
    partizip_perfekt = input("Partizip Perfekt: ").strip()

    # Retrieve correct answers
    correct_infinitive = verb['Infinitive'].strip()
    correct_prateritum = verb['Präteritum'].strip()
    correct_partizip_perfekt = verb['Partizip Perfekt'].strip()

    # Check if the answers are correct
    is_infinitive_correct = infinitive.lower() == correct_infinitive.lower()
    is_prateritum_correct = prateritum.lower() == correct_prateritum.lower()
    is_partizip_correct = partizip_perfekt.lower() == correct_partizip_perfekt.lower()

    if is_infinitive_correct and is_prateritum_correct and is_partizip_correct:
        print(Fore.GREEN + Style.BRIGHT + "Correct!")
        correct_count += 1
    else:
        print(Fore.RED + Style.BRIGHT + "Incorrect!")
        print(Fore.RED + "Correct answers:")
        # Display user's incorrect answers alongside correct ones
        if not is_infinitive_correct:
            print(Fore.RED + f"Infinitive: Your answer: {infinitive} | Correct: {correct_infinitive}")
        else:
            print(Fore.GREEN + f"Infinitive: {correct_infinitive}")
        if not is_prateritum_correct:
            print(Fore.RED + f"Präteritum: Your answer: {prateritum} | Correct: {correct_prateritum}")
        else:
            print(Fore.GREEN + f"Präteritum: {correct_prateritum}")
        if not is_partizip_correct:
            print(Fore.RED + f"Partizip Perfekt: Your answer: {partizip_perfekt} | Correct: {correct_partizip_perfekt}")
        else:
            print(Fore.GREEN + f"Partizip Perfekt: {correct_partizip_perfekt}")

    # Display the current score (optional)
    print(f"{Style.BRIGHT}Score: {correct_count}/{total_count}")
    print("-" * 40)
