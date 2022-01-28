#１．入力したキーワードで、キャラクターリスト(source)を検索して、存在すれば存在する旨を、存在しなければ存在しない旨をPrint文で表示してみましょう
#２．１に追加して結果が存在しなかった場合に、キャラクターリスト(source)に追加できるようにしてみましょう
#３．２に追加してキャラクターリスト(source)をCSVから読み込んで登録できるようにしてみましょう
#４．３に追加してキャラクターリスト(source)をCSVに書き込めるようにしてみましょう
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
# source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]
import csv
import pandas as pd

# filename = 'CharacterList.csv'C:\Users\handb\Desktop\PythonProject\issue1\
df = pd.read_csv("C:/Users/handb/Desktop/PythonProject/issue1/CharacterList.csv", sep=",",  encoding="utf8")
source = df['name'].tolist()
print(source)

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in source:
        print("{}が見つかりました".format(word))
    else:
        print("{}が見つかりませんでした".format(word))
        source.append(word)
        df.loc[word, 'name'] = word
        df.to_csv("C:/Users/handb/Desktop/PythonProject/issue1/CharacterList.csv",index=False, encoding='utf8')
        print("{}を追加しました".format(word))
        print(source)


if __name__ == "__main__":
    search()
