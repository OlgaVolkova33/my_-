def single_root_words(root_word,*other_words):

    same_words=[]
    root_word_l=root_word.lower()
    for word in other_words:
        other_words_l=word.lower()
        if root_word_l in other_words_l or other_words_l in root_word_l:
            same_words.append(word)
    return same_words
result1=single_root_words('absorb','absorbent','absorbing','absorbable', 'absent')
result2=single_root_words('Haircut', 'Cut', 'Hairball', 'Haircutter', 'Beacon')
print(result1)
print(result2)




