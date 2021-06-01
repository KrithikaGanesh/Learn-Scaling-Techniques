import threading

l1 = []

def append_to_list(l):
  l.append(200)

T = threading.Thread(target=append_to_list, args=(l1,))
T.start()
l1.append(100)
print(l1)

"""
Multithreading in python - Cons
# Due to Global Interpreter Lock, a lock acquired each time to execute byte code
# We see [200,100] or [100,200], append operation is atomic
# if not atomic memory corruption would occur, result would be [100],[200]
# There will be many contentions to acquire GIL, 
# if the the thread runs a lot of byte codes
"""