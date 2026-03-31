from engine.data import load_hist_data

data = load_hist_data(save_csv=True)
print(data.head())
print(data.columns)