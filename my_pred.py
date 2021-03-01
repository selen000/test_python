# データを居れたら決定木で予測してくれるようなものを作りたい
from sklearn import tree
from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sns


def _preprocess(df):
    """
    前処理用関数
    :return:
    """
    df["age"] = df["age"].fillna(df["age"].median())

    df["sex"][df["sex"] == "male"] = 0
    df["sex"][df["sex"] == "female"] = 1

    #df["Embarked"][df["Embarked"] == "S"] = 0
    #df["Embarked"][df["Embarked"] == "C"] = 1
    #df["Embarked"][df["Embarked"] == "Q"] = 2
    #df.fare[152] = df.fare.median()

    # テストデータと訓練データに分割する
    train_df, test_df = train_test_split(df, test_size=0.3)



    # 「train」の目的変数と説明変数の値を取得
    target = train_df["survived"].values
    features_one = train_df[["pclass", "sex", "age", "fare"]].values
    return target, features_one, train_df, test_df






if __name__ == '__main__':

    # テスト用のDataはタイタニックを使用
    df = sns.load_dataset("titanic")

    # 前処理
    target, features_one, train_df, test_df = _preprocess(df)

    # 決定木作成
    my_tree_one = tree.DecisionTreeClassifier()
    my_tree_one = my_tree_one.fit(features_one, target)

    test_features = test_df[["pclass", "sex", "age", "fare"]].values

    # 「test」の説明変数を使って「my_tree_one」のモデルで予測
    my_prediction = my_tree_one.predict(test_features)

    print(my_prediction)
