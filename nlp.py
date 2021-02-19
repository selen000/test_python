"""
自然言語処理ことはじめ
- つくりたいもの
 - 文章をしっかり管理できるツールを作成したい
"""
import yaml

from janome.tokenizer import Tokenizer

tokenizer = Tokenizer()

def keitaiso(sentenses):
    """
    形態素解析
    sentences : sentenceのリスト
    """
    for sentence in sentenses:
        print(sentence)
        for token in tokenizer.tokenize(data):
            print("    " + str(token))



if __name__ == __name__ == '__main__':

    with open('setting.yaml', "r", encoding='utf8') as file:
        config = yaml.safe_load(file.read())


    # 設定情報取得
    file_name = config["file_name"]
    file_path = config["file_path"]

    # 文章取得
    f = open(file_name, 'r')
    data = f.read()
    f.close()


    sentences = [data]
    # 形態素解析
    keitaiso(sentences)



