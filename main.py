from model import Factory, Machine, Task

from random import choice

factories = []

def solution():
    factories.append(Factory())
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

solutions = []

for i in range(1):
    solutions.append(solution())

print(min(solutions))