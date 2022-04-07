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
    def __str__(self):
        return f'{self.start_time} - {self.end_time}'
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

user_input="meeting 15:00-16:30 school 6:30-12:00 math 30 english 30"
clean=user_input.split()
counter=0
start_bound=Time(6,30)
end_bound=Time(22,0)

total_list=[]
while counter<len(clean):
    if clean[counter].isalpha():
        smaller_list=[clean[counter]]
        counter+=1
        while not clean[counter].isalpha():
            if clean[counter].isnumeric(): smaller_list.append(int(clean[counter]))
            else: smaller_list.append(clean[counter])
            counter+=1
            if counter==len(clean): break
    total_list.append(smaller_list)
#parses user input into "total_list"
task_list,event_list=[],[]
for l in total_list:
    if len(l)==2 and isinstance(l[1],int): task_list.append(Task(l[0],l[1]))
    else:
        time_length=l[1:]
        event=Event(l[0],*time_length)
        event_list.append(event)
#sorts lists in total_list into either tasks or events
event_list.sort(key=lambda x:x.start_time.as_int)
#sorts event_list by the start times

for c in range(len(event_list)-1):
    if (event_list[c].end_time.as_int>event_list[c+1].start_time.as_int):
        raise Exception("event times have overlap")

#change below somehow
empty_time_list=[start_bound]
for e in event_list:
    empty_time_list.append(e.start_time)
    empty_time_list.append(e.end_time)
empty_time_list.append(end_bound)
#empty_time_list is a list of times

gaps_list=[]
counter=0
while counter<len(empty_time_list)-1:
    empty_start=empty_time_list[counter]
    empty_end=empty_time_list[counter+1]
    empty_event=Event("gap",empty_start,empty_end)
    gaps_list.append(Gap(empty_event.diff,copy.deepcopy(empty_start)))
    counter+=2

big_tasks=[]
for task in task_list:
    inserted=False
    for g in gaps_list:
        if task.time<=g.time_available:
            g.insert(task)
            inserted=True
            break
    if not inserted: big_tasks.append(task)

for gap in gaps_list:
    start_time=gap.start_time
    #perhaps add buffer here?
    for t in gap.task_list:
        event_list.append(Event(t.name,copy.deepcopy(start_time),t.time))
        start_time+t.time
event_list.sort(key=lambda x:x.start_time.as_int)

for e in event_list:
    print(e.name,e)
