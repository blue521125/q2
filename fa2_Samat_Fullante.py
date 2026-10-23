class Patient:
    def __init__(self,name,bill_amount):
        self.name = name
        self.bill_amount = bill_amount
    
    def get_name(self):
        print("Patient Name:",self.name)
    
    def set_name(self, name):
        self.name = name
    
    def get_bill_amount(self):
        print("Original Bill:",self.bill_amount)
    
    def set_bill_amount(self,bill_amount):
        self.bill_amount = bill_amount
    
    def calculate_bill(self):
        print("Final Bill:",self.bill_amount)


class Senior(Patient):
    def __init__(self,name,bill_amount):
        super().__init__(name,bill_amount)
    
    def calculate_bill(self):
        print("Final Bill:",self.bill_amount*0.8)


class PhilHealth(Patient):
    def __init__(self,name,bill_amount):
        super().__init__(name,bill_amount)
    
    def calculate_bill(self):
        print("Final Bill:",self.bill_amount*0.85)

print("Hospital Billing")
patientguy = Patient("Calicks",1000)
patientguy.get_name()
patientguy.get_bill_amount()
patientguy.calculate_bill()
print("\n")

gurlll = Senior("Granny Linda",25213)
gurlll.get_name()
gurlll.get_bill_amount()
gurlll.calculate_bill()
print("\n")

philhelth3 = PhilHealth("Mary Louise Carbungco",200000)
philhelth3.set_name("poopyhead")
philhelth3.get_name()
philhelth3.get_bill_amount()
philhelth3.calculate_bill()
