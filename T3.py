import func


class T3:
    def minimal(self, e):
        min_k3 = func.minVect(e)
        return min_k3

    def res3(self, d, md, min_k, mc, c, mr, mz):
        MDC3 = func.multMatr(md, mc)
        MDCZ3 = func.multMatr(MDC3, mz)
        DC3 = func.scalarMult(d, c)
        DCE3 = func.Mult(min_k, DC3)
        MDCE3 = func.scalarMultMatr(DCE3, mr)
        MA3 = func.sumMatr(MDCE3, MDCZ3)
        return MA3

