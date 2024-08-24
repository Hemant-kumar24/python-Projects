# this is my automatic sending messages which is depend on the user input
#  how many times user want to send the message
import pyautogui
import time

def message_sender(message):
    print("open the what's app web ")
    time.sleep(5)
    for i in range(n):
        pyautogui.write(message)
        time.sleep(0.0001)
        pyautogui.press("enter")
    print("your message has been sent ")

message=input("Please Enter your message ")
n=int(input("Please Enter number of times "))
message_sender(message)
# pip instal pyautogui