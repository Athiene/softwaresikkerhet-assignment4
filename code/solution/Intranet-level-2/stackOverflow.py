import requests

def iterate():
    for i in range(50):
        dummy = 'A' * 1000
        dummyLogin(dummy)

# Login request
def dummyLogin(password):
    # Perform a POST request
    response = requests.post("http://10.13.13.254/login", json={'username': 'jonas.dahl', 'password': password})
    result = response.json()
    print(result)
    return result

iterate()