# elif

a = [1,2,3]
b = [10,22,35]
c = [111,222]

if (len(a) > len(b)) and (len(a) > len(c)):
    print("list a is max")

elif (len(b) > len(a)) and (len(b) > len(c)):
    print("list b is max")

elif (len(c) > len(a)) and (len(c) > len(b)):
    print("list c is max")
    
else:
    print("all list are equal")