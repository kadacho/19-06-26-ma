#gestor de películas

peliculas=[
    {"titulo": "Inception", "director": "Cristopher Nolan", "genero": "Ciencia Ficcion", "anio": 2010, "rate": 8.9},
    {"titulo": "Jurassic Park", "director": "Steven Spielberg", "genero": "Ciencia Ficcion", "anio": 1993, "rate": 9.6},
    {"titulo": "Se7en", "director": "David Fincher", "genero": "Thriller", "anio": 1997, "rate": 9.3}
]

def pausa():
    x=input()

def ingresarPeli():
    while True:
        titulo=(input("Ingrese el título: "))
        if len(titulo)<=2:
            print("El nombre debe tener más de 2 caracteres")
        else:
            break

    while True:
        director=(input("Ingrese el director: "))
        if " " not in director:
            print("El director debe tener apellido")
        else:
            break

    genero=(input("Ingrese el genero: "))

    while True:
        anio=int(input("Ingrese año de salida: "))
        if anio<1960 or anio>2026:
            print("Ingrese un año mayor a 1960 y menor a 2026")
        else:
            break

    val=float(input("Ingrese la valoración"))

    peliculas.append({"titulo": titulo, "director": director, "genero": genero, "anio": anio, "rate": val})

def quitarPeli():
    mostrarPeli()
    eliminar=int(input("Ingrese el número de la película que desea eliminar: "))
    peliculas.pop(eliminar-1)

def actualizarPeli():
    mostrarPeli()
    actualizar=int(input("Ingrese el número de la película que desea actualizar: "))
    while True:
        titulo=(input("Ingrese el título: "))
        if len(titulo)<=2:
            print("El nombre debe tener más de 2 caracteres")
        else:
            break

    while True:
        director=(input("Ingrese el director: "))
        if " " not in director:
            print("El director debe tener apellido")
        else:
            break

    genero=(input("Ingrese el genero: "))
    
    while True:
        anio=int(input("Ingrese año de salida: "))
        if anio<1960 or anio>2026:
            print("Ingrese un año mayor a 1960 y menor a 2026")
        else:
            break

    val=float(input("Ingrese la valoración: "))

    peliculas[actualizar-1]={"titulo": titulo, "director": director, "genero": genero, "anio": anio, "rate": val}

def mostrarPeli():
    cont=1
    for i in peliculas:
        print(f"{cont}.- Título: {i['titulo']} | Director: {i['director']} | Género: {i['genero']} | Año: {i['anio']} | Valoración: {i['rate']}")
        cont+=1

def mostrarTitu():
    cont=1
    for i in peliculas:
        print(f"{cont}.- {i['titulo']}")
        cont+=1
def anios():
    cont=1
    for i in peliculas:
        print(f"{cont}.- {i['anio']}")
        cont+=1

def mejorValoracion():
    print("hola")

def menu():
    try:
        while True:
            print("1.- Ingresar película")
            print("2.- Quitar película")
            print("3.- Actualizar película")
            print("4.- Mostrar películas")
            print("5.- Mostrar solo títulos")
            print("6.- Mostrar los años de las películas")
            print("7.- Mostrar película mejor calificada")
            print("8.- Salir")
            op=int(input("Ingrese una opción: "))
            match op:
                case 1:
                    ingresarPeli()
                case 2:
                    quitarPeli()
                case 3:
                    actualizarPeli()
                case 4:
                    mostrarPeli()
                    pausa()
                case 5:
                    mostrarTitu()
                    pausa()
                case 6:
                    anios()
                    pausa()
                case 7:
                    mejorValoracion()
                case 8:
                    print("Saliendo")
                    break
    except:
        print("Error")

menu()