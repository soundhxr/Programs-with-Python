import pywhatkit
phone =""
while len(phone) != 10:
    phone = input("Enter receiver's phone no.: ")
msg = input("Enter message: ")
time = input("When do you want to send the message?\nEnter Time in 24 Hour format (eg: 21:35): ")
lst = time.split(":")
pywhatkit.sendwhatmsg("+91"+phone, msg, int(lst[0]), int(lst[1]))
