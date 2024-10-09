'''1.	Stwórz listę o nazwie imiona, która zawiera imiona: Adam, Szymon, Gabriel, Dawid, Emilia, Michał.
2.	Dodaj na końcu listy imię Kinga za pomocą metody append.
3.	Wstaw imię Ania na drugą pozycję w liście za pomocą metody insert.'''

imiona = ['Adam', 'Szymon', 'Gabriel', 'Dawid', 'Emilia', 'Michał']
imiona.append('Kinga')
print(imiona)

imiona.insert(1, 'Ania')

print(imiona)

'''1.	Usuń imię Gabriel z listy za pomocą metody remove.
2.	Usuń ostatnie imię z listy za pomocą metody pop.
3.	Znajdź indeks (pozycję) imienia Emilia w liście za pomocą metody index i wyświetl go.'''


imiona.remove('Gabriel')
print(imiona)

imiona.pop(5)
print(imiona)

k = imiona.index('Emilia')
print(k)


'''1.	Zlicz, ile razy imię Adam występuje w liście za pomocą metody count.
2.	Posortuj listę imion w porządku alfabetycznym za pomocą metody sort, a następnie wyświetl zaktualizowaną listę.
3.	Odwróć kolejność elementów w liście za pomocą metody reverse i wyświetl listę.'''

counting = imiona.count('Adam')
print(counting)
imiona.sort()
print(imiona)

imiona.reverse()
print(imiona)

'''1.	Skopiuj listę imion do nowej listy o nazwie imiona_kopia za pomocą metody copy.
2.	Wyczyść oryginalną listę imiona za pomocą metody clear.s'''


imiona2 = imiona.copy()
print(imiona2)

imiona.clear()
print(imiona)