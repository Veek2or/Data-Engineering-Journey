from collections import Counter

with open('TheOdyssey.txt', encoding='UTF-8') as book:
    read_data = book.read() #load the text into a variable

lower_read_data = read_data.lower() #ignore case

#function that removes any punctuation
def removePunctuation(x): 
    book_noPunc = ""
    for character in x:
        if character.isalpha() or character == " ":
            book_noPunc += character
        else:
            book_noPunc += " "
    return book_noPunc

clean = removePunctuation(lower_read_data) #store cleaned book

words = clean.split() #split characters into word

print(len(words)) #print the number of words in the book

# most common words to filter
stopwords = {
    "the", "and", "of", "to", "a", "for"
}

# stores words without stopwords
filtered = [w for w in words if w not in stopwords]

# number of words reduced by about 50k
print(len(filtered))

# counts the number of time a word appears in the book
def countWords(x):
    word_dict = {}
    for word in x:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict

counts = countWords(filtered)
print(counts["house"])

# stores the top 20 most repeated words
top_20_repeated_words = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
print(top_20_repeated_words[:20])

# also prints the 20 most reprated words
c = Counter(counts)
print(c.most_common(20))



