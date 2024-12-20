nombre = "luis humberto"
ExtraerNombre = nombre[0:10:1] # Inicio desde 0 : final(cantidad de caracteres) : step (si se pone negativo escrivira alreves)
print(ExtraerNombre)
WebSite = "https://www.youtube.com"
sliceWeb = slice(12, -4) #Quitar el inicio , caracteres del final que no queremos
print(WebSite[sliceWeb])