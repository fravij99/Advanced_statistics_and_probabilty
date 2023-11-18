
import pandas as pd
import numpy as np
from scipy.stats import trim_mean
from statsmodels import robust
import seaborn as sns
import matplotlib.pylab as plt


# importiamo i dati
airlines = pd.read_csv("https://github.com/SZapperi/CorsoProbabilitaStatistica/raw/master/data/airline_stats.csv")
# apriamo il file (le prime 8 righe)
print(airlines.head(8)) 

airlines["airline"].unique()

(airlines['carrier_delay'].mean())


medie=airlines.groupby("airline").mean()
dev_standard=airlines.groupby("airline").std()

print(medie)