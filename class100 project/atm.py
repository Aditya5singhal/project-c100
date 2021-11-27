class Atm(object):
    def __init__(self,name,number,bankname,pin):
        self.name=name
        self.number=number
        self.bankname=bankname
        self.pin=pin
 
    def pinno(self):
        print("pinno")

p=Atm("abc",2,"sbi",1234)
print(p.pin)      