# 모듈
# 1 현재시간 출력 
from datetime import datetime

dt = datetime.now()
print(dt)

# 2 현재시간의 타입
dt = datetime.now()
print(dt,type(dt))

# 3 timedelta 
from datetime import timedelta
from datetime import datetime

dt = datetime.now()

for d in range(5,0,-1):
    delta = timedelta(days=d)
    date = dt - delta
    print(delta)

# 4 strftime
print(dt.strftime("%H:%M:%S"))

# 5 os 모듈
import os
re = os.getcwd()
print(re,type(re))

