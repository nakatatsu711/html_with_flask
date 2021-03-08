import time

import lxml.html
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


 # ヤフオクで'バッグ プラダ カーキ'と検索したURL
base_url = 'https://auctions.yahoo.co.jp/search/search?auccat=&tab_ex=commerce&ei=utf-8&aq=-1&oq=&sc_i=&fr=auc_top&p=%E3%83%90%E3%83%83%E3%82%B0+%E3%83%97%E3%83%A9%E3%83%80+%E3%82%AB%E3%83%BC%E3%82%AD&x=0&y=0'
# 設定値
chromedriver_path = 'ChromeDriverのパス'


def main():
    '''
    メインの処理
    残り時間が24時間以内のオークションを取得
    '''

    # Webページを取得
    options = Options()
    options.add_argument('--headless')  # ヘッドレスモードを有効にする
    driver = webdriver.Chrome(chromedriver_path, options=options)  # ChromeのWebDriverオブジェクトを作成
    driver.get(base_url)  # ページを開く
    assert 'ヤフオク!' in driver.title  # タイトルに'ヤフオク!'が含まれていることを確認

    items = []
    while True:
        items = get_items(driver, items)
        time.sleep(1)
        next_page = driver.find_elements_by_css_selector('.Pager__list--next > a')  # 次ページのリンクを取得
        if not next_page:
            break  # 最後のページならwhile文をbreak
        time.sleep(1)
        driver.get(next_page[0].get_attribute('href'))

    # ブラウザを閉じる
    driver.quit()

    return items


def get_items(driver, items):
    '''
    残り時間が２４時間以内のオークションのみ取得
    '''

    html = lxml.html.fromstring(driver.page_source)  # fromstring()関数で文字列をパース
    item_num = len(html.cssselect('ul.Products__items > li.Product'))
    times = html.cssselect('.Product__time')  # '残り時間'のオブジェクトを取得
    for i in range(item_num):
        if '時間' not in times[i].text:
            continue  # 入札数が0、残り時間が24時間以内のオークション以外はcontinue
        dict = {}
        dict['title'] = html.cssselect('.Product__titleLink')[i].text.replace('/', '-')  # 商品タイトルを追加
        dict['title_url'] = html.cssselect('.Product__titleLink')[i].get('href')  # 商品タイトルのURLを追加
        dict['price'] = html.cssselect('.Product__priceValue.u-textRed')[i].text  # 販売価格を追加
        dict['img_url'] = html.cssselect('.Product__imageData')[i].get('src')  # 商品画像のURLを取得
        if 'jpg' in dict['img_url']:
            dict['img_path'] = dict['title'] + '.jpg'
        elif 'png' in dict['img_url']:
            dict['img_path'] = dict['title'] + '.png'
        else:
            continue
        items.append(dict)
        download_image(dict['img_url'], dict['img_path'])
    return items


def download_image(img_url, img_path):
    '''
    オークション画像を取得し、staticフォルダに保存
    '''

    try:
        data = requests.get(img_url)
        with open('./static/' + img_path, 'wb') as f:  # staticフォルダに商品タイトルのファイル名で保存
            f.write(data.content)
    except Exception:
        print(img_url + 'は取得できませんでした')


if __name__ == '__main__':
    items = main()
    # 結果を表示
    for item in items:
        print(item['title'])
