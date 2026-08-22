#abstraction with employee ex
from abc import ABC ,abstractmethod
class employee:
        @abstractmethod
        def __init__(self,emp_name,emp_role):
                self.emp_name=emp_name
                self.emp_role=emp_role
        def work(self):
                pass
class developer(employee):
        def work(self):
                print("developer class")
                print(self.emp_name)
                print(self.emp_role)
class manager(employee):
        def work(self):
                print("manager class")
                print(self.emp_name)
                print(self.emp_role)

developer1=developer("prasad","tester")
manager1=manager("yash","software")
developer1.work()
manager1.work()
