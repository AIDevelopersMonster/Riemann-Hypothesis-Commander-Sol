# Размышлизмы о стационарной локальности с Commander Sol
## Private-Place Bridges, конечные мульти-адические окна и формульно-локальное сжатие

**Alex Malachevsky**  
ORCID: 0009-0008-6009-3196  
Версия 1.0 - 2026

## Аннотация

Мы исследуем двухсортное расширение арифметики Сколема, в котором простые атомы связаны с рациональными метками, а аддитивный целевой сорт снабжён конечным набором фиксированных p-адических предикатов интегральности. Мотивирующий пример задаётся метками

\[
u_p=\frac{\tau(p)^2-p^{11}}{p^{11}},
\]

где \(\tau\) - функция Рамануджана.

Основной результат работы - **Finite Stationary Locality Theorem**. Для конечного множества рациональных простых \(S\) рассматривается структура

\[
\mathcal B_{u,S}=
\Bigl((\mathbb N_{>0},\times),
      (\mathbb Q,+,0,(B_\ell)_{\ell\in S}),U\Bigr),
\qquad
B_\ell(x)\iff v_\ell(x)\ge0.
\]

Предполагается, что вне конечного исключительного множества метки regular primes интегральны во всех стационарных местах \(\ell\in S\), а каждому regular prime инъективно сопоставлено private denominator place \(\lambda(p)\notin S\), имеющее отрицательную valuation на \(u_p\) и неотрицательную valuation на всех остальных regular labels. Допускается конечное число exact common-label defect classes.

Мы доказываем, что для каждой фиксированной first-order формулы существует конечный multi-place depth vector и конечное исключительное множество простых, после удаления которого истинность формулы на хвосте простых инвариантна относительно всех перестановок, сохраняющих конечные локальные цвета и exact defect classes. Доказательство состоит из четырёх механизмов: прямой finite-depth normal form для аддитивного target sort, exact linear separation с помощью private places, fresh-private-place avoidance для незакреплённых target witnesses и finite-fragment back-and-forth для смешанных кванторов.

Отсюда следуют неопределимость обычного порядка и обычного отношения следующего простого на prime atoms и конечность Grid-Isolation Rank для каждого фиксированного isolator. Для меток Рамануджана условия теоремы выполняются для любого конечного stationary atlas. Более того, бесконечное семейство отдельно именованных предикатов \((B_\ell)_{\ell\in\mathbb P}\) всё ещё остаётся конечным формула-за-формулой, поскольку обычная first-order формула упоминает лишь конечное число имён мест. Поэтому следующая настоящая граница - uniformly indexed relation \(\mathsf B(\ell,x)\), где место становится first-order переменной.

---

## 1. Вопрос, стоящий за теоремой

Мультипликативная структура

\[
(\mathbb N_{>0},\times)
\]

обладает огромной симметрией на простых атомах. Любая перестановка простых единственным образом продолжается до автоморфизма всей структуры, если сохранять показатели простых в факторизации каждого положительного целого. Поэтому обычный порядок простых и отношение следующего простого невидимы для чистого умножения.

Естественный способ нарушить эту симметрию - связать каждый простой атом \(p\) с рациональной меткой \(u_p\) и позволить аддитивному target sort наблюдать эти метки. В примере Рамануджана

\[
\Delta(q)=q\prod_{n\ge1}(1-q^n)^{24}
        =\sum_{n\ge1}\tau(n)q^n
\]

и

\[
u_p=\frac{\tau(p)^2}{p^{11}}-1.
\]

Один фиксированный p-адический шар уже способен различать некоторые метки. Следующий естественный вопрос: могут ли несколько независимых локальных окон совместно создать двумерную систему адресации? При двух местах локальные подгруппы уже не образуют одну цепь, а китайская теорема об остатках позволяет согласовывать независимые локальные условия. Поэтому возникает реальная опасность: одно место может попытаться кодировать строки, другое - столбцы, а сложение - их пересечения.

Теорема ниже показывает, что при Private-Place гипотезах этого не происходит. Конечное число stationary windows расширяет конечную палитру цветов, доступных фиксированной формуле, но не превращает локальную глубину в равномерно движущуюся координату.

Это явление мы называем **стационарной локальностью**.

---

## 2. Source sort, target sort и bridge

Пусть

\[
S=\{\ell_1,\dots,\ell_s\}
\]

- непустое конечное множество рациональных простых.

Source sort:

\[
\mathcal N=(\mathbb N_{>0},\times).
\]

Prime atoms first-order определимы как неприводимые неединичные элементы.

Target sort:

\[
\mathcal A_S=(\mathbb Q,+,0,(B_\ell)_{\ell\in S}),
\]

где

\[
B_\ell(x)\iff v_\ell(x)\ge0.
\]

Bridge является графом отображения меток на простых атомах:

\[
\boxed{
U(n,x)\iff \operatorname{Prime}(n)\land x=u_n.
}
\]

Следовательно, composite source element никогда не получает bridge-label. Target видит \(u_p\), но не показатель степени \(p\) в \(p^k\). Это условие будем называть **prime-only** или **multiplicity-blind bridge**.

Вся структура обозначается

\[
\mathcal B_{u,S}=\bigl(\mathcal N,\mathcal A_S,U\bigr).
\]

---

## 3. Private-Place Bridge: точные гипотезы

После удаления конечного исключительного множества простых предположим, что остальные primes распадаются на бесконечное множество regular primes \(R\) и конечное число exact defect classes

\[
D_1,\dots,D_t.
\]

Все primes внутри \(D_j\) имеют одну фиксированную рациональную метку \(\delta_j\).

Для regular primes требуем следующее.

### H1. Интегральность в stationary places

Для каждого \(p\in R\) и каждого \(\ell\in S\)

\[
v_\ell(u_p)\ge0.
\]

### H2. Инъективное private place

Существует инъективное отображение

\[
\lambda:R\to\mathbb P\setminus S
\]

такое, что

\[
v_{\lambda(p)}(u_p)<0,
\]

а для различных \(p,q\in R\)

\[
v_{\lambda(p)}(u_q)\ge0.
\]

### H3. Интегральность defect labels в private places

После возможного увеличения конечного exceptional set

\[
v_{\lambda(p)}(\delta_j)\ge0
\]

для каждого regular \(p\) и каждой defect label \(\delta_j\).

Это условие автоматически достигается конечным исключением: defect labels рациональны, их конечное число, их общий denominator support конечен, а \(\lambda\) инъективно.

Bridge, удовлетворяющий H1-H3 вместе с функциональным prime-only условием раздела 2, будем называть **Private-Place Bridge над stationary atlas \(S\)**.

---

## 4. Предикаты фиксированной глубины

Для каждого фиксированного целого \(m\) положим

\[
B_{\ell,m}(x)\iff v_\ell(x)\ge m.
\]

Они определимы через \(B_\ell\). Если \(m>0\), то

\[
B_{\ell,m}(x)
\iff
\exists y\,(\ell^m y=x\land B_\ell(y)),
\]

а

\[
B_{\ell,-m}(x)
\iff
B_\ell(\ell^m x).
\]

Здесь принципиально важно слово «фиксированного»: variable-depth predicate в язык не добавляется.

Поскольку \((\mathbb Q,+)\) uniquely divisible, умножение на фиксированный рациональный коэффициент first-order задаётся линейным уравнением. Поэтому далее свободно используются rational linear forms

\[
L(\bar x)=a_1x_1+\cdots+a_nx_n+b.
\]

Базовые target conditions имеют виды

\[
L(\bar x)=0
\]

и

\[
L(\bar x)\in B_{\ell,m}.
\]

---

## 5. Local Coverage Lemma

Сначала замкнём единственную конечную комбинаторику, необходимую для отрицательных ball conditions.

### Лемма 5.1

Пусть для фиксированного \(\ell\)

\[
P=a+B_{\ell,m}
\]

- положительный базовый косет, а

\[
C_i=b_i+B_{\ell,n_i}
\]

- конечное семейство запрещённых косетов. Тогда условие

\[
P\setminus\bigcup_iC_i\ne\varnothing
\]

выражается конечной булевой комбинацией fixed-depth отношений между центрами.

### Доказательство

Два \(\ell\)-адических шара либо не пересекаются, либо один содержит другой. Удалим все \(C_i\), не пересекающиеся с \(P\). Если один из оставшихся \(C_i\) содержит \(P\), выжившее множество пусто. В противном случае каждый оставшийся \(C_i\) является proper subball базового шара, поэтому \(n_i>m\).

Если proper forbidden subballs не осталось, cell непуста. Иначе положим

\[
N=\max_i n_i,
\]

где максимум берётся только по proper surviving subballs. После refinement до глубины \(N\) вопрос покрытия решается в конечной факторгруппе

\[
B_{\ell,m}/B_{\ell,N},
\qquad
|B_{\ell,m}/B_{\ell,N}|=\ell^{N-m}.
\]

Взаимное положение конечного числа подкосетов определяется отношениями

\[
a-b_i\in B_{\ell,k},
\qquad
b_i-b_j\in B_{\ell,k}
\]

при конечном наборе фиксированных \(k\). Следовательно, непокрытие также выражается конечной булевой комбинацией таких условий. ∎

Если положительного базового шара в данном place вообще нет, конечное число запрещённых шаров не покрывает \(\mathbb Q\): достаточно выбрать \(y\) с \(v_\ell(y)\) меньше всех релевантных глубин и valuations центров. Тогда

\[
v_\ell(y-b_i)=v_\ell(y)
\]

для всех \(i\).

Конечным объектом здесь является именно refinement quotient \(B_{\ell,m}/B_{\ell,N}\). Фактор \(\mathbb Q/B_{\ell,m}\) конечным не предполагается.

---

## 6. Multi-Place Finite-Depth Normal Form

### Теорема 6.1

Каждая first-order формула в

\[
(\mathbb Q,+,0,(B_\ell)_{\ell\in S})
\]

эквивалентна булевой комбинации формул

\[
L(\bar x)=0
\]

и

\[
L(\bar x)\in B_{\ell,m},
\qquad \ell\in S,\quad m\in\mathbb Z,
\]

причём для каждой фиксированной формулы используется лишь конечное число fixed depths.

### Доказательство

После перехода к DNF достаточно устранить один existential target quantifier \(\exists y\) из одной конъюнкции литералов.

Если присутствует exact equation

\[
ay+t(\bar x)=0,
\qquad a\ne0,
\]

оно единственным образом задаёт

\[
y=-a^{-1}t(\bar x),
\]

и \(y\) устраняется подстановкой. Exact equations с нулевым коэффициентом при \(y\) остаются условиями на \(\bar x\).

Предположим, что exact equation не закрепляет \(y\). Каждый positive local literal с \(y\) переписывается как

\[
y\in a+B_{\ell,m}.
\]

Для одного fixed place пересекающиеся положительные шары вложены, поэтому их конъюнкция либо несовместима, либо сводится к одному наиболее глубокому positive base ball. Negative balls обрабатываются леммой 5.1. В результате в каждом \(\ell\in S\) получаем либо противоречие, либо непустое открытое локальное множество

\[
U_\ell\subseteq\mathbb Q_\ell.
\]

Если все \(U_\ell\) непусты, weak approximation для \(\mathbb Q\) даёт rational \(y\), удовлетворяющий всем локальным требованиям одновременно. После очистки знаменателей это же можно получить конечным CRT-аргументом.

Наконец, exact inequalities

\[
y\ne c_1,\dots,y\ne c_r
\]

удаляют конечное число точек. Любая непустая multi-place local cell содержит бесконечный refinement coset, поэтому finite point deletion не может её уничтожить.

Следовательно, projection остаётся в булевой алгебре, порождённой exact linear equations и fixed-depth local conditions. Повторяя аргумент, устраняем все target quantifiers. ∎

Общая теория pp-formulas в абелевых группах и модулях служит естественным фоном, но конкретная normal form здесь доказана напрямую.

---

## 7. Refinement непустой target cell

### Лемма 7.1. Generic Multi-Place Cell

Пусть \(C\subseteq\mathbb Q\) - непустая cell, заданная конечным набором fixed-depth local literals и конечным набором exact inequalities. Тогда существуют \(a\in C\) и finite depth vector

\[
\mathbf M=(M_\ell)_{\ell\in S}
\]

такие, что

\[
a+H_{\mathbf M}\subseteq C,
\qquad
H_{\mathbf M}=\bigcap_{\ell\in S}B_{\ell,M_\ell}.
\]

### Доказательство

Выберем \(a\in C\). Для каждого \(\ell\) возьмём \(M_\ell\) глубже всех локальных границ, встречающихся в описании cell. Тогда прибавление элемента из \(H_{\mathbf M}\) не меняет ни одно local membership/non-membership условие.

Если присутствуют exact exclusions \(y\ne c_j\), выберем одно место \(\ell_0\in S\) и увеличим \(M_{\ell_0}\) так, чтобы

\[
M_{\ell_0}>\max_j v_{\ell_0}(a-c_j).
\]

Тогда ни одна исключённая точка не попадёт в refinement coset. ∎

---

## 8. Exact Linear Separation через private places

Зафиксируем homogeneous coefficient scheme

\[
\sum_{i=1}^r c_i u_{p_i}=0.
\]

Очистим знаменатели фиксированных рациональных коэффициентов и сгруппируем равные regular primes. Пусть \(p\) представляет один equality block, а \(d\ne0\) - его aggregate coefficient.

Вне конечного множества regular primes, для которых \(\lambda(p)\mid d\), имеем

\[
v_{\lambda(p)}(d u_p)<0.
\]

Все остальные regular labels \(\lambda(p)\)-integral по H2, а defect labels - по H3. Поэтому сумма не может быть равна нулю.

### Лемма 8.1. Exact Linear Separation

Для каждой фиксированной homogeneous coefficient scheme существует конечное coefficient-dependent exceptional set такое, что на оставшемся regular tail отношение

\[
\sum_i c_i u_{p_i}=0
\]

может выполняться только тогда, когда aggregate coefficient каждого regular-prime equality block равен нулю, с учётом фиксированных exact relations между defect labels.

В частности, regular labels инъективны на хвосте.

---

## 9. Affine equations и bounded-anchor cylinders

Наивное утверждение «каждый affine fiber содержит лишь ограниченное число prime tuples» неверно. Например,

\[
u_{p_1}-u_{p_2}+u_{p_3}=u_q
\]

имеет бесконечное семейство

\[
(p_1,p_2,p_3)=(r,r,q).
\]

Первые две координаты образуют structural zero-sum block.

Зафиксируем equality pattern \(\pi\). Для блока \(C\in\pi\) положим

\[
d_C=\sum_{i\in C}c_i.
\]

Блоки с \(d_C=0\) исчезают из reduced equation.

### Лемма 9.1. Reduced Affine-Fiber Lemma

Для блоков с \(d_C\ne0\) число regular-prime assignments, удовлетворяющих фиксированному reduced affine equation, равномерно ограничено величиной, зависящей только от coefficient scheme, после конечного coefficient-dependent исключения.

### Доказательство

Пусть \((q_C)\) и \((q'_C)\) - два решения одного reduced equation. Их разность даёт homogeneous relation. Если бы regular prime из второго решения не встречался в первом, его private place видел бы единственный non-zero aggregate negative contribution, тогда как все остальные terms были бы integral. Это противоречит лемме 8.1.

Значит, второе решение использует только конечный набор regular primes первого решения. Если non-zero blocks всего \(m\), достаточно грубой оценки \(m^m\). ∎

Поэтому exact affine traces являются конечными объединениями **bounded-anchor cylinders**: zero-sum blocks свободны, non-zero blocks имеют лишь конечное число anchors.

---

## 10. Coefficient-Adjusted Local Colors

Local template может содержать рациональные коэффициенты, поэтому глубина цвета должна учитывать их p-адические порядки.

Рассмотрим

\[
L=\alpha+\sum_i a_i u_{p_i}
\]

и test

\[
L\in B_{\ell,m}.
\]

Если \(p_i\) и \(p_i'\) имеют одинаковый цвет modulo \(B_{\ell,K}\), то

\[
v_\ell(u_{p_i}-u_{p_i'})\ge K.
\]

Следовательно,

\[
v_\ell\left(\sum_i a_i(u_{p_i}-u_{p_i'})\right)
\ge
\min_i\bigl(v_\ell(a_i)+K\bigr).
\]

Поэтому достаточно потребовать

\[
K\ge \max_i\{m-v_\ell(a_i)\}.
\]

Для фиксированной формулы \(\Phi\) замкнём конечное семейство target templates относительно линейных подстановок и compatibility consequences, возникающих ниже. Выберем

\[
K_{\Phi,\ell}\ge0
\]

не меньше всех соответствующих bounds.

Для regular prime определим цвет

\[
c_{\mathbf K_\Phi}(p)
=
\bigl(u_p+B_{\ell,K_{\Phi,\ell}}\bigr)_{\ell\in S}.
\]

По H1 число цветов конечно, и

\[
\#\operatorname{Colors}(\Phi)
\le
\prod_{\ell\in S}\ell^{K_{\Phi,\ell}}.
\]

Именно в этом смысле fixed formula видит только конечную локальную информацию.

---

## 11. Fresh-Private-Place Avoidance

Теперь построим witness, остающийся внутри target cell и одновременно избегающий всех значений фиксированного семейства forbidden affine schemes.

### Лемма 11.1

Пусть непустая finite-depth target cell содержит

\[
a+H_{\mathbf M}.
\]

Пусть каждая релевантная forbidden affine scheme для новой target variable \(y\) использует не более \(r\) prime labels. Тогда существует rational \(y\in a+H_{\mathbf M}\), не равный ни одному значению ни одной такой схемы.

### Доказательство

Работаем относительно конечного текущего состояния back-and-forth. Составим finite rational support, включающий:

- stationary places \(S\);
- denominator support всех fixed rational coefficients;
- denominators внешних target parameters;
- denominators всех текущих target coordinates;
- denominator выбранного центра \(a\);
- labels конечного числа exceptional fixed source primes.

Поскольку \(R\) бесконечно, а \(\lambda\) инъективно, выберем regular primes

\[
t_1,\dots,t_{r+1}
\]

с private places

\[
q_j=\lambda(t_j)
\]

вне всего этого конечного support.

Положим

\[
D=q_1\cdots q_{r+1}
\]

и

\[
L=\prod_{\ell\in S}\ell^{N_\ell},
\qquad N_\ell\ge M_\ell.
\]

Определим

\[
y=a+\frac{L}{D}.
\]

Во всех stationary places знаменатель \(D\) является unit, поэтому

\[
y\in a+H_{\mathbf M}.
\]

В каждом fresh private place \(q_j\) число \(a\) integral, \(L\) integral, а \(D\) содержит \(q_j\) в первой степени. Поэтому

\[
v_{q_j}(y)=-1.
\]

Рассмотрим любое forbidden affine value

\[
z=\alpha+\sum_{i=1}^r c_i u_{p_i}.
\]

В нём встречается не более \(r\) prime labels, поэтому хотя бы один из \(t_1,\dots,t_{r+1}\), скажем \(t_k\), отсутствует. В private place \(q_k\) все terms в \(z\) integral, следовательно

\[
v_{q_k}(z)\ge0,
\]

тогда как \(v_{q_k}(y)=-1\). Значит \(y\ne z\). Аргумент одновременно работает для всех tuples всех фиксированных схем. ∎

Ключевой счёт здесь чрезвычайно прост:

\[
r+1\text{ fresh private places}>r\text{ slots for prime labels}.
\]

---

## 12. Target-Witness Transport

Зафиксируем first-order формулу \(\Phi\) и её finite template closure. Пусть \(\sigma\) - перестановка prime atoms, фиксирующая конечное exceptional set, сохраняющая каждый regular color class \(c_{\mathbf K_\Phi}\) и каждый exact defect class setwise.

Для нового target witness \(y\) возможны два случая.

### 12.1. Pinned case

Пусть выполняется exact equation

\[
ay+t=0,
\qquad a\ne0.
\]

Переносим все prime coordinates, встречающиеся в \(t\), посредством \(\sigma\) и определяем \(y'\) из transported equation.

Если одновременно выполняются несколько pinning equations, например

\[
a_1y+t_1=0,
\qquad
a_2y+t_2=0,
\]

их совместимость эквивалентна y-free condition

\[
a_2t_1-a_1t_2=0.
\]

Finite template closure заранее замкнут относительно всех таких compatibility consequences.

### 12.2. Free case

Пусть ни один релевантный exact instance не pin-ит \(y\). Coefficient-adjusted color preservation гарантирует, что transported local literals имеют тот же finite local pattern и задают непустую target cell. По лемме 7.1 она содержит full refinement coset. Лемма 11.1 выбирает в нём witness \(y'\), одновременно избегающий всех exact affine incidences, которые должны оставаться ложными.

Таким образом target witnesses переносятся в обе стороны внутри finite fragment, связанного с \(\Phi\).

---

## 13. Finite-Fragment Back-and-Forth

Чтобы mixed-quantifier step был явным, мы не используем никакой предполагаемый global automorphism двухсортной структуры.

Для finite syntactic closure, порождённого \(\Phi\), свяжем два конечных состояния, если:

1. source tuple переносится в другой source tuple multiplicative automorphism, индуцированным \(\sigma\);
2. все exact target templates из closure имеют одинаковые truth values;
3. все fixed-depth target templates из closure имеют одинаковые truth values;
4. все bridge incidences из closure совпадают.

Эта relation обладает следующими back-and-forth свойствами.

### Source forth/back

Если первое состояние содержит source witness \(n\), во втором берём \(\sigma(n)\). Обратный переход использует \(\sigma^{-1}\). Source atomics сохраняются, поскольку prime-coordinate permutations являются автоморфизмами \((\mathbb N_{>0},\times)\).

### Target forth/back

Для target witness используется pinned/free construction раздела 12. В обратную сторону применяется тот же механизм с \(\sigma^{-1}\).

### Atomic and Boolean preservation

Source atomics, target atomics и bridge atomics включены в controlled closure. Boolean connectives сохраняют эквивалентность непосредственно.

Стандартная индукция по subformulas \(\Phi\) теперь доказывает сохранение каждой subformula. Это именно finite-fragment argument: ни coloring, ни exceptional set не обязаны работать сразу для всех формул языка.

---

## 14. Finite Stationary Locality Theorem

### Теорема 14.1

Пусть \(S\ne\varnothing\) конечно и \(\mathcal B_{u,S}\) является Private-Place Bridge structure, удовлетворяющей условиям разделов 2-3. Тогда для каждой parameter-free first-order формулы

\[
\Phi(\bar p)
\]

со свободными source variables, ограниченными prime atoms, существуют конечное exceptional set \(F_\Phi\) и finite depth vector

\[
\mathbf K_\Phi=(K_{\Phi,\ell})_{\ell\in S}
\]

такие, что

\[
\mathcal B_{u,S}\models\Phi(\bar p)
\iff
\mathcal B_{u,S}\models\Phi(\sigma\bar p)
\]

для каждой prime permutation \(\sigma\), которая

1. фиксирует \(F_\Phi\) поточечно;
2. сохраняет каждый regular multi-place color class \(c_{\mathbf K_\Phi}\);
3. сохраняет каждый exact defect class как множество.

### Доказательство

Строим finite template closure формулы \(\Phi\), выбираем coefficient-adjusted depths раздела 10 и увеличиваем finite exceptional set на все coefficient-, defect- и finite-support исключения, возникающие в разделах 8-12. Finite-fragment back-and-forth раздела 13 сохраняет каждую subformula \(\Phi\), следовательно и саму \(\Phi\). ∎

Это свойство называется **Formula-Relative Tail Symmetry**.

Теорема является формульно-локальной и не утверждает существование одной глобальной группы автоморфизмов всей \(\mathcal B_{u,S}\), реализующей все эти перестановки одновременно.

---

## 15. Порядок, следующий простой и GIR

### Следствие 15.1. Prime order не определим

Обычный strict order на prime atoms не first-order определим в \(\mathcal B_{u,S}\).

### Доказательство

У гипотетической defining formula вне конечного exceptional set имеется лишь конечное число movable classes. Бесконечный regular tail содержит два различных prime atoms \(p\ne q\) одного класса. Их swap допустим, но strict linear order не инвариантен относительно такого swap. ∎

### Следствие 15.2. Prime successor не определим

Обычное отношение

\[
\operatorname{Succ}_{\mathbb P}(p,q)
\]

не определимо в \(\mathcal B_{u,S}\).

### Доказательство

Вне любого конечного множества существует бесконечно много consecutive ordinary prime pairs. Formula-relative partition имеет лишь конечное число ordered class pairs. Поэтому один ordered class pair встречается для бесконечно многих consecutive pairs, в частности для двух непересекающихся

\[
(p,q),\qquad(p',q').
\]

Элементы \(q,q'\) лежат в одном movable class. Swap \(q\leftrightarrow q'\), фиксирующий \(p\), сохраняет гипотетическую successor formula, но уничтожает обычное succession. ∎

Density theorem для defect primes здесь не используется.

### Следствие 15.3. Finite Grid-Isolation Rank

Для каждого fixed isolator \(I(p,q;r)\)

\[
\operatorname{GIR}(I)<\infty.
\]

### Доказательство

Применим теорему 14.1 к \(I\). Вне finite exceptional set имеется конечное число movable classes. В достаточно большой предполагаемой isolated grid некоторый movable class содержит по крайней мере четыре row primes. Зафиксируем одну column и один cell marker. Не более двух из этих четырёх rows могут совпадать с фиксированными column или marker. Выберем две другие строки того же класса и поменяем их местами, оставляя column и marker неподвижными. Formula-relative invariance заставила бы тот же marker изолировать две клетки в одном столбце, противоречие. ∎

Grid-Isolation Rank - специальный programme invariant для механизма uniform cell isolation. Его конечность не отождествляется со stability, NIP или другими глобальными model-theoretic свойствами.

---

## 16. Специализация к меткам Рамануджана

Проверим абстрактные условия для

\[
u_p=\frac{\tau(p)^2-p^{11}}{p^{11}}.
\]

Зафиксируем конечный непустой stationary atlas \(S\).

### 16.1. Интегральность в stationary places

Если \(p\notin S\) и \(\ell\in S\), то \(p^{11}\) является \(\ell\)-adic unit. Поэтому

\[
v_\ell(u_p)\ge0.
\]

### 16.2. Private denominator для good primes

Назовём \(p\ge5\) good prime, если \(\tau(p)\ne0\), и положим

\[
a=v_p(\tau(p)).
\]

Оценка Делиня

\[
|\tau(p)|\le2p^{11/2}
\]

даёт \(a\le5\): если \(a\ge6\), то

\[
p^6\le|\tau(p)|\le2p^{11/2},
\]

откуда \(\sqrt p\le2\), что невозможно при \(p\ge5\).

Поскольку \(2a<11\),

\[
v_p(\tau(p)^2-p^{11})=2a,
\]

и потому

\[
v_p(u_p)=2a-11<0.
\]

Для \(q\ne p\) denominator \(u_q\) является степенью \(q\), следовательно

\[
v_p(u_q)\ge0.
\]

Значит для good primes вне \(S\) можно взять

\[
\lambda(p)=p.
\]

### 16.3. Zero primes как один exact defect class

Если \(\tau(p)=0\), то

\[
u_p=-1.
\]

Поэтому все такие primes, если они существуют, образуют один exact common-label defect class.

### 16.4. Бесконечный резерв good primes

Абстрактной теореме нужен бесконечный regular reservoir. Для этого не требуется density theorem о возможных нулях \(\tau(p)\).

Конгруэнция Рамануджана даёт для prime \(p\)

\[
\tau(p)\equiv1+p^{11}\pmod{691}.
\]

Если

\[
p\equiv1\pmod{691},
\]

то

\[
\tau(p)\equiv2\pmod{691},
\]

следовательно \(\tau(p)\ne0\). По теореме Дирихле primes в прогрессии \(1\pmod{691}\) бесконечны. Значит good-prime reservoir бесконечен.

### Следствие 16.1

Для каждого finite non-empty множества рациональных простых \(S\) структура

\[
\mathcal B_{\Delta,S}
=
\Bigl((\mathbb N_{>0},\times),
      (\mathbb Q,+,0,(B_\ell)_{\ell\in S}),
      U_\Delta\Bigr)
\]

обладает Formula-Relative Tail Symmetry. Обычный порядок простых и prime-successor relation в ней не определимы, а каждый fixed isolator имеет конечный GIR.

---

## 17. Infinite Named Stationary Atlas

Рассмотрим target language

\[
(\mathbb Q,+,0,(B_\ell)_{\ell\in\mathbb P}),
\]

где для каждого rational prime имеется отдельный predicate symbol.

Язык бесконечен, но каждая ordinary first-order formula является конечной строкой. Поэтому fixed formula \(\Phi\) упоминает лишь конечное множество мест. Обозначим его \(S_\Phi\).

Для меток Рамануджана primes вне \(S_\Phi\) являются \(S_\Phi\)-integral, поэтому к \(\Phi\) применяется finite theorem.

### Следствие 17.1. Infinite Named Stationary Atlas

Ramanujan structure со всеми отдельно именованными \(B_\ell\) остаётся formula-by-formula compressed: у каждой фиксированной формулы есть собственное finite exceptional set и finite local color partition на хвосте простых.

При этом возникает красивое pointwise phenomenon. Если \(p\) good, его собственный named predicate \(B_p\) отличает \(p\) от всех других prime labels:

\[
q=p
\iff
\operatorname{Prime}(q)\land
\exists x\bigl(U_\Delta(q,x)\land\neg B_p(x)\bigr).
\]

То есть разные формулы могут индивидуально различать множество отдельных prime atoms, хотя единой формулы, задающей standard order или successor, всё ещё нет.

В терминах программы:

\[
\boxed{
\text{pointwise distinguishability}\ne\text{uniform orientation}.
}
\]

---

## 18. Следующая граница: Uniformly Indexed Locality

Предыдущее следствие показывает, что переход от конечного к бесконечному числу **отдельно именованных** stationary predicates сам по себе не является first-order phase transition.

Качественно иной язык появляется, когда place становится переменной структуры через единое отношение

\[
\mathsf B(\ell,x)
\iff
v_\ell(x)\ge0.
\]

Теперь одна formula может квантифицировать по неограниченному числу places. Для rational \(x\) формула

\[
\forall\ell\,
\bigl(\operatorname{Prime}(\ell)\to\mathsf B(\ell,x)\bigr)
\]

говорит об отсутствии любого prime denominator и поэтому определяет

\[
\mathbb Z\subseteq\mathbb Q.
\]

Именно здесь перестаёт работать finite syntactic-support mechanism настоящей статьи.

Мы не утверждаем, что uniformly indexed atlas имеет GIR∞, определяет prime successor или интерпретирует полную арифметику. Это следующая открытая граница.

---

## 19. Stationary information и scalable information

Теорема показывает, что expressive strength нельзя измерять просто числом локальных битов информации.

Для fixed formula конечное число stationary places даёт конечное произведение конечных local color spaces. Добавление новых мест может резко увеличить число цветов, но оно остаётся конечным и связано с синтаксисом данной формулы.

Что действительно отсутствует в доказанном слое - это механизм, превращающий fixed local windows в uniformly variable scale или coordinate. Поэтому естественная рабочая граница имеет вид

\[
\boxed{
\text{stationary local information}
\quad\Big|\quad
\text{uniformly scalable local information}.
}
\]

Теорема устанавливает один строгий регион слева от этой границы. Она не утверждает, что любой scalable observable обязательно даёт GIR∞, и не утверждает, что stationary locality является единственным возможным механизмом compression.

---

## 20. Связь с классической теорией моделей

Target sort относится к классической model theory абелевых групп и модулей. Результаты Шмелевой, теорема Баура об elimination для modules и теория abelian structures Фишера дают естественный фон для positive-primitive geometry с выделенными additive subgroups.

В данной работе необходимая target normal form доказывается напрямую через local coverage и weak approximation, поэтому общий machinery не используется как чёрный ящик.

Source sort - арифметика Сколема. Её model theory не является глобально «ручной» в смысле classical stability theory. Поэтому finite GIR нельзя понимать как stability или NIP. Аналогично, статья доказывает только неопределимость стандартного prime order и prime successor и конечность GIR каждого fixed isolator; она не доказывает decidability complete theory и не утверждает невозможность любой интерпретации арифметики.

---

## 21. Заключение

Один fixed p-adic ball дал первую внутреннюю точку между чистой симметрией prime atoms и ранее найденными grid-amplification mechanisms. Настоящая теорема превращает эту точку в целый регион.

Для каждого finite stationary atlas \(S\) Private-Place Bridge обладает Formula-Relative Tail Symmetry. В случае меток Рамануджана это верно для любого конечного атласа и formula-by-formula для полного семейства отдельно именованных local predicates.

Доказательство разделяет два типа информации. Fixed-depth local conditions сжимаются в конечное число formula-relative colors. Exact affine accidents контролируются private denominator places, а non-pinned target witness остаётся подвижным, потому что всегда можно выбрать больше fresh private places, чем фиксированная affine template способна упомянуть prime labels.

Центральный результат можно сжать в одну формулу мысли:

\[
\boxed{
\text{конечное число stationary local windows нарушает симметрию, но не создаёт scalable prime-addressing machine}.
}
\]

Следующий эксперимент начинается там, где сам local place получает право двигаться как first-order variable.

---

## Литература

1. W. Szmielew, **Elementary properties of Abelian groups**, *Fundamenta Mathematicae* **41** (1955), 203-271. DOI: 10.4064/fm-41-2-203-271.

2. W. Baur, **Elimination of quantifiers for modules**, *Israel Journal of Mathematics* **25** (1976), 64-70. DOI: 10.1007/BF02756561.

3. E. R. Fisher, **Abelian structures. I**, in *Abelian Group Theory*, Lecture Notes in Mathematics **616**, Springer, 1977, 270-322.

4. S. Ramanujan, **On certain arithmetical functions**, *Transactions of the Cambridge Philosophical Society* **22** (1916), 159-184.

5. P. Deligne, **Formes modulaires et représentations ℓ-adiques**, Séminaire Bourbaki, Exp. 355, Lecture Notes in Mathematics **179**, Springer, 1971, 139-172.

6. A. Stonestrom, **Some model theory of Th(N,·)**, *Mathematical Logic Quarterly* **68** (2022), 288-303. DOI: 10.1002/malq.202100049.

7. A. Bès and C. Richard, **Undecidable extensions of Skolem arithmetic**, *Journal of Symbolic Logic* **63** (1998). DOI: 10.2307/2586837.

---

## Авторская заметка

Работа входит в исследовательскую программу «Riemann Hypothesis - Commander Sol» и продолжает линию Prime-Successor Algebra / Two Walls. Термины **Private-Place Bridge**, **Finite Stationary Locality**, **Formula-Relative Tail Symmetry**, **bounded-anchor cylinder** и **Grid-Isolation Rank** используются как рабочие термины программы для выделенных здесь механизмов.
