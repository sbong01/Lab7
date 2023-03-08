#Lab 7
#author: saerin bong and katherine O'Roark
def find_o(word):
    count = 0
    for x in word:
        if x == 'o':
            count = count + 1
    return count

print(find_o('bonobos'))
