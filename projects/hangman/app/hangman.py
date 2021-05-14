from app.words import word_list
from app.stages import Hangman_Stages
import random

MAX_TRIES = 6


class Hangman:
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = MAX_TRIES

    def reset(self):
        self.guessed = False
        self.guessed_letters = []
        self.guessed_words = []
        self.tries = MAX_TRIES

    def get_word(self):
        self.word = random.choice(word_list).upper()
        return self.word

    def __letter_guess__(self, guess):
        if guess in self.guessed_letters:
            print("You already guessed the letter", guess)
        elif guess not in self.word:
            print(guess, "is not in the word.")
            self.tries -= 1
            self.guessed_letters.append(guess)
        else:
            print("Good job,", guess, "is in the word")
            self.guessed_letters.append(guess)
            indices = [i for i, letter in enumerate(self.word) if letter == guess]
            for index in indices:
                self.word_as_list[index] = guess
            self.word_completion = "".join(self.word_as_list)
            if "_" not in self.word_completion:
                self.guessed = True

    def __word_guess__(self, guess):
        if guess in self.guessed_words:
            print("You already guessed the word", guess)
        elif guess != self.word:
            print(guess, "is not the word.")
            self.tries -= 1
            self.guessed_words.append(guess)
        else:
            self.guessed = True
            self.word_completion = self.word

    def play(self, word):
        breakpoint()

        self.word = word
        self.word_completion = "_" * len(word)

        print("Let's play Hangman!")
        print(self.display_hangman(self.tries))
        print(f"{self.word_completion}\n")

        while not self.guessed and self.tries > 0:
            self.word_as_list = list(self.word_completion)

            if self.tries != MAX_TRIES:
                used_letters = " ".join(
                    list(set(self.guessed_letters) ^ set(self.word_as_list) ^ set("_"))
                )
                print(f"Used Letters: {used_letters}")
            guess = input("Please guess a letter or word: ").upper()
            if len(guess) == 1 and guess.isalpha():
                self.__letter_guess__(guess)
            elif len(guess) == len(word) and guess.isalpha():
                self.__word_guess__(guess)
            else:
                print("Not a valid guess.")
            print(self.display_hangman(self.tries))
            print(f"{self.word_completion}\n")
        if self.guessed:
            print("Congrats, you guessed the word! You win!")
            return True
        else:
            print(
                f"Sorry, you ran out of tries. The word was {self.word}. Maybe next time!"
            )
            return False

    def display_hangman(self, tries):
        stages = [
            Hangman_Stages.TURN_6.value,
            Hangman_Stages.TURN_5.value,
            Hangman_Stages.TURN_4.value,
            Hangman_Stages.TURN_3.value,
            Hangman_Stages.TURN_2.value,
            Hangman_Stages.TURN_1.value,
            Hangman_Stages.DEFAULT.value,
        ]
        return stages[tries]


# def main():
#     hangman = Hangman()
#     word = hangman.get_word()
#     hangman.play(word)
#     while input("Play Again? (Y/N) ").upper() == "Y":
#         hangman.reset()
#         word = hangman.get_word()
#         hangman.play(word)


# if __name__ == "__main__":
#     main()
