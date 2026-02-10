# match...case (python version >=3.10)

day = int(input("enter day:"))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wed")
    case 4:
        print("Thusday")
    case 5:
        print("Friday")
     case 1:
        print("Saturday")
    case _:
        # thi is default case
        print("bas sunday sudi j hoi")  