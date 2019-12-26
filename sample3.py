# -*- coding: utf-8 -*-
# Pandas、globのimport
import pandas as pd
import glob
 
# 2001～2018年の株価データをマージする
# globでファイル名の一覧を取得
stock_price_files = glob.glob('stockPrice/*.csv')
stock_price_list = []
 
# ファイルを読み込み、DataFrameでlistに格納する。
for f in stock_price_files:
    stock_price_list.append(pd.read_csv(f, header=1, encoding="shift-jis"))
     
# Listに格納されたデータを全てconcat関数で連結    
stock_price_all = pd.concat(stock_price_list)
stock_price_all.to_csv("stock_price.csv",index = False, encoding="shift-jis")