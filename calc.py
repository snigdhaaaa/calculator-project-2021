# Greet the user
print("Hello. I'm a fortune teller")
# Ask the user if their fortune told
answer = input("Do you want a fortune?")

while answer.lower() != "no":
    print("User asked for a fortune")
    answer = input("Do you want a fortune?")

# Fortune given 
# Ask if user wants another fortune
# Repeat until user quits