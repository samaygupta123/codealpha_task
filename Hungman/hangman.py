import tkinter as tk
from tkinter import messagebox

# Sample word list
WORDS = ["python", "hangman", "developer", "interface", "program"]

# Choose one word
import random
word = random.choice(WORDS).lower()
guessed_letters = set()
max_attempts = 6
attempts_left = max_attempts

# Displayed word as underscores
displayed_word = ["_" for _ in word]


# ---- GUI Setup ----
def guess_letter():
    global attempts_left
    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if not letter.isalpha() or len(letter) != 1:
        messagebox.showwarning("Invalid Input", "Please enter a single letter.")
        return

    if letter in guessed_letters:
        messagebox.showinfo("Already Guessed", f"You already guessed '{letter}'.")
        return

    guessed_letters.add(letter)

    if letter in word:
        for idx, char in enumerate(word):
            if char == letter:
                displayed_word[idx] = letter
        update_display()
        if "_" not in displayed_word:
            messagebox.showinfo("You Win!", f"Congratulations! The word was '{word}'.")
            reset_game()
    else:
        attempts_left -= 1
        attempts_label.config(text=f"Attempts left: {attempts_left}")
        if attempts_left == 0:
            messagebox.showinfo("Game Over", f"You're out of attempts! The word was '{word}'.")
            reset_game()


def update_display():
    word_label.config(text=" ".join(displayed_word))


def reset_game():
    global word, guessed_letters, attempts_left, displayed_word
    word = random.choice(WORDS).lower()
    guessed_letters = set()
    attempts_left = max_attempts
    displayed_word = ["_" for _ in word]
    update_display()
    attempts_label.config(text=f"Attempts left: {attempts_left}")


# Tkinter window setup
root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x300")

title_label = tk.Label(root, text="Hangman", font=("Arial", 24))
title_label.pack(pady=10)

word_label = tk.Label(root, text=" ".join(displayed_word), font=("Arial", 20))
word_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=5, justify='center')
entry.pack()

guess_button = tk.Button(root, text="Guess", command=guess_letter, font=("Arial", 12))
guess_button.pack(pady=5)

attempts_label = tk.Label(root, text=f"Attempts left: {attempts_left}", font=("Arial", 12))
attempts_label.pack(pady=5)

reset_button = tk.Button(root, text="Reset Game", command=reset_game, font=("Arial", 10))
reset_button.pack(pady=10)

root.mainloop()
