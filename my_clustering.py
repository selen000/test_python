import pandas as pd
import numpy as np
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
    # テスト用のDataはタイタニックを使用
    df = sns.load_dataset("iris")

    # 学習
    k_means_model, labels = my_k_means(df.iloc[:, 0:4], 3)

    # ラベルを付与する
    df["cluster"] = labels
    target_x = df.columns[0]
    target_y = df.columns[1]

    # クラスタの分布
    sns.countplot(x="cluster", data=df)

    # クラスタごとに色分けされた散布図
    m_plot.clusterring_scatter(df,target_x, target_y)

    # 特徴量の散布図を可視化
    # クラスタごとの特徴量を箱ひげ図として可視化
    m_func.my_box_plot(df, df["cluster"], target_y, target_hue="cluster")







