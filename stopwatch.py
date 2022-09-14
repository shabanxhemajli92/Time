from datetime import datetime

welcome_message="Hello Madam/sir,this your stopwatch"
print(welcome_message)

input_var=input("Type enter to view the date:")
today = datetime.now().time() # time object
if input_var=="enter":
    print("time is:", today)

    


 	