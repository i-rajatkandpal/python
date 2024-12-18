class prey:
    def flee(self):
        print("This animal is fleeing")

class predator:
    def hunt(self):
        print("This animal is hunting")

class rabbit(prey):
    pass

class hawk(predator):
    pass

class fish(prey,predator):
    pass

rabbit1 = rabbit()
hawk1 = hawk()
fish1 = fish()

fish1.flee()
fish1.hunt()