import string
from words import choose_word
from images import IMAGES
'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''
    if secret_word==letters_guessed:
        return True
     
    else:
        return False

    

# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])
def if_valid(a):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if len(a)==1 and a in alphabet:
        return True
       
    else:
        return False
             

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet2 = alphabet[:]

    def removeDupsBetter(L1, L2):
        L1Start = L1[:]
        for e in L1:
            if e in L1Start:
                L2.remove(e)
        return ''.join(str(e) for e in L2)

    return removeDupsBetter(letters_guessed, alphabet2)


def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    wordGuessed = False
    remaining_lives=8
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')

    letters_guessed = []
     
    count =0
    while(remaining_lives>0 and wordGuessed is False):
        if secret_word == get_guessed_word(secret_word, letters_guessed):
            wordGuessed = True
            break
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters))
        guess = input("Please guess a letter: ")
        if(if_valid(guess)==True and guess in available_letters):
            letter = guess.lower()
            
            remaining_lives-=1
            s=str(remaining_lives)
            print("Remaining Lives "+ s)
            
            print(IMAGES[count])

            if letter in secret_word:
                
                letters_guessed.append(letter)
                print("Good guess: {} ".format(
                    get_guessed_word(secret_word, letters_guessed)))
                if is_word_guessed(secret_word, letters_guessed) == True:
                    print(" * * Congratulations, you won! * * ", end='\n\n')
            else:
                print("Oops! That letter is not in my word: {} ".format(
                    get_guessed_word(secret_word, letters_guessed)))
                letters_guessed.append(letter)
                print("")
                count+=1
         
        else:
            print("wrong input")
    
    if wordGuessed==True:
        print("Congratulations you won")

    else:
         print("Sorry But You Died.The Correct word was  "+secret_word )  

# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
