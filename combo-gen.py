# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Yonglin Wang
# Date: 2021/1/29 6:24 PM
"""Print random distribution of fixed number of elements summed to a fixed integer"""

import argparse
import re

import numpy as np

SEPERATORS = "，|、|,|\."

CHN_PATTERN = re.compile(u'[\u4e00-\u9fa5]+')

# print formats
CHN_COUNT_FORMAT = "{0:{2}<{3}}：{1:>6}"
CHN_SUM_FORMAT = "共{}种，共计{}份"
CHN_CLASS = "份"
CHN_SEP = "："

EN_COUNT_FORMAT = "{0:{2}<{3}} -> {1:>6}"
EN_SUM_FORMAT = "Total types: {}\nTotal count: {}"
EN_CLASS = ""
EN_SEP = ": "


def has_chn_char(text: str):
    """check if string contains Chinese characters"""
    if CHN_PATTERN.search(text):
        return True
    else:
        return False


def text_to_list(text: str) -> list:
    """helper to process text into strings"""
    chunks = re.split(SEPERATORS, text)
    out = []

    for c in chunks:
        if c:
            out.append(c.strip())

    return out


def assign_num(items: list, total: int, has_chn: bool):
    """assign numbers to items; numbers sum to fixed total"""
    # get distribution
    dist = np.random.multinomial(total, np.ones(len(items)) / len(items))

    # check langauge
    if has_chn:
        count_str = CHN_COUNT_FORMAT
        sum_str = CHN_SUM_FORMAT
        class_str = CHN_CLASS
        filler = chr(12288)
    else:
        count_str = EN_COUNT_FORMAT
        sum_str = EN_SUM_FORMAT
        class_str = EN_CLASS
        filler = " "

    # print stats
    for item, count in zip(items, dist.tolist()):
        print(count_str.format(item, str(count) + class_str, filler,  max([len(s) for s in items])))
    print(sum_str.format(len(items), sum(dist)))


def main():
    # command line parser
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(prog="Name of Program",
                                     description="Program Description",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("items_text",
                        type=str,
                        help="Items to generate count for, separated by {}".format(str(SEPERATORS.split("|"))[1:-1]))
    parser.add_argument("total_numbers",
                        type=int,
                        help="Fixed sum of all item counts.")

    args = parser.parse_args()

    assign_num(text_to_list(args.items_text), args.total_numbers, has_chn=has_chn_char(args.items_text))


if __name__ == "__main__":
    main()
