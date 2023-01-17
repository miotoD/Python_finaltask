import random
color = ["red","blue","green","yellow","white","black","indigo","maroon"]
car = ["Mercedes","jaguar","ford","bugati","cheron","toyota","tata"]
animal = ["dog","cat","gorilla","snake","wolf","lion","tiger","girraffe"]
while True:
    try:
        num = int(input("How many password do you want? "))
        break
    except ValueError:
        print("Please enter numbers only .")


if num>24 or num<=0:
    print("Please enter number between 0 to 24.")
else:
    password = []
    for i in range (num):
        x = random.choice(color)
        y = random.choice(car)
        z = random.choice(animal)
        password = print("----->",x+y+z)