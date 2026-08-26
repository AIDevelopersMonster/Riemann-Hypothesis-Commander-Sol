# Размышлизмы о стационарной локальности с Commander Sol
## Private-Place Bridges, конечные мульти-адические окна и формульно-локальное сжатие

**Alex Malachevsky**  
ORCID: 0009-0008-6009-3196  
2026

## Аннотация

Мы исследуем двухсортное расширение арифметики Сколема, в котором простые атомы связаны с рациональными метками, а целевая аддитивная группа снабжена конечным набором фиксированных p-адических предикатов интегральности. Мотивирующий пример задаётся метками Рамануджана

\[
u_p=\frac{\tau(p)^2-p^{11}}{p^{11}}.
\]

Ранее для одного фиксированного p-адического шара было установлено, что такой локальный наблюдатель разрушает часть симметрии простых, но не восстанавливает стандартный порядок и отношение следующего простого. В этой работе мы выделяем механизм этого явления и доказываем конечную multi-place версию.

Для целевой структуры

\[
\mathcal A_S=(\mathbb Q,+,0,(B_\ell)_{\ell\in S}),
\qquad B_\ell(x)\iff v_\ell(x)\ge0,
\]

где \(S\) конечно, доказывается finite-depth normal form: каждая формула целевого сорта эквивалентна булевой комбинации точных рациональных линейных уравнений и условий фиксированной глубины \(L(\bar x)\in B_{\ell,m}\). Для класса **Private-Place Bridges** точные аффинные отношения между метками простых контролируются приватными знаменательными местами, а незакреплённые target-свидетели можно переносить внутри multi-place cell с помощью свежих private places вне стационарного атласа.

Это приводит к **Finite Stationary Locality Theorem**: для каждой фиксированной first-order формулы существует конечное исключительное множество простых и конечный вектор глубин по местам, после чего истинность формулы на хвосте простых инвариантна относительно допустимых перестановок, сохраняющих конечные локальные цветовые классы и точные defect-классы. Отсюда следуют неопределимость стандартного порядка и отношения следующего простого, а также конечность Grid-Isolation Rank для каждого фиксированного isolator.

Для меток Рамануджана гипотезы теоремы выполняются для любого конечного stationary atlas. Более того, даже бесконечное семейство отдельно именованных предикатов \((B_\ell)_{\ell\in\mathbb P}\) остаётся формула-за-формулой конечным: обычная first-order формула содержит лишь конечное число имён мест. Поэтому настоящая следующая граница проходит не между конечным и бесконечным списком именованных локальных окон, а между stationary named atlas и **uniformly indexed atlas**, где место само становится first-order переменной через отношение \(\mathsf B(\ell,x)\).

---

## 1. От одного фиксированного шара к стационарному атласу

Вопрос этой работы состоит не в том, сколько арифметической информации можно добавить к умножению, а в том, можно ли эту информацию переносить и масштабировать.

В структуре

\[
(\mathbb N_{>0},\times)
\]

простые числа выступают мультипликативными атомами. Любая перестановка простых продолжаетcя до автоморфизма всей структуры, если сохранять показатели в разложении на простые множители. Поэтому определение стандартного порядка или следующего простого требует разрушить эту симметрию согласованным способом.

Один естественный способ — связать каждый простой атом \(p\) с рациональной меткой \(u_p\). В нашем основном примере

\[
\Delta(q)=q\prod_{n\ge1}(1-q^n)^{24}
=\sum_{n\ge1}\tau(n)q^n
\]

и

\[
u_p=\frac{\tau(p)^2}{p^{11}}-1.
\]

Целевой аддитивный сорт может наблюдать эти метки через локальные p-адические окна

\[
B_\ell(x)\iff v_\ell(x)\ge0.
\]

Один фиксированный наблюдатель способен различать некоторые простые, но фиксированная формула не получает автоматически возможность превратить глубину \(m\) в

\[
B_{\ell,m}=\{x:v_\ell(x)\ge m\}
\]

в движущуюся внутреннюю координату.

При нескольких местах возникает потенциально опасная новая геометрия. Для \(\ell_1\) и \(\ell_2\) локальные подгруппы уже не образуют одну цепь; появляется решётка, а китайская теорема об остатках позволяет одновременно удовлетворять независимым локальным условиям. Возникает естественное подозрение: не может ли одно место кодировать строки, другое столбцы, а аддитивная структура — точки их пересечения?

Основной результат показывает, что при Private-Place гипотезах этого не происходит. Конечное число стационарных мест увеличивает число цветов, различимых фиксированной формулой, но не создаёт масштабируемую систему адресации.

Это явление мы называем **стационарной локальностью**.

---

## 2. Двухсортная структура

Пусть

\[
S=\{\ell_1,\dots,\ell_s\}
\]

— конечное множество рациональных простых.

Source sort:

\[
\mathcal N=(\mathbb N_{>0},\times).
\]

Prime atoms first-order определимы как неприводимые неединичные элементы. Любая перестановка prime atoms продолжается до автоморфизма \(\mathcal N\).

Target sort:

\[
\mathcal A_S=(\mathbb Q,+,0,(B_\ell)_{\ell\in S}),
\]

где

\[
B_\ell(x)\iff v_\ell(x)\ge0.
\]

Bridge \(U\) связывает два сорта. На простых он функционален:

\[
U(p,x)\iff x=u_p.
\]

Мы требуем **prime-only bridge**:

\[
U(n,x)\Longrightarrow \operatorname{Prime}(n).
\]

Это означает, что bridge не передаёт в target sort показатель степени из \(p^k\). Источник может видеть prime powers, но целевой сорт получает только метку самого prime atom.

Обозначим всю структуру через

\[
\mathcal B_{u,S}=\bigl(\mathcal N,\mathcal A_S,U\bigr).
\]

---

## 3. Private-Place Bridges

После удаления конечного множества исключительных prime atoms предположим, что оставшиеся простые распадаются на бесконечное множество regular primes \(R\) и конечное число exact defect classes

\[
D_1,\dots,D_t.
\]

Каждый defect class \(D_j\) имеет одну фиксированную рациональную метку \(\delta_j\).

Для regular primes предполагаем следующее.

### H1. Интегральность в стационарных местах

Для каждого \(p\in R\) и каждого \(\ell\in S\):

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

а для всех различных \(p,q\in R\)

\[
v_{\lambda(p)}(u_q)\ge0.
\]

То есть у каждой regular label имеется собственное знаменательное место, не принадлежащее никакой другой regular label.

Поскольку defect labels рациональны и их конечное число, их общий denominator support конечен. После увеличения конечного exceptional set можно также считать, что

\[
v_{\lambda(p)}(\delta_j)\ge0
\]

для всех regular \(p\) и всех defect labels.

Такую структуру будем называть **Private-Place Bridge над stationary atlas \(S\)**.

---

## 4. Предикаты фиксированной глубины

Для фиксированного \(m\in\mathbb Z\) положим

\[
B_{\ell,m}(x)\iff v_\ell(x)\ge m.
\]

Мы не добавляем variable depth в язык. Для каждого фиксированного \(m\) этот предикат уже определим через \(B_\ell\).

При \(m>0\)

\[
B_{\ell,m}(x)
\iff
\exists y\,(\ell^m y=x\wedge B_\ell(y)),
\]

а

\[
B_{\ell,-m}(x)
\iff
B_\ell(\ell^m x).
\]

Поскольку \((\mathbb Q,+)\) uniquely divisible, умножение на фиксированный рациональный коэффициент задаётся линейным уравнением. Поэтому target literals можно писать в форме

\[
L(\bar x)=0
\]

и

\[
L(\bar x)\in B_{\ell,m}.
\]

---

## 5. Local Coverage Lemma

Зафиксируем одно место \(\ell\). Пусть

\[
P=a+B_{\ell,m}
\]

— положительный базовый косет, а

\[
C_i=b_i+B_{\ell,n_i}
\]

— конечное семейство запрещённых косетов.

Два \(\ell\)-адических шара либо не пересекаются, либо один содержится в другом. Поэтому \(C_i\cap P\) либо пусто, либо равно \(P\), либо является proper subcoset внутри \(P\).

Если один из \(C_i\) содержит \(P\), surviving set пуст. Иначе все существенные запреты имеют глубину не меньше \(m\). Пусть

\[
N=\max_i n_i.
\]

После refinement до общей глубины \(N\) вопрос покрытия \(P\) решается в конечной фактор-группе

\[
B_{\ell,m}/B_{\ell,N},
\]

причём

\[
\left|B_{\ell,m}/B_{\ell,N}\right|=\ell^{N-m}.
\]

Следовательно,

\[
P\setminus\bigcup_iC_i\ne\varnothing
\]

эквивалентно конечной булевой комбинации условий между центрами вида

\[
a-b_i\in B_{\ell,k},
\qquad
b_i-b_j\in B_{\ell,k}.
\]

Если положительного base coset в данном place нет, конечное число forbidden balls не покрывает всю \(\mathbb Q\): достаточно выбрать \(y\) с достаточно отрицательной \(\ell\)-адической valuation.

Важно: конечен не \(\mathbb Q/B_{\ell,m}\), а только refinement quotient \(B_{\ell,m}/B_{\ell,N}\).

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
\qquad \ell\in S,\ m\in\mathbb Z,
\]

причём для каждой фиксированной формулы используется лишь конечное число пар \((\ell,m)\).

### Доказательство

После DNF достаточно устранить один target quantifier \(\exists y\) из конъюнкции литералов.

Если имеется точное уравнение

\[
ay+t(\bar x)=0,
\qquad a\ne0,
\]

то оно однозначно задаёт

\[
y=-a^{-1}t(\bar x),
\]

и \(y\) устраняется подстановкой.

Пусть exact equation, закрепляющего \(y\), нет. Каждый positive local literal приводится к

\[
y\in a+B_{\ell,m}.
\]

Для фиксированного \(\ell\) пересекающиеся положительные шары вложены друг в друга, поэтому они сводятся к несовместимости либо одному deepest base coset. Negative ball conditions обрабатываются Local Coverage Lemma.

Так для каждого \(\ell\in S\) получаем непустое локальное открытое множество

\[
U_\ell\subseteq\mathbb Q_\ell,
\]

либо вся conjunction несовместима.

Если все \(U_\ell\) непусты, finite weak approximation для \(\mathbb Q\), эквивалентная прямой CRT-конструкции после очистки знаменателей, даёт рациональный \(y\), лежащий одновременно во всех \(U_\ell\).

Exact inequalities

\[
y\ne c_1,\dots,y\ne c_r
\]

удаляют лишь конечное число точек. Любая непустая multi-place cell содержит достаточно глубокий косет

\[
a+\bigcap_{\ell\in S}B_{\ell,M_\ell}
\]

и поэтому бесконечна. Конечное удаление точек её не уничтожает.

Повторяя аргумент, устраняем все target quantifiers. ∎

---

## 7. Generic Multi-Place Cell

### Лемма 7.1

Каждая непустая Boolean cell, заданная конечным числом fixed-depth target conditions, содержит refinement coset

\[
a+H_{\mathbf M},
\qquad
H_{\mathbf M}=\bigcap_{\ell\in S}B_{\ell,M_\ell}.
\]

### Доказательство

Берём одну точку \(a\) внутри cell. Для каждого place выбираем \(M_\ell\) глубже всех границ, встречающихся в конечном наборе литералов. Прибавление элемента из \(H_{\mathbf M}\) не меняет ни одного из этих memberships/non-memberships. ∎

---

## 8. Exact Linear Separation

Рассмотрим фиксированную homogeneous relation

\[
\sum_{i=1}^r c_i u_{p_i}=0.
\]

Сгруппируем одинаковые regular primes. Если block с representative \(p\) имеет ненулевой aggregate coefficient \(d\), то вне конечного множества случаев, когда \(\lambda(p)\mid d\),

\[
v_{\lambda(p)}(d u_p)<0.
\]

Все остальные regular labels и defect labels \(\lambda(p)\)-integral. Поэтому сумма не может быть нулём.

Поскольку \(\lambda\) инъективно, для фиксированных коэффициентов исключений конечное число.

### Лемма 8.1. Exact Linear Separation

На regular tail фиксированная homogeneous relation может выполняться только тогда, когда aggregate coefficient каждого regular equality block равен нулю, если не считать конечного coefficient-dependent exceptional set и exact defect classes.

В частности, regular labels инъективны на хвосте.

---

## 9. Reduced Affine Fibers и bounded-anchor cylinders

Наивное утверждение, что

\[
\sum_i c_i u_{p_i}=t
\]

имеет uniformly bounded число prime tuples, неверно из-за структурных сокращений equality blocks. Например,

\[
u_{p_1}-u_{p_2}+u_{p_3}=u_q
\]

имеет все решения

\[
(p_1,p_2,p_3)=(r,r,q).
\]

Поэтому фиксируем equality pattern \(\pi\). Для блока \(C\in\pi\) положим

\[
d_C=\sum_{i\in C}c_i.
\]

Блоки с \(d_C=0\) исчезают из reduced equation и остаются свободными.

### Лемма 9.1. Reduced Affine-Fiber Lemma

Для блоков с \(d_C\ne0\) число regular-prime assignments, удовлетворяющих reduced affine equation, равномерно ограничено величиной, зависящей только от coefficient scheme, после удаления конечного coefficient-dependent exceptional set.

### Доказательство

Пусть имеется одно reduced solution \((q_C)\) и другое \((q'_C)\). После вычитания получаем homogeneous relation. Если некоторый prime второго решения не встречается в первом, его private valuation появляется с ненулевым aggregate coefficient и не может быть компенсирована другими terms. Exact Linear Separation даёт противоречие.

Значит второе решение использует только конечный набор primes из первого решения. Если non-zero blocks всего \(m\), грубой оценки \(m^m\) достаточно. ∎

Таким образом exact affine traces являются конечными объединениями **bounded-anchor cylinders**: zero-sum blocks свободны, а non-zero blocks могут закреплять лишь конечный prime support.

---

## 10. Fresh-Private-Place Avoidance

Пусть non-empty target cell содержит

\[
a+H_{\mathbf M}.
\]

Пусть каждая relevant affine scheme с новой target variable \(y\) содержит не более \(r\) prime labels.

Выбираем regular primes

\[
t_1,\dots,t_{r+1}
\]

с private places

\[
q_j=\lambda(t_j)
\]

вне:

1. stationary atlas \(S\);
2. denominator support уже названных target parameters;
3. denominator support rational coefficients в finite template family.

Это возможно, поскольку \(R\) бесконечно, а \(\lambda\) инъективно.

Положим

\[
D=q_1\cdots q_{r+1}
\]

и выберем

\[
L=\prod_{\ell\in S}\ell^{N_\ell},
\qquad N_\ell\ge M_\ell.
\]

Пусть

\[
y=a+\frac{L}{D}.
\]

В каждом stationary place \(\ell\in S\) знаменатель \(D\) — unit, поэтому

\[
y\in a+H_{\mathbf M}.
\]

В каждом fresh private place \(q_j\) центр \(a\) интегрален и

\[
v_{q_j}(L/D)=-1,
\]

поэтому

\[
v_{q_j}(y)=-1.
\]

Рассмотрим forbidden affine value

\[
z=\alpha+\sum_{i=1}^{r}c_i u_{p_i}.
\]

Среди \(t_1,\dots,t_{r+1}\) найдётся \(t_k\), отсутствующий среди \(p_i\). Тогда при \(q_k\) все labels, входящие в \(z\), интегральны; параметры и коэффициенты тоже были выбраны \(q_k\)-integral. Значит

\[
v_{q_k}(z)\ge0,
\]

тогда как

\[
v_{q_k}(y)=-1.
\]

Следовательно,

\[
y\ne z.
\]

### Лемма 10.1. Fresh-Private-Place Avoidance

Внутри любой non-empty finite-depth multi-place cell можно выбрать rational witness, одновременно избегающий всех значений любой фиксированной конечной семьи affine schemes, использующих не более \(r\) prime labels.

Ключевой принцип:

\[
r+1\ \text{fresh private places} > r\ \text{label slots}.
\]

---

## 11. Finite Template Closure и Target-Witness Transport

Зафиксируем mixed first-order formula \(\Phi\). Её синтаксис содержит только конечное число coefficients, source terms, bridge occurrences и local depths.

Замкнём этот конечный набор под операциями, возникающими при устранении target variable:

- подстановка из pinning equation;
- разности simultaneous pinning equations;
- finite refinements из Theorem 6.1;
- exact affine consequences после подстановки.

Получаем finite **template closure** для \(\Phi\).

Выбираем depth vector

\[
\mathbf K_\Phi=(K_{\Phi,\ell})_{\ell\in S}
\]

достаточно глубокий для всех fixed-depth templates в closure.

Для regular prime определяем formula-relative color

\[
c_{\mathbf K_\Phi}(p)
=
\bigl(u_p+B_{\ell,K_{\Phi,\ell}}\bigr)_{\ell\in S}.
\]

По H1 число цветов конечно. При неотрицательных глубинах можно использовать bound

\[
\prod_{\ell\in S}\ell^{K_{\Phi,\ell}}.
\]

Пусть \(\sigma\) — перестановка prime atoms, фиксирующая конечный exceptional set, сохраняющая regular color classes и каждый exact defect class.

### Pinned case

Если истинно

\[
ay+t=0,
\qquad a\ne0,
\]

то переносим все prime labels в \(t\) через \(\sigma\) и определяем \(y'\) из перенесённого уравнения.

Если pinning equations несколько,

\[
a_1y+t_1=0,
\qquad
a_2y+t_2=0,
\]

их совместимость эквивалентна

\[
a_2t_1-a_1t_2=0.
\]

Это template без \(y\), включённый в finite closure.

### Free case

Если ни один relevant exact instance не закрепляет \(y\), перенесённые local literals задают non-empty finite-depth cell. По Lemma 7.1 она содержит полный refinement coset. Fresh-Private-Place Avoidance выбирает внутри него witness \(y'\), сохраняя local profile и избегая всех exact affine incidences, которые должны оставаться ложными.

Так target witnesses транспортируются для finite fragment, порождённого \(\Phi\).

---

## 12. Finite Stationary Locality Theorem

### Теорема 12.1

Пусть \(S\) конечно и \(\mathcal B_{u,S}\) является Private-Place Bridge, удовлетворяющим гипотезам Section 3. Для каждой parameter-free first-order formula

\[
\Phi(\bar p)
\]

со свободными source variables, ограниченными prime atoms, существуют:

- конечное исключительное множество простых \(F_\Phi\);
- конечный multi-place depth vector \(\mathbf K_\Phi\),

такие что

\[
\mathcal B_{u,S}\models\Phi(\bar p)
\iff
\mathcal B_{u,S}\models\Phi(\sigma\bar p)
\]

для каждой prime permutation \(\sigma\), которая:

1. фиксирует \(F_\Phi\) поточечно;
2. сохраняет каждый regular color class \(c_{\mathbf K_\Phi}\);
3. сохраняет каждый exact defect class setwise.

### Доказательство

Индукция по синтаксису \(\Phi\).

Каждая перестановка prime atoms продолжается до автоморфизма \((\mathbb N_{>0},\times)\), поэтому source atomic formulas сохраняются. Bridge atom с composite source input ложен до и после transport. Bridge atom на prime — точное target incidence и входит в finite template family.

Boolean connectives сохраняются непосредственно.

Для existential source witness \(n\) берём его образ под multiplicative automorphism, индуцированным \(\sigma\).

Для existential target witness используем Pinned/Free Target-Witness Transport из Section 11.

Universal quantifiers устраняются через negation. Exceptional set увеличивается лишь конечное число раз вдоль конечного syntax tree и finite template closure. ∎

Это и есть **Formula-Relative Tail Symmetry**.

Теорема является formula-relative: она не утверждает существование одной глобальной группы автоморфизмов всей двухсортной структуры. Допустимое tail partition зависит от конкретной формулы.

---

## 13. Порядок и следующий простой

### Следствие 13.1. Стандартный порядок простых не определим

Отношение \(<_{\mathbb P}\) не определимо в \(\mathcal B_{u,S}\).

### Доказательство

У candidate formula существует конечное число movable classes вне finite exceptional set. Поскольку regular tail бесконечен, один класс содержит два различных простых \(p,q\). Их перестановка допустима, но strict linear order не может быть инвариантен относительно такой перестановки. ∎

### Следствие 13.2. Prime successor не определим

Стандартное отношение

\[
\operatorname{Succ}_{\mathbb P}(p,q)
\]

не определимо в \(\mathcal B_{u,S}\).

### Доказательство

Вне finite exceptional set существует бесконечно много consecutive prime pairs. Ordered movable class pairs конечное число, поэтому один class pair встречается для двух различных consecutive pairs

\[
(p,q),\qquad(p',q').
\]

Простые \(q,q'\) находятся в одном movable class. Меняем их местами, фиксируя \(p\). Hypothetical successor formula сохраняется, но фактический successor меняется. Противоречие. ∎

В этом доказательстве не используется density theorem для возможных zero primes.

---

## 14. Grid-Isolation Rank

Для фиксированной формулы \(I(p,q;r)\) говорим, что она изолирует \(n\times n\) grid, если существуют distinct row primes \(p_1,\dots,p_n\), distinct column primes \(q_1,\dots,q_n\) и markers \(r_{ij}\) такие, что

\[
I(p_k,q_l;r_{ij})
\iff
(k,l)=(i,j).
\]

Супремум таких \(n\) обозначим \(\operatorname{GIR}(I)\).

### Следствие 14.1

Для каждой фиксированной isolator formula \(I\)

\[
\operatorname{GIR}(I)<\infty.
\]

### Доказательство

Применяем Theorem 12.1 к \(I\). Вне finite exceptional set имеется лишь конечное число movable classes. В достаточно большой row family один класс содержит достаточно row primes, чтобы для выбранного column и marker переставить две строки, фиксируя column и marker. Formula-relative invariance заставит один marker изолировать две строки в одном столбце, что противоречит определению isolation. ∎

Это не утверждение NIP или model-theoretic stability. GIR — более узкий programme invariant, измеряющий конкретную способность uniform cell isolation.

---

## 15. Применение к меткам Рамануджана

Пусть

\[
u_p=\frac{\tau(p)^2-p^{11}}{p^{11}}.
\]

Зафиксируем finite stationary atlas \(S\).

### 15.1. Интегральность вне собственного простого

Если \(p\notin S\), то denominator \(p^{11}\) является \(\ell\)-adic unit для каждого \(\ell\in S\). Поэтому

\[
v_\ell(u_p)\ge0.
\]

Это H1.

### 15.2. Private denominator для good prime

Назовём \(p\ge5\) good, если

\[
\tau(p)\ne0.
\]

Пусть

\[
a=v_p(\tau(p)).
\]

По оценке Делиня

\[
|\tau(p)|\le2p^{11/2}.
\]

Если \(a\ge6\), то \(|\tau(p)|\ge p^6\), откуда

\[
p^6\le2p^{11/2},
\]

то есть \(\sqrt p\le2\), что невозможно при \(p\ge5\). Значит

\[
a\le5.
\]

Так как \(2a<11\),

\[
v_p(\tau(p)^2-p^{11})=2a,
\]

и потому

\[
v_p(u_p)=2a-11<0.
\]

Для \(q\ne p\) denominator \(u_q\) — степень \(q\), поэтому

\[
v_p(u_q)\ge0.
\]

Следовательно, на good-prime tail можно взять

\[
\lambda(p)=p.
\]

### 15.3. Zero-prime defect class

Если

\[
\tau(p)=0,
\]

то

\[
u_p=-1.
\]

Все такие primes, если существуют, образуют один exact common-label defect class.

### 15.4. Бесконечно много good primes без плотностной теоремы

Для общей теоремы нужен бесконечный резерв regular primes. Его можно получить из классических фактов без density estimate для возможных нулей \(\tau(p)\).

Для prime \(p\) известна конгруэнция Рамануджана

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

следовательно \(\tau(p)\ne0\). По теореме Дирихле в прогрессии \(1\bmod691\) существует бесконечно много простых.

Значит good regular primes бесконечно много.

### Следствие 15.1. Finite stationary Ramanujan atlases

Для каждого конечного \(S\) структура

\[
\mathcal B_{\Delta,S}
=
\Bigl((\mathbb N_{>0},\times),(\mathbb Q,+,0,(B_\ell)_{\ell\in S}),U_\Delta\Bigr)
\]

обладает Formula-Relative Tail Symmetry. Стандартный prime order и prime successor не определимы, а каждый fixed isolator имеет finite GIR.

---

## 16. Infinite Named Stationary Atlas

Рассмотрим язык с отдельным predicate \(B_\ell\) для каждого rational prime:

\[
\mathcal A_{\mathrm{name}}
=
(\mathbb Q,+,0,(B_\ell)_{\ell\in\mathbb P}).
\]

Язык бесконечен, но каждая first-order formula — конечная строка и потому упоминает лишь конечное множество place symbols

\[
S_\Phi\subset\mathbb P.
\]

Для Ramanujan bridge все primes вне \(S_\Phi\) \(S_\Phi\)-integral. Значит finite theorem применяется к каждой \(\Phi\) отдельно.

### Следствие 16.1

Ramanujan structure с separately named \(B_\ell\) для всех primes остаётся formula-by-formula compressed.

При этом для good prime \(p\) предикат \(B_p\) индивидуально выделяет \(p\):

\[
q=p
\iff
\operatorname{Prime}(q)
\wedge
\exists x\bigl(U_\Delta(q,x)\wedge\neg B_p(x)\bigr).
\]

Итак, многие prime atoms могут быть индивидуально различимы, хотя единой formula для стандартного порядка или successor по-прежнему нет.

В programme terminology:

\[
\boxed{\text{pointwise distinguishability}\ne\text{uniform orientation}.}
\]

---

## 17. Где находится следующая граница

Граница

\[
|S|<\infty
\quad\text{versus}\quad
|S|=\infty
\]

сама по себе не является first-order phase transition, если места лишь отдельно названы.

Качественно новый язык появляется, если ввести place sort и единое отношение

\[
\mathsf B(\ell,x)
\iff
v_\ell(x)\ge0,
\]

где \(\ell\) становится first-order переменной.

Теперь одной формулой можно агрегировать информацию по неограниченному числу places. Например,

\[
\forall\ell\,
\bigl(\operatorname{Prime}(\ell)\rightarrow\mathsf B(\ell,x)\bigr)
\]

для rational \(x\) выражает отсутствие любого простого в знаменателе, то есть определяет

\[
\mathbb Z\subset\mathbb Q.
\]

Finite-syntax support barrier исчезает.

Мы называем это **Uniformly Indexed Atlas Problem**. В этой статье не утверждается, что такая структура имеет GIR∞, определяет prime successor или интерпретирует полную арифметику. Мы лишь указываем точку, где механизм настоящего доказательства перестаёт применяться.

---

## 18. Stationary versus scalable information

Теорема показывает принципиальное различие между локальной информацией и масштабируемой локальной информацией.

Fixed-depth predicates

\[
B_{\ell,m}
\]

создают конечное число residue/depth colors, релевантных конкретной формуле. Несколько независимых places перемножают число цветов, но для фиксированной формулы оно остаётся конечным.

Поэтому важный переход имеет вид не

\[
\text{мало информации}\to\text{много информации},
\]

а скорее

\[
\boxed{\text{stationary local information}\to\text{uniformly scalable local information}.}
\]

Настоящая теорема доказывает существование одного строгого внутреннего режима этой фазовой картины. Она не утверждает, что stationary locality является единственным безопасным механизмом и не утверждает, что всякая scalable observable автоматически даёт GIR∞.

---

## 19. Связь с классической теорией моделей

Аддитивная target structure лежит в области теории моделей абелевых групп и модулей. Работы Шмелева и Baur-Monk дают классический фон, в котором definability сводится к pp-геометрии и конечным invariant data; abelian structures Фишера дают естественную среду для аддитивных групп с выделенными подгруппами.

В этой работе используется более узкий прямой путь. Нам не нужна полная классификация теории

\[
(\mathbb Q,+,0,(B_\ell)_{\ell\in S}).
\]

Local Coverage Lemma и finite weak approximation дают ровно ту target normal form, которая нужна для bridge theorem.

Также finite GIR не следует отождествлять с model-theoretic stability. Pure Skolem arithmetic сама обладает существенной комбинаторной сложностью. GIR измеряет только конкретный механизм uniform cell isolation, введённый в этой программе.

Наконец, наши выводы слабее глобальной non-interpretability: мы доказываем неопределимость стандартного prime order и successor и конечность GIR для каждого фиксированного isolator. Мы не утверждаем decidability полной теории, NIP, stability или невозможность любой интерпретации арифметики.

---

## 20. Что теперь находится внутри коридора

Fixed-Ball construction дала одну внутреннюю точку между multiplicative prime symmetry и right-wall grid-amplification mechanisms. Настоящая теорема превращает эту точку в область.

Для Ramanujan bridge имеем семейство

\[
\{\mathcal B_{\Delta,S}:|S|<\infty\},
\]

а formula-by-formula также полный named stationary atlas

\[
(\mathbb Q,+,0,(B_\ell)_{\ell\in\mathbb P}).
\]

В этом режиме:

- stationary local information различает некоторые primes;
- каждая fixed formula видит лишь finite local colors;
- exact affine accidents имеют форму bounded-anchor cylinders;
- свежие private places остаются доступны вне observed atlas;
- target witnesses транспортируются;
- стандартные prime order и successor остаются неопределимыми;
- каждый fixed grid-isolator имеет finite GIR.

Следующая граница уже не проходит между одним и несколькими p-adic balls и не между конечным и бесконечным списком named balls. Она проходит между stationary names и uniformly quantified local coordinate:

\[
(B_\ell)_{\ell\in\mathbb P}
\quad\Big|\quad
\mathsf B(\ell,x).
\]

---

## 21. Заключение

Основной результат можно выразить одной фразой:

\[
\boxed{\text{конечное число стационарных локальных окон разрушает симметрию, но не создаёт масштабируемую машину адресации простых}.}
\]

Target half доказательства сводит finite multi-adic additive geometry к fixed-depth local cells. Bridge half использует private denominator places для контроля exact relations и выбирает для non-pinned witness больше свежих private places, чем любая фиксированная affine scheme способна упомянуть.

Вместе эти два механизма дают Formula-Relative Tail Symmetry.

Для Ramanujan labels результат применяется ко всякому finite stationary atlas и formula-by-formula к infinite named atlas. Тем самым фазовая картина Prime-Successor programme становится точнее: решающим ресурсом оказывается не просто локальная информация, а способность сделать сам локальный индекс переменным и масштабируемым внутри first-order формулы.

---

## Литература

1. W. Szmielew, **Elementary properties of Abelian groups**, *Fundamenta Mathematicae* **41** (1955), 203–271. DOI: 10.4064/fm-41-2-203-271.

2. W. Baur, **Elimination of quantifiers for modules**, *Israel Journal of Mathematics* **25** (1976), 64–70. DOI: 10.1007/BF02756561.

3. E. R. Fisher, **Abelian structures. I**, in *Abelian Group Theory*, Lecture Notes in Mathematics **616**, Springer, 1977, 270–322.

4. S. Ramanujan, **On certain arithmetical functions**, *Transactions of the Cambridge Philosophical Society* **22** (1916), 159–184.

5. P. Deligne, **Formes modulaires et représentations ℓ-adiques**, Séminaire Bourbaki, Exp. 355, Lecture Notes in Mathematics **179**, Springer, 1971, 139–172.

6. A. Stonestrom, **Some model theory of Th(N,·)**, *Mathematical Logic Quarterly* **68** (2022). DOI: 10.1002/malq.202100049.

7. A. Bès and C. Richard, **Undecidable extensions of Skolem arithmetic**, *Journal of Symbolic Logic* **63** (1998). DOI: 10.2307/2586837.

---

## Авторская заметка

Работа входит в исследовательскую программу “Riemann Hypothesis — Commander Sol” и продолжает линию Prime-Successor Algebra / Two Walls. Термины **Private-Place Bridge**, **Finite Stationary Locality**, **Formula-Relative Tail Symmetry**, **bounded-anchor cylinder** и **Grid-Isolation Rank** используются как терминология программы для организации доказанных здесь механизмов.
