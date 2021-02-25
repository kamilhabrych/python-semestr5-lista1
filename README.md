# Lista 1 - Języki programowania wysokiego poziomu

## Python (1) - Zmienne, typy, print, input, if

Zadania:

(1) Wprowadź do 4 zmiennych a, b, c, d, wartości:
2,5,5.0 oraz 4.2
Wyświetl te zmienne za pomocą polecenia print.
Wyświetl a + b, a + c, a + d i podobnie z ∗ i / zamiast +.
Zinterpretuj wyniki.

(2) Wprowdź do 2 zmiennych s i t wartości:
’kot’ oraz ” i pies”
Wyświetl te zmienne (uwaga: w Pythonie nie ma różnicy między pojedynczym a podwójnym cudzysłowiem).
Wyświetl: s + t, t + s + t oraz 2 ∗ s i zinterpretuj wyniki.

(3) Polecenie input służy do wprowadzania danych z klawiatury.
Stosując składnię typu:
i=input(’Podaj i’)
wprowadź dwie zmienne i oraz j.
Wyświetl i, j oraz i + j. Jak należy zinterpretować wynik?
(wsk. spróbuj wprowadzać różne wartości do i oraz j).

(4) Konwersja w Pythonie pozwala na przekszatałcanie typów (np. zmiennoprzycinkowy 3.14 na całkowity 3, albo alfanumeryczny ’3.14’).
Podstawowe funkcje to int(), float() oraz str(). Powtórz zadanie (3) stosując składnię typu: i=int(input(’Podaj i’))
Jak teraz zinterpretować wyniki?

(5) Napisz program w którym użytkownik wprowadza 2 liczby całkowite.
Przetestuj na tych liczbach operator % (np. a%b lub i%j) dla pary wprowadzanych liczb. Spróbuj odgadnąć znaczenie tego operatora.
(wsk. przetestuj kilka przypadków z drugą liczbą równą 2, potem równą 3..)
Przetestuj w podobny sposób operator // tak aby odgadnąć jego znaczenie.

(6) Napisz program w którym użytkownik wprowadza 3 liczby całkowite.
Następnie, za pomocą polecenia if mają być wyświetlone tylko te z 3 liczb
które są większe od 10. Przetestuj parę razy.

(7) Napisz program w którym użytkownik wprowadza liczbę całkowitą po
czym, za pomocą if, else, ma być wyświetlone czy liczba jest parzysta czy
nieparzyta. Uwaga! Dwie wartości porównujemy za pomocą ==, np. if x==5
(wsk. dla parzystości: zadanie (5))

(8) Rok R jest przestępny jeśli jest podzielny przez 4 z wyjątkiem gdy jest
podzielny przez 100 (wtedy nie jest przestępny), chyba że jest podzielny
przez 400 (wtedy jest przestępny).
1
2
Stosując if, elif, else napisz program w którym użytkownik wprowadza rok
i jest wyświetlone czy jest przestępny czy nie.
Przetestuj np. dla: 1900, 1904, 1905, 1600.

(9) Użytkownik wprowadza liczbę zmiennoprzecinkową f (np. f = 93.7415).
Stosując operator % wyświetl cyfry zaraz przed przecinkiem i zaraz po (w
przyładzie: 3 i 7).

(10) Wprowadzone są dwie liczby zmiennoprzecinkowe f i g (np. 2.314 i
65.45). Zamień części całkowite w f i g i wyświetl nowe f i g (w przykładzie
65.314 i 2.45).

(11) Przetestuj, że operator ∗∗ jest potęgowaniem w pythonie. Wprowadzone są dwie liczby i oraz j i program sprawdza która z liczb jest większa
i
j
czy j
i
i wyświetla odpowedź następująco (na przykładzie i = 3, j = 2):
3 do 2 równe 9 jest większe od 2 do 3 równe 8.

(12) Sprawdź jak za pomocą ∗∗ można liczyć pierwiastki kwadratowe z liczby i ogólnie dowolnego stopnia n.
Oblicz √
2, √3
3 oraz √5
5. Która liczba jest największa? Która najmniejsza?
