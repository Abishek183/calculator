from app.commands import Command


class SubtractCommand(Command):
    def execute(self):
        value1 = int(input('enter the first value >> '))
        value2 = int(input('enter the second value >> '))
        print(value1 - value2)