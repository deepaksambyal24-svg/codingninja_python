# Global Variable
level_counter = 0


def increment_level_counter():
    global level_counter
    level_counter += 1
    return print(f'Level:{level_counter} completed.')

increment_level_counter()
increment_level_counter()