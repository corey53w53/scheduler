import time
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

t1=Time(4,30)
t2=Time(4,30)
print(t1==t2)