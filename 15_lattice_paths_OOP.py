"""The number of routes for a grid follows the central binomial coefficients (the numbers down the center of Pascal's Triangle)
The fastest way to get this value is by using (2*n)!/n!^2"""

class Grid:
    def __init__(self, sides):
        self.sides = sides
        
    def get_numerator_factorial(self):
        base_num = 1
        max_num = self.sides * 2
        factors = []
        
        for i in range(1, (max_num + 1)):
            base_num = base_num * i
        factors.append(base_num)
        numerator = factors[0]
        return numerator
            
    def get_denominator_factorial(self):
        base_num = 1
        max_num = self.sides
        factors = []
        
        for i in range(1, max_num + 1):
            base_num = base_num * i
        factors.append(base_num)
        denominator = factors[0]
        return denominator
            
    def calculate_routes(self):      
        result = int(self.get_numerator_factorial()/(self.get_denominator_factorial()**2))
        return result
        
    def output(self):
        print("The number of routes for a " , new_grid.sides, " by " , new_grid.sides, " grid is: ", new_grid.calculate())
        
new_grid = Grid(20)
new_grid.output()

#The number of routes for a  20  by  20  grid is:  137846528820
