invoice = '''
01234567
01234567
01234567
01234567
'''
i04 = slice(0, 5)
ins = list(filter(lambda x: x, invoice.split('\n')))

for item in ins:
    print(item[i04])
