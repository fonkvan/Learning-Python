def guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "correct":
        current_guess = ((high - low) // 2) + low
        feedback = input(f"Current guess is {current_guess}. Is this high, low, or correct?" )
        feedback = feedback.lower()
        if(feedback == "low"):
            low = current_guess
        if(feedback == "high"):
            high = current_guess
    print("Yay, I win!")

if __name__ == "__main__":
    guess(1000)