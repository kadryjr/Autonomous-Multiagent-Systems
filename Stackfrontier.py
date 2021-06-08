class Stack:
    def __init__(self):
        self.stack=[]
    def add(self, node):
        self.stack.append(node)
    def empty(self):
        if len(self.stack)==0:
            return True
        return False

    def remove(self):
        if self.empty():
            raise Exception("empty stack")
        else:
            node=self.stack[-1]
            self.stack.pop(len(self.stack)-1)
            return node

    def contains_state(self, state):
        return any(node.state == state for node in self.stack)