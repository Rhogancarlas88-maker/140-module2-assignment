Program to prompt user for name and age, then calculate and print birth year.

Input:
    name: stroing, entered via keyboard prompt
    age: integar, entered via keyboard prompt
   

Process:
    Calculate birth year by subtracting age from the current year (2026).

Output:
    Formatted greeting and birth year printed to the console.

Typical usage example:
    What is your name? Alex
    Hold old are you? 24
    Hello Alex! You were born in 2002.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
     name = input("What is your name?")
     age = int(input("How old are you?"))

    # Calculate user's approximate birth year.
      birth-year = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
      print(f"Hello{name}! You were born in {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# zyBooks. (2026). IT-140: Introduction to Scripting. Southern New Hampshire Universty.

