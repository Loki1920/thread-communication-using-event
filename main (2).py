import threading 
from threading import Event

n = int(input("enter a number:"))

ev = Event()
od = Event()

def odd(n): 
  
  for i in range(1,n+1):   
    if i % 2 !=0:
      print(threading.current_thread().getName()+" "+str(i))
      ev.set()
      od.clear()
      od.wait()

def even(n):  
  for i in range(1,n+1):   
    if i%2 ==0: 
      print(threading.current_thread().getName()+" "+str(i))
      od.set()
      ev.clear()
      ev.wait()

      
      
      
      
      

th1 = threading.Thread(target=odd,args=(n,))
th2 = threading.Thread(target=even,args=(n,))


th1.start()
th2.start()

th1.join()
th1.join()