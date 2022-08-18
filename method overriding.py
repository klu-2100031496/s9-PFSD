class Student:
    def add(self):
        print("base")
class Derived(Student):
    def add(self):          #overridden method
        print("derived")
ob=Derived()
ob.add()