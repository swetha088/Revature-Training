from oop.College import College

class TeacherDetail(College):
    def __init__(self, ccode, cname, empid ,tname, dept):
        College.__init__(self,ccode,cname)
        self.empid = empid
        self.tname = tname
        self.dept = dept

    def teachers_display(self):
        print(f'{self.ccode}\n {self.cname}\n '
              f' {self.empid}\n {self.tname}\n  {self.dept}')


