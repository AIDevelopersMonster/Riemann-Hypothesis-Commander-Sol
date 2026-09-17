# HATTER-SOL-16

## За пределами диэдральной лаборатории: инженерный расчёт неабелевой портовой томографии в A5 и PSL(2,7)

**Версия:** 1.1, кандидат к публикации после интеграции рецензии  
**Серия:** HATTER-SOL · Арифметическое чаепитие  
**Автор:** Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**ИИ-исследователь и соавтор исследовательского диалога:** Commander Sol / Hatter Sol  
**DOI серии:** 10.5281/zenodo.17996774  
**Дата:** 16 сентября 2026 г.

---

## Аннотация

В этой работе программа неабелевых портов доводится до конечного инженерного расчёта. Точно исследованы две простые группы: `A5` и `PSL(2,7)`. Для `A5` полный перебор порождающих пар и вещественное трёхмерное неприводимое представление дают точную томографию класса коммутатора и глобально разделённый скалярный Mahler-наблюдатель для всех `mu >= 4`. Для `PSL(2,7)` комплексное трёхмерное неприводимое представление по-прежнему различает все классы сопряжённости, однако нечувствительный к ориентации скалярный determinant/Mahler quotient склеивает два класса порядка 7. Потерянный бит восстанавливается одним знаковым коммутаторным квадратурным каналом длины четыре. Наконец, все 114 орбит порождающих пар относительно одновременного сопряжения восстанавливаются по пяти пробам

\[
A,\qquad B,\qquad AB,\qquad AB^{-1},\qquad[A,B],
\]

при максимальной глубине слова четыре. Ни одно подсемейство не более чем из четырёх проб из полного trace-word семейства глубины не выше 4 не разделяет все 114 орбит. Если разрешены только balanced closed loops, точная глубина восстановления возрастает до 14. В версии 1.1 явно введены определения наблюдателей, соглашения о переборе слов, аналитическое доказательство знака determinant phase и идентификаторы сертификатов. Результат H16 — инженерная спецификация; fixed-point расчёт, HDL, синтез и физическая реализация перенесены в HATTER-SOL-17.

**Ключевые слова:** конечные простые группы; неабелевы порты; томография; коммутаторная голономия; мера Малера; `A5`; `PSL(2,7)`; представительные каналы; инженерная спецификация.

---

# 1. Инженерная задача и точные определения наблюдателей

Пусть `G` — конечная группа, а `(A,B)` — упорядоченная порождающая пара. Пары отождествляются с точностью до одновременного сопряжения,

\[
(A,B)\sim(hAh^{-1},hBh^{-1}).
\]

Для унитарного представления

\[
\rho:G\to U(d)
\]

определим эрмитов двухпортовый оператор

\[
H_{A,B}(\theta,\phi)=
 e^{i\theta}\rho(A)+e^{-i\theta}\rho(A)^{-1}
 +e^{i\phi}\rho(B)+e^{-i\phi}\rho(B)^{-1}.
\]

Для каждого целого `n >= 0` нормированный торический момент равен

\[
\boxed{
S_n(A,B)=\frac1{(2\pi)^2}
\int_0^{2\pi}\!\int_0^{2\pi}
\operatorname{Tr}\bigl(H_{A,B}(\theta,\phi)^n\bigr)
\,d\theta\,d\phi.
}
\]

Инженерная задача состоит в восстановлении орбиты `(A,B)` относительно одновременного сопряжения по конечному набору внешне адресуемых портовых слов и конечному representation readout.

Положим

\[
K=[A,B]=ABA^{-1}B^{-1}.
\]

## Теорема 1. Универсальный четвёртый торический момент

Для любого конечномерного унитарного представления

\[
\boxed{
S_4(A,B)=28d+4\operatorname{Tr}\rho(K)+4\operatorname{Tr}\rho(K^{-1}).
}
\]

Для вещественного трёхмерного представления

\[
S_4=84+4\chi(K)+4\chi(K^{-1}),
\]

а когда характер инвариантен относительно обращения, как в используемом ниже вещественном `A5`-канале,

\[
\boxed{S_4=84+8\chi_3(K).}
\]

### Доказательство

Торическое усреднение уничтожает каждый моном с ненулевым суммарным показателем по `A` или `B`. На длине 4 имеется шесть balanced pure-`A` слов и шесть balanced pure-`B` слов; все они дают вклад единицы. Смешанный balanced-сектор состоит из всех `4!=24` перестановок

\[
A,\ A^{-1},\ B,\ B^{-1}.
\]

После использования цикличности следа 16 слов дают единичный вклад, 4 дают `K`, и 4 — `K^{-1}`. Поэтому коэффициент при единице равен

\[
6+6+16=28,
\]

что и доказывает формулу. `□`

Именно здесь впервые может появиться нетривиальная замкнутая неабелева информация.

---

# 2. Лаборатория A5

## 2.1. Точный перебор порождающих пар

Полный точный перебор даёт

\[
|A_5|=60,
\qquad 2280\text{ упорядоченных порождающих пар},
\qquad 38\text{ орбит одновременного сопряжения}.
\]

Для порождающей пары `(A,B)` общий централизатор равен

\[
C_{A_5}(A)\cap C_{A_5}(B)=C_{A_5}(\langle A,B\rangle)=Z(A_5)=1.
\]

Следовательно, каждая орбита имеет размер `60`, а `2280/60=38`.

Коммутаторы порождающих пар лежат только в классах

\[
3A,\qquad5A,\qquad5B,
\]

с числами орбит

\[
18,\qquad10,\qquad10.
\]

## 2.2. Вещественный 3D class channel

Возьмём стандартный вещественный трёхмерный неприводимый характер

\[
\chi_3=(3,-1,0,\varphi,\varphi'),
\qquad
\varphi=\frac{1+\sqrt5}{2},
\quad
\varphi'=\frac{1-\sqrt5}{2}.
\]

| класс | `1A` | `2A` | `3A` | `5A` | `5B` |
|---|---:|---:|---:|---:|---:|
| `chi_3` | `3` | `-1` | `0` | `phi` | `phi'` |

Все значения различны, поэтому один вещественный trace определяет класс сопряжённости.

Для соответствующего orientation-preserving 3D-представления набор собственных значений инвариантен относительно обращения, а определитель равен единице. Поэтому

\[
\boxed{
P_g(T)=\det(I-\rho_3(g)T)
=1-\chi_3(g)T+\chi_3(g)T^2-T^3.
}
\]

Коэффициент при `T^2` равен `Tr rho_3(g)^{-1}=chi_3(g)` именно для этого вещественного ортогонального determinant-one представления.

---

# 3. Скалярный Mahler-наблюдатель в A5

Для `mu >= 4` определим

\[
\boxed{
M_{A,B}(\mu)=\frac1{(2\pi)^2}
\int_0^{2\pi}\!\int_0^{2\pi}
\log\det\bigl(\mu I-H_{A,B}(\theta,\phi)\bigr)
\,d\theta\,d\phi.
}
\]

Сертифицированная спектральная щель при `mu=4` гарантирует положительность детерминанта и корректность логарифма и моментного разложения на всём естественном диапазоне `mu >= 4`.

Для класса коммутатора `C` введём конечное множество откликов

\[
\boxed{
\mathcal M_C(\mu)=
\{M_{A,B}(\mu):\langle A,B\rangle=A_5,\ [A,B]\in C\}.
}
\]

Эта запись устраняет неоднозначность более раннего варианта: внутри одного класса коммутатора может быть несколько точных determinant/Mahler типов.

## Теорема 2. Глобальное A5-разделение

Для каждого `mu >= 4`

\[
\boxed{
\sup\mathcal M_{5A}(\mu)<\inf\mathcal M_{3A}(\mu),
\qquad
\sup\mathcal M_{3A}(\mu)<\inf\mathcal M_{5B}(\mu).
}
\]

То есть каждый тип `5A` лежит ниже каждого типа `3A`, а каждый тип `3A` — ниже каждого типа `5B`.

### Сертифицированная архитектура доказательства

38 орбит порождающих пар сводятся к 14 точным determinant/Mahler типам: 4 типа в `5A`, 6 в `3A`, 4 в `5B`.

1. Точные моменты до порядка 40 над `Q(sqrt(5))` и рациональная оценка хвоста доказывают разделение при
   \[
   \mu\ge\frac{23}{5}.
   \]
2. Typewise tensor-Cayley spectral-gap сертификат даёт положительную рациональную щель для каждого из 14 типов; наихудшее значение удовлетворяет `gamma > 1/5`.
3. Интервальная квадратура с внешним округлением доказывает строгий порядок при `mu=4`.
4. Введём
   \[
   G(\mu)=M(\mu)-3\log\mu+\frac6{\mu^2}.
   \]
   Торический баланс зануляет нечётные моменты, точно получаем `S_2=12`, а эрмитовость даёт
   \[
   S_{2m}=\langle\operatorname{Tr}H^{2m}\rangle\ge0.
   \]
   Следовательно,
   \[
   G(\mu)=-\sum_{m\ge2}\frac{S_{2m}}{2m\mu^{2m}},
   \qquad
   \boxed{
   G'(\mu)=\sum_{m\ge2}\frac{S_{2m}}{\mu^{2m+1}}\ge0.
   }
   \]
5. 60 рациональных отрезков ширины `1/100` покрывают `[4,23/5]`; монотонность сводит каждый отрезок к двум сертифицированным endpoint inequalities. Совместно с большой-`mu` теоремой это закрывает все `mu >= 4`.

Таким образом, итог H15 в `A5` сохраняется, но доказательный механизм меняется:

\[
\boxed{
\text{3D irrep}\to\text{коммутаторный trace длины 4}
\to\text{tensor spectral gap}
\to\text{глобальное determinant separation}.
}
\]

---

# 4. Лаборатория PSL(2,7)

Реализуем

\[
G=PSL(2,7),\qquad |G|=168,
\]

в точном действии на `P^1(F_7)`.

Полный перебор даёт

\[
19152\text{ упорядоченных порождающих пар}
\]

и

\[
\boxed{114}
\]

орбит одновременного сопряжения. Как и выше, общий централизатор порождающей пары равен `Z(G)=1`, поэтому каждая орбита имеет размер `168`, и `19152/168=114`.

Размеры шести классов сопряжённости равны

\[
1,21,56,42,24,24
\]

для

\[
1A,2A,3A,4A,7A,7B.
\]

Числа орбит по классу коммутатора:

\[
\boxed{
36\times3A,\quad64\times4A,\quad7\times7A,\quad7\times7B.
}
\]

Выберем один комплексный трёхмерный неприводимый характер:

\[
\chi_3=
\left(
3,-1,0,1,
\frac{-1+i\sqrt7}{2},
\frac{-1-i\sqrt7}{2}
\right).
\]

| класс | `1A` | `2A` | `3A` | `4A` | `7A` | `7B` |
|---|---:|---:|---:|---:|---:|---:|
| `chi_3` | `3` | `-1` | `0` | `1` | `(-1+i√7)/2` | `(-1-i√7)/2` |

Все шесть значений различны, поэтому один complex 3D trace различает все классы.

---

# 5. Точный скалярный тип и склейка 7A/7B

Для порождающей пары определим Laurent determinant polynomial при граничном параметре `mu=4`:

\[
D_{A,B}(z,w)=\det\!\left(
4I-z\rho(A)-z^{-1}\rho(A)^{-1}
-w\rho(B)-w^{-1}\rho(B)^{-1}
\right).
\]

Два полинома имеют один и тот же **скалярный determinant/Mahler type**, если они переходят друг в друга посредством используемых в точном сертификате сохраняющих торическую меру симметрий

\[
(z,w)\mapsto(z^{\pm1},w^{\pm1}),
\qquad
(z,w)\mapsto(w,z),
\]

после чего совпадают как точные Laurent polynomials. Введём

\[
\boxed{
\mathcal T_C=\{
[D_{A,B}]:\langle A,B\rangle=PSL(2,7),\ [A,B]\in C
\}.
}
\]

Точная конечная классификация даёт

\[
|\mathcal T_{3A}|=6,\qquad
|\mathcal T_{4A}|=12,\qquad
|\mathcal T_{7A}|=|\mathcal T_{7B}|=3,
\]

и, главное,

\[
\boxed{\mathcal T_{7A}=\mathcal T_{7B}.}
\]

Это не недостаток комплексного 3D-представления. Потеря возникает при orientation-even scalarization.

Проективная матрица с квадратично-невычетным определителем в `PGL(2,7)` задаёт внешний автоморфизм `alpha`, для которого

\[
7A\leftrightarrow7B,
\qquad
\boxed{
\chi_3(\alpha(g))=\overline{\chi_3(g)}.
}
\]

Поэтому любой вещественный скалярный class observer, инвариантный относительно этой смены ориентации, обязан склеивать `7A` и `7B`.

---

# 6. Минимальный ориентированный замкнутый канал

Определим

\[
\boxed{
Q_4(A,B)=
\frac{\operatorname{Tr}\rho_3([A,B])-
\operatorname{Tr}\rho_3([A,B]^{-1})}{i\sqrt7}.
}
\]

## Теорема 3. Точный orientation bit

Для любой порождающей пары в `PSL(2,7)`

\[
Q_4(A,B)=
\begin{cases}
0,&[A,B]\in3A\cup4A,\\
+1,&[A,B]\in7A,\\
-1,&[A,B]\in7B.
\end{cases}
\]

### Доказательство

Для `7A`

\[
\chi_3(K)=\frac{-1+i\sqrt7}{2},
\qquad
\chi_3(K^{-1})=\frac{-1-i\sqrt7}{2},
\]

поэтому разность равна `i sqrt(7)`. На `7B` знак меняется, а значения на `3A` и `4A` вещественны. `□`

Нетривиального freely reduced balanced word длины меньше 4 не существует: баланс требует присутствия как минимум по одному `A,A^{-1},B,B^{-1}`. Поэтому длина 4 — первая возможная closed-loop глубина.

## Лемма 3.1. Знак determinant phase

Пусть

\[
P_K(t)=\det(I-t\rho_3(K)),\qquad 0<t<1.
\]

Для `K in 7A`

\[
P_{7A}(t)=R(t)-i\frac{\sqrt7}{2}t(1+t),
\]

а для `K in 7B`

\[
P_{7B}(t)=R(t)+i\frac{\sqrt7}{2}t(1+t),
\]

где

\[
R(t)=(1-t)\left(1+\frac32t+t^2\right)>0.
\]

Следовательно, для любого `0<t<1`

\[
\boxed{
\operatorname{Im}P_{7A}(t)<0,
\qquad
\operatorname{Im}P_{7B}(t)>0.
}
\]

Значит, orientation bit измеряется одним знаковым determinant-phase каналом.

---

# 7. Полная томография порождающей пары

Используем свободный алфавит

\[
\{A,a,B,b\},
\qquad a=A^{-1},\quad b=B^{-1}.
\]

Для слова `w` сначала выполняется свободное, затем циклическое сокращение. В trace tomography отождествляются циклические сдвиги и обратное слово, поскольку trace циклически инвариантен, а соглашение об обращении учитывается class channel. Обозначим через `W_{<=L}` множество канонических представителей всех ненулевых cyclically reduced trace words длины не выше `L`.

Точный генератор сертификата даёт

\[
\boxed{|W_{\le4}|=25.}
\]

На 114 орбитах порождающих пар накопленные числа различных сигнатур равны

\[
\boxed{
|\Sigma_{\le1}|=24,
\quad
|\Sigma_{\le2}|=107,
\quad
|\Sigma_{\le3}|=107,
\quad
|\Sigma_{\le4}|=114.
}
\]

## Теорема 4. Точная short-word глубина и пятипробовая сигнатура

Глубина 4 необходима и достаточна для полного восстановления орбиты порождающей пары. Уже пять проб

\[
\boxed{
A,\qquad B,\qquad AB,\qquad AB^{-1},\qquad[A,B]
}
\]

разделяют все 114 орбит.

Более того, сертификат перебирает **все** подмножества `W_{<=4}` размеров 1, 2, 3 и 4. Ни одно из них не разделяет все 114 орбит. Поэтому

\[
\boxed{
5\text{ проб минимальны внутри полного depth-}\le4\text{ trace-word family}.
}
\]

Это утверждение о минимальности в фиксированном конечном интерфейсе, а не абсолютная нижняя граница для произвольных нелинейных способов измерения.

---

# 8. Цена режима только замкнутых контуров

Слово называется **balanced**, если

\[
\exp_A(w)=0,
\qquad
\exp_B(w)=0.
\]

Точные числа новых канонических balanced words длин

\[
4,6,8,10,12,14
\]

равны

\[
\boxed{1,2,14,76,505,3386},
\]

то есть суммарно до глубины 14 имеется `3984` слова.

Накопленные числа различимых орбит равны

\[
\boxed{4,22,98,110,112,114}.
\]

## Теорема 5. Точная balanced-глубина

Balanced closed-loop trace tomography имеет точную глубину восстановления

\[
\boxed{14}.
\]

Глубина не выше 12 оставляет две нетривиальные коллизии, а глубина 14 разделяет все 114 орбит.

Одна сертифицированная достаточная восьмипробовая balanced-сигнатура задаётся словами

```text
AABBaabb
AAABAbabbaBaaB
AAbABaBBBabbab
AABBAbababaB
AAAABabaBabbaB
AABabaBAAbaBab
ABBAbaBBabbb
ABABABaBabbabb
```

где строчные буквы обозначают обратные порты. Минимальность числа 8 не утверждается.

---

# 9. Замороженная инженерная спецификация для H17

H16 фиксирует предпочтительный смешанный процессор:

\[
\boxed{
\text{PORT WORD ENGINE}
\longrightarrow
\text{ORIENTED 3D CHANNEL}
\longrightarrow
\text{5-PROBE SIGNATURE}
\longrightarrow
\text{114-ORBIT DECODER}.
}
\]

Word engine должен вычислять

\[
A,\qquad B,\qquad AB,\qquad AB^{-1},\qquad ABA^{-1}B^{-1}.
\]

Максимальная primitive word depth равна 4. Разделение `7A/7B` требует одного orientation-sensitive компонента; он может быть реализован как `I/Q`, как антисимметричная trace-квадратура `Q_4` или как знак determinant phase.

В H16 доказано точное арифметическое разделение. Здесь **не** доказана устойчивость к квантованию, fixed-point rounding, аналоговому шуму, пропуску измерений или timing faults. 114-state decoder предполагает точные безошибочные значения проб. H17 должен определить margins, разрядность, redundancy и аппаратное поведение при ошибках до любых физических заявлений.

---

# 10. Арифметический мост и границы утверждений

Для конечного расширения Галуа и неразветвлённого места `v` локальный Artin factor имеет representation-theoretic форму

\[
L_v(T,\rho)=\det(I-\rho(\operatorname{Frob}_v)T)^{-1}.
\]

В `A5` один вещественный 3D local factor различает все классы. В `PSL(2,7)` один комплексный 3D local factor также различает все классы и сохраняет ориентацию `7A/7B`, теряемую orientation-even scalarization.

Это локальный representation-theoretic Artin bridge. Общая автоморфность не утверждается.

H16 доказывает конечные информационные бюджеты для двух конкретных простых групп. Здесь не утверждается, что те же пять слов решают задачу для произвольных конечных групп, сетей или неизвестных топологий; также не делается заявлений о криптографической стойкости, PUF или физической неклонируемости.

---

# 11. Воспроизводимость и идентификаторы сертификатов

Переборы конечных групп используют точную permutation arithmetic. Алгебраические расчёты характеров выполняются точно над `Q(sqrt(5))` и `Q(i sqrt(7))`. A5 boundary/compact-strip Mahler certificates сочетают точные алгебраические конструкции с интервальной арифметикой с внешним округлением.

Авторитетная ветка:

`research/hatter-sol-16-nonsolvable-ports`.

Главные сертификаты и их Git content identities:

| сертификат | главное утверждение | Git blob SHA |
|---|---|---|
| `a5_generating_pair_commutator_certificate.py` | 2280 пар, 38 орбит, split 18/10/10 | `0198ca2abecb2a6a8082d69150d7b057a5e5da74` |
| `a5_mahler_separation_mu_23_over_5_certificate.py` | точное Mahler-разделение при `mu >= 23/5` | `987ffe58a79bcd9a6ea63af249efaec701cb1388` |
| `a5_uniform_spectral_gap_diameter_certificate.py` | uniform boundary spectral gap | `5d0bf981afb7d793cd9d8f5e6b804f01dc90edd1` |
| `a5_type_tensor_gap_certificate.py` | точные typewise tensor gaps | `d6a4490086c2c24fc1dee1e1b2e472fe5f82a638` |
| `a5_boundary_mahler_mu4_interval_certificate.py` | строгий порядок при `mu=4` | `c7fa2446ec9132047be0b05a998904535556bd5e` |
| `a5_global_mahler_mu_ge_4_certificate.py` | monotone compact-strip closure | `7887cf1ff164a21f8399d05bcaa688a1092a8098` |
| `psl27_generating_pair_and_scalar_collapse_certificate.py` | 114 орбит и точная scalar collapse `7A/7B` | `6a0c4ae4bb28b84142b7989f156312107880a85f` |
| `psl27_outer_orientation_minimal_observer_certificate.py` | outer involution и oriented 3D separation | `4e615ca2b5a7bb1d81961986c95f27e845e6d10f` |
| `psl27_oriented_loop_spectral_observer_certificate.py` | `Q_4`, depth 4, знак determinant phase | `20882008268ef62293cf3e64af42fc2e7c6fbee2` |
| `psl27_pair_tomography_short_word_certificate.py` | 25-word family, minimality пяти проб, balanced depth 14 | `a60113f99bc7a959bcbc6c9231d6b6c4893f8865` |

Publication package сопровождается release-level SHA-256 manifest. Git blob identities дополнительно связывают каждое утверждение с точным содержимым репозитория.

Команда запуска каждого standalone certificate:

```bash
python <certificate-file>.py
```

Каждый сертификат завершает выполнение явным `PASS` только после успешного прохождения всех exact или interval proof obligations.

---

# 12. Аннотированная библиография серии HATTER-SOL

Полная предыдущая серия включена, поскольку H16 является накопительным инженерным слоем. DOI приводятся только там, где отдельный выпуск уже имеет присвоенный DOI.

**Архив серии:** `10.5281/zenodo.17996774`.

**[01] HATTER-SOL-01. _A Tea Party in the Additive-Multiplicative World with Hatter Sol: The Number Line, the Observer, and Two Operations._** DOI `10.5281/zenodo.22639237`. Основополагающая работа серии: отделяет арифметическую структуру от наблюдателя и координатной системы.

**[02] HATTER-SOL-02. _Two Teapots, One Cup: “Who Are You?” Among the Primes._** DOI `10.5281/zenodo.22656414`. Развивает конечную probe complexity для идентификации простых, точные congruence/quadratic orbit counts и sparse rigidifying families.

**[03] HATTER-SOL-03. _The Cup That Asks Its Own Questions: Anonymous Probes, the Exact Predecessor of a Prime, and Recursive Rigidity._** DOI `10.5281/zenodo.22679521`. Переходит от внешних меток к внутренним отношениям и доказывает жёсткость exact prime-predecessor структуры.

**[04] HATTER-SOL-04. _The Cup Forgets Multiplicities: Radical Predecessor, the Multiplicity Tower, and the Cost of a Hypothetical Prime Symmetry._** Кандидат к публикации; DOI отдельного выпуска ожидает депонирования. Строит multiplicity tower и доказывает сильные ограничения на любую гипотетическую симметрию, не объявляя решённой глобальную automorphism problem.

**[05] HATTER-SOL-05. _Who Is Missing from the Table? Empty Fibers, Exact-Support Spectra, and the Survival of the 3↔5 Transposition._** DOI `10.5281/zenodo.22718278`. Уточняет задачу симметрии через exact-support fibers и их cardinality/compactness constraints.

**[06] HATTER-SOL-06. _Orbitwise Survival Kernel._** Исследовательский слой репозитория; отдельный DOI не присвоен. Локализует продолжение seed symmetry на точных support-orbit данных causal cone.

**[07] HATTER-SOL-07. _Alice in the Land of Free Threads: Factors as Nodes and the Exact Cost of Multiplicative Splitting._** DOI `10.5281/zenodo.22724185`. Вводит factor-as-node network model и точный free-boundary law.

**[08] HATTER-SOL-08. _From a Line to Space: Dimensional Suppression of Factor-Architecture Sensitivity._** DOI `10.5281/zenodo.22744644`. Исследует влияние path, planar и unrestricted carrier classes на чувствительность факторной сети.

**[09] HATTER-SOL-09. _World-Dependent Factor Networks and a Prime-Toggle Response Operator._** DOI `10.5281/zenodo.22732435`. Соединяет арифметические миры с typed factor networks, Pareto responses и prime-toggle hypercube/Laplacian.

**[10] HATTER-SOL-10. _Ideal Factor Networks Beyond Unique Element Factorization._** DOI `10.5281/zenodo.22734865`. Переходит от факторизации элементов к prime ideals и principalization witnesses, добавляя multistate nodes и точные phase transitions.

**[11] HATTER-SOL-11. _Orbital Port Filtrations: How Network Geometry Forgets Arithmetic Direction Data._** DOI `10.5281/zenodo.22746559`. Разделяет arithmetic, network и observational forgetting и описывает geometry-controlled collapse `3→2→1`.

**[12] HATTER-SOL-12. _Observer Laws, World Rotation, and Structural Memory of an Integer._** DOI `10.5281/zenodo.22747698`. Рассматривает видимость как совместную функцию integer, arithmetic world, carrier и observer; сравнивает planar/toroidal resolving power.

**[13] HATTER-SOL-13. _A Fixed Integer Across Growing Arithmetic Worlds: Unbounded Structural Diversity and the Topological Cost of Erasure._** DOI `10.5281/zenodo.22754637`. Доказывает неограниченное branching для фиксированного integer в растущих cyclotomic worlds и оценивает genus cost of erasure.

**[14] HATTER-SOL-14. _Galois-Equivariant Carriers: Same Graph, Different Arithmetic Homology._** DOI `10.5281/zenodo.22757307`. Показывает, что один абстрактный граф может нести различные arithmetic regular actions с неизоморфной equivariant homology.

**[15] HATTER-SOL-15. _Non-Abelian Ports: From Dihedral Commutator Holonomy to Universal Mahler Tomography._** Финальный release candidate v0.5; отдельный DOI на момент этой сборки не присвоен. Строит prime-dihedral two-port лабораторию и доказывает universal first-harmonic dominance для centered primitive Mahler observer; это прямой математический родитель H16.

---

# 13. Внешние источники

1. Serre, J.-P. _Linear Representations of Finite Groups_. Springer.
2. Isaacs, I. M. _Character Theory of Finite Groups_. Dover / классический источник.
3. Neukirch, J. _Algebraic Number Theory_. Springer.

---

# Заключение

Переход от prime-dihedral лаборатории к конечным простым группам меняет доказательную технику, но сохраняет портовый принцип. `A5` показывает, что глобальное scalar determinant separation выживает в неразрешимой простой группе. `PSL(2,7)` точно выявляет orientation information, теряемую вещественной scalarization, и восстанавливает её на первой возможной balanced depth. После сохранения oriented 3D channel пять trace-probes максимальной глубины 4 восстанавливают все 114 орбит порождающих пар.

\[
\boxed{
5\text{ ориентированных считываний}+\text{depth }4
\Longrightarrow
\text{полная pair-orbit tomography в }PSL(2,7).
}
\]

Это замороженная математическая спецификация, передаваемая HATTER-SOL-17 для reference software, golden vectors, fixed-point arithmetic, HDL, synthesis и physical-board validation.
