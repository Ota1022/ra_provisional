# 構文解析ベースの統計量
# import numpy as np
from typing import List
import fire
import pandas as pd
import spacy
import ginza

NLP = spacy.load("ja_ginza")
# 文節を表すchunkと形態素を表すmorphのAPIを使う


def count_chunk_depth(ix, sentchunk):
    if sentchunk[ix].srcs:
        return max(
            [count_chunk_depth(src, sentchunk) + 1 for src in sentchunk[ix].srcs]
        )
    else:
        return 0


def count_sent_depth(sentchunk):
    if len(sentchunk) == 0:
        return 0
    else:
        root_i = [c.dst for c in sentchunk].index(-1)
        return count_chunk_depth(root_i, sentchunk)


def analyse_dep(cfname: str, fname: str = None) -> None:
    """Apply dependency tree analyses and concat the original data"""
    with open(cfname, "r") as f:
        chunk_sents = read_chunks(f)

    docs = []
    doc = []
    for chunk_sent in chunk_sents:
        if chunk_sent:
            doc.append(chunk_sent)
        else:
            docs.append(doc)
            doc = []

    sr_depths = []
    sr_leaves = []
    sr_chunklen = []
    for doc in docs:
        depths = [count_sent_depth(sentchunk) for sentchunk in doc]
        sr_depths.append(pd.Series(depths).describe().to_frame().T)

        n_leaves = [len(sentchunk) for sentchunk in doc]
        sr_leaves.append(pd.Series(n_leaves).describe().to_frame().T)

        chunklen = [len(chunk.morphs) for sentchunk in doc for chunk in sentchunk]
        sr_chunklen.append(pd.Series(chunklen).describe().to_frame().T)

    # 構文木の深さ
    df_sdep = (
        pd.concat(sr_depths)
        .reset_index(drop=True)
        .rename(columns=lambda x: f"sdep_{x}")
    )
    # 構文木の葉の数（文節数）
    df_nleaf = (
        pd.concat(sr_leaves)
        .reset_index(drop=True)
        .rename(columns=lambda x: f"nleaf_{x}")
    )
    # 文節の長さ（形態素数）
    df_chklen = (
        pd.concat(sr_chunklen)
        .reset_index(drop=True)
        .rename(columns=lambda x: f"chklen_{x}")
    )

    if fname:
        df = pd.read_csv(fname)
        assert len(df) == len(df_sdep)
        pd.concat([df, df_sdep, df_nleaf, df_chklen], axis=1).to_csv(
            f"{fname}.parsed.csv", index=False
        )
    pd.concat([df_sdep, df_nleaf, df_chklen], axis=1).to_csv(
        f"{cfname}.parsed.csv", index=False
    )


if __name__ == "__main__":
    fire.Fire(analyse_dep)
