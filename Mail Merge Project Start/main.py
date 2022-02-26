#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


customer_name = open("./Input/Names/invited_names.txt", "r")
starting_letter = open("./Input/Letters/starting_letter.txt", "r")

names = customer_name.readlines()
letter_info = starting_letter.read()

for name in names:
    new_name = name.strip()
    change_letter = letter_info.replace("[name]", new_name)
    new_letter = open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", 'w')
    new_letter.write(change_letter)







