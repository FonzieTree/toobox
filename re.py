import re
data = '你/n 在/nn 【干 啥】/yy 啊/yy '
s1 = re.findall(r'\w+/n ', data)
s2 = re.findall(r'\w+/nn ', data)
s3 = re.findall(r'\w+/yy ', data)
s4 = re.findall(r'\【.*\】/yy ', data) + re.findall(r'\w+/yy ', data)
