def bool_to_int(X):
    return X.fillna(False).astype(int)