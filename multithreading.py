#  two libraries are available : thread and threading 

import threading 
def test(id):
    print("program start %d " % id)
print(test(45))
thread = [threading.Thread(target=test , args=(i,)) for i in range(10)]

for t in thread :
    t.start()