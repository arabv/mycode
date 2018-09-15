#!/usr/bin/python3

class Bird:
    energy=2
    def speak(self):
        print ((Bird.energy) * ("hi"))  #self.energy works as well

bird=Bird()
bird.speak()
