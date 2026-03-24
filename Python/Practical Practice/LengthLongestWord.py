sent = "I am playing video game"

start = 0
window = 0

max = -1
start_main = 0

while start < len(sent) and window < len(sent):
    if sent[window] != " ":
        window += 1
    else:
        # print(start, window)
        # print(sent[start: window])

        if max < (window-start):
            max = window - start
            start_main = start
        start = window+1
        window = window+1
if max < (window-start):
    max = window - start
    start_main = start

# print(start_main, max+start_main)
print("Max Word is :", sent[start_main: max +
      start_main], "\nLenght of the word is:", max)
