def giai_ptb1(a,b):
    """
    Đây là phương trình bậc 1 ax + b = 0
    :param a: hệ số a
    :param b: he số b
    :return: nghiệm theo a và b
    """
    if a == 0 and b== 0:
        return "Vô số nghiệm"
    elif a == 0 and b != 0:
        return "Vô nghiệm"
    else:
        return -b/a

#kq1 = giai_ptb1(0,0)
#print("0x + 0 = 0 ==>",kq1)

def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def pick_fib(n):
    fi = fibonacci(n)
    list_fib = []
    for i in range(1,n+1):
        f_item = fibonacci(i)
        list_fib.append(f_item)
    return fi,list_fib

x,y = pick_fib(6)
print("f6 =", x)
print("list 1 to 6 =", y)