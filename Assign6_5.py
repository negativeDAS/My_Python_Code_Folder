text = "X-DSPAM-Confidence:    0.8475"
temp = ' '
text = text + temp
ext_s = text.find('0')
ext_e = text.find(' ' ,ext_s)
ext = text[ext_s : ext_e]
num = float(ext)
print(ext)
