class Trigger:
    def triggerError():
        def inner():
            return 3/0
        return inner()

