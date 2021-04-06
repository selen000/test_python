#class Test:
#    pass # 何もしないクラス
class Test:
    member1 = 40 # メンバ変数の定義
    def __init__(self, num):
        # コンストラクタの定義 今回は引数としてnumを定義している
        self.num = num; # このクラスが持つnumというメンバ変数に引数のnumを格納する
    def __del__(self):
        print("デストラクタが呼ばれました")
    def method_1(self):
        """
        メソッドの作成
        """
        print("this is method_1")
    def method_print_num(self):
        print("引数で渡された変数numは{}です".format(self.num))
    def method_print_member(self):
        print(self.member1)
class Test2(Test): # Testクラスを継承する
    def print_test2_info(self):
        print("このクラスはTestクラスを継承しています")
        super().method_print_num() # 親クラス(Test)のmethod_print_numメソッドを呼ぶ
class Test3(): # Private検証用クラス
    def test_public(self):
        print("publicメソッドです")
        self.__test_private() # Privateメソッドは自分のクラス内部では呼べる
    def __test_private(self):
        print("privateメソッドです")
if __name__ == '__main__':
    num = 4
    test = Test(num) # インスタンス作成
    test.method_1() # メソッド呼び出し
    test.method_print_member() # メンバ呼び出し
    test.method_print_num() # コンストラクタに渡した引数の中身をprintするメソッド
    del test # デストラクタ呼ぶ (デストラクタは明示的に呼ばなくても自動的に呼ばれるっぽい)
    #test.method_print_num() # 当然ながらデストラクタで削除したインスタンスは実行できない
    # 継承
    test = Test2(10) # 継承しているので親クラスの引数numを指定し、インスタンスを作成する
    test.print_test2_info()
    # privateとpublic
    test = Test3()
    test.test_public()
    #test.__test_private() # これはエラーを吐く ---> Privateメソッドはクラスの外から呼べない
    # クラスとデストラクタ
    """
    # オブジェクト指向のクラスという概念
    - クラスとは「ある目的を持ったものの定義」つまり設計図
    - インスタンスとは、クラスをもとに実際に作成された実体
    - メンバとは、クラス内部で使用する変数
    # コンストラクタ
    - メソッドの中でもインスタンスが生成されるときに自動的に呼び出されるメソッドをコンストラクタと呼ぶ
    - コンストラクタの定義にはinitという名前のメソッドで定義される
    # デストラクタ
    - コンストラクタとは反対に、インスタンスが不要になり削除される時に呼ばれるメソッドをデストラクタと呼ぶ
    - デストラクタはdelという名前のメソッドで定義される
    # 継承
    - クラスを継承する場合は、クラス文に親となるクラスを指定する
    - 親のクラスのメソッドを呼び出す場合はsuper()を用いる
    # PrivateとPublicの指定
    - pythonではクラスのメンバ変数やメソッドの名前の前に__をつけることでprivateにできる
    - privateとはクラス内部でのみ干渉可能であるということ
    - 何もつけなければpublic, 
    - 具体的にはPrivateはインスタンス化した実体から直接呼ぶことが出来ない
    - クラス内のメソッドからのみ呼びだすことができる
    """