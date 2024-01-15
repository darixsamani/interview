

class Gen:

    start : int
    step: int

    def __init__(self, start, step) -> None:
        self.start = start
        self.step = step
    
    # def __next__(self):
    #     while True:

    #         yield self.start
    #         self.start = self.start + self.step4

    def __iter__(self):
        while True:
            yield self.start
            self.start = self.start + self.step


    def __enter__(self):
        print("strating...")
        return self
    

    def __exit__(self, *exc):
        print("end...")



with Gen(2,4) as gen:
    i = iter(gen)
    for _ in  range(4):
        print(next(i))
        
        