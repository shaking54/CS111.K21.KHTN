from timeit import default_timer as timer
from datetime import timedelta
start = timer()
print('Hello')
end = timer()
print(timedelta(seconds=end-start))
