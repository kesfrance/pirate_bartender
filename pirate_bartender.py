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
    answerdict = {}                     
    for keys, val in questions_dict.items():           
        inp = input(val.upper() + " Type [yes or y]: ")                
        if inp.lower() in ['yes', 'y']:                    
             answerdict[keys] = True                                   
    return answerdict                                                                         
                             
           
def constructdrink(answdict):
    """takes questionare dict and return recipe sugetions"""
    drinklist = []   
    for keys, val in answdict.items():
        if val==True:
            drinklist.append(random.choice(ingredients[keys]))
    return drinklist

def main():     
   """run the questionaire and constructdrink 
   functions and return recipe sugessions
   """
   while True:  
     print()
     print("Hi. Answer few questions and I will fix you something.!!")       
     print()
     choices = constructdrink(questionaire(questions))
     
     #prompt user if no selection was made
     if len(choices) == 0:
         print()
         print("No selection was made!!")
         continue
     
     #else print out a recipe
     else:
         print()
         print("One drink coming up....")
         print("It's full of good stuff.  The recipe is:")
         for flavors in choices:
             print("A {0}".format(flavors))                         
        
         #option for user to select more drinks or press enter to exit program
         while True:
           print()
           inp2 = input("Hit (Any key+ENTER) for more drinks or (ENTER to quit): ")
           if not inp2:
               print()
               print("Bye for now!!.")
               sys.exit()
           else:
               break
                
if __name__=="__main__":
     main()
     
