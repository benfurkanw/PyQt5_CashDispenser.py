import time
import json

class CashDispenser:
    def __init__(self):
        pass

    def Welcome(self):
        print("Welcome")
        time.sleep(1)

    def Login(self):
        print("Hello World!")

    def Register(self):
        # Prompt the user to enter their information
        self.name = input("Enter your name: ")
        self.password = input("Enter your password: ")
        self.email = input("Enter your email address: ")
        time.sleep(1)
        # Prompt the user to either go back or confirm their information
        self.Completed = input("Press '0' to go back or any other key to confirm your information: ")

        # Store the user's information in a dictionary
        registered_people_dict = {
            "name":self.name,
            "password":self.password,
            "email":self.email
        }

        # Open the file and read its contents as a string
        with open('registered_people.json', 'r+', encoding='utf-8') as f:
            data = f.read()
            # If the file is empty, create a new list
            if len(data) == 0:
                registered_people_list = []
            else:
                # Convert the JSON string to a Python list
                registered_people_list = json.loads(data)

        # Add the new record to the list
        registered_people_list.append(registered_people_dict)

        # Write the updated list back to the file in JSON format with indentation
        with open('registered_people.json', 'w', encoding='utf-8') as f:
            json.dump(registered_people_list, f, ensure_ascii=False, indent=4)

    def While(self):
        while True:
            # Prompt the user to select an action
            self.answer = input("Please choose an action:\nLogin -> 1\nRegister -> 2\nExit -> 3\nYour choice: ")
            if self.answer == "1":
                while True:
                    self.Login()
            
            elif self.answer == "2":
                while True:
                    self.Register()

                    # If the user presses "0", go back
                    if self.Completed == "0":
                        print("Your information was not saved.")
                        break
                    # Otherwise, confirm that the information was saved
                    else:
                        print("Your information was saved.")
            elif self.answer == "3":
                break
            
            else :
                print("Invalid input. Please try again.\n-----------------------------------------------")

def Work():
    Work = CashDispenser()
    Work.Welcome()
    Work.While()

Work()
