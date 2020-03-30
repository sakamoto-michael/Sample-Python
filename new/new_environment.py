import sys
import requests
import os
import math

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting

def customGreet(name):
    custom_greeting = "Hello, {}!".format(name)
    return custom_greeting

print(greet("World"))
name = input('What is your name? \n')
print(customGreet(name))

r = requests.get('https://google.com')
print(r.status_code)
