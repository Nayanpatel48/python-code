#matrix multiplicatin of 3*3
mat1 = [[1,2,3],[2,3,4],[6,7,8]]
mat2 = [[2,3,4],[5,6,7],[5,6,7]]


def matrixMultiplication(mat1, mat2):
    ansMat=[[0,0,0],[0,0,0],[0,0,0]]
    sum =0

    i=0
    j=0

    k=0
    l=0

    while i<3:
        while j<3:
            sum = 0
            while k<3:
                while l<3:
                    sum += mat1[k][l]*mat2[l][k]
                    l+=1
                k+=1
            ansMat[i][j]= sum
            j+=1
        i+=1
    print(ansMat)

matrixMultiplication(mat1,mat2)