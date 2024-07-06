import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*','(',')','?']
print("Welcome to the Password Generator!")
n_letters=int(input("How many letters would you like in your password?\n"))
n_symbols=int(input("How many symbols would you like?\n"))
n_numbers=int(input("How many numbers would you like?\n"))
password_list=[]
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password_list+=char
for i in range(1,n_symbols+1):
    symb=random.choice(numbers)
    password_list+=symb
for i in range(1,n_numbers+1):
    numb=random.choice(symbols)
    password_list+=numb
random.shuffle(password_list)
password=" "
for char in password_list:
    password+=char
print(password)
