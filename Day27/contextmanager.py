#creating a own context manager(auomatically setup ans cleanup)
class student:
    def __enter__(self):
        print("student entered")
        return self
    def __exit__(self,exc_type, exc_val, exc_tb):
        print("std exited automatically")
with student():
    print("learning python")