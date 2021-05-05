#!/usr/bin/env python
class Game:
    def __init__(self) -> None:
        self.word = input("What word are we using for a test?")

    def choose_letter(self, letter: str) -> bool:
        pass

    def __is_match(self, letter: str) -> bool:
        return letter in self.word

    def result(self):
        return True  # TODO: Do something with this


game = Game()
print(f"Result is {game.result()}")
