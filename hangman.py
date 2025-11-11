import random

def hangman():
    # List of words to choose from
    words = ["python", "developer", "hangman", "challenge", "programming", "openai"]
    word = random.choice(words).lower()
    guessed = "_" * len(word)
    guessed_letters = set()
    attempts = 6

    print("🎯 Welcome to Hangman!")
    print("Guess the word:")
    print(" ".join(guessed))

    while attempts > 0 and "_" in guessed:
        guess = input("\nEnter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single alphabetic character.")
            continue
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Correct!")
            guessed = "".join([letter if letter in guessed_letters else "_" for letter in word])
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")

        print("Word: " + " ".join(guessed))
        print("Guessed letters: " + ", ".join(sorted(guessed_letters)))

    if "_" not in guessed:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game over! The word was:", word)

if __name__ == "__main__":
    hangman()
