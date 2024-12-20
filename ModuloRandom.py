import random

x = random.randint(1,6)
print(x)

JanKenPo = random.choice("piedra" , "papel" , "tijeras")
print(JanKenPo)

cartas = {"A" , 2,3,4,5,6,7,8,9,10 ,"J" , "Q" , "K"}
random.shuffle(cartas)
print(cartas)