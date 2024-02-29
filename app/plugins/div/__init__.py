import sys
from app.commands import Command


class DivideCommand(Command):
    def execute(self):
        value1 = int(input('enter the first value >> '))
        value2 = int(input('enter the second value >> '))
        print(value1 / value2)