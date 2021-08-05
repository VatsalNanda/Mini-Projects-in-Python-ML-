import numpy as np
import sys


""" 
I/O Format 
2 2 (Dimension of Matrix 1) 
1 2  (First Matrix)
3 4 
2 2 (Dimension of Matrix 2)
1 2  (Second Matrix)
3 4 
"""

arguments = sys.argv

try : 
    sys.stdin = open(arguments[1], 'r')
    sys.stdout = open(arguments[2], 'w')
    type = arguments[3]

    n1,m1 = map(int,input().split())
    A = []

    for i in range(n1):
        temp = list(map(int,input().split()))
        A.append(temp.copy())

    n2,m2 = map(int,input().split())

    B = []
    for i in range(n2):
        temp = list(map(int,input().split()))
        B.append(temp.copy())
    
    A = np.array(A)
    B = np.array(B)
    
        if n1 != m2:
        print("Matrix Multiplication not possible") 
        exit() 

        print(np.matmul(A,B))
        
        

except:
        print("""Either you have used wrong format
        or some file is missing
        py <nameoffile>.py inputfile outputfile""")
