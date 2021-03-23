import time 
import pytz

c_t = time.localtime()
c_c = time.strftime("%H:%M", c_t)
IST = pytz.timezone('Asia/Kolkata')

print ("time in EAST cost :" c_c)
print (" time in kolkata is: "datetime.now(IST))
