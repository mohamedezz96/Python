class QueueError(IndexError):  # Choose base class for the new exception.
    pass



class Queue:
    def __init__(self):
        self.__queue = []


    def put(self, elem):
        self.__queue.insert(0, elem)


    def get(self):
        val = self.__queue[-1]
        del self.__queue[-1]
        return val



que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
    
