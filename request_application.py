import requests
import unittest

BASE = "http://127.0.0.1:5000/"

def post():
    """
    Get the information about the POST method
    """
    print("Write the information about the developer")
    
    print("Name")
    name = input()
    
    print("Gender")
    gender = input()
    
    print("Age")
    age = int(input())
    print("Hobby")
   
    hobby = input()
    
    print("Date of Birth")
    date_of_birth = input()
    
    data = {"name" : name,
            "gender" : gender,
            "age" : age,
            "hobby" : hobby,
            "date_of_birth" : date_of_birth
    }
    
    response = requests.post(BASE + "developer", data=data)
    print(response.json())

def put():
    """
    Get the information about the PUT method
    """
    print("What is the developer ID?")
    id = input()
    
    print("Choose the field which will be updated")
    print("1 - Name\n2 - Gender\n3 - Age\n4 - Hobby\n5 - Date of Birth")
    field = int(input())
   
    print("What is the new value?")
    value = input()
    
    if field == 1:
        data = {"name" : value}
    elif field == 2:
        data = {"gender" : value}
    elif field == 3:
        data = {"age" : value}
    elif field == 4:
        data = {"hobby" : value}
    elif field == 5:
        data = {"date_of_birth" : value}
    else:
        print("Invalid input")
        data = None
    
    if data != None:
        response = requests.put(BASE + "developer/" + str(id))
        print(response.json())

def get():
    """
    Get the information about the GET method
    """
    print("Choose the GET type")
    print ("1 - All table\n2 - Query\n3 - ID")
    get_type = int(input())
   
    if get_type == 1:
        response = requests.get(BASE + "developer")
        print(response.json())
    elif get_type == 2:
        print("Write a valid querystring")
    elif get_type == 3: 
        print("What is the developer ID?")
        id = input()
        response = requests.get(BASE + "developer/" + str(id))
        print(response.json())
    else:
        print("Invalid input")
    

def main():
    """
    Main application request
    """
    while(True):
        
        print("Choose the request")
        print("1 - GET\n2 - POST\n3 - PUT\n4 - DELETE\n5 - Quit")
        method = int(input())

        if method == 1:
            get()
        elif method == 2:
            post()
        elif method == 3:
            put()
        elif method == 4:
            print("What is the developer ID?")
            id = input()
            response = requests.delete(BASE + "developer/" + str(id))
            print(response)
        elif method == 5:
            break
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()

