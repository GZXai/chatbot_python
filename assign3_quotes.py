FILENAME = "movie_quotes.txt"


def get_quotes():
    """
    Returns a list of tuples (pairs) of movie quotes, where
    the first entry in the pair is a quote from a movie and
    the second entry is the response to that quote in that
    movie.
    """

    quotes = [] # 初始化空列表存储结果

    file = open(FILENAME, "r") # 以只读方式打开文件

    for line in file:  # 逐行读取文件
        parts = line.split("\t") # 用制表符分割每行，得到一个list，列表

        if len(parts) == 2: # 确保分割出两个部分
            parts[1] = parts[1].strip()# 去除第二部分的空白字符
            quotes.append((parts[0], parts[1]))# 添加元组（tuple类型）到列表,每个由一个台词对组成
        else:
            print("Warning: found problem line in movie quotes file:\n" + line)

    file.close()

    return quotes


def get_practice_quotes():
    """
    Returns a small set of (made up) quotes in the same format
    as get_quotes.
    """

    return [("quote1", "quote2"),
            ("first", "second"),
            ("first they said this", "then this"),
            ("what?", "that's what"),
            ("what?", "now you've it!")]