from abc import ABC, abstractmethod


# interface
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount: int) -> None:
        pass


class StripePayment(PaymentGateway):

    def pay(self, amount: int) -> None:
        print(f"paying {amount} via stripe")


class PaypalPayment(PaymentGateway):

    def pay(self, amount: int) -> None:
        print(f"paying {amount} via Paypal")



class PaymentFactory:

    _gateways: dict[str, PaymentGateway] = {
        "paypal" : PaypalPayment(),
        "stripe" : StripePayment()
    }

    @staticmethod
    def getPaymentGateway(paymentType: str) -> PaymentGateway:
    
        try: 
            return PaymentFactory._gateways[paymentType]
        except KeyError:
            raise ValueError("Unsupportedpayment type")
    

if __name__ == "__main__" :
    
    payment_gateway = PaymentFactory.getPaymentGateway("stripe")
    payment_gateway.pay(1000)
