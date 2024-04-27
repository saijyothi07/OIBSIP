import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digits=['0','1','2','3','4','5','6','7','8','9']
symbols=['@','#','$','%','&']
password=""
n_letters=int(input("Enter how many letters:"))
n_digits=int(input("Enter how many digits:"))
n_symbols=int(input("Enter how many symbols:"))
for i in range (0,n_letters):
    x=random.choice(letters)
    password=password+x
for j in range (0,n_digits):
    y=random.choice(digits)
    password=password+y
for k in range(0,n_symbols):
    z=random.choice(symbols)
    password=password+z
print("Generated password is",password)