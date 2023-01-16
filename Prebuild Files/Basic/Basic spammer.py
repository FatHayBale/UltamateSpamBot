import keyboard
import time

# Get input from user
A = input("Enter a phrase: ")
B = int(input("Enter a number of repetitions: "))
C = float(input("Enter delay in seconds between repetitions: "))
D = input("Simulate enter key? (y/n)")
E = float(input("Enter delay in seconds before starting the program: "))

# Wait for E seconds before starting the program
time.sleep(E)

# Use a for loop to simulate keystrokes B times
for i in range(B):
    keyboard.write(A) # simulate typing the phrase
    if D.lower() == "y":
        keyboard.press('enter') # simulate pressing the "Enter" key
    time.sleep(C) # delay for C seconds

print("Simulation completed.")
