#algorithm to add times into slots of free time to optimize the times that can be fit in.
class Gap:
    gap_num=0
    def __init__(self, time):
        self.time_available=time
        self.time=time
        self.id=Gap.gap_num
        self.contained_events=[]
        Gap.gap_num+=1
    def __str__(self):
        return f''
    def insert(self,event):
        #event should be a tuple of (name of event, event object)
        self.contained_events.append(event)
        event_object=event[1]
class Task:
    def __init__(self,name,time):
        self.name=name
        self.time=time
    def __str__(self):
        return f'{self.name} for {self.time} minutes'
g=Gap(30)
t=Task("math",30)
print(t)

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
