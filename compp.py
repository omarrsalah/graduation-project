import docx
#path = '/Users/Mohamed Agroudy/OneDrive/Desktop/aaa.docx' #your docx file path
doc = docx.Document("aaa.docx")
for p in doc.paragraphs:
    fonts = []
    texts = []
    sizes = []
    for i in p.runs:
        fonts.append(i.font.name)
        texts.append(i.text)
        sizes.append(i.font.size.pt)
        
    print(texts, fonts, sizes, sep="\n")