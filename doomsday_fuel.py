from __future__ import division
import numpy as np
from numpy.linalg import inv
from fractions import Fraction

# Run solution(m), m = Test case
def solution(m):
    m = np.array(m)
    RowSum = np.sum(m,axis=1)
    idxTranStat = np.flatnonzero(RowSum > m.diagonal().astype(int))
    idxTerminal = np.setdiff1d(np.array(range(0,len(m))),idxTranStat)
    TranLen = len(idxTranStat)
    r = m[np.ix_(idxTranStat, idxTerminal)] / RowSum[idxTranStat][:, None]
    q = m[np.ix_(idxTranStat,idxTranStat)]/RowSum[idxTranStat][:,None]
    FR = np.matmul(inv(np.identity(TranLen) - q), r)
    if (FR.shape[0] == 0):
        return np.append(np.append(1,np.zeros(m.shape[0]-1).astype(int)),1)
    dens = []
    nums = []
    for i in FR[0]:
        dens.append(Fraction(i).limit_denominator().denominator)
        nums.append(Fraction(i).limit_denominator().numerator)
    denominator = reduce(np.lcm,dens)
    coeff = np.array([denominator/x for x in dens]).astype(int)
    return np.append([nums * coeff],denominator)

# Uncomment following to see the example
# print(solution([[0,2,1,0,0],[0,0,0,3,4],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]))
