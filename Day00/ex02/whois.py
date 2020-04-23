import sys

if len(sys.argv)!=2:
    print("ERROR")
else:
    """if type(sys.argv[1])==type(1):
        print("ok")
    else:
        print("ERROR")"""
    try:
        nb=int(sys.argv[1])
        print(nb)
        if nb==0:
            print("I'm Zero.")
        elif nb%2==0:
            print("I'm even")
        else:
            print("I'm odd")
    except:
        print("ERROR")

a=1
for i in range(30, 15, -1):
    a*=i
print(a)