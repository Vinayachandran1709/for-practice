class Car:
    def __init__(self, model, year, color, for_sale):
        #in this model, year, color are attributes
        #self is pre built all the other 4 are given by us. Also learn why are we doing like this def __init__(self,
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You are driving a {self.color} colored {self.model} made in the {self.year}")
        #you can't just say model in the bracket you have to say self.model

    def stop(self):
        print(f"You are stopping a {self.color} colored {self.model} made in the {self.year}")