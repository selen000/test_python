import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

def func_correlogram(df):
    """
    コレログラム
    """
    # 自己相関のコレログラム
    fig = plt.figure(figsize=(18, 8))
    ax1 = fig.add_subplot(211)
    fig = sm.graphics.tsa.plot_acf(df, lags=40, ax=ax1)
    # 偏自己相関のコレログラム
    ax2 = fig.add_subplot(212)
    fig = sm.graphics.tsa.plot_pacf(df, lags=40, ax=ax2)
    plt.show()



def func_box_plot(df, target_x, target_y):
    """
    箱ひげ図作成用関数
    target_x : x軸カラム名
    target_y : y軸カラム名
    """
    plt.figure(figsize=(10, 10))
    ax = sns.boxplot(x=target_x, y=target_y, data=df)

    ax.set_title("boxplot : {}_{}".format(target_x, target_y), fontsize=20)
    ax.tick_params(labelsize=20)
    plt.show()


def func_swarm_plot(df,target_x, target_y):
    """
    Swarmplot作成用関数
    target_x : x軸カラム名
    target_y : y軸カラム名
    """
    plt.figure(figsize=(10, 5))
    ax = sns.swarmplot(x=target_x, y=target_y, data=df)
    ax.set_title("swarmplot : {}_{}".format(target_x,target_y), fontsize=20)
    ax.tick_params(labelsize=20)
    plt.show()


def func_count_plot(df, target_x):
    """
    df : 棒グラフの集計
    target_x : x軸カラム名
    """
    plt.figure(figsize=(10, 10))
    ax = sns.countplot(x=target_x,data=df)
    ax.set_title("countplot : {}".format(target_x), fontsize=20)
    ax.tick_params(labelsize=20)
    plt.show()


def clusterring_scatter(df, target_x, target_y):
    """
    clusterカラムと、二次元の特徴量を持ったデータフレームをクラスタごとに、散布図
    :param df:
    :return:
    """
    plt.figure(figsize=(6, 6))
    for cluster in df["cluster"].unique():
        tmp_df = df[df["cluster"] == cluster]
        plt.scatter(tmp_df[target_x], tmp_df[target_y], alpha=0.8)
    plt.show()
