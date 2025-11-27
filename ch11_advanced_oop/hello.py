class Hello(object):
    def hello(self, name='world'):
        print(f"Hello, {name}")

if __name__ == "__main__":
    h = Hello()
    h.hello('Zane')