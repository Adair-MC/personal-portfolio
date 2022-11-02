# FIFO Parte 2
# -------------------------
# Samuel Melo y Johan Yasno
class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.queue_list = []

    def put(self, elem):
        self.queue_list.append(elem)

    def get(self):
        if len(self.queue_list) > 0:
            val = self.queue_list[0]
            del self.queue_list[0]
            return val
        else:
            raise QueueError

class SuperQueue(Queue):
    def isempty(self):
        if len(self.queue_list) > 0:
            return False
        else:
            return True


que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")
