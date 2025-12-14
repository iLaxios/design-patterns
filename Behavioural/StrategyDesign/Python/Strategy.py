from abc import ABC, abstractmethod



class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount: int) -> None:
        pass


class UPIPaymentStrategy(PaymentStrategy):

    def pay(self, amount: int) -> None:
        print(f"Paying {amount} via UPI")


class PayPalPaymentStrategy(PaymentStrategy):

    def pay(self, amount: int) -> None:
        print(f"Paying {amount} via PayPal")


class StripePaymentStrategy(PaymentStrategy):

    def pay(self, amount: int) -> None:
        print(f"Paying {amount} via Stripe")

# context
class ShoppingCart:

    def __init__(self, strategy):
        self._paymentStrategy = strategy

    @property
    def paymentStrategy(self):
        return self._paymentStrategy

    @paymentStrategy.setter
    def paymentStrategy(self, strategy: PaymentStrategy):
        self._paymentStrategy = strategy

    def checkOut(self, amount: int) -> None:
            self._paymentStrategy.pay(amount)



cart = ShoppingCart(PayPalPaymentStrategy())
cart.paymentStrategy = StripePaymentStrategy()
cart.checkOut(1000)

cart.paymentStrategy = UPIPaymentStrategy()
cart.checkOut(5000)

