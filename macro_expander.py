import re
import sys
import os

try:
    path = sys.argv[1]
except IndexError:
    path = 'bf.bf'

with open(path) as f:
    rawtext = f.readlines()

text = ''

macropat = re.compile(r'([\w><]+) ?= ?(.+)')
macros = dict()

for line in rawtext:
    line = re.sub(
        f'{{({"|".join(macros.keys())})}}',
        lambda m: f'{macros.get(m.group(1))}',
        line
    )
    m = macropat.match(line)
    if m:
        macros[m.group(1)] = m.group(2)
    else:
        text += line

outpath = re.sub(r'([^.]+)\.?[^.]*', r'\1.expandedbf', path)

with open(outpath, 'w') as f:
    f.write(text)
