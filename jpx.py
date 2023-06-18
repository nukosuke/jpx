import os
import json
import urllib.request
import xlrd

def prepare():
    """出力先ディレクトリの作成"""
    if not os.path.exists('output'):
        os.makedirs('output')

def fetch():
    """
    xls ファイルのダウンロード
    https://www.jpx.co.jp/markets/statistics-equities/misc/01.html
    """
    urllib.request.urlretrieve('https://www.jpx.co.jp/markets/statistics-equities/misc/tvdivq0000001vg2-att/data_j.xls', 'data_j.xls')

def convert():
    """XLS -> JSON 変換"""
    book = xlrd.open_workbook('data_j.xls')
    sheet = book.sheet_by_index(0)
    for row in range(1, sheet.nrows):
        code = int(sheet.cell(row, 1).value)
        name = sheet.cell(row, 2).value
        market = sheet.cell(row, 3).value
        with open('output/{0}.json'.format(code), 'w') as f:
            json.dump({'code': code, 'name': name, 'market': market}, f, ensure_ascii=False)

if __name__ == '__main__':
    prepare()
    fetch()
    convert()
