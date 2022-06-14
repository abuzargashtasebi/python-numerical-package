

'''
Multiplication of two square matrices
'''
def matmul(a,b,n,m):
    c = [[0 for x in range(n)] for y in range(m)]
    for i in range(n):
        for j in range(m):
            s = 0.0
            for k in range(n):
                s += a[i][k]*b[k][j]
            c[i][j] = s
    return c


def matinv(n,m,a,b):
    pc = [0] * n
    pl = [0] * n
    cs = [0] * n
    det = 1.0
    eps = 2.0e-16

    #Find greatest pivot  
    for k in range(n):
        pv = a[k][k]
        ik = k
        jk = k
        pav = abs(pv)
        for i in range(k,n):
            for j in range(k,n):
                if(abs(a[i][j]) > pav):
                    pv = a[i][j]
                    pav = pav
                    ik = i
                    jk = j

        #Find terminated, the pivot is in location I=IK, J=JK.
        #Store pivot location
        pc[k] = jk
        pl[k] = ik

        if(ik != k):
            det = -det

        if(jk != k):
            det = -det

        det = det * pv
        if(abs(det) < eps):
            print('Determinant equals zero, no solution')
            return

        #placing pivot in k,k
        if(ik != k):
            for i in range(n):
                t = a[ik][i]
                a[ik][i] = a[k][i]
                a[k][i] = t

        if(m != 0):
            for i in range(m):
                t = b[ik][i]
                b[ik][i] = b[k][i]
                b[k][i] = t

        # Pivot is at correct line
        if (jk != k):
            for i in range(n):
                #exchange columns jk and k of matrix a
                t = a[i][jk]
                a[i][jk] = a[i][k]
                a[i][k] = t
        
        #Store column k in vector cs and set column k to 0
        for i in range(n):
            cs[i] = a[i][k]
            a[i][k] = 0.0

        cs[k] = 0.0
        a[k][k] = 1.0

        if(abs(pv) < eps):
            print('Pivot is too small - terminate')
            return

        for i in range(n):
            a[k][i] = a[k][i] / pv

        if(m != 0):
            for i in range(m):
                b[k][i] = b[k][i] / pv

        for j in range(n):
            if(j == k):
                pass
            for i in range(n):
                a[j][i] = a[j][i] - cs[j] * a[k][i]
            if(m != 0):
                for i in range(m):
                    b[j][i] = b[j][i] - cs[j] * b[k][i]

        for i in range(n-1,0,-1):
            ik = pc[i]
            if(ik == i):
                pass
            for j in range(n):
                t = a[i][j]
                a[i][j] = a[ik][j]
                a[ik][j] = t
            if(m != 0):
                for j in range(m):
                    t = b[i][j]
                    b[i][j] = b[ik][j]
                    b[ik][j] = t

        for j in range(n-1,0,-1):
            jk = pl[j]
            if(jk == j):
                pass
            for i in range(n):
                t = a[i][j]
                a[i][j] = a[i][jk]
                a[i][jk] = t
    
    return a, det


n = 5
a = [[0.200000E+01, -0.100000E+01,  0.100000E+01,  0.700000E+01, -0.125400E+02],
[0.100000E+01,  0.500000E+01, -0.200000E+01, -0.800000E+01,  0.100000E+03],
[0.300000E+01, -0.200000E+01,  0.300000E+01,  0.450000E+02,  0.273333E+02],
[0.110000E+02,  0.550000E+00, -0.200000E+01, -0.400000E+01,  0.100000E+01],
[0.330000E+02,  0.200000E+01,  0.000000E+00,  0.300000E+01,  0.500000E+01]]

m = 2
b = [[ 0.500000E+01, -0.100000E+01],
[ 0.100000E+01,  0.200000E+01],
[ 0.300000E+01,  0.755600E+01],
[ 0.400000E+01,  0.100000E+03],
[-0.100000E+02,  0.154000E-02]]

a, det = matinv(n, m, a, b)
print(det)

