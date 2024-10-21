from schedule import Schedule

class Population(object):
    def __init__(self, size, data):
        self.schedules = [Schedule(data).initialize() for _ in range(size)]

    def __str__(self):
        return "".join([str(x) for x in self.schedules])

    def sort_by_fitness(self):
        # Sort schedules by fitness in descending order
        self.schedules = sorted(self.schedules, key=lambda schedule: schedule.fitness, reverse=True)
        
        return self
