# IntSleuth! The game.
'''
Have fun with our IntSleuth number guesser!
Challenge the machine to guess the number you are thinking of.
'''

def main():
    '''Main function of the program'''
    print('=== 🎲 Welcome to IntSleuth! 🎲 ===\n') # Welcome message
    print('What range of numbers do you want to play? 🤔') # We ask for the range to make a list with said range of numbers.
    min_range = int(input('⬇ Enter the minimum range: ')) # The user adds the desired minimum range.
    max_range = int(input('⬆ Enter the maximum range: ')) # The user adds the desired maximum range.
    warnings(min_range, max_range)


def warnings(min_range: int, max_range: int):
    '''Checks whether the inserted ranges are valid.'''

    if min_range > max_range: # Activates if the minimum number is greater than the maximum range.
        print('⚠️ The minimum range cannot be greater than the maximum. Please try again.\n')
        main()
    elif min_range == max_range: # Activates if the minimum number is equal to maximum number.
        print('⚠️ The minimum range cannot be equal to the maximum range. Please try again.\n')
        main()
    else: # If numbers are correct, it starts the search in the range given.
        search_list = [number for number in range(min_range, max_range + 1)]
        # We create a list with the ranges added previously.
        attempts = 0 # Starts a count for the number of attempts finding the number.
        play(search_list, attempts) # It calls the function play.


def play(search_list, attempts):
    '''We use dichotomous (binary search) search to play and find the number.'''
    attempts += 1 # Each time the function is executed, it counts the attempts the machine has made.
    mid_index = len(search_list) // 2 # Gives you the middle index of the list.
    mid_value = search_list[mid_index] # Gets the middle value of the list.
    answer = str(input(f'Is {mid_value} the number you thought of? (Write "Yes" or "No"): '))
    # Asks you if the number found is correct, and gives Yes or No as the only options.
    if answer.lower() == 'yes': 
        # Activates if the answer is yes or Yes.
        result(mid_value, attempts)
    else: # Activates if the answer is No or no.
        answer_2 = str(input('Is the number greater or less 🤔?: ')) 
        # Asks you if the number is greater or less again.
        if answer_2.lower() == 'greater':
            # If the answer is greater, limit the list to numbers greater than the middle value.
            play(search_list[mid_index + 1:], attempts) # The function calls itself to search again
        elif answer_2.lower() == 'less':
            # If the answer is less, limit the list to numbers less than the middle value.
            play(search_list[:mid_index], attempts) #The function calls itself to search again.
        else: # Activates if the answer is wrong.
            print('⚠️ The answer is invalid, please try again.\n') # Tells you the answer is invalid.
            play(search_list, attempts - 1) # The function calls itself and subtracts 1 from attempts.


def result(num_searched, attempts):
    '''After finding the number, you decide if you want to play again or not.'''
    print(f"I won 🎉! I found the number {num_searched} in {attempts} attempts.") 
    # Tells you that the program found the number in 'x' attempts correctly
    answer = str(input("Do you want to play again 🔃?: "))
    # A variable with an input to tell the program if you want to play again or not.
    if answer.lower() == 'yes':
    # The program restarts if the answer is yes.
        main()
    else: # If the answer is no or No, then the program stops
        print("Have a nice day 🤭") # It gives an answer if you do not want to play again


if __name__ == '__main__': 
    main()
