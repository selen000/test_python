# 時系列分析用
# とりあえずSARIMA実装

import configparser
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import my_plotting as m_plot

def preprocess_(df):
    """
    前処理用関数
    :return:
    """
    return df

def sarima_learning(df):
    """
    # SARIMAモデル　学習用関数
    :return:
    """
    return sm.tsa.SARIMAX(df, order=(3, 1, 2), seasonal_order=(1, 1, 1, 12)).fit()


if __name__ == '__main__':

    # 設定情報読み込み
    ini = configparser.ConfigParser()
    ini.read('./setup.ini', 'UTF-8')

    #input_file_path = ini["FILE_PATH"]["CSV_FILE_PATH"]
    #input_file_name = ini["FILE_PATH"]["FILE_NAME"]
    #output_file_path = ini["FILE_PATH"]["OUTPUT_FILE_PATH"]
    input_file_name = './data/AirPassengers.csv'

    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
    df = pd.read_csv(input_file_name, index_col='Month', date_parser=dateparse, dtype='float')

    # 周期性確認用にコレログラム可視化
    m_plot.func_correlogram(df)

    # 前処理
    df = preprocess_(df)

    # 学習
    SARIMA_3_1_2_111 = sarima_learning(df)

    predict_start = "1960-01-01"
    predict_end = "1965-12-01"

    pred = SARIMA_3_1_2_111.predict(predict_start, predict_end)

    # 実データと予測結果の図示
    plt.plot(df, label="actual")
    plt.plot(pred, "r", label="predict")
    plt.legend()
    plt.show()


