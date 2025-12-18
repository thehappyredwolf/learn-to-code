def filter_messages(messages):
    filtered = []
    dang_count = []

    for message in messages:
        words = message.split()
        good_words = []
        dangs = []
        for word in words:
            if (word == "dang"):
                dangs.append(word)
            else:
                good_words.append(word)
        good_message = " ".join(good_words)
        filtered.append(good_message)
        dang_count.append(len(dangs))
    return filtered, dang_count
