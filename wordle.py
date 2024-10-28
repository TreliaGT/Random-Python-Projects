import tkinter as tk
from tkinter import messagebox
import random

# A list of possible five-letter words (expand as needed)
WORDS = [
    "apple", "grape", "peach", "lemon", "berry", "mango", "plumb", "guava", "olive", "melon", "chili",
    "onion", "radar", "motel", "sugar", "spice", "brave", "crane", "stone", "flint", "shine", "robin",
    "drake", "flame", "ghost", "sword", "trace", "liver", "piano", "flock", "spark", "climb", "wrist",
    "glide", "blink", "float", "print", "slide", "creep", "blush", "crash", "flute", "straw", "moose",
    "sheep", "tiger", "eagle", "whale", "frost", "cider", "giant", "steel", "plant", "ocean", "plaza",
    "bench", "creek", "brush", "shine", "smile", "earth", "blaze", "grill", "cabin", "storm", "cloud",
    "vapor", "stone", "prism", "laser", "lodge", "ghost", "pearl", "ninja", "amber", "grape", "spear",
    "globe", "fauna", "flora", "polar", "gorge", "plank", "shell", "tulip", "crown", "steep", "valve",
    "hazel", "brisk", "thief", "kneel", "ridge", "smoke", "flame", "beach", "plane", "frost", "cliff",
    "mirth", "sleet", "doubt", "gravy", "stone", "blink", "haunt", "fable", "sling", "wrist", "crisp",
    "brisk", "slide", "shine", "orbit", "boast", "clamp", "stork", "lunar", "solar", "ridge", "blast"
]

TARGET_WORD = random.choice(WORDS).upper()

# Initialize the tkinter window
root = tk.Tk()
root.title("Wordle in Python")

# Number of allowed attempts
num_attempts = 6
guess_length = 5
attempt = 0

# Create a grid to hold each guess's feedback
guess_labels = [[tk.Label(root, text="", width=4, height=2, font=("Helvetica", 18), borderwidth=2, relief="solid") 
                 for _ in range(guess_length)] for _ in range(num_attempts)]

# Place the labels in the grid
for i in range(num_attempts):
    for j in range(guess_length):
        guess_labels[i][j].grid(row=i, column=j, padx=5, pady=5)  # Offset by 2 rows for spacing

# Function to check the guess and update the grid
def check_guess():
    global attempt
    guess = guess_entry.get().upper()
    
    # Validation: Check if guess is five letters
    if len(guess) != guess_length:
        messagebox.showwarning("Invalid Guess", f"Please enter a {guess_length}-letter word.")
        return

    # Display feedback in the guess grid
    for i in range(guess_length):
        color = "gray"
        if guess[i] == TARGET_WORD[i]:
            color = "green"   # Correct letter and position
        elif guess[i] in TARGET_WORD:
            color = "yellow"  # Correct letter, wrong position
        guess_labels[attempt][i].config(text=guess[i], bg=color)
    
    # Check if the guess is correct
    attempt += 1
    
    if guess == TARGET_WORD:
        messagebox.showinfo("Congratulations!", "You guessed the word!")
        root.quit()
    elif attempt >= num_attempts:
        messagebox.showinfo("Game Over", f"Out of attempts! The word was {TARGET_WORD}.")
        root.quit()

    guess_entry.delete(0, tk.END)



# Display instructions
instructions = tk.Label(root, text="Green: Correct letter & position , Yellow: Correct letter & wrong position.")
instructions.grid(row=num_attempts+1, column=0, columnspan=5,  padx=5, pady=5)

instructions = tk.Label(root, text="Enter a 5-letter word and press Guess:")
instructions.grid(row=num_attempts+2, column=0, columnspan=5 , padx=5, pady=5)

# Entry widget for the guess
guess_entry = tk.Entry(root, width=10, font=("Helvetica", 14))
guess_entry.grid(row=num_attempts+3, column=1, columnspan=3, padx=5, pady=5)

# Submit button
guess_button = tk.Button(root, text="Guess", command=check_guess , bg="blue" , fg="white",relief="raised")
guess_button.grid(row=num_attempts+3, column=4 , padx=5, pady=5)

# Run the game
root.mainloop()
