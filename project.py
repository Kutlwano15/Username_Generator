from xml.dom import UserDataHandler
import string
 
        
def user_details():

    n = set(string.punctuation)
    
    first_name = input("Insert First Name:")
    for i in first_name:
        if i.isdigit():
            print("invalid name" )
            first_name = input("Insert first Name:")
        if any(character in n for character in first_name):
            print("invalid name" )
            first_name = input("Insert first Name:")
        if len(first_name) == 2:
            first_name = first_name + "o"
        elif len(first_name) == 1:
            first_name = first_name + "oo"
        while first_name == "invalid name":
            first_name = input("Insert first Name:")
    
    last_name = input("Insert Last Name:")
    for i in last_name:
        if i.isdigit():
            print("invalid name")
            last_name = input("Insert Last Name:")
        if any(character in n for character in first_name):
            print("invalid name" )
            last_name = input("Insert Last Name:")
        if len(last_name) == 2:
            last_name = last_name + "o"
        elif len(last_name) == 1:
            last_name = first_name + "oo"

    try:
        cohort = int(input("Cohort Year:"))
    except ValueError:
        print("invalid cohort")
        cohort = int(input("Cohort Year:"))

    campus_ = input("Final Campus:")

    campus = user_campus(campus_)

    return(first_name, last_name, cohort,campus)


def create_user_name(first_name, last_name, cohort, campus):
    if cohort < 2022:
        return "Invalid cohort"
    
    final_username = first_name[-3:] + last_name[:3] + campus + str(cohort)
    print("Final username:",final_username)

    is_valid = input("Is username correct? y/n")
    if is_valid == "y":
        print("username valid")
    else:
        print("Invalid username")

def user_campus(campus):
    if campus == "Johannesburg":
        return "JHB"
    elif  campus == "Durban":
        return "DBN"
    elif campus == "Cape Town":
        return "CPT"
    elif campus == "Phokeng":
        return "PHO"
    else:
        return "Invalid campus name"
    
  

if __name__ == '__main__':
   first_name, last_name, cohort,campus = user_details()
   create_user_name(first_name, last_name, cohort, campus)
    
    