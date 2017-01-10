for i in range (1,10):
    score = int(raw_input("What score between 60 and 100 did you recieve?>> "))
    if (score<60):
        print("Invalid Response!")
    elif (score<=69):
        print("Score: " + str(score) + "; Your grade is D")
    elif (score<=79):
        print("Score: " + str(score) + "; Your grade is C")
    elif (score<=89):
        print("Score: " + str(score) + "; Your grade is B")
    elif (score<=100):
        print("Score: " + str(score) + "; Your grade is A")
