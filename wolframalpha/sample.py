import wolframalpha

textinput=input("enter question ")

client=wolframalpha.Client("U2WEAW-XVJ47X33XK")

res=client.query(textinput)

answer=next(res.results).text

print(answer)
