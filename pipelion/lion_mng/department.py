

class Department:

    def __init__(self, id, type, name, programs, steps):
        self.id = id
        self.type = type
        self.name = name
        self.programs = programs
        if len(steps) > 0 and steps[0] != "created":
            steps. insert(0, "created")
        self.steps = steps

    def insertStep(self, step, index):
        if step in self.steps or index < 1 or index > len(self.steps):
            return False
        self.steps.insert(index,step)
        return True
        #Kendra TODO: Add Backend Calls to change steps in each element of bodies

    def deleteStep(self, step):
        self.steps.remove(step)

    def moveStep(self, step, index):
        self.steps.remove(step)
        self.steps.insert(index,step)
