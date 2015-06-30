#!/usr/bin/python3
#
# Author Francis Kessie
#
"""The bartender will invent a new and delicious cocktail for 
you based upon your answers to some simple questions.
"""

import random
import sys

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

 
def questionaire(questions_dict):
    """ask few questions and return an answer dict"""
    questlist = [i for i in questions_dict.values()]     
    answerlist = []
    answerdict = {}
    #allow for review of selection before providing recipe
    while True:
        counter = len(questlist) #counter to track options
        for i in range(len(questlist)):
            print()
            selection = "Type [y or yes], else hit Enter for more options: "
            inp = input(questlist[i].upper()+ '\n' + selection)
            for keys in questions_dict:
                
                if questions_dict.get(keys) ==questlist[i]:
                    if inp.lower() in ['yes', 'y']:
                        answerdict[keys] = True                        
                    else:
                        answerdict[keys] = False                                                             
            counter -=1 
            if counter == 0:                       
               while True:
                options = [keys for keys in answerdict if answerdict.get(keys)]
                if len(options) > 1:
                    option = ", ".join(options[:-1]) + " and " + options[-1]
                else:
                     option = ", ".join(options)

                print()
                # let client confirm his selections or non selection
                if len(options) == 0:
                    print("Options Exhausted. No selections made.\n")                                 
                else:
                    print("Hope I got you right. You like something "+ option+"?")
                    print()                                
                inp2 = input("Type (Any key+Enter) to Review or (Enter to continue): ")
                                                      
                if inp2:
                    break
                else:
                    return answerdict
      
                     
           
def constructdrink(answdict):
    """takes questionare dict and return recipe sugetions"""
    drinklist = []   
    for val in [keys for keys in answdict if  answdict.get(keys)]:
        drinklist.append(random.choice(ingredients[val]))
    return drinklist

def main():     
   """run the questionaire and constructdrink 
   functions and return sugessions
   """
   #allow for more drinks if so desired 
   while True:  
     print()
     print("Hi. Answer few questions and I will fix you something.!!")       
     choices = constructdrink(questionaire(questions))
     if len(choices) == 0:
         print()
         print("Well. No selections, Bye for now!!")
     else:
         print("One drink coming up....")
         print("It's full of good stuff.  The recipe is:")
         for flavors in choices:
             print("A {0}".format(flavors))                         
         while True:
           inp3 = input("Hit (Any key+ENTER) for more options or (ENTER to quit): ")
           if not inp3:
               print()
               print("Bye for now. The Pirate Bartender. Always at your service !!.")
               sys.exit()
           else:
               break
                
if __name__=="__main__":
     main()
