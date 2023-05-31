import numpy as np

s = 30;

emt=np.zeros([s,s],dtype=int)
# -------------------------------------------------

glider=np.zeros([s,s],dtype=int)
glider[0][0]=1
glider[0][2]=1
glider[1][1]=1
glider[1][2]=1
glider[2][1]=1

# --------------------------------------------------

xmen=np.zeros([s,s],dtype=int)

for i in range(s):
        xmen[i][i]=1
        xmen[i][s-i-1]=1

# -----------------------------------------------------

checkers=np.zeros([s,s],dtype=int)

for i in range(s):
    for j in range(s):
        if i%2==0 and j%2==0:
            checkers[i][j]=1
        elif i%2!=0 and j%2!=0:
            checkers[i][j]=1
        
# -------------------------------------------------------

swastik=np.zeros([s,s],dtype=int)

swastik[8][11]=1
swastik[8][13]=1
swastik[8][14]=1
swastik[8][15]=1
swastik[8][15]=1
swastik[9][11]=1
swastik[9][13]=1
swastik[10][11]=1
swastik[10][12]=1
swastik[10][13]=1
swastik[10][14]=1
swastik[10][15]=1
swastik[11][13]=1
swastik[11][15]=1
swastik[12][11]=1
swastik[12][12]=1
swastik[12][13]=1
swastik[12][15]=1