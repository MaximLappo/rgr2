import func


class T4:
    def __init__(self, mr, mz):
        self.mr = mr
        self.mz = mz

    def minimal(self, e):
        min_k4 = func.minVect(e)
        return min_k4

    def res4(self, d, md, min_k, mc, c, mr, mz):
        MDC4 = func.multMatr(md, mc)
        MDCZ4 = func.multMatr(MDC4, mz)
        DC4 = func.scalarMult(d, c)
        DCE4 = func.Mult(min_k, DC4)
        MDCE4 = func.scalarMultMatr(DCE4, mr)
        MA4 = func.sumMatr(MDCE4, MDCZ4)
        return MA4
