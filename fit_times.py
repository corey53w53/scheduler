#algorithm to add times into slots of free time to optimize the times that can be fit in.
def insert_task(task_time,gaps):
    counter=0
    while counter<len(gaps):
        if task_time<gaps[counter]:
            gaps[counter]-=task_time
            return gaps
        counter+=1
    raise AssertionError
gaps=[50,20,30,100]
gaps=[[i] for i in gaps]
print(gaps)
task_list=[["math",30],["WHAP",90]]
task_times=[]
for task in task_list:
    task_times.append(task[1])
for task_time in task_times:
    gaps=insert_task(task_time,gaps)
    gaps.sort()
print(gaps)
