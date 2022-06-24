class Contest:
    def __init__(self,name,div):
        self.name = name
        self.div = div
    def get_name(self):
        return self.name
    
stu = Contest("Aminul", "Barishal")
print(stu.get_name())