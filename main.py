from data import jobs
from model import Factory, Machine, Task

f = Factory(jobs)
for i in range(1, 11):
    f.add_machine(Machine(i))
f.giveTasks()