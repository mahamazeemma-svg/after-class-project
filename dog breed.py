class dog:
    def __init__(self,breed):
        self.breed = breed

    def display(self):
        print("dog breed:",self.breed)

dog1 = dog("labrodor")
dog2 = dog("chuiaha")
dog1.display()
dog2.display()