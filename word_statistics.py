import sys


def read_file(file_path):
    try:
        file = open(file_path, "r", encoding="utf-8")
        text = file.read()
        file.close()
        return text
    except:
        print("Could not read the file")
        sys.exit(1)


def clean_punctuation(text):
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    cleaned = ""
    for char in text:
        if char not in punctuation:
            cleaned += char
    cleaned = cleaned.lower()
    return cleaned


def split_words(text):
    words = []
    current_word = ""
    for char in text:
        if char == " " or char == "\n" or char == "\t":
            if current_word != "":
                words.append(current_word)
                current_word = ""
        else:
            current_word += char
    if current_word != "":
        words.append(current_word)
    return words


def total_words(words):
    count = 0
    for word in words:
        count += 1
    return count


def unique_words(words):
    unique = []
    for word in words:
        if word not in unique:
            unique.append(word)
    return unique


def word_frequency(words):
    frequency_list = []
    word_list = unique_words(words)
    for unique_word in word_list:
        count = 0
        for word in words:
            if word == unique_word:
                count += 1
        frequency_list.append((unique_word, count))
    return frequency_list


def average_word_length(words):
    total_length = 0
    for word in words:
        total_length += len(word)
    if len(words) == 0:
        return 0
    return total_length / len(words)


def longest_words(words, top_n=5):
    result = []
    for i in range(top_n):
        longest = ""
        for word in words:
            if word not in result and len(word) > len(longest):
                longest = word
        if longest != "":
            result.append(longest)
    return result


def shortest_words(words, top_n=5):
    result = []
    for i in range(top_n):
        shortest = None
        for word in words:
            if word not in result:
                if shortest is None or len(word) < len(shortest):
                    shortest = word
        if shortest is not None:
            result.append(shortest)
    return result


def main():
    if len(sys.argv) < 2:
        print("Filename not found")
        sys.exit(1)

    file_path = sys.argv[1]
    text = read_file(file_path)
    cleaned_text = clean_punctuation(text)
    words = split_words(cleaned_text)

    print("\n-------------- Word Statistics ------------")
    print("Total words:", total_words(words))
    unique = unique_words(words)
    print("Unique words:", total_words(unique))
    print("Average word length:", round(average_word_length(words), 2))

    print("\nWord frequencies:")
    freqs = word_frequency(words)
    for wordfrequency in freqs[:10]:
        print(wordfrequency[0], ":", wordfrequency[1])

    print("\nLongest words:")
    for word in longest_words(words):
        print(word)

    print("\nShortest words:")
    for word in shortest_words(words):
        print(word)


if __name__ == "__main__":
    main()
