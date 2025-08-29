

class Hello():
    def __init__(self,name) :
        self.name=name
    def showInfo(self) :
        print(self.name)

    #h = Hello()    
    #h.showInfo('张三')


h = Hello('张三')
h.showInfo()