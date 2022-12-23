from temperature import Temperature

class Calorie:
    '''
    Represesnt teh amount of calories calculated with
    BMR = 10 x weight + 6.5 x height - 5 x age - 10 x temperature
    '''

    def __init__(self, weight, height, age, temperature):
        self.weight = float(weight)
        self.height = float(height)
        self.age = float(age)
        self.temperature = float(temperature)

    def calculate(self):
        result = 10*self.weight + 6.5*self.height - 5*self.age - 10*self.temperature
        return result


if __name__ == '__main__':
    temperature = Temperature(country='hong-kong', city='').get()
    calorie = Calorie(temperature=temperature, weight=85, height=180, age=26)
    print(calorie.calculate())