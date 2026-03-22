class Feature:
    def __init__(self, index, description):
        self.id = index
        self.description = description

    def __str__(self):
        return "Feature #" + str(self.id) + ": " + self.description