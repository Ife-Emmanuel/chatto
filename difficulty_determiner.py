"""Returns the 'both' which is a list containing three things: level_option, list_number and level"""
def level_option_list_number_level():
    """returns three as the name implies respectively."""
    both = []
    status = True
    while status:
        try:
            level_option = int(input('\nChoose difficulty level : '))
        except ValueError:
            status = True
        else:
            if level_option == 1:
                list_number = 2
                level = 'easy'
            elif level_option == 2:
                list_number = 3
                level = 'medium'
            elif level_option == 3:
                list_number = 4
                level = 'legend'
            else:
                continue
            status = False
            both.append(level_option)
            both.append(list_number)
            both.append(level)
    return both