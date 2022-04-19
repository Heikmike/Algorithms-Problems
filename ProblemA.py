'''We first get the inputs'''
str_n, str_c, str_e = input().split()

n = int(str_n)
c = int(str_c)
e = int(str_e)

a = [0] * n
b = [0] * n
for i in range(n):
    str_a, str_b = input().split()

    a[i] = int(str_a)
    b[i] = int(str_b)

'''I define a max function just to be sure'''   
def myMax(a, b):
    return a if a >= b else b

def setZero(a):
    return 0 if a < 0 else a

'''We use a bottom up implementation for the recurrence 
given in the exercise'''
def Grocery(n, c, e):
    '''We innitialize our array'''
    d = [[[0 for i in range(e + 1)] for j in range(c + 1)] for k in range(n + 1)]

    '''We implement the base cases'''
    d[0][0][0] = 1

    for j in range(c + 1):
        for k in range(e + 1):
            if j != 0 or k != 0:
                d[0][j][k] = 0

    '''We implement the recurrence'''
    for i in range(1, n + 1):
        for j in range(c + 1):
            for k in range(e + 1):
                if j == 0 and k == 0:
                    d[i][j][k] = 1
                elif k == 0 or j == 0:
                    d[i][j][k] = 0
                elif j - a[i - 1] < 0 or k - b[i - 1] < 0:
                    d[i][j][k] = d[i - 1][j][k]
                else:
                    d[i][j][k] = myMax(d[i - 1][j][k], d[i - 1][setZero(j - a[i - 1])][setZero(k - b[i - 1])])
        
    return "Yes\n" if d[n][c][e] == 1 else "No\n"

def main():
    print(Grocery(n, c, e))

if __name__ == "__main__":
    main()