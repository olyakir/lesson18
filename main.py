class Bill:
    def __init__(self):
        self.money =  9

    def add(self, count):
        self.money += count

    def buy(self, count, name):
        pass

leo_bill = Bill()
print(leo_bill.money)

leo_bill.add(10)
leo_bill.add(20)
print(leo_bill.money)

kate_bill = Bill()
print(kate_bill.money)

kate_bill.add(1)
print(kate_bill.money)

print('ocnfkjcm 30', leo_bill.money)




class Person:
    def say(self, message):
        print(message)

    def say_hello(self):
        self.say("Hello work")

tom = Person()
tom.say_hello()




class Cat:
    def __init__(self, color, eye):
        self.color = color
        self.eye = eye
    def say1(self):
        print(self.color, self.eye)


siam = Cat('Blue','Brown')
siam.say1()




