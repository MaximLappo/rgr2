import func


class T2:
    def __init__(self, mc, c):
        self.mc = mc
        self.c = c

    def minVect(self,vect):
        minVect = min(vect)
        return minVect

    def minimal(self, k1, k2, k3):
        min_k2 = func.minVect(k1)
        min_k = min(min_k2, k2, k3)
        return min_k

    def res2(self, d, md, min_k, mc, c, mr, mz):
        MDC2 = func.multMatr(md, mc)
        MDCZ2 = func.multMatr(MDC2, mz)
        DC2 = func.scalarMult(d, c)
        DCE2 = func.Mult(min_k, DC2)
        MDCE2 = func.scalarMultMatr(DCE2, mr)
        MA2 = func.sumMatr(MDCE2, MDCZ2)
        return MA2

    def sum_ma(self, ma1, ma2, ma3):
        ma12 = func.sumMatr(ma1, ma2)
        ma = func.sumMatr(ma12, ma3)
        return ma
