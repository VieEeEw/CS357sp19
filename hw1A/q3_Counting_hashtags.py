tweets = ["All I see is corn. #UIUC #WhatAboutSoybeans",
          "@datsik is coming back to the Canopy Club on Feb 18th! Come and get it #uiuc"]

frequency_dict = {}
for tweet in tweets:
    for word in tweet.lower().split():
        if (word[0] == "#"):
            frequency_dict[word] = frequency_dict.get(word, 0) + 1

hashtag_counts = list(frequency_dict.items())
# 先按照数量，再按照字母排序，代码的时候，反过来写就对了
hashtag_counts.sort(key=lambda tup: tup[0])
hashtag_counts.sort(key=lambda tup: tup[1], reverse=True)
print(hashtag_counts)
