import listop

numbers = [10, 20, 30, 20, 40]

num=listop.add_element(numbers, 50)
print("After add:", num)

print("Sum:", listop.find_sum(numbers))
print("Max:",listop.find_max(numbers))
print("Min:",listop.find_min(numbers))
print("Length:", listop.list_length(numbers))

print("Sorted:",listop.sort_ascending(numbers))
print("Reverse:",listop.reverse_list(numbers))
print("Count of 20:",listop.count_element(numbers, 20))
print("Unique:",listop.get_unique_elements(numbers))
print("Exists 30:",listop.element_exists(numbers, 30))
