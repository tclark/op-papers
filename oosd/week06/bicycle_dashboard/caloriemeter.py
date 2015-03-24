class Caloriemeter:
    def __init__(self, bicycle):
        self.cals = 0
        self.subject = bicycle
        bicycle.add_observer(self)

    def update(self, rpms):
        self.cals = 5 * rpms
