import time

time.start = time.time()

class Data:
    class Interaction:
        data = []

        def add(self, value):
            self.data.append({
                "time": time.time() - time.start,
                "value": value
            })

        def get(self):
            exports = self.data
            self.data = []
            return exports

    commands  = Interaction()
    state = Interaction()


game = Data()
vision = Data()
