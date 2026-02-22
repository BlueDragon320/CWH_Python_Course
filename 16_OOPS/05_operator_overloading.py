class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def sum(self, p):
        return Point((self.x + p.x), (self.y + p.y))
    def print_pt(self):
        print(f"X = {self.x}\nY = {self.y}")
        
p1 = Point(3, 2)
p2 = Point(6, 3)

p=p1.sum(p2)

p.print_pt()