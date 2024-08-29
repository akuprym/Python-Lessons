# count vowels in string

def count_vowels(string):
    VOWELS = "aoieuyAOIEUY"
    count = 0
    for char in string:
        if char in VOWELS:
            count += 1
    print(count)

count_vowels("hello, world!")


def nothing():
    pass


def format_date(*, number: int, month: str) -> str:
    return f"The date is {number} of {month}"

print(format_date(number=29, month="August"))

