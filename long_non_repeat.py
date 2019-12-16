"""
There are four substring missions that were born all in one day and you shouldn’t be needed more than one day to solve them.
All of those mission can be simply solved by brute force, but is it always the best way to go?
(you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).

A very similar to the first is the second mission of the series with only one distinction is that you should look in
a completely different way. You need to find the first longest substring with all unique letters. For example,
in substring "abca" we have two substrings with unique letters "abc" and "bca", but we should take the first one,
so the answer is "abc".

Input: String.

Output: String.

"""


def non_repeat(line):
    count = ""
    word = ""
    for i, element in enumerate(line):
        for letter in line[i:]:
            print(letter)
            if letter not in word:
                word += letter
                if len(word) > len(count):
                    count = word
            else:
                word = ""
                break
    return count


if __name__ == '__main__':
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    assert non_repeat('w') == 'w', "one letter"
