#import tensorflow 
from typing import Any
import numpy as np
import pandas as pd
from pandas._libs.missing import NA

class Query():
    def __init__(self, filename) -> None:
        self.df = pd.read_csv(filename)
        self.df.fillna(value=0.0,inplace=True)

    def __repr__(self) -> str:
        noZeroStartIndex = 0
        noZeroEndIndex = str(self.df.size - 1)
        i = 0
        for label, content in self.df.items():
            for index, value in content.items():
                
                if value != 0.0:
                    i = index
                    break
            if i > noZeroStartIndex: noZeroStartIndex = i

        for label, data in reversed(list(self.df.iterrows())):
            print(data)
            for index, value in data.items():
                
                if value != 0.0:
                    i = index
                    break
            if i < noZeroEndIndex: noZeroEndIndex = i
        
        return repr(self.df.loc[noZeroStartIndex:noZeroEndIndex])

if __name__ == '__main__':
    filename = 'Sample datasets\PP_DER.csv'
    query = Query(filename)
    print(query)

# def mask(df, f):
#   return df[f(df)]
# Then you can do stuff like:

# df.mask(lambda x: x[0] < 0).mask(lambda x: x[1] > 0)