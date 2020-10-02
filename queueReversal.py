

# Class for Queue generation
class Queue: 
    def __init__(self): 
        self.items = [] 
  
  # check for empty queue
    def isEmpty(self): 
        return self.items == [] 
  
  # add elements to the queue
    def add(self, item): 
        self.items.append(item) 
  
  # pop elements from queue
    def pop(self): 
        return self.items.pop(0) 
  
  # add new elements at the start of the queue
    def front(self): 
        return self.items[0] 
  
  # o/p queue to the console
    def printQueue(self): 
        for i in self.items: 
            print(i, end =" ") 
        print("") 
  
  
# Recursive Function to reverse the queue 
def reverseQueue(q): 
  
    # Base case 
    if (q.isEmpty()): 
        return
  
    # Dequeue current item (from front)  
    data = q.front(); 
    q.pop(); 
  
    # Reverse remaining queue   
    reverseQueue(q) 
  
    # Enqueue current item (to rear)   
    q.add(data) 
  
  
# Driver Code 
q = Queue() 
q.add(50) 
q.add(60) 
q.add(80) 
q.add(20) 
q.add(40) 
q.add(30) 
q.add(70) 
q.add(60) 
q.add(90) 
q.add(100) 
reverseQueue(q) 
q.printQueue() 
