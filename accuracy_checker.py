# How to call:
#   from accuracy_checker import Accuracy
# Then with the text outputted from the speech-to-text function call:
#   acc = Accuracy.accuracy(text)
# and use acc as a parameter for data_to_csv

class Accuracy:
    # test is string and actual is dictionary
    def accuracy(test):
        # dictionary for gmu dataset
        actual = {"her" : 4, "the": 3, "and" : 3, "a" : 3, "we" : 2, "things" : 2,
                  "these" : 2, "of" : 2, "for" : 2, "with" : 1, "will" : 1,
                  "wednesday" : 1, "train" : 1, "toy" : 1, "to" : 1, "three" : 1,
                  "thick" : 1, "store" : 1, "stella" : 1, "station" : 1, "spoons" : 1,
                  "snow" : 1, "snake" : 1, "snack" : 1, "small" : 1, "slabs" : 1,
                  "six" : 1, "she" : 1, "scoop" : 1, "red" : 1, "please" : 1,
                  "plastic" : 1, "peas" : 1, "need" : 1, "meet" : 1, "maybe" : 1,
                  "kids" : 1, "into" : 1, "go" : 1, "from" : 1, "frog" : 1, "fresh" : 1,
                  "five" : 1, "cheese" : 1, "can" : 1, "call" : 1, "brother" : 1,
                  "bring" : 1, "bob" : 1, "blue" : 1, "big" : 1, "bags" : 1, "at" : 1,
                  "ask" : 1, "also" : 1}
        # lowercase test string
        test = test.lower()

        # remove possible punctuation from test string
        remove = ".,!?;:"
        for c in remove:
            test = test.replace(c, '')

        # split string into words
        words_to_check = test.split()
        incorrect_words = 0
        for word in words_to_check:
            # if word in dictionary, update value, else add one to the
            # incorrect_words counter
            if word in actual:
                actual[word] = actual[word] - 1
            else:
                #incorrect_words += 1
                pass
                # seems to be more accurate without this

        # check the word counts in the dictionary, add to incorrect_words if less
        # than or greater than 0
        for word, count in actual.items():
            if count < 0:
                incorrect_words += - (count)
            elif count > 0:
                incorrect_words += count

        return str(incorrect_words)
