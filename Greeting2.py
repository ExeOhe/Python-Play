#Define the Function 'hello'
def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")
#Define Greeting to use later?
greeting = "Hello"
#Ask for Gender
title= input("What's your Gender? Mr/Mrs?")
#Ask for First Name
first= input("What's your First Name?")
#Ask for Last Name
last= input("What's your Last Name?")
#Call the Function 'hello'
hello(greeting, title, first, last)