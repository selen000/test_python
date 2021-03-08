import pandas as pd
import numpy as np
import configparser

import seaborn as sns
from sklearn.cluster import KMeans
import my_plotting as m_plot
import my_func as m_func

def my_k_means(df, n):
    """

    :param df:
    :return:
    labels クラスタリング結果のラベル
    """
    kmeans_model = KMeans(n_clusters=n, random_state=10).fit(df)
    # 分類結果のラベルを取得する
    labels = kmeans_model.labels_
    return kmeans_model, labels

if __name__ == '__main__':

    # 設定情報読み込み
    ini = configparser.ConfigParser()
    ini.read('./setup.ini', 'UTF-8')

    input_file_path = ini["FILE_PATH"]["CSV_FILE_PATH"]
    input_file_name = ini["FILE_PATH"]["FILE_NAME"]
    output_file_path = ini["FILE_PATH"]["OUTPUT_FILE_PATH"]

    # テスト用のDataはタイタニックを使用
    #df = sns.load_dataset("iris")
    df = pd.read_csv(input_file_path + input_file_name)

    # 学習用データフレーム作成
    # ToDo ここ特徴量はconfigから取得する仕組みにする
    df_ = df.iloc[:, 0:4]

    # データ処理
    df_ = m_func.my_preprocess_(df_)

    # 学習
    k_means_model, labels = my_k_means(df_, 3)

    # ラベルを付与する
    df["cluster"] = labels

    # 可視化対象
    target_x = df.columns[0]
    target_y = df.columns[1]

    # クラスタの分布
    sns.countplot(x="cluster", data=df)

    # クラスタごとに色分けされた散布図
    m_plot.clusterring_scatter(df,target_x, target_y)

    # 特徴量の散布図を可視化
    # クラスタごとの特徴量を箱ひげ図として可視化
    m_func.my_box_plot(df, df["cluster"], target_y, target_hue="cluster")







