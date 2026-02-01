sent = input()
target = input()
repl = input()
sent1 = sent
if (target in sent):
    sent1 = sent.replace(target, repl)
print(sent1)