class encounter:
    def __init__(self, description, options, results):
        self.description = description
        self.optons = options
        self.results = results
    def spawned(self):
        print(self.description)
        for i in self.optons:
            print(i)
    def action(self, actionn):
        act = actionn.lower()
        if act not in self.optons:
            print("sorry the action you have typed is not available")
        else:
            idx = self.optons.index(act)
            print(self.results[idx])
#golbil = encounter("A horde of goblins leap out of the forest attaacking you", ["fight", "run", "hide"], ["You manage to fight them off, -5 hp", "You manage to get away saftley", "you hide but they spot you"])
#golbil.spawned()
#player = input("what would you like to do: ")
#golbil.action(player)