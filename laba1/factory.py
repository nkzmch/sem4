from workers import Workers

class Factory:
    def __init__(self, workers: Workers) -> None:
        self.workers = workers

    def number_of_workers(self) -> None:
        print("Number of workers:", self.workers.number)

    def work(self) -> None:
        print("We are working")
