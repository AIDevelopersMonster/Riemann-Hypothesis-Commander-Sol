# LAB-02 — Восемь probes и 24-битный fingerprint

## Цель

Разобрать путь от пары A,B до восьми class codes и 24-битного fingerprint.

## Восемь слов

~~~text
AAB
Abb
AAAB
Abbb
AABAb
AAbAb
ABABB
ABaBB
~~~

Строчные буквы: a=A^-1, b=B^-1.

## Известный пример

~~~text
A   = 5e3b88
B   = 7ecc11
raw = 8d256a
~~~

Декодирование:

~~~text
8d256a
= 100 011 010 010 010 101 101 010
=   4   3   2   2   2   5   5   2
=  7A  4A  3A  3A  3A  7B  7B  3A
~~~

## Helper

Из корня LAB-01:

~~~powershell
py -3 .\labs\support\decode_signature.py 8d256a
~~~

## Задание

1. Декодировать 8d256a вручную.
2. Проверить helper-скриптом.
3. Сопоставить восемь координат восьми probe-словам.
4. Найти все строки для этой пары:

~~~powershell
Select-String -Path .\vectors\full.txt -Pattern '^5e3b88 7ecc11 '
~~~

5. Построить таблицу word / 3-bit code / class.

## Вопрос

Почему переход от элемента группы к классу сопряжённости является сжатием информации?
