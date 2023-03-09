import pandas


class Definition:
    def __init__(self, term):
        self.term = term

    def get(self):
        df = pandas.read_csv('data.csv')
        result = tuple(df.loc[df['word'] == 'acid']['definition'])
        return result


if __name__ == '__main__':
    sun = Definition('sun')
    print(sun.get())
