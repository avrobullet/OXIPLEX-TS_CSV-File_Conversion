class Time_Points():
    def __init__(self, name = None):
        if name is None:
            print("Oh hi!")
        elif name is not None:
            print("Oh hi", name, "!")

    def getTimePoints(self):
        time_1 = input("First time point: ")
        time_2 = input("Second time point: ")

def initiateTimePoints():
    tp = Time_Points()
    tp.getTimePoints()