from studexcurr import StudExCurr
from TeacherDetail import TeacherDetail

class FinalEval(StudExCurr,TeacherDetail):
    def __init__(self, ccode,cname,rollno,sname, m1,m2,m3, exm1, exm2,
                 empid,tname, dept,
                feedbackfromteacher):
        StudExCurr.__init__(self, ccode, cname, rollno, sname, m1, m2, m3, exm1, exm2)
        TeacherDetail.__init__(self, ccode, cname, empid, tname, dept)

        self.feedbackfromteacher = feedbackfromteacher






