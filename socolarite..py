#class of module
class Module:
    
    def __init__(self,name,note):
        self.__module = { name : note }
    
    def show(self):
        return self.__module
    
    #return note of module
    def get_note(self,name):
        return self.__module[name] 
        
    

    
#parent class
class Person:
    def __init__(self,first,last,age):
        self.__firstName = first
        self.__lastName = last
        self.__age = age
    
    def show(self):
        return 'my name is {} {} and my age {} '.format(self.__firstName,self.__lastName,self.__age)
    
class Student(Person):
    def __init__(self, first, last, age):
        super().__init__(first, last, age)
        self.modules = []
        self.build()
    
    # build list of modules by user 
    def build(self):
        for name in ['analyse','algebre','loqique','proba']:
            note = input('entre note of {}  '.format(name))
            note = float(note)
            self.modules.append(Module(name,note))
    
    #show moudules of student 
    def showMod(self):
        print('****list of modules****')
        for module in self.modules:
            print(module.show())
    
    #calcule moyenne of student
    def clacule(self):
        sum = 0
        i = 0
        for name in['analyse','algebre','loqique','proba']:
            module = self.modules[i]
            sum += module.get_note(name)
            i += 1
        return(sum/4)
    




class Teacher(Person):
    def __init__(self, first, last, age,hours=0):
        super().__init__(first, last, age)
        self.__hours = hours
    
    # add hours to the teacher ساعة بشكل افتراضي او المستخدم يحدد عدد الساعات المضافة
    def add_hour(self,h=1):
        self.__hours += h
    
    #calclue salary of teacher اما بقيمة افتراضية او المستخدم يحددها
    def salary(self,priceForHour=100):
        return(self.__hours * priceForHour)
    

#test module
#mod1 = Module('analyse',7)
#print(mod1.showMod())    

ahmed = Student('ben','Ahmed',20)
ahmed.show()
ahmed.showMod()
print('moyenne is {}'.format(ahmed.clacule()))

ali = Teacher('ben','ali',35)
ali.add_hour(10)
print('salary of the teacher : {}'.format(ali.salary(150)))