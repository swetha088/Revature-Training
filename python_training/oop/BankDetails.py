from typing import final


class BankDetails:

    def __init__(self, custid, cname, bal):
        self.custid = custid
        self.cname = cname
        self.bal = bal

    def wel_message(self):
        print("Welcome to SBI")
    @final
    def display_details(self):
        print(f'{self.custid} - {self.cname} - {self.bal}')
