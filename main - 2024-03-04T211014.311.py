import pyautogui
import time

# Delay before starting typing (to switch to iPhone screen)
time.sleep(5)

# Passcode to be entered
passcode = "1234"  # Replace with your passcode

# Define positions of passcode digits on the iPhone screen
digit_positions = {
    "1": (100, 200),
    "2": (200, 200),
    "3": (300, 200),
    "4": (100, 300),
    "5": (200, 300),
    "6": (300, 300),
    "7": (100, 400),
    "8": (200, 400),
    "9": (300, 400),
    "0": (200, 500),
}

# Function to type a digit on the iPhone screen
def type_digit(digit):
    position = digit_positions[digit]
    pyautogui.click(position)

# Iterate through each digit of the passcode and type it
for digit in passcode:
    type_digit(digit)
    # Add a small delay between typing each digit (adjust if needed)
    time.sleep(0.5)

# Optional: Click on the "Enter" button if needed
# enter_button_position = (300, 500)  # Adjust the position according to your iPhone screen
# pyautogui.click(enter_button_position)
