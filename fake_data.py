import sys
import csv
import random
import itertools as it

import matplotlib.pyplot as plt

times = range(1000)
value = float(sys.argv[1])
csv_name = sys.argv[2]+'.csv'
bound = float(sys.argv[3])

data = [random.triangular(value-bound, value+bound, value) for _ in times]
avg = sum(data)/len(data)

plt.hist(data, bins=len(data)//100, density=True)
plt.axvline(avg, color='r', linestyle='dashed', linewidth=2)

min_ylim, max_ylim = plt.ylim()

plt.text(avg*1.008, max_ylim*0.9, 'Среднее: {:.2f}'.format(avg))

plt.xlabel("Время сжатия")
plt.savefig(sys.argv[4])


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


with open(csv_name, 'w') as f:
    writer = csv.writer(f)
    table = chunks(list(map(lambda t: (t[0]+1,round(t[1],1)), enumerate(data))), 10)
    writer.writerows([it.chain.from_iterable(l) for l in table])
