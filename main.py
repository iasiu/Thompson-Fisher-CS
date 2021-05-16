from model import Factory, Machine, Task
from random import choice
import gc

factories = []

def solution():
    factories = [Factory()]
    available = list(factories[-1].machinesIds)

    while True:
        if len(available) == 0:
            break
        chosenId = choice(available)
        task = factories[-1].jobs[chosenId - 1].pop_task()
        jobtime = factories[-1].give_task(task, factories[-1].jobs[chosenId - 1])
        factories[-1].jobs[chosenId - 1].currentTime = jobtime
        if len(factories[-1].jobs[chosenId - 1].taskQueue) == 0:
            available.pop(available.index(chosenId))
    times = [m.executionTime for k, m in factories[-1].machines.items()]

    return max(times)
    factories.clear()
    gc.collect()

mintime = 5000
iterations = 30000000
for i in range(iterations):
    if i % int(iterations/100) == 0:
        print("{}%".format(int(i/(iterations/100))))
    time = solution()
    if time < mintime:
        mintime = time

print(mintime)