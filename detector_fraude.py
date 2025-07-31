import pandas as pd
import kagglehub 

#Charging the data
path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")
df = pd.read_csv(f"{path}/creditcard.csv")  
print(df.head())
