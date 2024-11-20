

""" Estás preparando un gran banquete para tus mejores amistades en casa y quieres
 hacer un programa para preparar el menú y hacer la lista de la compra.
 El menú está formado por:
 """
# Ayuda Mi

"""Los set en Python son un tipo que permite almacenar varios elementos y acceder a ellos de una forma muy similar a las listas pero con ciertas diferencias:
Los elementos de un set son único, lo que significa que no puede haber elementos duplicados.
"""
""" La función update() del conjunto añade elementos sin duplicados. Si algún ingrediente ya está en lista_de_la_compra, no se añadirá de nuevo."""
""" El lenguaje de programación C permite usar las secuencias de escape \n (nueva línea) y \r (retorno de carro)."""


# Diccionario
menu = {
    "aperitivo": {
        "guacamole": {
        "cilantro fresco", "cebolla", "chile fresco", "ajo", "tomate",
        "aguacates", "zumo de limon", "sal"
        }
    },
    "primer plato": {
        "pimientos del piquillo rellenos": {
        "huevo duro", "palitos de cangrejo", "atún en aceite de oliva", "mayonesa", "pimientos del piquillo", "pimiento verde",
        "pimiento rojo", "cebolla", "vinagre de vino", "sal", "aceite de oliva"
        }
    },
    "postre": {
         "brownie de chocolate con helado de turrón": {
            "chocolate amargo", "mantequilla sin sal", "azúcar", "huevos", "sal fina", "harina de trigo", "nueces"
         }
    }
}

# Funcion

"""def lista_de_la_compra(menu):
    lista_de_la_compra = set() # Lo pongo para que no se usen duplicados arriba explico 

    for ingredientes in menu.values():
        lista_de_la_compra.update(ingredientes) # arriba explico update

    return list(lista_de_la_compra)    


lista_compra = lista_de_la_compra(menu)
print("Lista de la compra:")
for ingrediente in lista_compra:
    print("-", ingrediente)
"""

def ingredientes_por_plato(menu, tipo_plato, plato):
    ingredientes = menu[tipo_plato].get(plato)
    if ingredientes:
        print(f"\nIngredientes necesarios para {plato}:")
        for ingrediente in ingredientes:
            print("-", ingrediente)
    else :
        print(f"\nNo se encontró el plato '{plato}' en el menú.")

def interactuar_con_usuario(menu):
    # Imprimo mensaje de introduccion
    print ("""\nEstás preparando un gran banquete para tu gente en casa
            y quieres  preparar el menú y hacer la lista de la compra.
            El menú está formado por:\n""")
    
    print("Tipos de platos disponibles:")
    for tipo_plato in menu.keys():
        print("-", tipo_plato)
    tipo_plato_seleccionado = input("\n¿Qué tipo de plato quieres cocinar hoy (Aperitivo, Primer plato, Postre)? ")

    if tipo_plato_seleccionado in menu:
        print(f"\nPlatos disponibles en {tipo_plato_seleccionado}:")
        for plato in menu[tipo_plato_seleccionado].keys():
            print("-", plato)

        plato_seleccionado = input(f"\n¿Qué {tipo_plato_seleccionado} quieres cocinar hoy? ")
        ingredientes_por_plato(menu, tipo_plato_seleccionado, plato_seleccionado)
    else:
        print(f"\nEl tipo de plato '{tipo_plato_seleccionado}' no está en el menú.")                               



interactuar_con_usuario(menu)