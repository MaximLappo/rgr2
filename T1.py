import func


class T1:
    def __init__(self, e, d, md):
        self.e = e
        self.d = d
        self.md = md

    def minVect(self,vect):
        minVect = min(vect)
        return minVect

    def minimal(self, e, e1):
        min_k1 = func.minVect(e)
        min_k14 = min(min_k1,e1)
        return min_k14

    def res1(self, d, md, min_k, mc, c, mr, mz):
        MDC1 = func.multMatr(md, mc)
        MDCZ1 = func.multMatr(MDC1, mz)
        DC1 = func.scalarMult(d, c)
        DCE1 = func.Mult(min_k, DC1)
        MDCE1 = func.scalarMultMatr(DCE1, mr)
        MA1 = func.sumMatr(MDCE1, MDCZ1)
        return MA1

    def sum_ma14(self, Ma1, Ma2):
        ma14 = func.sumMatr(Ma1, Ma2)
        return ma14
