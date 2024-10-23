from . import bst_node as bn
from DataStructures.List import array_list as al

def new_map():
    return {'root': None, 'type': 'BST'}

    
def put(my_bst, key, value):
    if is_empty(my_bst):
        my_bst['root'] = bn.new_node(key, value)
    else:
        insert_node(my_bst['root'], key, value)
    return my_bst


def insert_node(root, key, value):
    
    if default_compare(key, root['key']) == -1:
        if root['left'] == None:
            root['left'] = bn.new_node(key, value)
            root['size'] += 1
        else:
            old_size = root['left']['size']
            insert = insert_node(root['left'], key, value)
            if insert['size'] > old_size:
                root['size'] += 1
    
    elif default_compare(key, root['key']) == 1:
        if root['right'] == None:
            root['right'] = bn.new_node(key, value)
            root['size'] += 1
        else:
            old_size = root['right']['size']
            insert = insert_node(root['right'], key, value)
            if insert['size'] > old_size:
                root['size'] += 1
    
    else:
        root['value'] = value
    
    return root 


def get(my_bst, key):
    return get_node(my_bst['root'], key)

def get_node(root, key):
    if root is None:
        return None
    comparison = default_compare(key, bn.get_key(root))
    
    if comparison == 0:
        return root['value']
    elif comparison == -1:
        return get_node(root['left'], key)
    else:
        return get_node(root['right'], key)


def remove(my_bst, key):
    my_bst['root'] = remove_node(my_bst['root'], key)
    return my_bst

def remove_node(root, key):
    if root == None:
        return root
    
    comparison = default_compare(key, bn.get_key(root))
    if comparison == 0:
        if root['left'] != None:
            return root['left']
        else:
            return root['right']
    
    elif comparison == -1:
        if root['left'] != None:
            old_size = root['left']['size']
            removal = removal_node_check(root, key, 'left')
            
            if old_size > removal['size']:
                root['size'] -= 1
        
        return root
        
    elif comparison == 1:
        if root['right'] != None:
            old_size = root['right']['size']
            removal = removal_node_check(root, key, 'right')
            
            if old_size > removal['size']:
                root['size'] -= 1
        
        return root
def min_node(root):
    while root['left'] is not None:
        root = root['left']
    return root

def delete_min(root):
    if root['left'] is None:
        return root['right']
    root['left'] = delete_min(root['left'])
    root['size'] = 1 + size_tree(root['left']) + size_tree(root['right'])
    return root
            
def removal_node_check(root, key, direction):
    comparison = default_compare(key, bn.get_key(root[direction]))
    
    if comparison == 0:
        if root[direction]['size'] == 1:
            root[direction] = None
        elif (root[direction]['left'] != None) ^ (root[direction]['right'] != None):
            root[direction] = remove_node(root[direction], key)
        else:
            current_root = root[direction]['right']
            if current_root['size'] == 1:
                current_root['left'] = root[direction]['left']
                current_root['size'] += 1
                root[direction] = current_root
            else:
                pass
                
        root['size'] -= 1
        return root
    else:
        return remove_node(root[direction], key)

def contains(my_bst, key):
    return get(my_bst, key) is not None


def size(my_bst):
    return size_tree(my_bst['root']) if not is_empty(my_bst) else 0

def size_tree(root):
    return root['size'] if root is not None else 0



def is_empty(my_bst):
    return my_bst['root'] is None


def key_set(my_bst):
    key_list = al.new_list()
    if not is_empty(my_bst):
        key_set_tree(my_bst['root'], key_list)
    return key_list

def key_set_tree(root, key_list):
    if root is not None:
        key_set_tree(root['left'], key_list)
        al.add_last(key_list, root['key'])
        key_set_tree(root['right'], key_list)


def value_set(my_bst):
    value_list = al.new_list()
    if not is_empty(my_bst):
        value_set_tree(my_bst['root'], value_list)
    return value_list

def value_set_tree(root, value_list):
    if root is not None:
        value_set_tree(root['left'], value_list)
        al.add_last(value_list, root['value'])
        value_set_tree(root['right'], value_list)



def left_key(my_bst):
    return left_key_node(my_bst['root']) if not is_empty(my_bst) else None

def left_key_node(root):
    while root['left'] is not None:
        root = root['left']
    return root['key']

def right_key(my_bst):
    return right_key_node(my_bst['root']) if not is_empty(my_bst) else None

def right_key_node(root):
    while root['right'] is not None:
        root = root['right']
    return root['key']



def delete_left(my_bst):
    if size(my_bst) <= 1: return my_bst
    
    delete_left_tree(my_bst['root'])
    return my_bst
    
def delete_left_tree(root):
    if root['left'] == None:
        root = None
        return root
    else:
        root['left'] = delete_left_tree(root['left'])
        root['size'] -= 1
        return root

def delete_right(my_bst):
    if size(my_bst) <= 1: return my_bst
    
    delete_right_tree(my_bst['root'])
    return my_bst

def delete_right_tree(root):
    if root['right'] == None:
        root = None
        return root
    else:
        root['right'] = delete_right_tree(root['right'])
        root['size'] -= 1
        return root

def floor(my_bst, key):
    return floor_key(my_bst['root'], key) if not is_empty(my_bst) else None

def floor_key(root, key):
    if root is None:
        return None
    comparison = default_compare(key, root['key'])
    if comparison == 0:
        return root['key']
    elif comparison == -1:
        return floor_key(root['left'], key)
    temp = floor_key(root['right'], key)
    return temp if temp is not None else root['key']

def ceiling(my_bst, key):
    return ceiling_key(my_bst['root'], key) if not is_empty(my_bst) else None

def ceiling_key(root, key):
    if root is None:
        return None
    comparison = default_compare(key, root['key'])
    if comparison == 0:
        return root['key']
    elif comparison == 1:
        return ceiling_key(root['right'], key)
    temp = ceiling_key(root['left'], key)
    return temp if temp is not None else root['key']



def select(my_bst, pos):
    if is_empty(my_bst): return None
    result = select_key(my_bst['root'], pos)
    if result != None:
        return result['key']
    return None

def select_key(root, pos):
    if root is None:
        return None
    left_size = size_tree(root['left'])
    if pos < left_size:
        return select_key(root['left'], pos)
    elif pos > left_size:
        return select_key(root['right'], pos - left_size - 1)
    else:
        return root

            

def rank(my_bst, key):
    return rank_keys(my_bst['root'], key)

def rank_keys(root, key):
    if root is None:
        return 0
    comparison = default_compare(key, root['key'])
    if comparison == -1:
        return rank_keys(root['left'], key)
    elif comparison == 1:
        return 1 + size_tree(root['left']) + rank_keys(root['right'], key)
    else:
        return size_tree(root['left'])


def height(my_bst):
    return height_tree(my_bst['root']) if not is_empty(my_bst) else -1

def height_tree(root):
    if root is None:
        return -1
    return 1 + max(height_tree(root['left']), height_tree(root['right']))


def keys(my_bst, key_lo, key_hi):
    key_list = al.new_list()
    if not is_empty(my_bst):
        keys_range(my_bst['root'], key_lo, key_hi, key_list)
    return key_list

def keys_range(root, key_lo, key_hi, list_key):
    if root == None: return None
    low_comparison = default_compare(key_lo, root['key'])
    hi_comparison = default_compare(key_hi, root['key'])
    
    if low_comparison == -1:
        keys_range(root['left'], key_lo, key_hi, list_key)
    
    if low_comparison == -1 and hi_comparison == 1 or low_comparison == 0 or hi_comparison == 0:
        al.add_last(list_key, root['key'])
    
    if hi_comparison == 1:
        keys_range(root['right'], key_lo, key_hi, list_key)
    
    return list_key

def values(my_bst, key_lo, key_hi):
    value_list = al.new_list()
    if is_empty(my_bst): return value_list
    
    return values_range(my_bst['root'], key_lo, key_hi, value_list)

def values_range(root, key_lo, key_hi, list_values):
    if root == None: return None
    low_comparison = default_compare(key_lo, root['key'])
    hi_comparison = default_compare(key_hi, root['key'])
    
    if low_comparison == -1:
        values_range(root['left'], key_lo, key_hi, list_values)
    
    if low_comparison == -1 and hi_comparison == 1 or low_comparison == 0 or hi_comparison == 0:
        al.add_last(list_values, root['value'])
    
    if hi_comparison == 1:
        values_range(root['right'], key_lo, key_hi, list_values)
    
    return list_values

def default_compare(key, element):
    if element == None:
        return None
    if key > element:
        return 1
    elif key == element:
        return 0
    else:
        return -1