import wikipedia

text=input()
answer=wikipedia.summary(text,sentences=5)
print(answer)
