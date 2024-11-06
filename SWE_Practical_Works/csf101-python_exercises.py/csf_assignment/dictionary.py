import docx2txt as d2t

docx_file = 'dictionary.docx'
txt_file = 'dzo.txt'

docx = d2t.process(docx_file)

file=open(txt_file, 'w', encoding='utf-8')
file.write(docx)
file.close()