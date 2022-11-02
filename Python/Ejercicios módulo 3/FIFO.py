# FIFO
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

que = Queue()
que.put(1)
que.put("perro")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Error de Cola")
