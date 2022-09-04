import time

class FiboIter():
    
    
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self
    
    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            # self.n1 = self.n2
            # self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux
        
        
if __name__ == "__main__":
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(2)

# 0 1 1 2