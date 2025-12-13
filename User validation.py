# validate the user 
# Useranme : not more than 12 char, no spaces , no digits 

u = input("Enter your username: ")

if len(u) > 12:
    print("Cannot exceed more than 12 characters")
elif not  u.find(" ") == -1:
    print("Username cannot contain spaces")
elif not u.isalpha():
    print("Username cannot contain digits")

else:
    print(f"Welcome {u}")