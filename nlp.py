"""
自然言語処理ことはじめ
- つくりたいもの
 - 文章をしっかり管理できるツールを作成したい
"""

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
    # Todo ファイル名称config化
    file_name = "aaa.txt"

    # Data読み込み
    f = open('aaa.txt', 'r')
    data = f.read()
    f.close()

    sentences = [data]

    # 形態素解析
    keitaiso(sentences)


