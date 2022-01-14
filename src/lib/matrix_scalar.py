a=3
b=[[3,6,9],[1,2,3],[2,4,8]]

def matrix_per_scalar(matrix,scalar):
  result=[]
  for i in range(len(matrix)):
    tmp=[]
    for j in range(len(matrix[i])):
      tmp.append(matrix[i][j]*scalar)
    result.append(tmp)
  return result

def print_matrix(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      print(str((matrix[i][j]))+"\t",end='')
    print("\n")

print("Input:")
print("Scalar="+str(a))
print("Matrix=")
print_matrix(b)

print("Matrix x scalar multiplication result:")
print_matrix(matrix_per_scalar(b,a))