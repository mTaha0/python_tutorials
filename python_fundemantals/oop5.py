class Math:

    @staticmethod
    def sum(x):
        return x + 5
    
    @staticmethod
    def abs(x):
        if x >= 0:
            return x
        else:
            x = -x
            return x

print(Math.sum(5))