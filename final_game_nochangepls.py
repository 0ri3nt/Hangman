# from time import sleep
# from functools import reduce
# from wonderwords import RandomWord as r

from random import choice
from tkinter import CENTER, Frame, Button, Canvas, Label, Tk, E, messagebox
from pygame import mixer
from string import ascii_uppercase

#Global Variables
dark_sound_config = 0 
back_limit = 0
guesses_left = 6
word_picked = ""
guessed_letters = set()
secretWord = ""
bg = "black"    #Setting the default colors on startup
fg = "white"
category = ""
words = {"Cities" : ["Mumbai", "Kolkata", "Bangalore", "Delhi", "Indore", "Nagpur", "Chennai", "Hyderabad","Lucknow","Kharagpur"],
         "Fruits" : ['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple', 'apricot', 'lemon', 'coconut', 'watermelon'],
         "Flowers": ["Lily", "Sunflower", "Lotus", "Rose", "Marigold", "Jasmine", "Orchid", "Tulip", "Daffodils", "Daisy", "Hibiscus"]}


#Setting Characteristics to Window
root = Tk()
root.title("Hangman Game - Python Project")
root.geometry('750x500')

#Setting Frames to root window
mainframe = Frame(root)
keyboard_frame = Frame(root)
back_frame = Frame(root)
game_frame = Frame(root)
text_frame = Frame(root)
hang_frame = Frame(root)

#Setting up canvas for hangman
canvas =  Canvas(hang_frame, height=200, width=200, highlightthickness = 0)
word_label = Label(text_frame)
hint_label = Label(text_frame)

#Defining & Initializing sounds
mixer.init()
start_sound = mixer.Sound("menuhit.wav")
back_sound = mixer.Sound("menuback.wav")
sound_positive = mixer.Sound("button_positive.wav")
sound_negative = mixer.Sound("button_negative.wav")
quit_sound = mixer.Sound("quit.wav") 
key_press = mixer.Sound("key_press.wav")
correct_sound = mixer.Sound("correct.wav")
incorrect_sound = mixer.Sound("incorrect.wav")


def start_color(bg):
    root.configure(bg = bg)
    mainframe.config(bg = bg)
    keyboard_frame.config(bg = bg)
    text_frame.config(bg = bg)


def menu(x,fg,bg):
    #Menu Buttons
    hangman_title = Label(mainframe,text = "H A N G M A N",
                        foreground = fg,
                        bg = bg)

    hangman_title.config(font=('Fira Code SemiBold',40))

    start_button = Button(mainframe, text = "Start",
                            width = 30,
                            height = 3,
                            fg = fg,
                            bg = bg,
                            command = start)
    start_button.config(font = ("Arial", 12))
    
    dark_mode_button = Button(mainframe, text = "Dark Mode Toggle",
                            width = 30,
                            height = 3,
                            fg = fg,
                            bg = bg,
                            command = dark_mode)
    dark_mode_button.config(font = ("Arial", 12))

    quit_button = Button(mainframe, 
                            text = "Quit",
                            width = 30,
                            height = 3,
                            fg = fg,
                            bg = bg,
                            command= lambda : quit_func())
    quit_button.config(font = ("Arial", 12))

    if x == 1: #Placess buttons initially and never again so they don'dark_sound_config displace each other on reinitialization
        start_button.place(relx = 0.5, rely = 0.4, anchor = CENTER)
        dark_mode_button.place(relx = 0.5, rely = 0.6, anchor = CENTER)
        quit_button.place(relx = 0.5, rely = 0.8, anchor = CENTER)
        hangman_title.place(relx = 0.5, rely = 0.2, anchor = CENTER)
        
    elif x == 2: #Updates the color of each widget and places it back on the frame
        start_button.config(bg=bg,fg=fg)
        dark_mode_button.config(bg=bg,fg=fg)
        quit_button.config(bg=bg,fg=fg)
        hangman_title.config(bg=bg,fg=fg)
        start_button.place(relx = 0.5, rely = 0.4, anchor = CENTER)
        dark_mode_button.place(relx = 0.5, rely = 0.6, anchor = CENTER)
        quit_button.place(relx = 0.5, rely = 0.8, anchor = CENTER)
        hangman_title.place(relx = 0.5, rely = 0.2, anchor = CENTER)
        
    mainframe.pack(side = "top", expand = True, fill = "both")


def start():
    ui()
    start_sound.play()


def dark_mode():
    global dark_sound_config
    global bg, fg
    if bg == "black": 
        bg = "white"
    elif bg == "white": 
        bg = "black"
    if fg== "black": 
        fg= "white"
    elif fg== "white": 
        fg= "black"
    clear(bg,fg)
    menu(2,fg,bg)
    start_color(bg)
    
    if dark_sound_config%2==0:
        sound_positive.play()
    else:
        sound_negative.play()
    dark_sound_config+=1


def quit_func():
    result = messagebox.askquestion("Quit Hangman", "Are you sure you want to quit?")
    if result == "yes":
        quit_sound.play()
        root.destroy()


def getRandomWord():
    global wordPicked, secretWord, category
    category = choice(list(words.keys()))
    wordPicked = choice(words[category]).lower()
    secretWord = ["_" if letter.isalpha() else letter for letter in wordPicked]


def drawHangman(fg):
    # Draw the hangman based on the number of guesses left
    if guesses_left == 6:
        canvas.create_line(10, 190, 190, 190, width=4, fill=fg)  # Base
        canvas.create_line(90, 190, 90, 10, width=4, fill=fg)  # Pole
        canvas.create_line(90, 10, 170, 10, width=4, fill=fg)  # Top line
        canvas.create_line(170, 10, 170, 40, width=4, fill=fg)  # Rope
    elif guesses_left == 5:
        canvas.create_oval(155, 40, 185, 70, width=4, outline=fg)  # Head
    elif guesses_left == 4:
        canvas.create_line(170, 70, 170, 120, width=4, fill=fg)  # Body
    elif guesses_left == 3:
        canvas.create_line(170, 80, 150, 100, width=4, fill=fg)  # Left arm
    elif guesses_left == 2:
        canvas.create_line(170, 80, 190, 100, width=4, fill=fg)  # Right arm
    elif guesses_left == 1:
        canvas.create_line(170, 120, 150, 150, width=4, fill=fg)  # Left leg
    elif guesses_left == 0:
        canvas.create_line(170, 120, 190, 150, width=4, fill=fg)  # Right leg


def ui():
    global secretWord
    clear(bg,fg)
    mainframe.pack_forget()
    back_frame.place(x=25, y=25)
    keyboard_frame.place(x=10, y=250)
    
    canvas.config(bg=bg)
    canvas.pack()
    hang_frame.place(x = 500, y = 230)
    drawHangman(fg)
    
    getRandomWord()
    word_label.config(text=" ".join(secretWord)+"\n", font=("Helvetica", 24),bg = bg, fg = fg)
    word_label.pack()
    hint_label.config(text = f"Hint: {category}", font=("Oswald", 24),bg = bg, fg = fg)
    hint_label.pack(side = "left")
    text_frame.place(x = 225, y = 75)
    
    n = 0
    for i in ascii_uppercase:
        Button(keyboard_frame,
               width=4,
               text=i,
               bg=bg, fg=fg,
               font=("Oswald", 12),
               command=lambda letter = i, text = i: [getGuess(letter),key_press.play(), button_forget(text)]
               ).grid(row=1 + n // 9, column=n % 9, padx=7, pady=10)
        n += 1

    Button(keyboard_frame,
           bg=bg, fg=fg,
           text="New",
           command = playAgain,
           width=4,
           font=("Oswald", 12)
           ).grid(row=3, column=8, padx=2, sticky = E)


def button_forget(text):
    for widget in keyboard_frame.winfo_children():
        if widget.cget("text") == text:
            widget.grid_forget()


def getGuess(letter):
    global wordPicked, secretWord, guessed_letters, guesses_left
    key_press.play()
    if letter.lower() in guessed_letters:
        return
    guessed_letters.add(letter.lower())
    if letter.lower() in wordPicked:
        for i in range(len(wordPicked)):
            if wordPicked[i].lower() == letter.lower():
                secretWord[i] = wordPicked[i]
    else:
        guesses_left -= 1
        drawHangman(fg)
    updateHangman(0)


def updateHangman(x):
    global hint_label
    word_label.config(text=" ".join(secretWord)+"\n",bg = bg, fg = fg)
    word_label.place()
    
    if "_" not in secretWord:
        word_label.config(text="You Win! The word was:\n"+wordPicked.capitalize())
        word_label.place()
        correct_sound.play()
        for widget in keyboard_frame.winfo_children():
            if widget.cget('text') in ascii_uppercase:
                widget.destroy()
        hint_label.pack_forget()
                
    elif guesses_left == 0:
        word_label.config(bg = bg, fg = fg,text=f"You lose! The word was:\n {wordPicked.capitalize()}")
        word_label.place()  
        incorrect_sound.play()
        for widget in keyboard_frame.winfo_children():
            if widget.cget('text') in ascii_uppercase:
                widget.destroy()
        hint_label.pack_forget()

    
def playAgain():
    global guesses_left, guessed_letters
    guesses_left = 6
    guessed_letters = set()
    getRandomWord()
    word_label.config(bg = bg, fg = fg,text=" ".join(secretWord)+"\n")
    word_label.place()
    canvas.delete("all")
    drawHangman(fg)
    ui()   


def clear(bg, fg):
    global back_limit
    for widget in back_frame.winfo_children():
        widget.destroy()

    back_button = Button(
        back_frame,
        text="Back",
        width=10,
        height=2,
        command=click)

    back_button.configure(bg=bg, fg=fg)
    back_button.pack()
    back_frame.place()


def click():
        back_sound.play()
        text_frame.place_forget()
        hang_frame.place_forget()
        keyboard_frame.place_forget()
        back_frame.place_forget()
        global guesses_left, guessed_letters
        guesses_left = 6
        guessed_letters = set()
        getRandomWord()
        word_label.config(bg = bg, fg = fg,text=" ".join(secretWord)+"\n")
        word_label.place()
        canvas.delete("all")
        menu(0,fg,bg)


start_color(bg)
menu(1,fg,bg)
root.mainloop()