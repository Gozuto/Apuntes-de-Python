try:
    with open("BloomDiva.txt") as file:
        file.write("Indestructible")
        print(file.read())
except FileNotFoundError:
    print('El archivo no fue encontrado')

