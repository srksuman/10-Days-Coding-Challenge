class AgeException(Exception):
    def __init__(self) -> None:
        super().__init__("Age below 18 cannot vote!")

class Voting:
    def __init__(self,age) -> None:
        self.__age = age
    
    def checkAge(self):
        if self.__age<18:
            raise AgeException
        else:
            print("You have right to vote")

vote = Voting(2)
vote.checkAge()
