import time
import copy
class Time:
    def __init__(self,hour=time.localtime().tm_hour,min=time.localtime().tm_min):
        assert(0<=hour<24)
        assert(0<=min<60)
        self.hour=hour
        self.min=min
        self.as_int=self.hour*60+self.min
    def __str__(self,military=True):
        str_min=str(self.min)
        if len(str_min)==1:
            str_min="0"+str_min
        if military:
            return(f'{self.hour}:{str_min}')
        elif self.hour<12:
            if self.hour==0:
                return(f'12:{str_min} AM')
            return(f'{self.hour}:{str_min} AM')
        else:
            if self.hour==12:
                return(f'12:{str_min} PM')
            new_hour=self.hour-12
            return(f'{new_hour}:{str_min} PM')
    def __add__(self,num):
        self.min+=num
        self.make_valid()
    def __lt__(self,t2):
        return self.to_int()<t2.to_int()
    def __gt__(self,t2):
        return self.to_int()>t2.to_int()
    def __le__(self,t2):
        return self.to_int()<=t2.to_int()
    def __ge__(self,t2):
        return self.to_int()>=t2.to_int()
    def calc_next_fifteen(self, buffer=5):
        next_min=15*(self.min//15+1)
        while next_min-self.min<=buffer:
            next_min+=15
        self.min=next_min
        self.make_valid()
        return self
    def make_valid(self):
        while self.min>=60:
            self.min-=60
            self.hour+=1
        self.hour%=24
    def to_int(self):
        return self.hour*60+self.min
    def difference(self,t2):
        return -self.to_int()+t2.to_int()
class Event(Time):
    def __init__(self, name,*args):
        self.name=name
        if len(args)==1:
            start,end=args[0].split("-")
            self.start_hour,self.start_min=start.split(":")
            self.end_hour,self.end_min=end.split(":")
            self.start_time=Time(int(self.start_hour),int(self.start_min))
            self.end_time=Time(int(self.end_hour),int(self.end_min))
        elif len(args)==2:
            if isinstance(args[0],Time):
                if isinstance(args[1],Time):
                    self.start_time=args[0]
                    self.end_time=args[1]
                elif isinstance(args[1],int):
                    start=args[0]
                    self.start_time=args[0]
                    inc=int(args[1])
                    self.end_time=copy.deepcopy(self.start_time)
                    self.end_time+inc 
            else:
                start=args[0]
                self.start_hour,self.start_min=start.split(":")
                self.start_time=Time(int(self.start_hour),int(self.start_min))
                inc=int(args[1])
                self.end_time=copy.deepcopy(self.start_time)
                self.end_time+inc
        self.diff=(self.start_time).difference(self.end_time)
        if self.start_time>self.end_time:
            raise Exception("event start time is after end time")
    def __str__(self):
        return f'{self.name}: {self.start_time} - {self.end_time}'
    def has_conflict(self,e2):
        return (self.start_time>e2.end_time and self.end_time<e2.start_time) or (self.start_time<e2.end_time and self.end_time>e2.start_time)
class Gap:
    gap_num=0
    def __init__(self, time, start_time):
        self.time_available=time
        self.time=time
        self.id=Gap.gap_num
        self.task_list=[]
        self.start_time=start_time
        Gap.gap_num+=1
    def __str__(self):
        if len(self.task_list)==0:
            return f'Gap {self.id}: {self.time} mins total with no tasks, starting at {self.start_time}'
        else:
            s=f'Gap {self.id}: {self.time} minutes total with {self.time_available} minutes left, contains:'
            for task in self.task_list:
                s+=f'\n{task.name} for {task.time} minutes'
            return s+f'\nstarts at {self.start_time}'
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

start_time=Time(6,30)
task1=Task("task1",30)
task2=Task("task2",60)
task3=Task("task3",60)
event_list=[]

big_tasks=[task1,task2,task3]
for t in big_tasks:
    # event_list.append(Event(t.name,copy.deepcopy(start_time),t.time))
    print(type(t.name))
    print(type(copy.deepcopy(start_time)))
    print(type(t.time))
    # start_time+=t.time
for t in event_list:
    print(t)