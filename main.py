def func_1():
    """
    test用スクリプト
    """
    print("hello")

def func_2(data):
    """
    入力した数値を10倍にする
    data int
    """
    data = data * 10
    return data

if __name__ == '__main__':
    # 関数1
    func_1()

    data = 10
    print(data)

    data = func_2(data)
    print(data)