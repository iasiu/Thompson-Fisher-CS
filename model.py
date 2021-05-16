import itertools
from data import PRINTINFO, jobsData

class Solution:
    def createRandom(self):
        pass

class Factory:
    def __init__(self):
        if PRINTINFO:
            print("Created Factory")
        self.machines = {}
        self.machinesIds = []
        self.create_machines()

        self.jobs = []
        self.create_jobs()

        self.jobsData = jobsData
        self.tasksToGive = []
        self.create_tasks()
        self.assign_tasks_to_jobs()
    
    def create_machines(self):
        for i in range(1, 11):
            self.add_machine(Machine(i))
    
    def create_jobs(self):
        for i in range(10):
            self.add_job(Job(i))
    
    def add_job(self, job):
        self.jobs.append(job)
        if PRINTINFO:
            print("Added {} to factory".format(str(job)))
    
    def assign_tasks_to_jobs(self):
        for i, task in enumerate(self.tasksToGive):
            self.jobs[task.jobId].add_task(task)

    def create_tasks(self):
        for jobId, job in enumerate(self.jobsData):
            for taskId, operation in enumerate(job):
                self.tasksToGive.append(Task(jobId, taskId, operation[0], operation[1]))
    
    def give_task(self, task, job):
        if task:
            if task.machineId in self.machinesIds:
                return self.machines[task.machineId].add_task(task, job)
        else:
            return None
    
    def add_machine(self, machine):
        machineId = machine.id
        self.machines[machineId] = machine
        self.machinesIds.append(machineId)
        if PRINTINFO:
            print("Added {} to factory".format(str(machine)))
    
    def add_machines_list(self, machinesList):
        for machine in machinesList:
            self.add_machine(machine)

class Machine:
    def __init__(self, id):
        self.id = id
        self.tasks = []
        self.executionTime = 0
        if PRINTINFO:
            print("Created {}".format(str(self)))
    
    def add_task(self, task, job):
        task.startTime = self.executionTime if self.executionTime > job.currentTime else job.currentTime
        self.tasks.append(task)
        self.executionTime = task.startTime + task.duration
        if PRINTINFO:
            print("Added {} to {}, start at-{}".format(str(task), str(self), task.startTime))
        return self.executionTime
    
    def add_tasks_list(self, tasksList):
        for task in tasksList:
            self.add_task(task)
    
    def __str__(self):
        return "Machine-{}".format(self.id)

class Job:
    def __init__(self, jobId):
        self.id = jobId
        self.taskQueue = []
        self.currentTime = 0
        if PRINTINFO:
            print("Created {}".format(str(self)))
    
    def add_tasks_list(self, tasksList):
        for task in tasksList:
            self.add_task(task)

    def add_task(self, task):
        self.taskQueue.append(task)
        if PRINTINFO:
            print("Added {}, to {}".format(str(task), str(self)))
    
    def pop_task(self):
        if len(self.taskQueue) > 0:
            task = self.taskQueue.pop(0)
            return task
        else:
            return None
    
    def __str__(self):
        return "Job-{}".format(self.id)

class Task:
    def __init__(self, jobId, taskId, machineId, duration):
        self.jobId = jobId
        self.id = taskId
        self.machineId = machineId
        self.duration = duration
        self.startTime = 0
        if PRINTINFO:
            print("Created {}".format(str(self)))
    
    def __str__(self):
        return "Task-{}.{} for Machine-{}, duration-{}".format(self.jobId, self.id, self.machineId, self.duration)
