#challenge:secure student portal
class studentportal:
    def __init__(self,name,branch,marks):
        self.name=name#public
        self._branch=branch#protected
        self.__marks=marks #private
    def show_profile(self):
        print("std1:",self.name)
        print("std1:",self._branch)
    def show_marks(self):
        print("std2 marks:",self.__marks)
std1=studentportal("deepthi","AIML",45)
std2=studentportal("gorge","CSE",78)
std1.show_profile()
std1.show_marks()
std2.show_profile()
std2.show_marks()
print("public:",std1.name)
print(std1._branch)#protected
print(std2.name)
print(std2._branch)
        