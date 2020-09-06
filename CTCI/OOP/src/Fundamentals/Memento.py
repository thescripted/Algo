from abc import ABC, abstractmethod
from datetime import datetime

class Originator:
    _state = None
    
    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: My initial state is {self._state}")
    
    def do_something(self) -> None:
        print("Originator: I'm doing something")
        self._state = "ajbipoarh"
        print(f"Originator: state has changed to {self._state}")
    
    def save(self) -> Memento: 
        return ConcreteMemento(self._state)
    
    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")
    

class Memento(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    def get_date(self) -> str:
        pass

    
class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]
    
    def get_name(self) -> str:
        return f"{self._date} / ({self._state[0:9]}...)"
    
    def get_date(self) -> str:
        return self._date

    def get_state(self) -> str:
        return self._state


class CareTaker:
    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator
    
    def backup(self) -> None:
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return
        
        try:
            restore_memento = self._mementos.pop()
            self._originator.restore(restore_memento)
        except Exception: 
            self.undo()
    

if __name__ == "__main__":
    pass


