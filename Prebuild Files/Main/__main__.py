import keyboard
from ursina import *
from pynput.keyboard import Key, Listener
import threading
import Configuration_Grabber
import greeter


app = Ursina()
input_field = None
window.color = color._20

numbers = []
letters = []
input_complete = False
input_started = False

# Specify spam variables
Spamming = False
A = "@jnkdz#4972 "
B = 150
C = float(0.1)
D = bool(True)
E = float(4.5)
F = int(1)
G = 150
H = ''
J = bool(False)
K = bool(False)


A = Configuration_Grabber.message
B = Configuration_Grabber.time_inbetween_messages
E = Configuration_Grabber.wait_time_to_start_program
J = Configuration_Grabber.repeat_messaging_infinitely
D = Configuration_Grabber.should_enter_be_pressed_by_default


# Spam Indentifyer
counter = Text(text='Not Spamming', y=.45, z=-1, scale=2, origin=(0,0), background=True)

# Spam Start Button
button = Button(color=color.green, highlight=False, scale= .185, y = -.4)
button.scale_x = .25
button.tooltip = Tooltip(f'Start The Program')

# Start button counter In
Start_Button = Text(text='Start Spamming:', y=-.25, z=-1, highlight=False, scale=2, origin=(0,0), background=True, color = color.green)

# Toggle enter button
button_2 = Button(color=color.dark_gray, highlight=False, scale= .125, origin=(1.7,-1.5), background=True)
button_2.tooltip = Tooltip(f'Toggle Enter')

#Enter button text
InputModeCounter = Text(text='Toggle Enter', x= -.16, y=.19, z=-1, scale=2, origin=(1,0), background=True)

# Text input field
InputMode = Button(color=color.green,hover_color = None, highlight=False, scale= .125, origin=(1.7,-2.58), background=True)
InputMode.tooltip = Tooltip(f'Change Input Mode')


#Input Mode Switch
InputModeCounter = Text(text='Number Input Mode', highlight=False, x= -.55, y=.325, z=-1, scale=2, origin=(0,0), background=True)


# Number Input Stuff
NumberCounter = Text(text='How may times does the program have to run?', origin = (0,-1.3), background=True, scale = 1.5)


# Global flipping settings infertace stuff
InfinityButton = Button(color = color.dark_gray, hover_color = None, highligh = False, scale = .125, origin=(-5.8,-2.58), background = True)
InfinityCounter = Text(text='Program should repeat infinetly', highlight=False, x= .25, y=.325, z=-1, scale=2, origin=(0,0), background=True)
InfinityButton.tooltip = Tooltip(f'Repeat spamming cycle infinetly')


#Information Field
Impy = Text(text='Press Backspace to delete last digit', highlight=False, y=-.06, scale=1.5, origin=(0,0), background=True)
Orty = Text(text='For additional settings modify config.txt file', highlight=False, y=-.15, scale=1.5, origin=(0,0), background=True)



def button_click():
    global Spamming
    if Spamming:
        Spamming = False
    else:
        Spamming = True
    
    if Spamming == True:
        counter.text = 'Spamming'
        time.sleep(E)
        try:
            B = int(G)
        except:
            B = 150
        for i in range(B):
            keyboard.write(A) # simulate typing the phrase
            if D:
                keyboard.press('enter') # simulate pressing the "Enter" key
            time.sleep(C) # delay for C seconds
        print("Simulation completed.")
        counter.text = 'Not Spamming'
    while J:
        counter.text = 'Spamming'
        try:
            B = int(G)
        except:
            B = 150
        for i in range(B):
            keyboard.write(A) # simulate typing the phrase
            if D:
                keyboard.press('enter') # simulate pressing the "Enter" key
            time.sleep(C) # delay for C seconds
        print("Simulation completed.")
        counter.text = 'Not Spamming'

def button_enter_toggle():
    global D
    if D:
        D = False
    else:
        D = True

def button_Infinity_toggle():
    global J
    if J:
        J = False
    else:
        J = True

def button_change_input_mode():
    global F, InputModeCounter
    F = F + 1

    if F == 2:
        F = 0

    if F == 0:
        InputMode.color = color.dark_gray
        InputModeCounter.text = "No Input Mode Selected"
    if F == 1:
        InputMode.color = color.green
        InputModeCounter.text = "Number input mode"


button.on_click = button_click
button_2.on_click = button_enter_toggle
InputMode.on_click = button_change_input_mode
InfinityButton.on_click = button_Infinity_toggle



#Main Functions

numbers = []
input_complete = False

def input(key):
    global G, F, H, K
    global numbers, input_complete, input_started, letters
    if '0' <= key <= '9':
        if F == 1:
            try:
                if int(''.join(map(str,numbers))) > 100000:
                    numbers.pop()
            except:
                print("Wat Da fuck you doing, stop messing with the source code")
            try:
                if not input_complete:
                    if F == 1 and K == False:
                        if key.isnumeric():
                            K = True
                            numbers.append(int(key))
                            input_started = True
                        elif F ==1 and K == True and len(numbers) < 10000:
                            numbers.append(int(key))
                            input_started = True
                        else:
                            print("Please enter a number")
                    key = ''
                    G = int(''.join(map(str,numbers)))
                    print(G)
                    input_complete = True
                elif input_started:
                    if key.isnumeric() and numbers != []:
                        numbers.append(int(key))
                    elif key == 'backspace' or key == 'delete':
                        numbers = ['']
                    key = ''
                    G = int(''.join(map(str,numbers)))
                    print(G)
            except:
                print("Ops you did it again")

def show(key):
    global numbers, G, F
    if F == 1 and key == Key.backspace and G != '':
        print("KEYPRESS")
        try: 
            if G <10:
                numbers = ['']
                G = ''
            else:
                numbers.pop()
            G = int(''.join(map(str,numbers)))
            print(G)
            input_started = True
        except:
            print("small error, happens sometimes")

listener = Listener(on_press = show)
t = threading.Thread(target=listener.start)
t.start()

def update():
    global G, D, B, numbers, J
    if D:
        button_2.color = color.green
    else:
        button_2.color = color.dark_gray
    
    if J:
        InfinityButton.color = color.green
    else:
        InfinityButton.color = color.dark_gray

    try:
        if J == False:
            B = D
            if G > 0 and G != 99999:
                NumberCounter.text = str("The program will run: " + str(G))
            elif G == 99999:
                if G > 99999:
                    numbers.pop()
                    G = int(''.join(map(str,numbers)))
                NumberCounter.text = str("The program will run max amount of times: " + str(G))
            else:
                NumberCounter.text = str("How may times does the program have to run?")
        else:
            NumberCounter.text = str("The program will run infinetly")
    except:
        NumberCounter.text = str("How may times does the program have to run?")
    

greeter.Greet()
app.run()
