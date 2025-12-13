# reverse numbers in a docx word(a word by docx format), pass, Debugging(Watch), save
# pip install docx library, reading document
from docx import Document

NumberOfFixes = 0
NumbersDone = 0
document = Document("C:/Users/Persatech/Desktop/Mohammad.docx")


for Paragraphs in document.paragraphs:
    NewText = ""
    for Charackters in Paragraphs.text:
        if Charackters in "0123456789":
            NumberOfFixes += 1
            if NumbersDone == 0:
                NewText += Charackters
                NumbersDone += 1
            else:
                NewText = NewText[:-1 * NumbersDone] + Charackters + NewText[-1 * NumbersDone:]
                NumbersDone += 1
        else:
            NewText += Charackters
            NumbersDone = 0
    Paragraphs.text = NewText


Address = "C/Users/Persatech/Desktop/Fixed.Mohammad.docx"
print("in total i fixed", NumberOfFixes)
Paragraphs.save(Address)
