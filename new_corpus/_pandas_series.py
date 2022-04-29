import numpy as np
import pandas as pd

import pandas as pd
'''
@test($$;type(pd))
@alt(表データ|データフレーム)
@alt(カラム|列)
@alt(インデックス|行)
@alt(どの程度|どれだけ)
@alt(欠損値|NaN|未入力値)
@alt(変更する|増やす|減らす)
@alt(保存する|保存する|書き込む)
@alt(抽出する|取り出す)
@alt(読み込む|読む)
@alt(読み込んで|読んで)
@alt(全ての|すべての|全)
@alt(の名前|名)
@alt(丸める|四捨五入する)
@alt(丸めて|四捨五入して)
@prefix(df;データフレーム)
@prefix(ds;データ列;カラム)
@prefix(col;カラム;カラム)
@prefix(value;[文字列|日付|])
データ列を使う
データ列をインポートする
'''


__X__ = df

# ds の操作

__X__.value_counts()
'''
@X(ds;df[col])
@Y(ds;dfのcol)
@test(df=ds=missing;alist=['A','B'];$$)
__Y__の各[データ|]値の出現[|回]数[|を求める]
__Y__の各[データ|値]が_何回出現するか見る
'''

__X__.unique()
'''
@test(df=ds=missing;alist=['A','B'];$$)
__Y__の[ユニーク|一意]な[値|要素][|を見る]
'''

__X__.nunique()
'''
@test(df=ds=missing;alist=['A','B'];$$)
__Y__の[ユニーク|一意]な[値の個数|要素数][|を見る]
'''

__X__.astype(object)
'''
@X(df[col]|ds)
@Y(dfのcol|ds)
__Y__をカテゴリデータに変換する
'''

__X__.str.len()
'''
@test(df=ds=missing;$$)
__Y__の文字列長を列として得る
'''

__X__.map({s: 1, s2: 0})
'''
__Y__を[0と1|1と0]に[マップする|変換する]
'''

__X__.unique().tolist()
'''
__Y__からユニークな[要素|値]を抽出し、リスト化する
'''

set(ds.unique().tolist()+ds2.unique().tolist())
'''
dsとds2から重複を取り除く
'''

df[col] = df[col2].astype(ty)
'''
@alt(に代入する|[と|に]する)
dfのcol2をtyに変換し、[|新たに|dfの]colに代入する
'''

# ビン

pd.cut(__X__, n)
'''
@test(pd=df=ds=missing;$$)
@X(ds;df[col];alist;array)
@Y(ds;dfの中のcol;alist;array)
@alt(ビン分割する|分割する|ビ[|ン]ニングする)
@alt(ビン数|分割数)
@alt(等間隔で|)
{__Y__を|ビン数nで_}ビン分割する
{__Y__を|等間隔で|n個に|}ビン分割する
'''

pd.cut(__X__, alist)
'''
@test(pd=df=ds=missing;$$)
__Y__をビン分割する
{__Y__を|alistを境界値として}ビン分割する
'''

pd.cut(__X__, n, labels=names)
'''
@test(pd=df=ds=missing;$$)
{__Y__を|ビン数nで_}ビン分割して、namesのラベルをつける
{__Y__を|n個に|[|等間隔で]}ビン分割して、namesのラベルをつける
'''

pd.qcut(__X__, n)
'''
@test(pd=df=ds=missing;$$)
@alt(等量で|等しい量になるように)
{__Y__を|等量で|ビン数nで_}ビン分割する
{__Y__を|等量で|n個に|}ビン分割する
'''

pd.qcut(__X__, 2)
'''
@test(pd=df=ds=missing;$$)
{__Y__を|中央値で}ビン分割する
'''

pd.qcut(__X__, 4)
'''
@test(pd=df=ds=missing;$$)
{__Y__を|四分位数[ごとに|で]}ビン分割する
'''
