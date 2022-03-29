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

input="chinese 60 lunch 30 whap 30 english 20"
clean=input.split()
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
t=Time().calc_next_fifteen()
break_time=10
for l in total_list:
    if len(l)==2:
        if l[1].isdecimal():
            before=copy.deepcopy(t)
            t+int(l[1])
            print(f'{l[0]}: {before} - {t}')
            t+break_time
        else:
            initial,final=l.split("-")
#TODO have a way to make events? and then somehow fill in the space
#calculate the space in between events.
#add way to identify days

#school 6:30-7:00 band 8:00-9:00
#calculate now to school, and then school to band
#uploaded to github!!!! poggies :))))))))
#havish and jeff helping me rn, screensharing to them!
# hashtag fun times with friends!