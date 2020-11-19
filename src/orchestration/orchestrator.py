class Orchestrator():
    def __init__(self, sportsbooks):
        self.sportsbooks = sportsbooks

    def orchestrate(self):
        for book in self.sportsbooks:
            book.retrieve_nfl_data_frame()
            print(book)

