from Node import State,Node
from Stackfrontier import Stack
class Robot:
    def __init__(self):
        x_position=(input("please enter the initial horizontal position of the robot : "))
        y_position=(input("please enter the initial vertical position of the robot : "))
        self.initial=(x_position,y_position,0,False)

    def get_actions(self,Node,explored):

        Node_state = State(Node.state[0], Node.state[1], Node.state[2], Node.state[3])

        seed_increment=Node_state.no_seeds+1
        actions = [ ]
        #print((Node_state.xposition,Node_state.yposition))
        if (Node_state.xposition,Node_state.yposition) not in explored:
            Node_state.seeded=False

        if Node_state.xposition=="left":
           actions.append( ("right", ("right",Node_state.yposition,Node_state.no_seeds,Node_state.seeded)))
        if Node_state.xposition=="right":
           actions.append( ("left", ("left",Node_state.yposition,Node_state.no_seeds,Node_state.seeded)))
        if Node_state.yposition=="up":
           actions.append( ("down", (Node_state.xposition,"down",Node_state.no_seeds,Node_state.seeded)))
        if Node_state.yposition=="down":
           actions.append( ("up", (Node_state.xposition,"up",Node_state.no_seeds,Node_state.seeded)))
        if Node_state.seeded == False:
               actions.append(("seed", (Node_state.xposition, Node_state.yposition, seed_increment, True)))



        return actions



























