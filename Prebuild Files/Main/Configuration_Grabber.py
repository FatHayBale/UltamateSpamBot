import re

def read_config():
    # Open the config file
    with open('config.txt', 'r') as file:
        # Read the contents of the file
        contents = file.read()

        # Use regular expressions to find the values of the variables
        message = re.search('Message = "(.*?)"', contents).group(1)
        time_inbetween_messages = float(re.search('Time_Inbetween_Messages = "(.*?)"', contents).group(1))
        wait_time_to_start_program = float(re.search('Wait_Time_To_Start_The_Program = "(.*?)"', contents).group(1))
        repeat_messaging_infinitely = re.search('Repeat_Messaging_Infinetly = (.*)', contents).group(1)
        should_enter_be_pressed_by_default = re.search('Should_Enter_Be_Pressed_By_Default = (.*)', contents).group(1)

        # Convert the 'repeat_messaging_infinitely' and 'should_enter_be_pressed_by_default' string to a boolean
        if repeat_messaging_infinitely == 'True':
            repeat_messaging_infinitely = True
        else:
            repeat_messaging_infinitely = False
        
        if should_enter_be_pressed_by_default == 'True':
            should_enter_be_pressed_by_default = True
        else:
            should_enter_be_pressed_by_default = False

    return message, time_inbetween_messages, wait_time_to_start_program, repeat_messaging_infinitely, should_enter_be_pressed_by_default

message, time_inbetween_messages, wait_time_to_start_program, repeat_messaging_infinitely, should_enter_be_pressed_by_default = read_config()

print(message)
print(time_inbetween_messages)
print(wait_time_to_start_program)
print(repeat_messaging_infinitely)
print(should_enter_be_pressed_by_default)
