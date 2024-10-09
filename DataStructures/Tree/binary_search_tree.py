from DataStructures.Tree import bst_node as bst_node
from DataStructures.List import array_list as al


def new_map(cmp_function):
    """Crea una tabla de simbolos ordenada basada en un árbol binario de búsqueda (BST) vacía

    Se crea una tabla de símbolos ordenada con los siguientes atributos:

    - **root**: Raíz del árbol. Inicializado en ``None``
    - **type**: Tipo de árbol. Inicializado en "BST"
    - **cmp_function**: Función de comparación. Inicializado en ``None``

    :returns: La tabla de símbolos ordenada sin elementos
    :rtype: binary_search_tree

    """
    bst = {"root": None, "type": "BST", "cmp_function": None}

    if cmp_function is None:
        bst["cmp_function"] = default_compare
    else:
        bst["cmp_function"] = cmp_function

    return bst


def put(my_bst, key, value):
    """Ingresa una pareja llave,valor. Si la llave ya existe, se reemplaza el valor.

    :param my_bst: El BST
    :type my_bst: binary_search_tree
    :param key: La llave asociada a la pareja
    :type key: any
    :param value: El valor asociado a la pareja
    :type value: any

    :returns: El arbol con la nueva pareja
    :rtype: binary_search_tree
    """
    my_bst["root"] = insert_node(my_bst["root"], key, value, my_bst["cmp_function"])
    return my_bst


def get(my_bst, key):
    """
    Retorna la pareja lleve-valor con llave igual  a key
    Args:
        my_bst: El arbol de búsqueda
        key: La llave asociada a la pareja
    Returns:
        La pareja llave-valor en caso de que haya sido encontrada
    Raises:
        Exception
    """
    return get_node(my_bst["root"], key, my_bst["cmp_function"])


def remove(my_bst, key):
    """
    Elimina la pareja llave,valor, donde llave == key.
    Args:
        my_bst: El arbol de búsqueda
        key: La llave asociada a la pareja
    Returns:
        El arbol sin la pareja key-value
    Raises:
        Exception
    """
    my_bst["root"] = remove_node(my_bst["root"], key, my_bst["cmp_function"])
    return my_bst


def contains(my_bst, key):
    """
    Informa si la llave key se encuentra en la tabla de hash
    Args:
        my_bst: El arbol de búsqueda
        key: La llave a buscar
    Returns:
        True si la llave está presente False en caso contrario
    Raises:
        Exception
    """
    return get(my_bst, key) is not None


def size(my_bst):
    """
    Retorna el número de entradas en la tabla de simbolos
    Args:
        my_bst: El arbol de búsqueda
    Returns:
        El número de elementos en la tabla
    Raises:
        Exception
    """
    return size_tree(my_bst["root"])


def is_empty(my_bst):
    """
    Informa si la tabla de simbolos se encuentra vacia
    Args:
        my_bst: El arbol de búsqueda
    Returns:
        True si la tabla es vacía, False en caso contrario
    Raises:
        Exception
    """
    return my_bst["root"] is None


def key_set(my_bst):
    """
    Retorna una lista con todas las llaves de la tabla
    Args:
        my_bst: La tabla de simbolos
    Returns:
        Una lista con todas las llaves de la tabla
    Raises:
        Exception
    """
    key_list = al.new_list()
    key_list = key_set_tree(my_bst["root"], key_list)
    return key_list


def value_set(my_bst):
    """
    Construye una lista con los valores de la tabla
    Args:
        my_bst: La tabla con los elementos
    Returns:
        Una lista con todos los valores
    Raises:
        Exception
    """
    value_list = al.new_list()
    value_list = value_set_tree(my_bst["root"], value_list)
    return value_list


def min_key(my_bst):
    """
    Retorna la menor llave de la tabla de simbolos
    Args:
        my_bst: La tabla de simbolos
    Returns:
        La menor llave de la tabla
    Raises:
        Exception
    """
    node = min_key_node(my_bst["root"])
    if node is not None:
        return node["key"]
    return node


def max_key(my_bst):
    """
    Retorna la mayor llave de la tabla de simbolos
    Args:
        my_bst: La tabla de simbolos
    Returns:
        La mayor llave de la tabla
    Raises:
        Exception
    """
    node = max_key_node(my_bst["root"])
    if node is not None:
        return node["key"]
    return node


def delete_min(my_bst):
    """
    Encuentra y remueve la menor llave de la tabla de simbolos
    y su valor asociado
    Args:
        my_bst: La tabla de simbolos
    Returns:
        La tabla de simbolos sin la menor llave
    Raises:
        Exception
    """
    return delete_min_tree(my_bst["root"])


def delete_max(my_bst):
    """
    Encuentra y remueve la mayor llave de la tabla de simbolos
    y su valor asociado
    Args:
        my_bst: La tabla de simbolos
    Returns:
        La tabla de simbolos sin la mayor llave
    Raises:
        Exception
    """
    return delete_max_tree(my_bst["root"])


def floor(my_bst, key):
    """
    Retorna la llave mas grande en la tabla de simbolos,
    menor o igual a la llave key
    Args:
        my_bst: La tabla de simbolos
        key: La llave de búsqueda
    Returns:
        La llave más grande menor o igual a key
    Raises:
        Exception
    """
    node = floor_key(my_bst["root"], key, my_bst["cmp_function"])
    if node is not None:
        return bst_node.get_key(node)
    return node


def ceiling(my_bst, key):
    """
    Retorna la llave mas pequeña en la tabla de simbolos,
    mayor o igual a la llave key
    Args:
        my_bst: La tabla de simbolos
        key: la llave de búsqueda
    Returns:
        La llave más pequeña mayor o igual a Key
    Raises:
        Exception
    """
    node = ceiling_key(my_bst["root"], key, my_bst["cmp_function"])
    if node is not None:
        return bst_node.get_key(node)
    return node


def select(my_bst, pos):
    """
    Retorna la siguiente llave a la k-esima llave mas pequeña de la tabla
    Args:
        my_bst: La tabla de simbolos
        pos: la pos-esima llave mas pequeña
    Returns:
        La llave más pequeña mayor o igual a Key
    Raises:
        Exception
    """
    node = select_key(my_bst["root"], pos)
    if node is not None:
        return bst_node.get_key(node)
    return node


def rank(my_bst, key):
    """
    Retorna el número de llaves en la tabla estrictamente menores que key
    Args:
        my_bst: La tabla de simbolos
        key: La llave de búsqueda
    Returns:
        El nuemero de llaves encontradas
    Raises:
        Exception
    """
    return rank_keys(my_bst["root"], key, my_bst["cmp_function"])


def height(my_bst):
    """
    Retorna la altura del arbol de busqueda
    Args:
        my_bst: La tabla de simbolos
    Returns:
        La altura del arbol
    Raises:
        Exception
    """
    return height_tree(my_bst["root"])


def keys(my_bst, key_lo, key_hi):
    """
    Retorna todas las llaves del arbol que se encuentren entre
    [key_lo, key_hi]

    Args:
        my_bst: La tabla de simbolos
        key_lo: limite inferior
        key_hi: limite superiorr
    Returns:
        Las llaves en el rago especificado
    Raises:
        Exception
    """
    list_key = al.new_list()
    list_key = keys_range(
        my_bst["root"], key_lo, key_hi, list_key, my_bst["cmp_function"]
    )
    return list_key


def values(my_bst, key_lo, key_hi):
    """
    Retorna todas los valores del arbol que se encuentren entre
    [key_lo, key_hi]

    Args:
        my_bst: La tabla de simbolos
        key_lo: limite inferior
        key_hi: limite superiorr
    Returns:
        Las llaves en el rago especificado
    Raises:
        Exception
    """
    list_values = al.new_list()
    list_values = values_range(
        my_bst["root"], key_lo, key_hi, list_values, my_bst["cmp_function"]
    )
    return list_values


# _____________________________________________________________________
#            Funciones Helper
# _____________________________________________________________________

def insert_node(root, key, value, cmp_function):
    
    if root is None:
        root = bst_node.new_node(key, value)
    else:
        cmp = cmp_function(key, root)
        if cmp == 0:
            root["value"] = value
        elif cmp < 0:
            root["left"] = insert_node(root["left"], key, value, cmp_function)
        else:
            root["right"] = insert_node(root["right"], key, value, cmp_function)
    
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root

def get_node(root, key, cmp_function):    
    if root is not None:
        cmp = cmp_function(key, root)
        if cmp == 0:
            return root["value"]
        elif cmp < 0:
            return get_node(root["left"], key, cmp_function)
        return get_node(root["right"], key, cmp_function)
    return None



def remove_node(root, key, cmp_function):
    if root is not None:
        cmp = cmp_function(key, root)
        if cmp < 0:
            root["left"] = remove_node(root["left"], key, cmp_function)
        elif cmp > 0:
            root["right"] = remove_node(root["right"], key, cmp_function)
        else:
            if root["right"] is None:
                return root["left"]
            elif root["left"] is None:
                return root["right"]
            elem = root
            root = min_key_node(root["right"])
            root["right"] = delete_min_tree(elem["right"])
            root["left"] = elem["left"]
        root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
        return root
     
    return None


def size_tree(root):
    if root is None:
        return 0
    else:
        return root["size"]


def value_set_tree(root, value_list):
    if root is not None:
        value_set_tree(root["left"], value_list)
        al.add_last(value_list, root["value"])
        value_set_tree(root["right"], value_list)
    return value_list


def key_set_tree(root, key_list):
    if root is not None:
        key_set_tree(root["left"], key_list)
        al.add_last(key_list, root["key"])
        key_set_tree(root["right"], key_list)
    return key_list


def min_key_node(root):
    if root is not None:
        if root["left"] is None:
            return root
        return min_key_node(root["left"])
    return None


def max_key_node(root):
    if root is not None:
        if root["right"] is None:
            return root
        return max_key_node(root["right"])
    return None


def delete_min_tree(root):
    if root is not None:
        if root["left"] is None:
            return root["right"]
        else:
            root["left"] = delete_min_tree(root["left"])
        root["size"] = 1+size_tree(root["left"])+size_tree(root["right"])
        return root
    return None

def delete_max_tree(root):
    if root is not None:
        if root["right"] is None:
            return root["left"]
        else:
            root["right"] = delete_max_tree(root["right"])
        root["size"] = 1+size_tree(root["left"])+size_tree(root["right"])
        return root
    return None


def floor_key(root, key, cmp_function):
    if root is not None:
        cmp = cmp_function(key, root)
        if cmp == 0:
            return root
        elif cmp < 0:
            return floor_key(root["left"], key, cmp_function)
        k = floor_key(root["right"], key, cmp_function)
        return k if k else root
    return None


def ceiling_key(root, key, cmp_function):
    if root is not None:
        cmp = cmp_function(key, root)
        if cmp == 0:
            return root
        elif cmp > 0:
            return ceiling_key(root["right"], key, cmp_function)
        k = ceiling_key(root["left"], key, cmp_function)
        return k if k else root
    return None


def select_key(root, key):
    if root is not None:
        pos = size_tree(root["left"])
        if pos == key:
            return root
        elif pos > key:
            return select_key(root["left"], key)
        else:
            return select_key(root["right"], key - pos - 1)
    return None


def rank_keys(root, key, cmp_function):
    if root is not None:
        cmp = cmp_function(key, root)
        pos = size_tree(root["left"])
        if cmp == 0:
            return pos
        elif cmp < 0:
            return rank_keys(root["left"], key, cmp_function)
        return rank_keys(root["right"], key, cmp_function) + pos + 1
    return 0

def height_tree(root):
    if (root is not None) and (root["left"] or root["right"]):
        return 1 + max(height_tree(root["right"]), height_tree(root["left"]))
    return 0


def keys_range(root, key_lo, key_hi, list_key, cmp_function):
    if root is not None:
        cmp_lo = cmp_function(key_lo, root)
        cmp_hi = cmp_function(key_hi, root)
        if cmp_lo < 0:
            keys_range(root["left"], key_lo, key_hi, list_key, cmp_function)
        if cmp_lo <= 0 and cmp_hi >= 0:
            al.add_last(list_key, root["key"])
        if cmp_hi > 0:
            keys_range(root["right"], key_lo, key_hi, list_key, cmp_function)
    return list_key


def values_range(root, key_lo, key_hi, list_values, cmp_function):
    if root is not None:
        cmp_lo = cmp_function(key_lo, root)
        cmp_hi = cmp_function(key_hi, root)
        if cmp_lo < 0:
            values_range(root["left"], key_lo, key_hi, list_values, cmp_function)
        if cmp_lo <= 0 and cmp_hi >= 0:
            al.add_last(list_values, root["key"])
        if cmp_hi > 0:
            values_range(root["right"], key_lo, key_hi, list_values, cmp_function)
    return list_values


def default_compare(key, element):
    """
    Función de comparación por defecto. Compara una llave con la llave de un elemento llave-valor.

    :param key: Llave a comparar
    :type key: any
    :param element: ``entry`` a comparar
    :type element: map_entry

    :return: **0** si son iguales, **1** si ``key`` > la llave del ``element``, **-1** si ``key`` < que la llave del  ``element``
    :rtype: int
    """
    if key == bst_node.get_key(element):
        return 0
    elif key > bst_node.get_key(element):
        return 1
    return -1
