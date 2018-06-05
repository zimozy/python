#!/usr/bin/env python

class Basket:

    # Always remember the *self* argument
    def __init__(self,contents=None):
        self.contents = contents or []

    def add(self,element):
        self.contents.append(element)

    def print_me(self):
        result = ""
        for element in self.contents:
            result = result + " " + `element`
        print "Contains:"+result


b = Basket(['apple','orange'])
b.add("lemon")
b.print_me()
