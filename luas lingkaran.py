from time import sleep
from tqdm import tqdm
for i in tqdm(range(100)):
    if i == 6:
    	sleep(2)
    if i == 70:
    	sleep(3)
    sleep(0.1)
