from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
from DataStructures.List import array_list as lt
import random as rd

def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.next_prime(num_elements//load_factor)
    scale = rd.randint(1, prime-1)
    shift = rd.randint(0, prime-1)
    
    hashtable = {
        "prime": prime,
        "capacity": capacity,
        "scale": scale,
        "shift": shift,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0,
        "type": "PROBING",
    }
    
    hashtable["table"] = lt.new_list()
    
    for _ in range(capacity):
        lt.add_last(hashtable["table"], me.new_map_entry(None, None))
    
    return hashtable

def put(map, key, value):
    prob_pos = mf.hash_value(map, key)
    entry = me.new_map_entry(key, value)
    ocupado, pos = find_slot(map, key, prob_pos)
    lt.change_info(map["table"], pos, entry)
    if not ocupado:
        map["size"] += 1
        map["current_factor"] = map["size"] / map["capacity"]
    
    if map["current_factor"] >= map["limit_factor"]:
        rehash(map)
    return map

def contains(map, key):
    prob_pos = mf.hash_value(map, key)
    ocupado, _ = find_slot(map, key, prob_pos)
    return ocupado

def get(map, key):
    prob_pos = mf.hash_value(map, key)
    ocupado, pos = find_slot(map, key, prob_pos)
    return lt.get_element(map["table"], pos)["value"] 

def remove(map, key):
    prob_pos = mf.hash_value(map, key)
    ocupado, pos = find_slot(map, key, prob_pos)
    
    if ocupado:
        lt.change_info(map["table"], pos, me.new_map_entry("__EMPTY__", "__EMPTY__"))
        map["size"] -= 1
    return map

def size(map):
    return map["size"]

def is_empty(map):
    return map["size"] == 0

def key_set(map):
    keys = lt.new_list()
    for i in range(map["capacity"]):
        if not is_available(map["table"], i):
            entry = lt.get_element(map["table"], i)
            lt.add_last(keys, entry["key"])
    
    return keys

def value_set(map):
    values = lt.new_list()
    for i in range(map["capacity"]):
        if not is_available(map["table"], i):
            entry = lt.get_element(map["table"], i)
            lt.add_last(values, entry["value"])
    
    return values
    
def rehash(map):
    old_table = map["table"]
    map["capacity"] = mf.next_prime(map["capacity"]*2)
    map["size"] = 0
    map["current_factor"] = 0
    map["table"] = lt.new_list()
    for _ in range(map["capacity"]):
        lt.add_last(map["table"], me.new_map_entry(None, None))
    
    for pos in range(lt.size(old_table)):
        if not is_available(old_table, pos):
            entry = lt.get_element(old_table, pos)
            put(map, entry["key"], entry["value"])
    
    return map
    

def find_slot(map, key, hash_value):
    table = map["table"]
    if is_available(table, hash_value):
        if lt.get_element(table, hash_value)["value"] is None:
            return False, hash_value
    else:
        entry = lt.get_element(table, hash_value)
        if default_compare(key, entry) == 0:
            return True, hash_value
    
    
    pos = (hash_value + 1) % map["capacity"]
    pos_resp = -1
    centinela = True
    while pos!=hash_value and centinela:
        entry = lt.get_element(table, pos)
        if is_available(table, pos):
            if pos_resp == -1:
                pos_resp = pos
            if entry["key"] is None:
                centinela = False
        else:
            if default_compare(key, entry) == 0:
                return True, pos
        pos = ((pos+1) % map["capacity"])
    
    return False, pos_resp
    

def is_available(table, pos):
    entry = lt.get_element(table, pos)
    return (entry["key"] is None or entry["key"] == "__EMPTY__")

def default_compare(key, element):
    if(key == element['key']):
        return 0
    elif(key > element['key']):
        return 1
    return -1