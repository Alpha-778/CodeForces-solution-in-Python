class Doubler:
    def process(self, value):
        result = value * 2
        print(result)
class Application:
    def __init__(self):
        self.doubler = Doubler()
    def run(self):
        test_cases = int(input())
        for _ in range(test_cases):
            number = int(input())
            self.doubler.process(number)
if __name__ == "__main__":
    app = Application()
    app.run()