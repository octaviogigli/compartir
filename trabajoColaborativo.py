# el resto del equipo git clone url-repo-github
#el sistema de ramas (branching) --> permite el trabajo colaborativo
# para crear una rama es: git branch nombre
# git checkout nombre-de-la-rama para cambiar de rama
# gir marge, mescla las ramas puntaje = 0
num = int(input("ingrese numero: "))
puntaje = 0
for i in range(1,11):
  respuesta = int(input(f"{i}x{num}= "))
  if respuesta == i*num:
    print("correcto")
    puntaje += 1
  else:
    print("incorrecto")
print(f"tu puntaje fue {puntaje}/10")
if puntaje == 10:
    print("hiciste la mayor marca")
else:
   print('a')