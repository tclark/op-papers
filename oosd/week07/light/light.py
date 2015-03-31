class Light:
    def __init__(self):
        self.state = Off(self)

    def show(self):
        return self.state.state_display

    def switch(self):
        self.state.switch()


class Off:

    def __init__(self, light):
        self.state_display = "Light is off"
        self.light = light

    def switch(self):
        self.light.state = On(self.light)

class On:
    def __init__(self, light):
        self.state_display = "Light is on"
        self.light = light

    def switch(self):
        self.light.state = Off(self.light)
