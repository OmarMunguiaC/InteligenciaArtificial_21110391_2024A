
def f1(): #Definir funcion 1
    global n1 #Variable global
    n1 = 974102863 #Valor
    f2() #Iniciar funcion 2

def f2(): #Definir funcion 2
    print('Funcion anidada dentro de otra función (por eso es anidada xd)')
    print(n1)

f1() #Ejecutar funcion 1, (tambien ejecuta la 2 por estar dentro de ella)
