import time

class StopTimer:
    def __init__(self, timeout_seconds=10 * 60, iterations=100):
        self.timeout_seconds = timeout_seconds
        self.iterations = iterations
        self.reset()

    @property
    def epoch(self):
        return self.iteration

    def reset(self):
        self.start_time = None
        self.iteration = 0

    def tick(self):
        if self.start_time is None:
            self.start_time = time.time()
        self.iteration += 1
        
    def is_done(self):
        if self.start_time is None:
            raise Exception("has to run tick first")
        return self.iterations <= self.iteration \
            or self.timeout_seconds <= (time.time() - self.start_time)
