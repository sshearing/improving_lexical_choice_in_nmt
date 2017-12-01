import codecs

lexfile = codecs.open("lex.de","r","utf8")

src_train = codecs.open("train.de","r","utf8")
trg_train = codecs.open("train.en","r","utf8")

src_out = codecs.open("train.lex.de","w","utf8")
trg_out = codecs.open("train.lex.en","w","utf8")

for line in src_train:
    src_out.write(line)

for line in trg_train:
    trg_out.write(line)

for line in lexfile:
    line = line.strip().split(",")
    if line[0] != "" and line[1] != "":
        src_out.write(line[0] + "\n")
        trg_out.write(line[1] + "\n")
