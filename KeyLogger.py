from pynput import keyboard

def on_press(key):
    try:
        print(f'Key {key.char} pressed!')
    except AttributeError:
        print(f'Special Key {key} pressed!')

def on_release(key):
    print(f'Key {key} released')
    if key == keyboard.Key.esc:
        # Stop the listener
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
