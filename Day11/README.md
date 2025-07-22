# 🃏 Blackjack Game

A text-based Blackjack (21) game where the player competes against the computer (dealer), built using Python lists and control flow.

## 📌 What It Does

- Simulates a game of Blackjack in the terminal.
- Deals random cards to player and dealer.
- Allows the player to hit (draw a card) or stand.
- Automatically plays dealer's turn based on standard rules.
- Calculates and compares final scores to determine the winner.

## 🧠 Concepts Covered

- Lists and list manipulation
- Random selection with `random.choice()`
- Function decomposition
- Conditional logic (`if` / `else`)
- Game loop and score comparison
- Handling special case of Ace (value 11 or 1)

## 🃎 Rules Implemented

- Aces count as 11 unless it would cause a bust.
- The dealer must draw until reaching 17 or more.
- Blackjack is an instant win (Ace + 10-value card).
- The game ends when the user chooses to stand or goes over 21.