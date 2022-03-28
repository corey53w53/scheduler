import time
import copy
class Time:
    def __init__(self,hour=time.localtime().tm_hour,min=time.localtime().tm_min):
        assert(0<=hour<24)
        assert(0<=min<60)
        self.hour=hour
        self.min=min
    def __str__(self,military=False):
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
        return self.hour*60+self.sec
    def difference(self,t2):
        return abs(self.to_int()-t2.to_int())

class Event(Time):
    def __init__(self, *args):
        if len(args)==1:
            start,end=args[0].split("-")
            self.start_hour,self.start_min=start.split(":")
            self.end_hour,self.end_min=end.split(":")
            self.start_time=Time(int(self.start_hour),int(self.start_min))
            self.end_time=Time(int(self.end_hour),int(self.end_min))
        elif len(args)==2:
            start=args[0]
            self.start_hour,self.start_min=start.split(":")
            self.start_time=Time(int(self.start_hour),int(self.start_min))
            inc=int(args[1])
            self.end_time=copy.deepcopy(self.start_time)
            self.end_time+inc
    def __str__(self):
        return f'{self.start_time} - {self.end_time}'
user_input="school 6:30-14:30 math 15:00 30"
clean=user_input.split()
counter=0
total_list=[]
while counter<len(clean):
    if clean[counter].isalpha():
        smaller_list=[clean[counter]]
        counter+=1
        while not clean[counter].isalpha():
            smaller_list.append(clean[counter])
            counter+=1
            if counter==len(clean):
                break
    total_list.append(smaller_list)
print(total_list)
# input1=["5:30-5:45"]
# input2=["3:30","15"]
# event_list=[]
# i1=Event(*input1)
# i2=Event(*input2)
# event_list.append(i1)
# event_list.append(i2)
# for i in event_list:
#     print(i)