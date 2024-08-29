# count vowels in string

def count_vowels(string):
    VOWELS = "aoieuyAOIEUY"
    count = 0
    for char in string:
        if char in VOWELS:
            count += 1
    print(count)

count_vowels("hello, world!")
