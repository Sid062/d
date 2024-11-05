def smm(a,b):
    if len(a)!=2 or len(b)!=2 or len(a[0])!=2 or len(b[0])!=2 :
        raise ValueError("2x2")

    a11,a12,a21,a22=a[0][0],a[0][1],a[1][0],a[1][1]
    b11,b12,b21,b22=b[0][0],b[0][1],b[1][0],b[1][1]

    m1=(a11+a22)*(b11+b22)
    m2=(a21+a22)*b11
    m3=a11*(b12-b22)
    m4=a22*(b21-b11)
    m5=(a11+a12)*b22
    m6=(a21-a11)*(b11+b12)
    m7=(a12-a22)*(b21+b22)

    c11=m1+m4-m5+m7
    c12=m3+m5
    c21=m2+m4
    c22=m1-m2+m3+m6

    result=[[c11,c12],[c21,c22]]
    return result

matrix1=[[1,2],[3,4]]
matrix2=[[5,6],[7,8]]

result=smm(matrix1,matrix2)
print("the matrix is :")
for row in result:
    print(row)