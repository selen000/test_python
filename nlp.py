"""
自然言語処理ことはじめ
- 文章いれたら出現数 名詞top100を可視化する
"""
import yaml
import collections
import pandas as pd
from janome.tokenizer import Tokenizer

tokenizer = Tokenizer()

def preprocess_(texts):
    """
    前処理

    :return:
    texts :前処理実行後のtext
    """
    # 改行除去
    texts = [text_.replace('\n', '') for text_ in texts]
    return texts


def keitaiso(sentenses):
    """
    形態素解析
    sentences : sentenceのリスト
    """
    word_list = []
    for sentence in sentenses:
        for token in tokenizer.tokenize(data):
            split_token = token.part_of_speech.split(',')
            ## 一般名詞を抽出する
            if split_token[0] == '名詞':
                word_list.append(token.surface)
            else:
                pass

    return word_list

def count_word_to_df(word_list):
    """
    単語のリストを集計してpandasDataFrameとして返却する

    :param word_list:
    :return: df
    """

    c = collections.Counter(word_list)
    df = pd.DataFrame.from_dict(c, orient='index')
    df.columns = ["count"]

    return df


if __name__ == __name__ == '__main__':

    with open('setting.yaml', "r", encoding='utf8') as file:
        config = yaml.safe_load(file.read())


    # 設定情報取得
    file_name = config["file_name"]
    file_path = config["file_path"]

    # 文章取得
    f = open(file_path + file_name, 'r')
    data = f.read()
    f.close()
    # リスト化
    sentences = [data]

    # 前処理
    sentences = preprocess_(sentences)

    # 形態素解析 名詞だけのリストを取得する
    word_list = keitaiso(sentences)

    # リストの中のものを集計する処理
    print("集計対象の単語母集団:",len(word_list))

    df = count_word_to_df(word_list)


    print(df)

    # 不要語
    # tf-idfによる頻度解析
    # 可視化

    # 特定の品詞だけ抽出する






