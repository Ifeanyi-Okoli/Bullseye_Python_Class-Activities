
class StreamVideo:
    def __init__(self) -> None:
        self.isComplete = False

    def start(self):
        self.isComplete = True
        return "Video started"

    def stop(self):
        self.isComplete = False
        return "Video stopped"

    def pause(self):
        self.isComplete = False
        return "Video paused"

    def resume(self):
        self.isComplete = True
        return "Video resumed"