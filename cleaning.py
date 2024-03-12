type_vehic = [
    "price",
    "vehicle_type",
    "registration_year",
    "gearbox",
    "model",
    "fuel_type",
    "brand",
]

# def imput_kNN(df : pd.DataFrame, n:int,  k : int, features : list):

# n=
# k=
# features=
df = data

# Limpieza de datos exclusiva
categoric = ["vehicle_type", "gearbox", "model", "fuel_type", "brand"]
df_clean = df.dropna(axis=0, how="any")
df_clean = df_clean[features]
df_encoded = pd.get_dummies(df_clean, columns=categoric, drop_first=True)
scaler = MinMaxScaler()
df_final = scaler.fit_transform(df_encoded)
display(df_final)

nbrs = sklearn.neighbors.NearestNeighbors(n_neighbors=k)
nbrs.fit(df_final)

indices = nbrs.kneighbors([df_final.iloc[n][features]], k, return_distance=False)


#    return indices
