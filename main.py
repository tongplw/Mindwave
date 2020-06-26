import time
import mindwave
import pandas as pd
from datetime import datetime


headset = mindwave.Headset('COM6')
time.sleep(10)

# print headers
wave = headset.waves
keys = ['raw', 'attention', 'meditation'] + list(wave.keys())
print(''.join(f'{k:<14}' for k in keys))

starttime = time.time()
values = []

while True:

    time.sleep(1/256 - ((time.time() - starttime) % (1/256)))

	# print values
    wave = headset.waves
    values += [[datetime.now()] + [headset.raw_value, headset.attention, headset.meditation] + list(wave.values())]
    # print(''.join(f'{v:<14}' for v in values[-1]), end='\r')
    
    # save data every 10 lines
    if len(values) % 1024 == 0:
        df = pd.DataFrame(values)
        df.to_csv('raw.csv', mode='a', index=False, header=False)
        values = []
    
    # time.sleep(1/256)
