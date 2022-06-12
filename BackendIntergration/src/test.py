import pandas as pd

# print(str(pd))

def somestuff():
    data = [['tom', 10], ['nick', 15], ['juli', 14]]
    df = pd.DataFrame(data, columns=['Name', 'Age'])
    return str(df)


# print(somestuff())