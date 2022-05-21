import new_username
def another_player_prompt():
    """Prompt whether to allow another user to play or rather continue as thesame player"""
    while True:
        try:
            response = int(input('Do you want another user to play this game ? \nif yes press  1'
          ', else press 2 : '))
        except Exception:
            print('make sure you read clearly the information and '
                  'input your response again')
            continue
        else:
            if response == 1:
                username = new_username.get_new_username()
                print('Welcome ' + username.title() + '. Your name will be remembered when next you log in.')
                return username
                break
            elif response == 2:
                return
                break
