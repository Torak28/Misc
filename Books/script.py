input_str = open('input', 'r', encoding='utf-8').read().splitlines()

out = ''
for line in input_str:
	title = line.split('\t')[0]
	author = line.split('\t')[1]
	new_version = ' * _' + author + '_, __' + title + '__\n'
	out += new_version

print(out, file=open('output', 'a', encoding='utf-8'))
