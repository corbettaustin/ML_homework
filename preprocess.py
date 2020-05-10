def prep_data(df):


    df = df.assign(farmers_measure=(df["Length2"] * df["Width"] * df["Width"] / 1200))

    X = df[["Width", "Length2", "farmers_measure"]].values
    y = df["Weight"].values

    return X, y