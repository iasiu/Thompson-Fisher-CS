import itertools

class Factory:
    def __init__(self, jobsData):
        self.machines = {}
        self.jobsData = jobsData
        self.machinesIds = []
        print("Created factory")
        self.tasksToGive = []
        self.createTasks()

    def createTasks(self):
        for jobId, job in enumerate(self.jobsData):
            for taskId, operation in enumerate(job):
                self.tasksToGive.append(Task(jobId, taskId, operation[0], operation[1]))
        self.jobsData.clear()
    
    def giveTasks(self):
        for i, task in enumerate(self.tasksToGive):
            if task.machineId in self.machinesIds:
                pass
            else:
                print("Machine-{} not found in factory, task-{} remains in tasksToGive".format(task.machineId, task.id))
    
    def add_machine(self, machine):
        machineId = machine.id
        self.machines[machineId] = machine
        self.machinesIds.append(machineId)
        print("Added machine-{} to factory".format(machineId))
    
    def add_machines_list(self, machinesList):
        for machine in machinesList:
            self.add_machine(machine)

class Machine:
    def __init__(self, id):
        self.id = id
        self.tasks = []
        self.executionTime = 0
        print("Created machine-{}".format(self.id))
    
    def add_task(self, task):
        task.startTime = self.executionTime
        self.tasks.append(task)
        self.executionTime += task.duration
        print("Added task-{}{} to machine-{}, start at-{}, duration-{}".format(task.jobId, task.id, self.id, task.startTime, task.duration))
    
    def add_tasks_list(self, tasksList):
        for task in tasksList:
            self.add_task(task)

class Task:
    newId = itertools.count()
    def __init__(self, jobId, taskId, machineId, duration):
        self.jobId = jobId
        self.id = taskId
        self.machineId = machineId
        self.duration = duration
        self.startTime = 0
        print("Created task-{}.{}, for machine-{}, duration-{}".format(self.jobId, self.id, self.machineId, self.duration))
