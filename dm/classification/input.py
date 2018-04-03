import numpy as np
import pandas as pd
input_file = {1:'student-mat.scv', 2:'student-por.scv'}

if __name__ == '__main__':
    data = pd.read_csv(input_file[1], header=None, na_values='?')
    print('hi')