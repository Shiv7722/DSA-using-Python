import time
import math

class TimerError(Exception):
    """Timer misuse error: timer has been started twice or stopped before starting."""

class Timer:
    def __init__(self):
        self.start_time=None
        self.elapsed_time=None
    
    def start(self):
        if(self.start_time==None):
            self.start_time=time.perf_counter()
        else:
            raise TimerError("Timer has been running already, cannot start new untill stopped")
        
    def stop(self):
        if(self.start_time==None):
            raise TimerError("Please start the timer first")
        else:
            self.elapsed_time=time.perf_counter()-self.start_time
            self.start_time=None

    def elapsed(self):       
        return self.elapsed_time
    
    def __str__(self):
        return str(self.elapsed_time)