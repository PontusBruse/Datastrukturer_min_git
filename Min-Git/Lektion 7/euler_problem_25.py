import sys
# 0, 1, 1, 2, 3, 5, 8
# Vilket inder har första talet med 1000 siffror

def fib(a=0, b=1, index=1):
    if len(str(b)) == 1000:
        return index

    return fib(b, a+b, index+1)


if __name__ == '__main__':
    sys.setrecursionlimit(5000)
    answer = fib()
    print(answer)