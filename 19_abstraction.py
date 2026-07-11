   # Abstractions in python programing 
from abc import ABC, abstractmethod;

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    
class Bicycle(Vehicle):
    
    def start(self):
        print("Bicycle starting ....!");
        
        
bic = Bicycle();
bic.start();