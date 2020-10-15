'''
Adding N-bits (Array A, Array B)
'''
def addingNBits(a,b):
    carry = 0
    lst = [0]*(len(a)+ 1) #Initializing length w/ lst filled w/ 0's
    n = len(a)
    for i in range(n -1 , -1, -1):
        lst[i + 1] = (a[i] + b[i] + carry)%2 
        print(lst[i + 1])
        if (a[i] + b[i] + carry) >= 2:
            carry = 1
        else:
            carry = 0
    lst[0] = carry
    return lst


a = [0, 1, 0, 1]
b = [0, 0, 1, 1]
print(addingNBits(a, b))
