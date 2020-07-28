import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase 
    s2 = string.ascii_uppercase 
    s3 = string.digits 
    s4 = string.punctuation
    
    i = 0
while i <=2:  # Here we can get to chance to get password if we are not satisfied with first one
    pass_len = int(input("Enter password length : \n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    random.shuffle(s)
    
    print("Your password is :")
    print("".join(s[0:pass_len]))
    print("Thank you !")
    i += 1
		
