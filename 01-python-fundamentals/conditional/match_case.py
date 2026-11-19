from unittest import case

x=2
match x:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case _:
        print("invalid")  #   _ under score used for default case


