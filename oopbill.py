class Bill():
    def __init__(self,first_person,second_person):
        self.rent = int(input("Enter rent : "))
        self.time_bill = input("Enter bill period : ")
        self.first_person = first_person
        self.second_person = second_person
    def calculator(self):
        share = self.rent / (self.first_person.time_in_dormitory + self.second_person.time_in_dormitory)
        self.rent_first_person = share * self.first_person.time_in_dormitory
        self.rent_second_person = share * self.second_person.time_in_dormitory
    def print_bill(self):
        print(self.time_bill)
        print(self.first_person.name,'pays',self.rent_first_person)
        print(self.second_person.name,"pays",self.rent_second_person)
class Person():
    def __init__(self):
        self.name = input("Enter person name : ")
        self.time_in_dormitory = int(input("Enter time lived in dormitory : "))
first_person = Person()
second_person = Person()
bill = Bill(first_person,second_person)
bill.calculator()
bill.print_bill()