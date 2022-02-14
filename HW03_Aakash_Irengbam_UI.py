import HW03_Aakash_Irengbam_Dictionary
def userinterface(RightWord):
    GuessedWordList = []     #To keep track of the words guessed by the user and notify if the same word has been guessed before
    attempt = 0
    while(attempt<6):         #To limit the number of attempts of the user to 6

        guess = input("Enter your 5 letter word guess:  ").lower()    #Take the input from the user
        if(len(guess) == 0):
            quit()
        if(guess in GuessedWordList):          #Check if the word has already been guessed
            print("This was a previous guess please try again")
        else:
            if((len(guess) > 5) or (len(guess) < 5) or (guess.isalpha() == False) or (HW03_Aakash_Irengbam_Dictionary.checking(guess) == False)):   #To check if input has been according to the guidelines
                print("The input should be 5 letters and alphabets and in dictionary only")
                continue
            elif guess == RightWord:           #check if the entered word is correct
                print("This is the correct word")
                Win+=1
                break
            else:                              #to check the condtions on if and where the entered letter locations match with the correct word
                letter_counts: dict = {}
                appraisal = []

                for letter in RightWord:
                    if letter in letter_counts.keys():
                        letter_counts[letter] += 1
                    else:
                        letter_counts[letter] = 1

                for index in range(len(RightWord)):
                    if guess[index] == RightWord[index]:
                        appraisal.append(' ')
                        letter_counts[RightWord[index]] -= 1
                    else:
                        appraisal.append('"')

                for index in range(len(RightWord)):
                    if guess[index] != RightWord[index]:
                        if guess[index] in letter_counts:
                            if letter_counts[guess[index]] > 0:
                                letter_counts[guess[index]] -= 1
                                appraisal[index] = "'"

                print(" "*33 + ''.join(appraisal))
        attempt+=1
        GuessedWordList.append(guess)
    else:                                                                #if the number of attempts have exceeded 6 enterr the condition
        print("Failed in 6 tries no more tries left, try again next time")
