
class Node :
    def __init__(self,state,parent,action):
        self.state=state
        self.parent=parent
        self.action=action

class State :
    def __init__(self,xposition,yposition,number,seeded_or_not):
        self.xposition=xposition
        self.yposition=yposition
        self.no_seeds=number # goal state should have 4 seeds but initial should have zero of it
        self.seeded=seeded_or_not #boolean
