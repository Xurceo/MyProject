class Feature:
    def __init__(self, index, description):
        self.Id = index
        self.Description = description

    def __str__(self):
        return "Feature #" + str(self.Id) + ": " + self.Description