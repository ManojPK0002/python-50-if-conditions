'''
Simulate a coin flip by generating a random outcome (heads or tails).
Ask the user to predict the outcome and determine whether the prediction was correct.
'''
import random


coin_result = random.choice([0, 1])


user_prediction = input("Predict the coin flip result (heads or tails): ")


if (user_prediction == "heads" and coin_result == 0) or (user_prediction == "tails" and coin_result == 1):
    print("Congratulations! Your prediction was correct.")
else:
    print("Sorry, your prediction was incorrect. Better luck next time.")


print(f"The coin flip resulted in {'heads' if coin_result == 0 else 'tails'}.")
