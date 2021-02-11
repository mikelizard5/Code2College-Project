import random
def converse(user_input):
  while user_input != quit:
    if " where are you from " in user_input:
      print("I'm from Texas, but I was on a cruise recently and last night there was a shipwreck and now i washed up one shore and found this old ham radio. Wanna ask anything else?\n")
    elif "old " in user_input:
        print("I'm 23 funny enough my birthday was just a few days ago. Wanna ask anything else?\n")
    elif " work " in user_input:
          print("I was in programming and I made some good money, but i guess it don't mean much now I'm stuck herer in no where. Wanna ask me anything else?\n")
    elif " what happened " in user_input:
      print("I can't remember much I was partying last night on a crusie then out of no where the ship started sinking and next thing i know i washed up on this island being lucky enough to talk to anyone. Wanna ask me anyhting else?\n")
    elif " programming " in user_input:
      print(" oh well to be exact i was in cyber security and i got this super amazing job for a big tech company and I was really living the high life. Wanna ask me anyhting else?\n")
    print(respond())
    user_input = input(name + question())

def question():
  questions = [
    " what day is it?\n",
    " where are you from?\n",
    " how's your...day going?\n",
    " whats the weather like?\n",
    " did you have...a good...christmas?\n",
    " do you/did you have any new year resolutions?\n",
    " you have...any plans with school?\n",
    " do you work and if so what do you do?\n",
    " you wanna ask me anything?\n"
    ]
  random_question = random.choice(questions)
  return random_question
  questions.remove(random_question)

def respond():
  responds = [
    " Oh ok",
    " Ah cool",
    " oh thats interesting",
    "wow alright",
    "thats all good"
  ]
  return random.choice(responds)

def end_chat():
  quit = 'I gotta go' or 'i gotta go'
  print("Alright thanks for talking to me "+ name + '\n')

response=input("...Hello...Can anyone hear...Me\n")
if "yes" in response:
  print("oh thank...goodness\n")
elif "no" in response:
  print("please...no time...for jokes\n")
else:
  print("I'm sorry...my connection...isn't well\n")

name = input("Alright...first things first what is your name?\n")

talk = input("Alright " + name + " I'm sorry if this is to much to ask for but to escape from me going crazy would you mind just talking to me\n")

if "yes" or "sure" in talk:
  print('Thank you and if you wish to stop talking just say "I gotta go" and the conversation will end\n')
  converse(user_input = input(name + question()))
elif "no" or "nah" in talk:
  end_chat()
else:
  print("I'll just take that as a yes")
  converse(user_input = input(name + question()))
