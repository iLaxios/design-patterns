from abc import ABC, abstractmethod
# from typing import Tuple

# observer
class Inverstor(ABC):

    @abstractmethod
    def receiveUpdate(self, stock: str, value: float) -> None:
        pass


# notifier
# notifier will have the data, and notify the subscribers
# observers will subscribe to data, notifier will update them
class StockMarket:

    def __init__(self):
        self.stocks: dict[str, float]  = {}
        self.investors: list[Inverstor]  = []

    def addInvestor(self, invester: Inverstor) -> None:
        self.investors.append(invester)
    
    def removeInvestor(self, invester: Inverstor) -> None:
        self.investors.remove(invester)
    
    def updateStock(self, stock: str, value: float) -> None:
        self.stocks[stock] = value

        # update investors
        for investor in self.investors:
            investor.receiveUpdate(stock, value)

class PhoneInvestor(Inverstor):

    def __init__(self, name: str):
        self.name = name

    def receiveUpdate(self, stock: str, value: float) -> None:
        print(f"Hey {self.name}, new stock update: {stock} :  {value}")


if __name__ == "__main__":

    alexInvestor = PhoneInvestor("Alex")
    robInvestor = PhoneInvestor("Rob")

    sm = StockMarket()

    sm.addInvestor(alexInvestor)
    sm.addInvestor(robInvestor)

    sm.updateStock("NVDA", 100.12)
    sm.updateStock("TSLA", 5.97)

        
