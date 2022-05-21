#! /usr/bin/python3
"""Using my usermade json-module to store and retrieve
users data"""
import difficulty_determiner
import random
import decorator_function
import first_player
import program_end
#Load the username, if it has been stored previously.
#Otherwise, prompt for the username and store it.

players_details = []

active = True
while active:
    #To issue introduction and prompt to the first user.
    username = first_player.first_player_prompt_and_welcome()
    well = True
    while well:
        details = []
        profile = []  # for appending the level(easy/medium/legend) used for the round of a game.
        response_2 = input('Start game now ? (1/2) : ')# Initial question
        print('\n===============================================================================\n')

        # Now for the game: A number guess game.
        if response_2 == '1':
            #If response to initial question is 1, game will play.

            total_guesses = []   #total guesses is the list of all user's guesses both valid and invalid.
            valid_guesses = []  # Valid guesses is the list of user's guess that end up being thesame as the computer correct guess.

            decorator_function.game_prompt()  # Imported decorated function to prompt player of GAME START
            #Using function from imported module to prompt and get and determine difficulty.
            both = difficulty_determiner.level_option_list_number_level()
            level_option = both[0]
            list_number = both[1]
            level = both[2]
            profile.append(level)

            #MAIN PROGRAM LOGIC
            print('\nWhenever you want to quit, please enter "0".\n')
            good = True
            while good:  #loop works continueing asking for numbers and guesses until 5 numbers are entered.
                another_good = True #Flag that determines whether the just following loop runs unstop
                # due to user innocent error of entering number less than potential number options of a level option
                while another_good:
                    try:
                        entered_number = int(input('Enter a number : '))
                        if entered_number == 0:
                            break
                        condition_1 = level_option == 1 and entered_number < 2
                        condition_2 = level_option == 2 and entered_number < 3
                        condition_3 = level_option == 3 and entered_number < 4
                        if condition_1 :
                            print('Enter a number that is equal or more than 2!')
                            continue
                        elif condition_2:
                            print('Enter a number that is equal or more than 3! ')
                            continue
                        elif condition_3:
                            print('Enter a number that is equal or more than 4! ')
                            continue

                    except ValueError:
                        print('Enter numbers not letters! ')

                    else:
                        number_list = [(i + 1) for i in range(entered_number)]
                        listing = random.sample(number_list, list_number) #number_list is the iteratable list of elements in range of list_number.
                        another_good = False  #False flag to stop the loop once there is
                        #no user innocent error of entering number less than potential number options of each option

                print(username)
                print(username.title() + ', you will have ' + str(list_number) + ' numbers! '
                                'from 1 to ' + str(entered_number))
                print('Here is the list of numbers. >>>>Guess the one golden number.')
                for number in listing:
                    print(number)
                random.shuffle(listing)
                correct_guess = listing[1] # Correct guess is the guess produced by the computer upon using the random.shuffle() function
                status_here = True
                while status_here: #loop for the guess number incase number enter is not valid
                    try:
                        user_guess = int(input('Enter your guess : '))
                    except ValueError:
                        print('Enter a number not letter')
                        continue
                    else:
                        if user_guess == 0:
                            end_response = input('Are you sure you want to stop this game? If yes press "1", else press "2".')
                            if end_response == 1:
                                good = False
                            elif end_response == 2:
                                good = True
                        total_guesses.append(user_guess)
                        if len(total_guesses) == 5:
                            good = False

                        if user_guess == correct_guess:
                            print('Wow! you got it.')
                            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
                            valid_guesses.append(user_guess)
                        else:
                            print('oops you missed it.\n'
                                  'You can play again.')
                            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n')
                        status_here = False

            valid_score = len(valid_guesses)
            profile.append(valid_score)
            total_score = len(total_guesses)
            details.append(username)
            details.append(profile)
            players_details.append(details)
            print(username.title() + ' Your score in Guess game is ' + str(valid_score) +
                  ' out of ' + str(total_score) + ' attempted guesses.')

            #Another question for a user who has just finished playing.

            question_status = True
            while question_status:
                response_3 = input('Do you want to play again : ')
                if response_3 == '1':
                    question_status = False
                    good = False
                    continue
                elif response_3 == '2':
                    well = False
                    question_status = False
                else:
                    question_status = True

        #Action if user says no to initial question
        elif response_2 == '2':
            continue
        elif response_2 == '0':
            well = False
        else:
            print('Enter a valid number (1 or 2)')
            continue

    #Asking question if user wants to finally quit game
    response_4 = (input('Quit Game ? : '))
    print('\n========================================\n')
    if response_4 == '1':
        active = False
    elif response_4 == '2':
        active = True

##GAME CONCLUSION
print('\n=====================================================================')
print(username.title() + ', You have successfully closed Guess Game!!!')
print('=====================================================================\n')

#list_number of top three scorers
print('\n==========================================================================')
ranked_players = sorted(players_details, reverse=True, key=lambda player: player[1][1])
first_three = ranked_players[: 3]
decorator_function.top_winners() # Imported decorated function of top three players
print('Below are the top three scorers : ')
print('{:<12}{:<12}{:<12}{:<12}'.format('S/N', 'Player', 'Level', 'Score'))
for i, (player, (level, score)) in enumerate(first_three):
    print('{:<12}{:<12}{:<12}{:<12}\n'.format(str(i + 1) + '.', player.title(), level, score))
print('=====================================================================\n')

## If we were to rank the all the players.
ranked_players = sorted(players_details, reverse=True, key=lambda x : x[1][len(x[1])-1])
print('\nBelow is the rank of all ' + str(len(players_details)) +  ' : \n')
print('{:<12}{:<12}{:<12}{:<12}'.format('S/N', 'Player', 'Level', 'Score'))
for i, (player, (level, score)) in enumerate(ranked_players):
    print('{:<12}{:<12}{:<12}{:<12}\n'.format(str(i + 1) + '.', player.title(), level, score))
print('=======================================================================')
program_end.exit_program()