import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

def bool_to_int(X):
    return X.fillna(False).astype(int)

class THIFeatureCreator(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.temperature_median_ = None
        self.humidity_median_ = None
        self.feature_names_ = ["Temperature", "Humidity(%)", "THI"]

    def fit(self, X, y=None):
        self.temperature_median_ = X["Temperature"].median()
        self.humidity_median_ = X["Humidity(%)"].median()
        return self

    def transform(self, X):
        X = X.copy()
        X["Temperature"] = X["Temperature"].fillna(self.temperature_median_)
        X["Humidity(%)"] = X["Humidity(%)"].fillna(self.humidity_median_)

        thi = (
            0.8 * X["Temperature"]
            + (X["Humidity(%)"] / 100)
            * (X["Temperature"] - 14.4)
            + 46.4
        )

        return pd.DataFrame(
            {
                "Temperature": X["Temperature"],
                "Humidity(%)": X["Humidity(%)"],
                "THI": thi,
            },
            index=X.index
        )

    def get_feature_names_out(self, input_features=None):
        return self.feature_names_


class GoodWeatherFeatureCreator(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.snowfall_mode_ = None
        self.rainfall_mode_ = None
        self.feature_names_ = ["Rainfall(mm)", "Snowfall (cm)", "Good_Weather"]

    def fit(self, X, y=None):
        self.rainfall_mode_ = X["Rainfall(mm)"].mode(dropna=True).iloc[0]
        self.snowfall_mode_ = X["Snowfall (cm)"].mode(dropna=True).iloc[0]
        return self

    def transform(self, X):
        X = X.copy()
        X["Rainfall(mm)"] = X["Rainfall(mm)"].fillna(self.rainfall_mode_)
        X["Snowfall (cm)"] = X["Snowfall (cm)"].fillna(self.snowfall_mode_)

        good_weather = (
            (X["Rainfall(mm)"] == 0)
            & (X["Snowfall (cm)"] == 0)
        ).astype(int)

        return pd.DataFrame(
            {
                "Rainfall(mm)": X["Rainfall(mm)"],
                "Snowfall (cm)": X["Snowfall (cm)"],
                "Good_Weather": good_weather,
            },
            index=X.index
        )

    def get_feature_names_out(self, input_features=None):
        return self.feature_names_
