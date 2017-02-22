#!/usr/bin/env python3

class Clock:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m

    def tick(self, m=1):
        self.minutes = self.minutes + m
        self.hours = self.minutes//60 + self.hours
        self.hours = self.hours % 24
        self.minutes = self.minutes % 60

    def __str__(self):
        return '{:02d}:{:02d}'.format(self.hours, self.minutes)

if __name__ == '__main__':

    clock1 = Clock()
    clock2 = Clock(23, 55)

    print('clock 1 set at: ',  clock1)
    print('clock 2 set at: ',  clock2)

    clock1.tick()
    clock2.tick(6)

    print('clock 1 after tick is set at: ', clock1)
    print('clock 2 after 6 minute tick is set at: ',  clock2)
