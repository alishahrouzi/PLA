import numpy as np 

i = 0

#Create_Matrix :

def cec(n,m):
  mat = np.zeros((n,m))
  return mat

def fill_cec(mat) :
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            mat[i,j] = (input(f"Data {i+1,j+1} :"))
    return mat

#Input:

n = int(input("number of sample: "))
m = int(input("number of data : "))
d = int(input("Enter Number of Itrable :"))
print("\nplease enter sample data: ")

#Fill_Matrixs:

mat = cec(n,m)
mat = fill_cec(mat)
b = np.full((n, 1),1)
mat = np.hstack([mat, b])
# print("Transpose matrix data : \n" , mat)
transpose_mat = np.transpose(mat)
print("matrix data: \n" , transpose_mat)

#Data_Train_Matrix:

mat_train = cec(n,1)
print("\nData Train is :")
def fill_cec_train(mat_train):
    for i in range(mat_train.shape[0]):
        mat_train[i,0] = (input(f"Data {i+1} :" ))
    return mat_train    
mat_train = fill_cec_train(mat_train)
transpose_mat_train = np.transpose(mat_train)
# print("Data Train : \n" , mat_train)
transpose_mat_train = np.array(transpose_mat_train.flatten().tolist())
print("\nTranspose Data Train : \n" , transpose_mat_train)

#Value_Matrix:

mat_value = cec(m,1)
print("\ninitial Value is : ")
def fill_cec_value(mat_value):
    for j in range(mat_value.shape[0]):
        mat_value[j,0] = (input(f"Data {j+1} :" ))
    return mat_value    
mat_value = fill_cec_value(mat_value)
b = np.full((1, 1),0)
mat_value = np.vstack((mat_value, b))
transpose_mat_value = np.transpose(mat_value)
transpose_mat_value = np.array(transpose_mat_value.flatten().tolist())
print("\nWeight Zero Stage =" , transpose_mat_value)

#Learnin_Rate:

Lr = float(input("\nplease enter Learning Rate = "))
print("\nyour Learning rate = " , Lr)

# process_Output :

def func_output (transpose_mat_value,transpose_mat) :
        mat_output = np.matmul(transpose_mat_value,transpose_mat)
        return mat_output
mat_output = func_output(transpose_mat_value,transpose_mat)
result = mat_output[:]

# Select Function : 1.sgn() 2.sig() 3.stp()

result = np.array(result.flatten().tolist())
p = int(input("\nChoice Your Function : \t1.sgn() \t2.sigmoid() \t3.stp()\n"))
def choice_func(p, result):
    if p == 1:
        def sgn(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            else:
                return 0
        return list(map(sgn, result))
    elif p == 2:
        def sigmoid(x):
            return 1 / (1 + np.exp(-x))
        return list(map(sigmoid, result))
    elif p == 3:
        def stp(x):
            if x < 0:
                return 0
            else:
                return 1
        return list(map(stp, result))
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
output = choice_func(p, result)
print("\n(first stage)Output F(x) = ",output) 

#Erorr:

def Erorr_func(output) :
    mat_E = []
    mat_E = np.subtract(transpose_mat_train,output)
    return mat_E
mat_E = Erorr_func(output)
print("\nErorr Zero Stage :", mat_E)

#Weight:

def weight_func(mat_value,Lr,mat,mat_E):
    weight = []
    weight = np.add(mat_value,np.multiply(Lr,(np.matmul(mat_E,mat))))
    return weight[1,:]
weight = weight_func(mat_value,Lr,mat,mat_E)
# print("\nWeight first Satge :",weight)

#Iterable:

def itrable_func(output,transpose_mat_train,result,weight,mat_value,mat_E) :
    for i in range(d) :
        if ((Erorr_func(output)) == 0).all() :
            mat_E = Erorr_func(output)
            print("\nfinal output = ",output)
            print("\nfinal Erorr = ",mat_E)
            break
        elif not(Erorr_func(output) == 0).all() :
            mat_E = Erorr_func(output)
            mat_value = weight 
            weight = np.add(mat_value,np.multiply(Lr,(np.matmul(mat_E,mat))))
            result = np.array(func_output(weight,transpose_mat).flatten().tolist())
            output = choice_func(p,result)
            print(f"\tStage{i+1}")
            print("\noutput = ",output)
            print("erorr = ",transpose_mat_train-output)
            print("weight = ",mat_value)
            print("---------------------------")
itrable_func(output,transpose_mat_train,result,weight,mat_value,mat_E)