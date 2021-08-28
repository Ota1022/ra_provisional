from collections import Counter
import os
import re
from typing import List, Tuple, Dict, Union
import unicodedata as ud

import fire
from natto import MeCab
import pandas as pd
import numpy as np

Num = Union[int, float]

#この辺を引数にする Fire絡み　Apply file
NM = MeCab()  # NOTE: assume IPADIC
NMN = MeCab("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

with open(os.path.join(os.path.dirname(__file__), "./data/stopwords_jp.txt"), "r") as f:
    STOPWORDS_JP = [line.strip() for line in f]
STOPPOS_JP = ["形容動詞語幹", "副詞可能", "代名詞", "ナイ形容詞語幹", "特殊", "数", "接尾", "非自立"]

with open(os.path.expanduser("./data/AWD-J_EX.txt"), "r") as f:
    rows = [line.strip().split("\t") for line in f]
    AWD = {word: score for word, score, _, _ in rows}
DF_jiwc = pd.read_csv(os.path.expanduser("./data/2017-11-JIWC.csv"), index_col=1).drop(
    columns="Unnamed: 0"
)

def apply_file(fname, col):
    if frame is none:
        
    else:
        if fname.endswith(".csv"):
            df = pd.read_csv(fname)
        elif fname.endswith(".xls") or fname.endswith(".xlsx"):
            df = pd.read_excel(fname)
        else:
            raise ValueError("Unsupported input format: please use CSV or Excel data")

        assert col in df.columns, f"{col} is not found in the input data"

        pd.concat(
            [df, df.apply(lambda row: apply_all(row[col]), result_type="expand", axis=1)],
            axis=1,
        ).to_csv(f"{fname}.measured.csv", index=False)

#apply_allを解体，引数にjiwcなどを入れて逐一対応しない引数に処理を書く

if __name__ == "__main__":
    fire.Fire(apply_file)
