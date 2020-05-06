class Maths:
    def __init__(self):
        print("Maths Module")

    @staticmethod
    def getNumber(text):
        res = [int(i) for i in text if i.isdigit()]
        return res[0]

    @staticmethod
    def addition(text):
        res = [int(i) for i in text if i.isdigit()]
        value = 0
        for i in res:
            value+=i
        print("Addition of numbers:",value)
    @staticmethod
    def subraction(text):
        res = [int(i) for i in text if i.isdigit()]
        value = 0
        for i in res:
            value-=i
        print("Subraction of numbers:",value)
    @staticmethod
    def multiplication(text):
        res = [int(i) for i in text if i.isdigit()]
        value = 1
        for i in res:
            value*=i
        print("Muplication of numbers:",value)
    @staticmethod
    def division(text):
        res = [int(i) for i in text if i.isdigit()]
        value = 1
        for i in res:
            value = i / value
        print("Division of numbers:",value)


