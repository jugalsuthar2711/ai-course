#list- Functions: 
# list-operations:

def add_element(lst, element):
    lst.append(element)
    return lst

def add_multiple(lst, elements):
    lst.extend(elements)
    return lst

def remove_element(lst, element):
    if element in lst:
        lst.remove(element)
    return lst

def remove_by_index(lst, index):
    if 0 <= index < len(lst):
        lst.pop(index)
    return lst

def clear_list(lst):
    lst.clear()
    return lst

def list_length(lst):
    return len(lst)

def find_sum(lst):
    return sum(lst)

def find_max(lst):
    return max(lst)

def find_min(lst):
    return min(lst)

def sort_ascending(lst):
    return sorted(lst)

def sort_descending(lst):
    return sorted(lst, reverse=True)

def reverse_list(lst):
    return lst[::-1]

def count_element(lst, element):
    return lst.count(element)

def element_exists(lst, element):
    return element in lst

def get_unique_elements(lst):
    return list(set(lst))
