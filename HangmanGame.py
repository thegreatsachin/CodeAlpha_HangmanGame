import random

# List of predefined words
word_list = ["apple", "house", "tiger", "plane", "robot"]
chosen_word = random.choice(word_list)

# Game variables
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

# Display setup
display_word = ["_" for _ in chosen_word]

print("🎮 Welcome to Hangman!")
print("Guess the word. You have 6 incorrect guesses.\n")

# Game loop
while incorrect_guesses < max_guesses and "_" in display_word:
    print("Word:", " ".join(display_word))
    print(f"Guessed Letters: {', '.join(guessed_letters)}")
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("✅ Correct guess!\n")
        for idx, letter in enumerate(chosen_word):
            if letter == guess:
                display_word[idx] = guess
    else:
        print("❌ Wrong guess.\n")
        incorrect_guesses += 1

# Game result
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("💀 You lost! The word was:", chosen_word)
