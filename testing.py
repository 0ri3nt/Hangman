import tkinter as tk
import random
from tkinter import *
from string import ascii_uppercase
from tkinter import messagebox

#Default Theme is dark mode
bg = "white";fg = "black"

class Hangman:
    def __init__(self):
        global bg,fg
        #Setting Characteristics to Window
        root = tk.Tk()
        root.title("Hangman Game - Python Project")
        root.configure(bg = bg)
        root.geometry('750x500')
        mainframe = Frame(root)
        mainframe.config(bg = bg)
        gameframe = Frame(root)
        gameframe.config(bg = bg)
        options_frame = Frame(root)
        options_frame.config(bg = bg)
        return gameframe, mainframe, options_frame
        

    def switch_color():
        if bg == "black" : bg = "white"  
        else : bg = "black",
        if fg == "white" : fg = "black"  
        else : fg = "white",
    

    def menu():
        #Menu Buttons
        hangman_title = tk.Label(mainframe,text = "H A N G M A N",
                            foreground = fg,
                            bg = bg)

        hangman_title.config(font=('Fira Code SemiBold',40))

        start_button = tk.Button(mainframe, text = "Start",
                                width = 30,
                                height = 3,
                                fg = fg,
                                bg = bg,
                                command = ui)
        start_button.config(font = ("Arial", 12))
        
        options_button = tk.Button(mainframe, text = "Dark Mode Toggle",
                                width = 30,
                                height = 3,
                                fg = fg,
                                bg = bg,
                                command = options)
        options_button.config(font = ("Arial", 12))

        quit_button = tk.Button(mainframe, 
                                text = "Quit",
                                width = 30,
                                height = 3,
                                fg = fg,
                                bg = bg,
                                command= root.destroy)
        quit_button.config(font = ("Arial", 12))

        start_button.place(relx = 0.5, rely = 0.4, anchor = CENTER)
        options_button.place(relx = 0.5, rely = 0.6, anchor = CENTER)
        quit_button.place(relx = 0.5, rely = 0.8, anchor = CENTER)
        hangman_title.pack(side = TOP,pady = 50)
        mainframe.pack(side = "top", expand = True, fill = "both")


    def game():
        def getRandomWord():
            words = ['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple', 'apricot','lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon']
            word = random.choice(words)
            return word


        def displayBoard(hang, missedLetters, correctLetters, secretWord):
            print(hang[len(missedLetters)])
            print()

            print('Missed Letters:', end=' ')
            for letter in missedLetters:
                print(letter, end=' ')
            print("\n")

            blanks = '_' * len(secretWord)

            for i in range(len(secretWord)):  # replace blanks with correctly guessed letters
                if secretWord[i] in correctLetters:
                    blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

            for letter in blanks:  # show the secret word with spaces in between each letter
                print(letter, end=' ')
            print("\n")


        def getGuess(alreadyGuessed):
            while True:
                guess = input('Guess a letter: ')
                guess = guess.lower()
                if len(guess) != 1:
                    print('Please enter a single letter.')
                elif guess in alreadyGuessed:
                    print('You have already guessed that letter. Choose again.')
                elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                    print('Please enter a LETTER.')
                else:
                    return guess


        def playAgain():
            return input("\nDo you want to play again? ").lower().startswith('y')


        missedLetters = ''
        correctLetters = ''
        secretWord = getRandomWord()
        gameIsDone = False


        while True:
            displayBoard(hang, missedLetters, correctLetters, secretWord)

            guess = getGuess(missedLetters + correctLetters)

            if guess in secretWord:
                correctLetters = correctLetters + guess

                foundAllLetters = True
                for i in range(len(secretWord)):
                    if secretWord[i] not in correctLetters:
                        foundAllLetters = False
                        break
                if foundAllLetters:
                    print('\nYes! The secret word is "' +
                        secretWord + '"! You have won!')
                    gameIsDone = True
            else:
                missedLetters = missedLetters + guess

                if len(missedLetters) == len(hang) - 1:
                    displayBoard(hang, missedLetters,
                                correctLetters, secretWord)
                    print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                        str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
                    gameIsDone = True

            if gameIsDone:
                if playAgain():
                    missedLetters = ''
                    correctLetters = ''
                    gameIsDone = False
                    secretWord = getRandomWord()
                else:
                    break


    def ui():
        clear()
        gameframe.pack(side="top", expand=True, fill="both")
        n = 0
        for i in ascii_uppercase:
            Button(gameframe,width = 4, text = i, font = ("Oswald",12)).grid(row = 1+n//9, column = n%9,padx = 10, pady = 10, sticky = W)
            n+= 1 
        Button(gameframe, text = "New Game",font = ("Oswald",12)).grid(row = 3, column = 8, padx = 2)
        

    def options():
        clear()
        global bg, fg
        options_frame.pack(side="top", expand=True, fill="both")
        Button(options_frame, text = "Toggle Dark Mode", height = 5, width = 20, command = switch_color)


        root.configure(bg= bg)
        root.mainloop()


    def clear():
        gameframe.pack_forget()
        mainframe.pack_forget()
        options_frame.pack_forget()
        back_button = tk.Button(gameframe,
                                text = "Back",
                                bg = bg,
                                fg = fg,
                                command = lambda : [menu(),click(back_button)],
                                width = 10,
                                height = 2)

        back_button.place(relx = 0.05 , rely = 0.05, anchor = NW)


    def click(b):
            b.pack_forget()


    
    menu()
    root.mainloop()


