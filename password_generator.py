import random
import string

def gen():
    s1 = string.ascii_uppercase

    s2 = string.ascii_lowercase

    s3 = string.digits

    s4 = string.punctuation

    passion=int(input("Enter the password length\n"))

    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    print(s) #Total number of characters available for the password

    random.shuffle(s)
    pas=("".join(s[0:passion]))
    print(pas)

gen()
