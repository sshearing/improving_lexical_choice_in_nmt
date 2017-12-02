import codecs

lexfile = codecs.open("lex.de","r","utf8")
src_out = codecs.open("train.delex","w","utf8")
trg_out = codecs.open("train.enlex","w","utf8")

for line in lexfile:
    line = line.strip().split(",")
    if line[0] != "" and line[1] != "":
        src_out.write(line[0] + "\n")
        trg_out.write(line[1] + "\n")
