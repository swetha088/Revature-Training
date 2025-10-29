class College:
    def __init__(self, ccode, cname):
        self.ccode = ccode
        self.cname = cname

        @property
        def ccode(self):
            return self._ccode

        @property
        def cname(self) :
            return self._cname
    def coll_display(self) :
        return self.ccode, self.cname




