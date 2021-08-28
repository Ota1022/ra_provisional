# 言語学的尺度集

著者の態度や心理的傾向との関係が示唆されている、著者検出のための文体測定法を集めたライブラリです。
本ライブラリは、Asaishi(2017)で整理された日本語テキストメトリクスをベースに、12種類のスタイロメトリクスを算出することができる。

対応する自然言語

- 日本語
- 英語

## インストール

> NOTE: `pip` によるインストール可能なパッケージは、現在開発中のもので、ご迷惑をおかけします。

### 要件

- Python 3.6 以上
  - f-string (PEP 536):
  - Type Hints (PEP 484):
- (お待たせしました)

### 依存関係

`pipenv` を使用している場合は、`pipenv install` でこのライブラリの仮想環境が作成されます。
それ以外の場合は、`pip install -r requirements.txt` で十分です。

また，本ライブラリは，日本語処理のために以下の外部コマンドにも依存しています．

- MeCab (日本語テキスト処理用):
    - [mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd) (日本語のNERを向上させる):
- CaboCha (`analyse_parseddoc.py` 用):

### リソース

さらに、日本語メトリクスの場合は、以下の言語資源が必要です。

- [AWD-J EX](http://sociocom.jp/~data/2019-AWD-J/)をファイル名`AWD-J_EX.txt`とする。
- JIWCをファイル名 `2017-11-JIWC.csv`として
- 日本語のストップワードをファイル名 `stopwords_jp.txt` として保存

以上を`data/`フォルダに入れます。

> 今後はオプションにしていきます。
> また、リソースの置き場所も設定できるようにする予定です。

## 使い方

**重要：テキストの正規化はユーザーの責任です**。

### `measure_lang.py`

実行することで、テキストファイルからテーブルデータを生成することができます。

```
python measure_lang.py [csv/excel ファイルパス] [ターゲットカラム名]
```

`your_data.csv` を入力すると、入力ファイルと同じ場所に `your_data.measure.csv` が作成されます。

適切な文数を計算するために、入力テキストは1行に1文のような形式にすることをお勧めします。

また、以下のようにインポートして各メジャーを使用することもできます。

```python
import measure_lang as ml

def your_fancy_func(string):
    # ...
    res = ml.calc_ttrs(string)
    # ...
```

すべての関数は文字列を読みます（改行された長い文章でもOKです）。
文字列のリストに適用したい場合には、リストの上で反復する必要があります。

各メジャーの詳細な使用方法は、そのメジャーのdocstring（ワークインプログレス）に記載されています。

### `analyse_parseddoc.py`

(ここのドキュメントは作業中です)

準備します。
- 1行に1つの文、空白行なし
- ドキュメントは1つの空白行で分割されます

例を挙げると
```python
import re
import pandas as pd

import split_sentence  # find a great library to split sentences

col = "column_name"

with open('formatted_text.txt', 'w') as f:
    f.writelines(
        [
            re.sub("^$", "", re.sub("\n+", "\n", re.sub("\s", " ", t))) + "\n\n"
            for t in df[col].to_list()
        ]
    )
```
そして，`sentence-splitter formatted_text.txt > formatted_text-sentsplit.txt ` などと実行すると，`sentence-splitter` が入力されたテキストを，空白行を保持したまま一行一文の形式に分割します（良い本物のツールを見つけなければなりませんが，英語では `nltk` が提供しています）．

実行してみてください。
```shell
cabocha -f1 your_text.txt > your_text.cabocha.txt
python analyse_parseddoc.py your_text.cabocha.txt [your_csv.measured.csv]
```

第2引数に `measure_lang.py` で生成された測定済みの csv ファイルを追加すると、`analyse_parseddoc.py` は結果を列ごとに連結します (GNU `paste(1)` のように、ただし csv 内のエスケープされた複数行のテキストを考慮します)。

## 対策

```python
import measure_lang as ml
import analyse_parseddoc as ap
```

- **Percentages of character types** (`ml.count_charcat`):  
テキスト中の文字に対する、ひらがな、カタカナ、漢字のそれぞれの文字種の割合を表します。

- **Type Token Ratio (TTR)** (`ml.calc_ttrs`):  
テキスト中の総単語数に対する異種単語の比率。

- **Percentage of content words** (`ml.measure_pos`):  
テキストの総単語数に対する内容語(名詞、動詞、形容詞、副詞)の割合です。

- **Modifying words and Verb Ratio (MVR)** (`ml.measure_pos`):  
文章中の単語に対して、動詞と形容詞・副詞・接続詞の割合を表したもの。作者推定の指標の一つとして用いられている。

- **Percentage of proper nouns** (`ml.measure_pos`):  
テキスト中の全単語に対する固有名詞(名前付き実体)の割合です。

- **Word abstraction** (`ml.measure_abst`):  
テキストに含まれる単語の抽象度。具体的には、最も抽象度の高い単語の最大値と、抽象度の高い上位5つの単語の平均値を用いました。抽象度は、日本語の単語抽象度辞書である [AWD-J EX](http://sociocom.jp/~data/2019-AWD-J/)から取得した。

- **Ratios of emotional words** (`ml.calc_jiwc`):  
「悲しみ」、「不安」、「怒り」、「嫌悪」、「信頼」、「驚き」、「喜び」の7つの感情に関連する単語の、テキスト中の全単語に対する比率を表しています。7つの値は、確率の性質を満たすように変換されています（各値は0から1の間にあり、すべての値の合計は1になります）。感情との関連度は、日本語の感情語辞典JIWCに基づいて決定した。

- **Number of sentences** (`ml.measure_sents`):  
テキストを構成する文の総数。

- **Length of sentences** (`ml.measure_sents`):  
文章を構成する各文の文字数の記述統計（平均値、標準偏差、四分位値、最小値、最大値）。  
特に、平均文量は、書き手の創造的な態度や性格との関連が示唆されている。

- **Percentage of conversational sentences** (`ml.count_conversations`):  
テキストに含まれる会話文の総数の割合。

- **Depth of syntax tree** (`ap.analyse_dep`):  
テキストの各文の依存関係ツリーの深さを算出した記述統計。

- **Mean of the number of chunks per sentence** (`ap.analyse_dep`):  
文章ごとのチャンク数の平均値について計算された記述統計量。

- **Mean of the words per chunk** (`ap.analyse_dep`):  
チャンクあたりの単語数の平均値を計算した記述統計量。

### 要約表

| Stylometric                               | Sub-measures (value format)                                                 |
| :---------------------------------------- | :-------------------------------------------------------------------------- |
| Percentages of character types            | Hiragana, katakana, and kanji (Chinese characters) (%)                      |
| Type Token Ration (TTR)                   | (%)                                                                         |
| Percentages of content words              | (%)                                                                         |
| Modifying words and Verb Ratio (MVR)      | (%)                                                                         |
| Percentage of proper nouns                | (%)                                                                         |
| Word abstraction                          | The maximum, and the average of the top five abstract words (real number)   |
| Ratios of emotional words                 | sadness, anxiety, anger, disgust, trust, surprise, and happiness (%)        |
| Number of sentences                       | (integer)                                                                   |
| Length of sentences                       | mean, standard deviation, interquartile, minimum, and maximum (real number) |
| Percentage of conversational sentences    | (%)                                                                         |
| Depth of syntax tree                     | mean, standard deviation, interquartile, minimum, and maximum (real number) |
| Mean of the number of chunks per sentence | mean, standard deviation, interquartile, minimum, and maximum (real number) |
| Mean of the words per chunk               | mean, standard deviation, interquartile, minimum, and maximum (real number) |

---
## リファレンス

- [Asaishi, 2007]: 浅石卓真. (2017). テキストの特徴を計量する指標の概観. 日本図書館情報学会誌, 63(3), 159–169. https://doi.org/10.20651/jslis.63.3_159