A=[[4,5,6]]
B=[[1],
   [3],
   [5]]
def Matrix(A,B):
    rows_A=len(A)
    cols_b=len(A[0])
    rows_B=len(B)
    cols_B=len(B[0])
    if cols_A!=rows_B:
        return ["Cannot multiply the twi matrices. Incorrect dimensions."]
    C=[]
    for i in range(rows_A):
        
        
