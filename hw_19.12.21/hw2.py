with open('стих.txt') as stih:
	stih_lines = stih.readlines()
	str_count = 0
	for num, line in enumerate(stih_lines):
		str_count += 1
		words_count = len(line.split())
		print(f'#{num + 1} - {words_count} слов(а)')
	print(f'{str_count} строк(и).')
