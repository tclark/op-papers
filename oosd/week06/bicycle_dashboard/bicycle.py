
class Bicycle:
    """ This class acts as the subject of our observer pattern
    demo.  It stores the current RPMs that the bicycle crank 
    is turning, lets us register/deregister obervers, and notifies
    them.
    """
    def __init__(self):
        self.observers = []
        self.current_rpms = 0

    def add_observer(self, o):
        self.observers.append(o)

    def remove_observer(self, o):
        self.observers.remove(o)

    def notify_observers(self):
        for o in self.observers:
            o.update(self.current_rpms)

    def _set_rpms(self, rpms):
        self.__dict__["current_rpms"] =  rpms
        self.notify_observers()

    def __setattr__(self, name, value):
        if name == "current_rpms":
            self._set_rpms(value)
        else:
            self.__dict__[name] = value


