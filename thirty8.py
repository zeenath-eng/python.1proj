class OttSubscription:
    def __init__(self,id,plan,payment):
        self.id=id
        self.plan=plan
        self.payment=payment

    def subscribe(self):
        print(f"subscriber with{self.id} is subscribed to {self.plan}plan ")
    def unsubscribe(self):
        print(f"subscriber with{self.id} is unsubscribed to{self.plan}plan ")

class Premium(OttSubscription):
    def __init__(self,id,plan,payment,screens):
        super().__init__(id, plan, payment)
        self.screens=screens

    def max_screen(self,screens):
        self.screens = screens
        print(f"maximum screen set to {self.id} in premium plan ")

myott=OttSubscription(2,"quater",100)
print(myott.plan)
myott.subscribe()
myott.unsubscribe()