class Employee:
    def __init__(self, empid, ename, bp):
        self.empid = empid
        self.ename = ename
        self.bp = bp


    def calc_allowance(self):
        return (self.bp * 0.1) + (self.bp * 0.05)


    def calc_ded(self):
        return self.bp * 0.03

    def calc_grosspay(self):
        return self.bp + self.calc_allowance()

    def calc_netpay(self):
        return self.calc_grosspay() - self.calc_ded()
