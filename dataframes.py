import pandas as pd

class Display:

    # To display top number of lines as output
    @staticmethod
    def toprows(df, num):
        print(df.head(num))

    # To display first number of columns
    @staticmethod
    def firstcolumns(df, num):
        print(df.iloc[:, :num])
