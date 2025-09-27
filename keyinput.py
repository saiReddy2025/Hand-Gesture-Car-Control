from pynput.keyboard import Controller, Key

# Initialize the keyboard controller
keyboard = Controller()

def press_key(key):
    """
    Simulates pressing a key.
    :param key: The key to press (e.g., 'a', 'w', 's', 'd').
    """
    keyboard.press(key)

def release_key(key):
    """
    Simulates releasing a key.
    :param key: The key to release (e.g., 'a', 'w', 's', 'd').
    """
    keyboard.release(key)