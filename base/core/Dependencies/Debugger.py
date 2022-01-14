class Debugger():
    debug = False

    def log(str: str):
        if Debugger.debug:
            print(str)