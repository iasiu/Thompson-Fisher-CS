from data import jobsData
from model import Factory, Machine, Task

from random import choice


f = Factory(jobsData)
available = list(f.machinesIds)

while True:
    if len(available) == 0:
        break
    chosenId = choice(available)
    task = f.jobs[chosenId - 1].pop_task()
    task.offset = f.jobs[chosenId - 1].currentTime
    jobtime = f.give_task(task)
    f.jobs[chosenId - 1].currentTime += task.duration
    if len(f.jobs[chosenId - 1].taskQueue) == 0:
        available.pop(available.index(chosenId))

maxtime = [m.executionTime for k, m in f.machines.items()]
print(maxtime)