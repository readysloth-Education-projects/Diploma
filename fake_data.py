import sys
import random
import matplotlib.pyplot as plt

times = range(1000)
value = float(sys.argv[1])
bound = float(sys.argv[2])

data = [random.triangular(value-bound, value+bound, value) for _ in times]
avg = sum(data)/len(data)

plt.hist(data, bins=len(data)//100, density=True)
plt.axvline(avg, color='r', linestyle='dashed', linewidth=2)

min_ylim, max_ylim = plt.ylim()

plt.text(avg*1.008, max_ylim*0.9, 'Среднее: {:.2f}'.format(avg))

plt.xlabel("Время сжатия")
plt.savefig(sys.argv[3])
