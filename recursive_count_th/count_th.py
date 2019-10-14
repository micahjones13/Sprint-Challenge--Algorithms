'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # made count a list because I can't remember how to make it not re-start at 0 with recursion
    count = []
    # starting point for letter search
    x = 0

    def helper(x, word):
        # base cases, if it's less than or equal to the len(word), then there can't be any th's
        if x == len(word) - 1:
            return
        elif len(word) <= 1:
            return
        # not base case, then compare the neighboring letters
        elif word[x] + word[x+1] == 'th':
            # if they are th, then add a 1 to the count list
            count.append(1)
        return helper(x+1, word)
    helper(x, word)
    # add up all the nums in count for the answer
    answer = sum(count)
    return answer


print(count_th('the'))
