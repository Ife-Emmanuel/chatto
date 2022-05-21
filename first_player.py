"""For the first player to launch the game/program on a device."""
import stored_username
import new_username
import not_first_player

def first_player_prompt_and_welcome():
    """To issue introduction and prompt to the first user."""
    try:
        username = stored_username.get_stored_username()
    except FileNotFoundError:
        username = new_username.get_new_username()
        print(username.title() + '. Your name will be remembered')
        return username
    else:
        #first welcome back the previous player
        print('Welcome back ' + username.title())
        #then To prompt the current user if another user wants to play.
        another_username = not_first_player.another_player_prompt()
        if another_username:
            return another_username
        else:
            return username