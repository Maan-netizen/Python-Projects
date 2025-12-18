import datetime
import time

name= input("Hello! Enter your name:")
presentHour= datetime.datetime.now().hour

if 5<= presentHour <=11:
    print("Good Morning", name)

elif 11<= presentHour <=17:
    print("Good Afrernoon", name)

elif 17<= presentHour:
    print("Good Evening", name)

else:
    print("Good Night", name)

print("Hello! Welcome to Rule Based Chatbot")
print("You can ask me basic questions. Type bye to exit from the bot.")
responses = {
    "hello" : "Hi . Welcome. How Can I help You?",
    "how are you" : "I am very fine. Thank You.",
    "who are you?" : "I am smart AI Chatbot.",
    "motivate me" : "Keep going. Every bug of your project makes you a better coder.",
    "happy"       : "Great to hear that"
}
def getresponseofbot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
    return("I am not able to tell yet.I will tell after sometime." )
while True:
    userInput = input("Please ask your questions.")
    reply= getresponseofbot(userInput)
    print("Bot response is:", reply)
    if "bye" in userInput.lower():
        break