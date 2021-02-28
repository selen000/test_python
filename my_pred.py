# データを居れたら決定木で予測してくれるようなものを作りたい
from sklearn import tree
import seaborn as sns


def _preprocess(df):
    """
    前処理用関数
    :return:
    """
    # 「train」の目的変数と説明変数の値を取得
    target = df["survived"].values
    features_one = df[["pclass", "sex", "age", "fare"]].values

    return target, features_one






if __name__ == '__main__':

    # テスト用のDataはタイタニックを使用
    df = sns.load_dataset("titanic")
    print(df)


    target_df,features_one = _preprocess(df)

    print(target_df)
    print("-"*30)
    print(features_one)
