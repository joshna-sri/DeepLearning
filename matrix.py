'''
A=[[1,2,3],
   [4,5,6],
   [7,8,9]]

B= [[0,3,4],
    [6,7,3],
    [1,9,8]]

result =[[0,0,0],
         [0,0,0],
         [0,0,0]]

print("length A",len(A))
print("length B",len(B))
print("range A",len(A[0]))
print("range B",len(B[0]))  '''
def matrix_multiplication(A, B ,result):
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k]*B[k][j]
        print("\n")
    return result
'''
resulted = matrix_multiplication(A,B,result)

for i in range(len(A)):
   print(resulted[i])


#print("multiplied matrix:",result)



X = [[1,2,3]]

Y = [[0],
    [6],
    [1]]

Z =[[0,0,0],
         [0,0,0],
         [0,0,0]]

resulted = matrix_multiplication(X,Y,Z)
print("multiplied matrix (1X3)*(3X1):",resulted)



A=[[1,2,3 ,2],
   [4,5,6,9],
   [7,8,9,6]]

B= [[0,3,4],
    [6,7,3],
    [1,9,8],
    [2,6,3]]

resulted = matrix_multiplication(A,B,Z)
print("multiplied matrix (3X4)*(4X3):",resulted)

X_1 = [[1,2,3,4]]

Y_1 = [[0,5],
       [6,9],
       [1,3],
       [9,2]]

Z_1 = [[0,0,0],
       [0,0,0],
       [0,0,0]]

resulted = matrix_multiplication(X_1,Y_1,Z_1)
print("multiplied matrix (1X4)*(4X2):",resulted)

'''
X_2 = [[1,2,3,4]]

Y_2 = [[0,5],
       [6,9],
       [1,3]]

Z_2 = [[0,0,0],
       [0,0,0],
       [0,0,0]]

resulted = matrix_multiplication(X_2,Y_2,Z_2)
print("multiplied matrix (1X4)*(3X2):",resulted)