class Speedometer:
    def __init__(self, bicycle):
        self.speed = 0
        self.wheelcirc = 205
        self.subject = bicycle
        bicycle.add_observer(self)

    def update(self, rpms):
        self.speed = self.wheelcirc * (60 * rpms)/100000.0
