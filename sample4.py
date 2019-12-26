from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif
 
# 単変量統計による特徴量選択
for i in range(1, 6):
    # 上位i個の特徴量を取得する。（評価関数 = f_classif）
    selector = SelectKBest(k=i)
    selector.fit(X_train , y_train)
    # 各特徴量を選択したか否かのmaskを取得
    mask = selector.get_support() 
    print('上位' + str(i) + '個の特徴量を選択')
    print('始値', '高値', '安値', '終値', '出来高', '終値調整値')
    print(mask)