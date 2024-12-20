try:
    a = int(input("Ingresa un numero:\n"))
    b = int(input("Ingresa otro numero: \n"))
    c = a/b
    print(c)
except ValueError:
    print("SOLO NUMEROS!!")
    
except ZeroDivisionError:
    print("No se puede dividir entre 0")

except Exception:
    print("QUE HICISTE!?!?!?!")