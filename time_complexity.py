"""time complexity"""

#time
import time
start=time.time()
print("hi")
end=time.time()
print(f"duration:{start-end:.4f}")

#datetime.now()
from datetime import datetime
start1=datetime.now()
print("hiiiiiiii")
end1=datetime.now()
print(start-end)

"""space complexity"""

#sys
import sys
lists=[1,2,3]
size=(sys.getsizeof(lists))
print(size)

#pympler

