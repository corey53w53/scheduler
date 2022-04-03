#algorithm to add times into slots of free time to optimize the times that can be fit in.
from tkinter import S


class Gap:
    gap_num=0
    def __init__(self, time):
        self.time_available=time
        self.time=time
        self.id=Gap.gap_num
        self.task_list=[]
        Gap.gap_num+=1
    def __str__(self):
        if len(self.task_list)==0:
            return f'Gap {self.id}: {self.time} mins total with no tasks'
        else:
            s=f'Gap {self.id}: {self.time} minutes total with {self.time_available} minutes left, contains:'
            for task in self.task_list:
                s+=f'\n{task.name} for {task.time} minutes'
            return s
            #30 minutes total with 15 minutes left, contains math for 15 minutes, english for 0 minutes
    def insert(self,task):
        #event should be a tuple of (name of event, length)
        self.task_list.append(task)
        self.time_available-=task.time
class Task:
    def __init__(self,name,time):
        self.name=name
        self.time=time
    def __str__(self):
        return f'{self.name} for {self.time} min'
g=Gap(40)
t=Task("math",30)
t2=Task("english",60)
g.insert(t)
print(g)
task_list=[]
task_list.append(t)
task_list.append(t2)
gaps=[50,20,30,100]
gap_list=[]
for gap in gaps:
    gap_list.append(Gap(gap))

for g in gap_list:
    print(g)

# def insert_task(task_time,gaps):
#     counter=0
#     while counter<len(gaps):
#         if task_time<gaps[counter][0]:
#             gaps[counter].append(task_time)
#             return gaps
#         counter+=1
#     raise AssertionError
# gaps=[50,20,30,100]
# gaps=[[i] for i in gaps]
# print(gaps)
# task_list=[["math",30],["WHAP",110]]
# task_times=[]
# for task in task_list:
#     task_times.append(task[1])
# for task_time in task_times:
#     gaps=insert_task(task_time,gaps)
#     gaps.sort()
# print(gaps)
