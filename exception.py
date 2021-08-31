a=5
b=0
k=int(input("enter the number"))
print(k)
try:
    print("file opened")
    print(a/b)
except ValueError as e:
    print("value error")
except Exception as e:
    print("hey! you cannot divide that number", e)

finally:
    print("file closed")
