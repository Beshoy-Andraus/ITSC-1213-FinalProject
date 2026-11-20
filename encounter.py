class encounter:
    def __init__(self, description, options, results):
        self.description = description
        self.optons = options
        self.results = results
    def spawned(self):
        print(self.description)
        print(self.options)
    