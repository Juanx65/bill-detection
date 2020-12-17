user = open('usuarios_2.txt')
libros = open('libros_2.txt')

dicc = dict()
for linea in user:

    if " " not in linea:
        nombre = linea.strip()
    else:
        l_int = []
        lista = linea.strip().split(" ")
        for n in lista:
            l_int.append(int(n))


        dicc[nombre] = l_int
user.close()

def compatible(nombre1,dicc):
    pt1 = dicc[nombre1]
    coin_max = 0
    nombre2 = ''
    for nombre in dicc:
        coincidencia = 0
        if nombre != nombre1:
            for i in range(len(pt1)):
                coincidencia += pt1[i]*dicc[nombre][i]
        if coincidencia > coin_max:
            coin_max = coincidencia
            nombre2 = nombre
    return nombre2


lista_libros = []
for linea in libros:
    lista_libros.append(linea.strip())
libros.close()

def buscar_noleidos(nombre1,dicc):
    no_leidos = []
    nombre2 = compatible(nombre1,dicc)
    print(nombre2)
    for i in range(len(lista_libros)):
        if (dicc[nombre1][i] == 0) and (dicc[nombre2][i] == 5):
            no_leidos.append(lista_libros[i])


    return no_leidos
print(buscar_noleidos('Federico',dicc))

def resultado(dicc):
    arch = open('Resultados.txt','w')
    for nombre in dicc:
        arch.write('Información para usuario ' + nombre + '\n')
        afin = compatible(nombre,dicc)
        arch.write('        Usuario más afín: ' +afin+'\n' )
        arch.write('        Libros calificados con 5 por '+ afin + ' no leidos por '+ nombre+ '\n')
        lista = buscar_noleidos(nombre,dicc)
        for libro in lista:
            arch.write('               '+libro.replace(', ', ' por ')+ '\n')
        arch.write('--------------'+ '\n')
    arch.close()

print(resultado(dicc))

    
