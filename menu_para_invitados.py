

""" Estás preparando un gran banquete para tus mejores amistades en casa y quieres
 hacer un programa para preparar el menú y hacer la lista de la compra.
 El menú está formado por:
 """
# Ayuda Mi

"""Los set en Python son un tipo que permite almacenar varios elementos y acceder a ellos de una forma muy similar a las listas pero con ciertas diferencias:
Los elementos de un set son único, lo que significa que no puede haber elementos duplicados.
"""
""" La función update() del conjunto añade elementos sin duplicados. Si algún ingrediente ya está en lista_de_la_compra, no se añadirá de nuevo."""

# Diccionario

menu = {
    "Aperitivo: Guacamle": {
        "cilantro fresco", "cebolla", "chile fresco", "ajo", "tomate",
        "aguacates", "zumo de limon", "sal"
    },
    "Primer plato: Pimientos del piquillo rellenos": {
        "huevo duro", "palitos de cangrejo", "atún en aceite de oliva", "mayonesa", "pimientos del piquillo", "pimiento verde",
        "pimiento rojo", "cebolla", "vinagre de vino", "sal", "aceite de oliva"
    },
    "Postre: Brownie de chocolate con helado de turrón": { "chocolate amargo", "mantequilla sin sal", "azúcar", "huevos", "sal fina", "harina de trigo", "nueces"
}
}

# Funcion

def lista_de_la_compra(menu):
    lista_de_la_compra = set() # Lo pongo para que no se usen duplicados arriba explico 

    for ingredientes in menu.values():
        lista_de_la_compra.update(ingredientes) # arriba explico update

    return list(lista_de_la_compra)    


lista_compra = lista_de_la_compra(menu)
print("Lista de la compra:")
for ingrediente in lista_compra:
    print("-", ingrediente)

