class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)



def enter_room(room, visited_rooms):
    visited_rooms[room.id] = {}
    for exit_direction in room.get_exits():
        visited_rooms[room.id][exit_direction] = '?'


def bfs(visited_rooms):
    visited = set()
    my_queue = Queue()
    room = player.current_room

    # add room id
    my_queue.enqueue([room.id])
    
    
    while my_queue.size() > 0:
        path = my_queue.dequeue()
        # the last node
        end = path[-1]
        if end not in visited:
            visited.add(end)
            # checks if last room has been visited
            for exit_direction in visited_rooms[end]:
                # if no exit exists
                if (visited_rooms[end][exit_direction] == '?'):
                    return path
                # when it hasn't been visited run this
                elif (visited_rooms[end][exit_direction] not in visited):
                    # create/ add a new path
                    new_path = path + [visited_rooms[end][exit_direction]]
                    # add the new path
                    my_queue.enqueue(new_path)
    return path