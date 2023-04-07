import re
import random
import json
import time
import os
from poem import generate_poem
from name import analyze_name



# Define the file name and path to save the inputs
file_path = "unknown_inputs.txt"

# If the file doesn't exist, create it
if not os.path.exists(file_path):
    open(file_path, 'w').close()

# Define a function to save inputs to the file
def save_to_file(input_text):
    with open(file_path, 'a') as f:
        f.write(input_text + "\n")

#JSON
with open("bot.json") as json_data:
    responses_data = json.load(json_data)
    

def getAnswer(user_input):
    words = re.split(r'\s+|[,;?!.-]\s*', user_input)
    highest_prob_list = {}

    # ANALYZE USER NAME
    report = analyze_name(user_input)
    if report: return report


   # GENERATE POEM
    if "poem" in words:
        poem = generate_poem()
        return poem

    def response(bot_response, list_of_words, single_response, required_words):
        nonlocal highest_prob_list
        message_certainty = 0
        has_required_words = True
       
        for word in words:
            if word in list_of_words:
                message_certainty +=1

        for r_word in required_words:
            if r_word not in user_input:
                has_required_words = False
                break

        percentage = float(message_certainty)/ float(len(list_of_words))
        #print(highest_prob_list)
        if has_required_words or single_response==1:
             highest_prob_list[bot_response] = int(percentage*100)
        else:
            highest_prob_list[bot_response] = 0
    


    


    for r in responses_data:
        response(r["bot_response"][random.randrange(3)], r["list_of_words"], r["single_response"], r["required_words"])

    best_response = max(highest_prob_list, key=highest_prob_list.get)

    if highest_prob_list[best_response] > 0 : return best_response
    else:
        wrost_response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][random.randrange(4)]
        
        save_to_file(user_input)
        return wrost_response

        





# TESTING
print("Welcome back! What would you like to chat about?")
print("-------------------------------------------")
while True:
    user_input = input("You --> ")
    # To Exit
    if user_input.lower() == "exit": break
        
    print("-------------------------------------------")
    Potrobot_output = getAnswer(user_input.lower())
    print("bot --> ",sep=' ', end='', flush=True)
    
    # OUTPUT WITH ANIMATION
    for i in range(0,len(Potrobot_output)):
        print(Potrobot_output[i],sep=' ', end='', flush=True)
        time.sleep(0.1)
        if(i==len(Potrobot_output)-1): print("");
    print("-------------------------------------------")

    