#import tensorflow 
from typing import Any
import pandas as pd

class Query():
    def __init__(self, filename) -> None:
        self.df = pd.read_csv(filename, na_values='')
        self.df.fillna(value=0.0, inplace=True)

    def __repr__(self) -> str:
        noZeroStartIndex = 0
        for label, content in self.df.items():
            for index, value in content.items():
                if value != 0.0:
                    i = index
                    break
            if i > noZeroStartIndex: noZeroStartIndex = i

        return repr(self.df.loc[noZeroStartIndex:])

if __name__ == '__main__':
    filename = 'Sample datasets\PP_DER.csv'
    query = Query(filename)
    print(query)
