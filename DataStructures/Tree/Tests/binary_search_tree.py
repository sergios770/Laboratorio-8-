from . import bst_node as nodo

def new_map():  
  bst = {'root': None,
         'type': 'BST'}
  
  return bst

def put(my_bst, key, value):
  my_bst['root'] = insert_node(my_bst['root'], key, value)
  
  return my_bst

def get(my_bst, key):
    valor = get_node(my_bst["root"], key)
    return valor