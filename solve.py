from Node import Node,State
from Stackfrontier import Stack
from Robot import Robot


class solve(Robot):
        def __init__(self):
            super().__init__()
            self.solution=None
            self.num_explored=0
            self.explored = set()
            self.position_explored=set()
            # Initialize frontier to just the starting position
            self.start = Node(state=self.initial, parent=None, action=None)

        def solve(self):


            frontier = Stack()
            frontier.add(self.start)


            while True:
                #print("hi")
                if frontier.empty():
                    raise Exception("stack is empty")

                node = frontier.remove()
                self.num_explored += 1
                if node.state[2]==4:
                    actions = []
                    cells = []
                    while node.parent is not None:
                        actions.append(node.action)
                        cells.append(node.state)
                        node = node.parent
                    actions.reverse()
                    cells.reverse()
                    self.solution = (actions, cells)
                    return

                self.explored.add(node.state)

                for action, state in self.get_actions(node,explored=self.position_explored):
                    if not frontier.contains_state(state) and state not in self.explored:
                        child = Node(state=state, parent=node, action=action)
                        frontier.add(child)
                self.position_explored.add((node.state[0],node.state[1]))

        def print(self):
            for i in range(len(self.solution[0])):
                print("action",i,": ",self.solution[0][i],"        state",i,": ",self.solution[1][i][:3],"\n")
