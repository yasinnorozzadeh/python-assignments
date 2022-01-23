def check_words(s):
    count = 0
    for i in range(0, len(s)):
        if s[i] == " ":
            count += 1
    return count +1
s = input()
print("number of words : ",check_words(s))
