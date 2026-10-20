class animal():
    alive=False
    def eat(self):
        print("animal is eat food")
    def sleep(self):
        print("animal is sleeping")
    
class rabbit(animal):
    pass
class hen(animal):
    pass
class cow(animal):
    pass
'''rabbitu=rabbit()
henu=hen()
cowu=cow()'''

print(rabbit.alive)
hen().eat()
cow().sleep()