import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn import preprocessing

def my_bar_plot(df, target_x, target_y):
    """
    棒グラフ可視化用関数
    :param
    df: 可視化対象のDataFrame
    target_x : x軸のカラム名
    target_y : y軸のカラム名
    :return:
    """
    sns.barplot(x=target_x, y=target_y, data=df)
    plt.show()

def my_count_plot(df, target_x):
    """
    ヒストグラムを作成する
    :param df:　集計対象のPandasDataFrame
    :param target_x: 集計対象のカラム名
    :return:
    """
    sns.countplot(x=target_x, data=df)
    plt.show()

def my_box_plot(df, target_x, target_y, target_hue=None):
    """
    箱ひげ図可視化
    :param df:
    :param target_x:
    :param target_y:
    target_hue : 区分値
    :return:
    """
    ax = sns.boxplot(x=target_x, y=target_y, data=df, hue=target_hue)
    plt.show()


def my_preprocess_(df):
    """
    データ前処理まとめ
    :param df:
    :return:
    """

    # 欠損値補間 0埋め
    df = df.fillna(0)

    # データの正規化
    ss = preprocessing.StandardScaler()
    df = ss.fit_transform(df)
    return df



if __name__ == '__main__':

    # テスト用のDataはタイタニックを使用
    df = sns.load_dataset("titanic")

    # 可視化テスト用
    #my_bar_plot(df, target_x="class", target_y="age")
    #my_count_plot(df,target_x="class")
    my_box_plot(df, target_x="sex", target_y="age", target_hue="class")

    



