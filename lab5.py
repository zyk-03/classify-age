def classify_age():
    age = int(input("How old are you?: "))
    if age >= 65:
        print("You are a Senior.")
    elif age >= 20:
        print("You are an Adult.")
    elif age >= 13:
        print("You are a Teen.")
    elif age < 0:
        print("Please enter a valid age.")
    else:
        print("You are a Child.")
        
classify_age()
