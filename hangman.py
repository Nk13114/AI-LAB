class Hangman():
    def _init_(self):
        print("Welcome to 'Hangman'! Ready to die?")
        choice = input("(1)Yes, (2)No ->")
        if choice == '1':
            print("Loading nooses... let's start!")
            self.start_game()
        elif choice == '2':
            print("Goodbye!")
            exit()


        else:
            print("Please choose (1) or (2).")
            self._init_()


    def start_game(self):
        print("You have 6 guesses. Guess the word or face doom!")
        self.core_game()


    def core_game(self):
        word, guesses, used_letters = "pizza", 0, ""
        progress = ["?"] * len(word)
        
        while guesses < 6:
            guess = input("Guess a letter ->").lower()
            
            if len(guess) != 1:
                print("Please enter a single letter!")
                continue
            
            if guess in word and guess not in used_letters:
                used_letters += guess
                progress = self.update_progress(guess, word, progress)
                print(f"Right! {''.join(progress)} Used: {used_letters}")
            elif guess not in word and guess not in used_letters:
                guesses += 1
                used_letters += guess
                print(f"Wrong! {''.join(progress)} Used: {used_letters}")
            elif guess in used_letters:
                print("You've already guessed that letter.")
            
            self.hangman_graphic(guesses)
            
            if "".join(progress) == word:
                print("You won!")
                break
        else:
            print("You were hanged! Game over.")
            self._init_()


    def hangman_graphic(self, guesses):
        stages = [
            "______\n|      |\n|       \n|       \n|       \n|       ",
            "______\n|      |\n|      0\n|       \n|       \n|       ",
            "______\n|      |\n|      0\n|     / \n|       \n|       ",
            "______\n|      |\n|      0\n|     /|\n|       \n|       ",
            "______\n|      |\n|      0\n|     /|\\\n|       \n|       ",
            "______\n|      |\n|      0\n|     /|\\\n|     / \n|       ",
            "______\n|      |\n|      0\n|     /|\\\n|     / \\\n|       "
        ]
        print(stages[guesses])


    def update_progress(self, guess, word, progress):
        return [guess if word[i] == guess else progress[i] for i in range(len(word))]


game = Hangman()