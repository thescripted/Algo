class Monitor(object):
    def __init__(self, items):
        pass

    def subscribe(self, item):
        """exposes a method to classes that want to subscribe to the monitor"""
    


class Stacks(object):

    def __init__(self, num_stacks, stack_size):
        self.num_stacks = num_stacks
        self.stack_size = stack_size
        self.stack_array = [None] * self.num_stacks * self.stack_array
        self.stack_pointers = [-1] * num_stacks
        pass

    def abs_index(self, stack_index):
        return stack_index * self.stack_size + self.stack_pointers[stack_index]

    def push(self, stack_index, data):
        self.stack_pointers[stack_index] += 1
        self.stack_array[self.abs_index(stack_index)] = data

    def pop(self, stack_index):
        data = self.stack_array[self.abs_index(stack_index)]
        self.stack_array[self.abs_index(stack_index)] = None
        self.stack_pointers[stack_index] -= 1


s = Stacks(3, 10)

s.push(1, "hello")
s.push(1, "howdy")
s.push(1, "sup")
s.push(2, "hey")
s.push(s.pop(1))

