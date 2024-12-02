class Day1:
    def __init__(self):
        with open ('input1.txt', 'r') as f:
            lines = f.readlines()
            self.col1 = [x.strip('\n').split('   ')[0] for x in lines]
            self.col2 = [x.strip('\n').split('   ')[1] for x in lines]

    def part_one(self):
        return sum([abs(int(b) - int(a)) for a, b in zip(sorted(self.col1), sorted(self.col2))])
    
    def part_two(self):
        return sum([int(x) * int(self.col2.count(x)) for x in self.col1])

    

if __name__ == '__main__':
    x = Day1()
    print(x.part_two())
