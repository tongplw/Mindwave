import time
import mindwave


headset = mindwave.Headset('COM6')

# print headers
time.sleep(2)
wave = headset.waves
print(''.join(f'{k:<14}' for k in wave.keys()))

while True:
	# print values
    time.sleep(0.5)
    wave = headset.waves
    print(''.join(f'{v:<14}' for v in wave.values()), end='\r')


    # print (f'Raw value: {headset.raw_value}, Attention: {headset.attention}, Meditation: {headset.meditation}')