from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random


window = Tk()
window.title('H A N G M A N - Fruit Edition')

photos = [PhotoImage(file="images/hang5.png"),
PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"), PhotoImage(file="images/hang8.png"),
PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]

def newGame():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses=0
    words = ['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple', 'apricot','lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon']
    the_word= random.choice(words)
    the_word_withSpaces = " ".join(the_word)
    lblWord.set(' '.join("_"*len(the_word)))

def guess(letter):
	global numberOfGuesses
	if numberOfGuesses<7:
		txt = list(the_word_withSpaces)
		guessed = list(lblWord.get())
		if the_word_withSpaces.count(letter)>0:
			for c in range(len(txt)):
				if txt[c]==letter:
					guessed[c]=letter
				lblWord.set("".join(guessed))
				if lblWord.get()==the_word_withSpaces:
					messagebox.showinfo("Hangman","You guessed it!")
		else:
			numberOfGuesses += 1
			imgLabel.config(image=photos[numberOfGuesses])
			if numberOfGuesses==6:
					messagebox.showwarning("Hangman","Game Over")
	


imgLabel=Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)


  
lblWord = StringVar()
Label(window, textvariable  =lblWord,font=('consolas 24 bold')).grid(row=0, column=3 ,columnspan=6,padx=10)
l =['']*26
n=0
for c in ascii_uppercase:
    l[ord(c)-65] = Button(window, text=c, state=tk.ENABLED, command=lambda c=c: guess(c), font=('Helvetica 18'), width=4).grid(row=1+n//9,column=n%9)
    n+=1

Button(window, text="New\nGame", command=lambda:newGame(), font=("Helvetica 10 bold")).grid(row=3, column=8)

newGame()
window.mainloop()
