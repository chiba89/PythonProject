# ### この課題はマイナビにアクセスしてキーワード検索を行い結果を取得するものです。
# 当方のサンプルを用意していますので、追記する形で始めていただければと思います。
# 説明動画：https://youtu.be/vNJ5DcrdvhM<br>
# Seleniumの基本：https://techacademy.jp/magazine/28392<br>
# Seleniumの応用：https://tanuhack.com/selenium/#URL<br>
# Pandasの基本：https://note.nkmk.me/pandas/<br>
# ログ出力(テキストファイル出力)：https://note.nkmk.me/python-file-io-open-with/<br>
# サンプルコードは、検索結果の１番上の会社名を取得するようになっています。
# 下記の課題に従って、レベルアップさせてみましょう。
# Seleniumは副業案件においては、非常に重要な技術です。これを習得すれば月５万円程度の収入を得ることが可能です。
# 頑張って学習してみましょう！

# ## ０  難易度★☆☆☆☆
# Chromeのバージョンを、URLにchrome:://version と入力して確認し  
# これとメジャーバージョン（先頭の91等の数字）が一致するdriverを以下よりダウンロードしてください。  
# https://chromedriver.chromium.org/downloads

# ## １　難易度★★☆☆☆
# 会社名を取得して画面にprint文で表示してみましょう。
# ## １　難易度★☆☆☆☆
# サンプルでは会社名を含む情報を取得するようになっています。
# サンプルを実行して、会社名を含む情報をprintされることを確認してみましょう。

# ## ２　難易度★★★☆☆
# for文を使って、１ページ内の求人一覧を取得できるように改造してみましょう。
# また、会社名以外の項目として、求人タイトルも取得してください。
# 会社名以外の項目として、求人タイトルも取得できるようにしてみましょう。   
# ![画像](https://i.gyazo.com/4b86808ee00d8b28096fe7578b7f093a.png)

# ## ３　難易度★★★☆☆
# ２ページ目以降の情報も含めて取得できるようにしてみましょう

# ## ４　難易度★★☆☆☆
# 任意のキーワードをコンソール（黒い画面）から指定して検索できるようにしてみましょう
# サンプルでは、プログラム内で予め指定した文字列で検索するようになっていますが  
# これを、任意のキーワードをコンソール・ターミナル（黒い画面）から指定して検索できるようにしてみましょう  
# ※Hint: inputを使用すると簡単です  

# ## ５　難易度★★★★☆
# 取得した結果をpandasモジュールを使ってCSVファイルに出力してみましょう
# @@ -44,13 +42,6 @@ for文を使って、１ページ内の求人一覧を取得できるように
# ライブラリを用いることもできますが、テキストファイルを出力する処理で簡単に実現できるので、試してみましょう。
# (今何件目、エラー内容、等を表示)

# ## ８　難易度★☆☆☆☆
# Chromeドライバーがバージョンアップの際に自動で更新されるようにしてみましょう。  
# 参考：https://qiita.com/YoshikiIto/items/000f241f6d917178981c
    # driver = webdriver.Chrome(ChromeDriverManager().install())

# 以下は、オプション課題です。少し難易度が高いのでトライしたい方のみ<BR>
# 挑戦してみてください。

# ## オプション１ 難易度★★★★☆
# 検索時等にWeb画面を更新する処理はurlにより制御されます。
# そのため、検索窓を使用せずにURLを直接変更することでも検索結果を取得することが可能です。

#########

from asyncio.windows_events import NULL
import os
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Selenium4対応済

def set_driver(hidden_chrome: bool=False):
    '''
    Chromeを自動操作するためのChromeDriverを起動してobjectを取得する
    '''
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    options = ChromeOptions()

    # ヘッドレスモード（画面非表示モード）をの設定
    if hidden_chrome:
        options.add_argument('--headless')

    # 起動オプションの設定
    options.add_argument(f'--user-agent={USER_AGENT}') # ブラウザの種類を特定するための文字列
    options.add_argument('log-level=3') # 不要なログを非表示にする
    options.add_argument('--ignore-certificate-errors') # 不要なログを非表示にする
    options.add_argument('--ignore-ssl-errors') # 不要なログを非表示にする
    options.add_experimental_option('excludeSwitches', ['enable-logging']) # 不要なログを非表示にする
    options.add_argument('--incognito') # シークレットモードの設定を付与
    
    # ChromeのWebDriverオブジェクトを作成する。
    service=Service(ChromeDriverManager().install())
    return Chrome(service=service, options=options)

def main():
    '''
    main処理
    '''
    search_keyword = input("検索キーワードを入力してください >>> ")
    # driverを起動
    driver = set_driver()
    
    # Webサイトを開く
    driver.get("https://tenshoku.mynavi.jp/")
    time.sleep(3)
    
    '''
    ポップアップを閉じる
    ※余計なポップアップが操作の邪魔になる場合がある
      モーダルのようなポップアップ画面は、通常のclick操作では処理できない場合があるため
      excute_scriptで直接Javascriptを実行することで対処する
    '''
    driver.execute_script('document.querySelector(".karte-close").click()')
    time.sleep(3)
    # ポップアップを閉じる
    driver.execute_script('document.querySelector(".karte-close").click()')

    '''
    find_elementでHTML要素(WebElement)を取得する
    byで、要素を特定する属性を指定するBy.CLASS_NAMEの他、By.NAME、By.ID、By.CSS_SELECTORなどがある
    特定した要素に対して、send_keysで入力、clickでクリック、textでデータ取得が可能
    '''
    # 検索窓に入力
    driver.find_element(by=By.CLASS_NAME, value="topSearch__text").send_keys(search_keyword)
    # 検索ボタンクリック
    driver.find_element(by=By.CLASS_NAME, value="topSearch__button").click()

    '''
    find_elements(※複数形)を使用すると複数のデータがListで取得できる
    一覧から同一条件で複数のデータを取得する場合は、こちらを使用する
    '''
    # 空のDataFrame作成
    df = pd.DataFrame()
    
    count = 1
    
    while True:
        recruit_elms = driver.find_elements(by=By.CSS_SELECTOR,value=".cassetteRecruit__content")
    
        for recruit_elm in recruit_elms:
            
            try:
                name =  recruit_elm.find_element(by=By.CSS_SELECTOR,value=".cassetteRecruit__name").text
                copy =  recruit_elm.find_element(by=By.CSS_SELECTOR,value=".cassetteRecruit__copy").text
                
                df = df.append({
                    "会社名": name, 
                    "タイトル": copy,
                    # "項目C": ""
                    }, 
                    ignore_index=True)
                
                print(f"{count} 件目成功")
            
            except Exception as e:
                print(f"{count} 件目失敗")
            
            finally:
                count += 1
                
        nextpage = driver.find_elements(by=By.CSS_SELECTOR,value=".iconFont--arrowLeft")

        if nextpage:
            url = nextpage[0].get_attribute("href")
            driver.get(url)
        else:
            break
            
    print(df)
    
    df.to_csv('C:/Users/handb/Desktop/PythonProject/issue2/test2.csv',index=False, encoding='utf-8-sig')

    # 1ページ分繰り返し
    # print(len(name_elms))
    '''
    name_elmsには１ページ分の情報が格納されているのでforでループさせて１つづつ取り出して、Dataframeに格納する
    '''
    # for name_elm in name_elms:
        # DataFrameに対して辞書形式でデータを追加する
    
    # for copy_elm in copy_elms:

# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()