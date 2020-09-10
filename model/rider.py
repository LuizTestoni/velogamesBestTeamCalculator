class Rider:
    def __init__(self, name, team, class_, points, cost, ratio):
        self.name = name
        self.team = team
        self.class_ = type
        self.points = points
        self.cost = cost 
        self.ratio = ratio

    def __init__(self, name, team, class_, points, cost):
        self.name = name
        self.team = team
        self.class_ = class_
        self.points = points
        self.cost = cost 
        self.ratio = points/cost
