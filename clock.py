#!/usr/bin/env python3

class Clock:
    def __init__(self, h=0, m=0):
        try:
            if type(h) != type(1):
                raise TypeError("Didn't enter integers for hours/minutes") 
            elif h<0 or h>23 or m<0:
                raise ValueError("hour(s) and/or minute(s) set out of range")
        except (TypeError, ValueError):
            print("Entered wrong type of argument(s) or argument(s) out of range")
            raise
        else:
            self.hours = h
            self.minutes = m
            self.hours = self.minutes//60 + self.hours
            self.minutes = self.minutes % 60
            self.hours = self.hours % 24
            

    def tick(self, m=1):
        self.minutes = self.minutes + m
        self.hours = self.minutes//60 + self.hours
        self.hours = self.hours % 24
        self.minutes = self.minutes % 60

    def __str__(self):
        return '{:02d}:{:02d}'.format(self.hours, self.minutes)

if __name__ == '__main__':

    clock0 = Clock()
    clockN = Clock(23, 55)

    clock0.tick()
    print("The time should be: 00:01\n")
    print(clock0)
    print()

    clockN.tick(6)
    print("The time should be: 00:01\n")
    print(clockN)
    print()

    clockN.tick(61)
    print("The time should be: 01:02\n")
    print(clockN)
    print()

    clock0.tick(61)
    print("The time should be: 01:02\n")
    print(clockN)
    print()

