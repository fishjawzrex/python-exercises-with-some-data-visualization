    

def hangman(secretWord):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num_guess=8
    #warnings=3
    
    n=len(secretWord)
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is ", n," letters long.")
    print("-----------------")
    #print("You have ", warnings, " warnings left.")
    print("You have ", num_guess, " guesses left.")
    lettersGuessed=[]
    print("Available letters: ", getAvailableLetters(lettersGuessed))
    vowels='aeiou'
    score_count=0
    while num_guess>0:
        #print("-----------------")
        s0=str.lower(input("Please guess a letter: "))
        if s0 in string.ascii_lowercase and s0 in lettersGuessed:
            #warnings-=1
           
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            #if warnings<=0:
                #num_guess-=1
            
              
                
        lettersGuessed.append(s0)
        lg=lettersGuessed[:len(lettersGuessed)-1:]
        if s0 in secretWord and len(s0)==1 and s0 not in lg:
            print("Good guess: ", getGuessedWord(secretWord, lettersGuessed))
           
            score_count+=1
        elif s0=='*':
            x=getGuessedWord(secretWord, lettersGuessed)
            print(show_possible_matches(x))
            
        elif s0 in string.ascii_lowercase and s0 not in lg:
            num_guess-=1
            print("Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed))
            #if s0 in vowels:
                #num_guess-=1

        #elif s0 not in string.ascii_lowercase:
            #warnings-=1
  
            #print("Oops! That is not a valid letter. You have ", max(0,warnings), " warning(s) left: ", get_guessed_word(secret_word, letters_guessed))
            #if warnings<=0:
                #num_guess-=1

        num_guess=max(0,num_guess)
        print("-----------------")
        
        if isWordGuessed(secretWord, lettersGuessed)==True:
            #print("-----------------")
            print("Congratulations, you won!")
            break
        if num_guess==0:
            #print("-----------------")
            print("Sorry, you ran out of guesses. The word was", secretWord)
            break
        print("You have ", num_guess, " guess(es) left.")
        print("Available letters: ", getAvailableLetters(lettersGuessed))
        

