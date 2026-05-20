# Write your code here!
class toolbox:
    def __init__(self):
        self.tools = []

    def add_tool(self, tools):
        self.tools.append(tools)

    def remove_tool(self, tools):
        self.tools.remove(tools)

class hammer:
    def __init__(self):
        self.hammer = []
    
    def paint(self, colour):
        self.paint.append(colour)

    def remove_nails(self, nails):
        self.nails.remove(nails)
    
    def hammer_in(self, nails):
        self.nails.append(nails)


# Solutions below

class Toolbox:
    def __init__(self):
        self.tools = []

    def add_tool(self, tool):
        self.tools.append(tool)

    def remove_tool(tool):
        self.tools.remove(tool)

class Screwdriver:
    def __init__(self, size):
        self.size = size

    def tighten(self, screw):
        pass

    def loosen(self, screw):
        pass

class Hammer:
    def __init__(self, color):
        self.color = color

    def paint(self, color):
        self.color = color

    def hammer_in(self, nail):
        pass

    def remove(self, nail):
        pass
