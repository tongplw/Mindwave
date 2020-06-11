import time
import mindwave
import pandas as pd


headset = mindwave.Headset('COM6')
time.sleep(10)

# print headers
wave = headset.waves
keys = ['raw', 'attention', 'meditation'] + list(wave.keys())
print(''.join(f'{k:<14}' for k in keys))

values = []

while True:

	# print values
    wave = headset.waves
    values += [[headset.raw_value, headset.attention, headset.meditation] + list(wave.values())]
    print(''.join(f'{v:<14}' for v in values[-1]), end='\r')

    # save data every 10 lines
    # if len(values) % 10 == 0:
    #     df = pd.DataFrame(values)
    #     df.to_csv('data.csv', mode='a', index=False, header=False)
    #     values = []
    
    time.sleep(1)