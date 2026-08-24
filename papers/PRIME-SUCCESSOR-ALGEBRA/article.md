# Размышлизмы о следующем простом с Commander Sol

## Prime-Successor Algebra between Symmetry, Rigidity and Full Arithmetic

**Alex Malachevsky**  
ORCID: **0009-0008-6009-3196**  
Zenodo DOI: **10.5281/zenodo.22077920**  
Date: **24 August 2026**

---

## Аннотация

В мультипликативной арифметике Сколема $(\mathbb N_{>0},\times)$ простые числа естественно определимы как мультипликативные атомы, однако их стандартный порядок $2<3<5<7<11<\cdots$ не определяется: произвольная перестановка простых продолжается до автоморфизма мультипликативного моноида. Отсюда возникает узкий вопрос: какой минимальный дополнительный слой структуры требуется, чтобы атомы получили именно стандартную ориентацию и стало first-order определимо отношение следующего простого $S_{\mathbb P}$, но при этом еще не восстанавливалась полная арифметика $(\mathbb N,+,\times)$?

В заметке формализуется несколько шагов этой границы. Доказывается автоморфизмный барьер для любого расширения, определяющего prime successor. Затем показано, что при наличии умножения отношение $S_{\mathbb P}$ и обычный порядок, ограниченный простыми, first-order интеропределимы. В сочетании с теоремой Maurin это дает разрешимый промежуточный уровень между чистой мультипликативной арифметикой и полной арифметикой.

Далее доказывается общий **Dilation-Collapse Theorem**: всякая унарная функция $F$, монотонная по делимости вдоль обычного порядка и имеющая неограниченно много собственных скачков, уже позволяет first-order определить обычный порядок всех положительных натуральных. В частности, $R(n)=\operatorname{rad}(n!)$, кумулятивный НОК и факториал оказываются слишком сильными кандидатами: вместе с умножением они восстанавливают обычный порядок, а затем, по Julia Robinson, и сложение.

Наконец, для расширения $(\mathbb N_{>0},\times,\varphi)$ доказывается pointwise definability: каждый конкретный натуральный элемент определим без параметров. Это влечет полную жесткость структуры, но само по себе не дает единой равномерной формулы порядка простых. Центральный оставшийся вопрос формулируется как граница между индивидуализацией атомов и их uniform orientation.

**Ключевые слова:** Skolem arithmetic, prime successor, definability, decidability, automorphisms, Euler totient, pointwise definability, prime order, arithmetic expansions.

---

## Abstract

In Skolem arithmetic $(\mathbb N_{>0},\times)$ prime numbers are naturally definable as multiplicative atoms, whereas their usual order is not: every permutation of the primes extends to an automorphism of the multiplicative monoid. This suggests a narrow definability problem: what is the weakest additional structure that orients the atoms in the standard prime sequence and makes the prime-successor relation $S_{\mathbb P}$ first-order definable, while still failing to recover full arithmetic $(\mathbb N,+,\times)$?

We establish an automorphism obstruction for every expansion defining prime successor. We then show that, in the presence of multiplication, prime successor and the usual order restricted to primes are first-order interdefinable. Together with Maurin's decidability theorem, this yields a genuine decidable intermediate level between pure multiplication and full arithmetic.

We next prove a general **Dilation-Collapse Theorem**: any unary function $F$ which is divisibility-monotone along the ordinary order and has unboundedly many proper jumps already first-order defines the usual order on all positive integers. Consequently, the cumulative radical $R(n)=\operatorname{rad}(n!)$, cumulative least common multiple, and factorial all cross the right-hand boundary into full arithmetic once multiplication is present.

Finally, we prove that $(\mathbb N_{>0},\times,\varphi)$ is pointwise definable: every positive integer is parameter-free definable. Thus all multiplicative atoms are individually named and the structure is rigid. This does not by itself supply one uniform first-order formula for the standard order on primes. The remaining problem is therefore sharpened to the gap between individualization and uniform orientation.

---

# 1. От простоты к следующему простому

В структуре

$$
(\mathbb N_{>0},\times)
$$

простые определимы без параметров как неединичные элементы, не разлагающиеся в произведение двух неединичных элементов. Иными словами, мультипликативная структура уже знает, **что такое простой**.

Но она не знает, почему атомы должны читаться именно как

$$
2,3,5,7,11,\ldots
$$

Если $\sigma:\mathbb P\to\mathbb P$ — произвольная перестановка множества простых, то отображение

$$
\widehat\sigma\!\left(\prod_p p^{e_p}\right)
=
\prod_p \sigma(p)^{e_p}
$$

является автоморфизмом $(\mathbb N_{>0},\times)$.

Отсюда исходная интуиция статьи:

> Умножение видит атомность и факторизационные координаты, но не их абсолютную ориентацию.

Дальнейший вопрос не о тесте простоты и не о формуле prime gaps. Он о цене ориентации:

$$
\boxed{\text{сколько структуры нужно добавить, чтобы определить }p_k\mapsto p_{k+1}?}
$$

Везде ниже слово **definable** означает *first-order definable without parameters*, если явно не сказано иное.

---

# 2. Базовые first-order определения

Единица задается формулой

$$
\operatorname{One}(e)\;:\Longleftrightarrow\;\forall x\;(ex=x).
$$

Делимость определяется через умножение:

$$
a\mid b\;:\Longleftrightarrow\;\exists c\;(ac=b).
$$

Простота:

$$
\operatorname{Prime}(p)
:\Longleftrightarrow
\neg\operatorname{One}(p)
\land
\forall a\forall b\,
(ab=p\rightarrow \operatorname{One}(a)\lor\operatorname{One}(b)).
$$

Обозначим через $S_{\mathbb P}(p,q)$ отношение «$q$ — следующий простой после $p$», а через $p<_{\mathbb P}q$ — обычный числовой порядок, ограниченный простыми.

---

# 3. Лемма симметрийного барьера

## Лемма 1 (Automorphism obstruction)

Пусть

$$
\mathcal A_\Omega=(\mathbb N_{>0},\times,\Omega).
$$

Если $S_{\mathbb P}$ определимо в $\mathcal A_\Omega$, то всякий автоморфизм $\mathcal A_\Omega$ фиксирует каждый простой:

$$
\operatorname{Aut}(\mathcal A_\Omega)|_{\mathbb P}=\{\mathrm{id}\}.
$$

### Доказательство

Первый простой $2$ определяется как единственный простой без predecessor относительно $S_{\mathbb P}$. Поэтому любой автоморфизм фиксирует $2$. Затем он обязан фиксировать единственный $q$ с $S_{\mathbb P}(2,q)$, то есть $3$. После этого фиксируется $5$, затем $7$ и так далее. По внешней индукции фиксируются все простые. $\square$

### Замечание

Для чистого умножения вывод даже сильнее: никакой фиксированный конечный набор параметров не позволяет определить весь стандартный prime order. Всегда можно переставить два простых, не входящих в простые поддержки этих параметров, сохранив параметры поточечно.

Отсюда первый no-go фильтр:

$$
\boxed{\text{нетривиальная prime symmetry}\Longrightarrow S_{\mathbb P}\text{ неопределим}.}
$$

Но обратное неверно как логический принцип: отсутствие автоморфизмов само по себе еще не строит одной равномерной формулы порядка.

---

# 4. Как умножение превращает successor в порядок

В голой бесконечной successor-цепи локальное соседство и глобальный порядок first-order не обязаны совпадать: first-order логика не имеет оператора транзитивного замыкания.

Но в натуральных с умножением появляется необычная память: одно число кодирует конечное множество простых своими простыми делителями.

Для натурального $m$ положим

$$
D_m(r):\Longleftrightarrow \operatorname{Prime}(r)\land r\mid m.
$$

Определим $\operatorname{Segment}(m;p,q)$ как conjunction следующих условий:

1. $D_m(p)$ и $D_m(q)$;
2. внутри prime support числа $m$ у $p$ нет predecessor;
3. внутри prime support числа $m$ у $q$ нет successor;
4. каждый другой простой делитель $m$ имеет predecessor внутри support;
5. каждый другой простой делитель $m$ имеет successor внутри support.

Формально:

$$
D_m(p)\land D_m(q),
$$

$$
\neg\exists r\,(D_m(r)\land S_{\mathbb P}(r,p)),
$$

$$
\neg\exists r\,(D_m(r)\land S_{\mathbb P}(q,r)),
$$

$$
\forall r\left[(D_m(r)\land r\neq p)\to
\exists s\,(D_m(s)\land S_{\mathbb P}(s,r))\right],
$$

$$
\forall r\left[(D_m(r)\land r\neq q)\to
\exists s\,(D_m(s)\land S_{\mathbb P}(r,s))\right].
$$

## Теорема 2 (Prime-successor/order interdefinability)

В присутствии умножения $S_{\mathbb P}$ и $<_{\mathbb P}$ first-order интеропределимы:

$$
\boxed{
(\mathbb N_{>0},\times,S_{\mathbb P})
\equiv_{\mathrm{def}}
(\mathbb N_{>0},\times,<_{\mathbb P}).
}
$$

### Доказательство

Определим

$$
p\preceq_{\mathbb P}q
:\Longleftrightarrow
\operatorname{Prime}(p)\land\operatorname{Prime}(q)
\land
\exists m\,\operatorname{Segment}(m;p,q).
$$

Если $p=p_i$ и $q=p_j$ при $i\le j$, берем

$$
m=p_i p_{i+1}\cdots p_j.
$$

Его множество простых делителей является требуемым конечным successor-отрезком.

Обратно, prime support любого натурального $m$ конечен. Условия $\operatorname{Segment}$ дают в нем ровно одну вершину без predecessor и ровно одну вершину без successor. Дополнительный компонент невозможен: конечный дополнительный компонент имел бы собственный левый и правый концы. Цикл невозможен, поскольку стандартное отношение следующего простого ациклично. Поэтому support есть один конечный successor-отрезок от $p$ до $q$.

Тем самым $\preceq_{\mathbb P}$ определено через $S_{\mathbb P}$ и умножение. Строгий порядок получается добавлением $p\ne q$.

В обратную сторону

$$
S_{\mathbb P}(p,q)
\Longleftrightarrow
p<_{\mathbb P}q
\land
\neg\exists r\,(
\operatorname{Prime}(r)\land p<_{\mathbb P}r\land r<_{\mathbb P}q).
$$

$\square$

---

# 5. Разрешимый промежуточный уровень

Françoise Maurin доказала, что first-order теория положительных натуральных с multiplication и обычным порядком, ограниченным простыми, разрешима [1].

Из Теоремы 2 немедленно следует:

## Следствие 3

$$
\boxed{Th(\mathbb N_{>0},\times,S_{\mathbb P})\text{ разрешима}.}
$$

Кроме того, этот уровень строго сильнее чистого умножения из-за автоморфизмов последнего и строго слабее полной арифметики: если бы сложение определялось в $(\mathbb N,\times,<_{\mathbb P})$, то неразрешимая first-order теория полной арифметики переводилась бы в разрешимую теорию Maurin.

Получаем строгую цепь:

$$
\boxed{
(\mathbb N,\times)
<
(\mathbb N,\times,S_{\mathbb P})
\equiv_{\mathrm{def}}
(\mathbb N,\times,<_{\mathbb P})
<
(\mathbb N,+,\times).
}
$$

Иными словами, искомый «коридор» существует как строгий model-theoretic уровень. Открытым остается не его существование, а естественная реализация этого уровня без явного внесения prime order или prime successor.

---

# 6. Почти идеальный кандидат: cumulative radical

Рассмотрим

$$
R(n)=\operatorname{rad}(n!)=\prod_{p\le n}p.
$$

На первый взгляд функция очень близка к нужной. Она хранит, какие простые уже «появились» к моменту $n$, но стирает multiplicities. Казалось бы, она должна кодировать order-on-primes, не обязательно весь ordinary order.

Однако масштабирование аргумента превращает такую cumulative filtration в значительно более сильный объект.

---

# 7. Dilation-Collapse Theorem

Назовем функцию

$$
F:\mathbb N_{>0}\to\mathbb N_{>0}
$$

**divisibility-monotone**, если во внешнем обычном порядке

$$
a\le b\Longrightarrow F(a)\mid F(b).
$$

Пусть ее множество собственных скачков

$$
J_F=\{j\ge2:F(j-1)\ne F(j)\}.
$$

## Теорема 4 (Dilation-Collapse Theorem)

Если $F$ divisibility-monotone и $J_F$ неограниченно, то обычный строгий порядок всех положительных натуральных first-order определим в $(\mathbb N_{>0},\times,F)$. Более точно,

$$
\boxed{
x<y
\Longleftrightarrow
\exists t\;\bigl(F(tx)\mid F(ty)\land F(tx)\ne F(ty)\bigr).
}
$$

Правая часть означает строгую делимость; формально она записана как одновременное выполнение

$$
a\mid b\qquad\text{и}\qquad a\ne b.
$$

### Доказательство

Пусть $x\ge y$. Тогда для любого $t$ имеем $ty\le tx$, следовательно

$$
F(ty)\mid F(tx).
$$

Поэтому невозможно иметь одновременно $F(tx)\mid F(ty)$ и $F(tx)\ne F(ty)$: делимость положительных натуральных антисимметрична. Правая часть формулы ложна.

Теперь пусть $x<y$. Выберем jump point $j\in J_F$ настолько большим, чтобы

$$
\frac{j(y-x)}{xy}>1.
$$

Это возможно, поскольку $J_F$ неограниченно. Интервал

$$
\left[\frac jy,\frac jx\right)
$$

имеет длину больше единицы, поэтому содержит положительное целое $t$. Тогда

$$
tx<j\le ty.
$$

Так как $tx$ и $j$ целы,

$$
tx\le j-1.
$$

По монотонности по делимости

$$
F(tx)\mid F(j-1).
$$

Поскольку $j$ — собственный скачок,

$$
F(j-1)\mid F(j),\qquad F(j-1)\ne F(j).
$$

А из $j\le ty$ следует

$$
F(j)\mid F(ty).
$$

Таким образом,

$$
F(tx)\mid F(j-1)\mid F(j)\mid F(ty),\qquad F(j-1)\ne F(j),
$$

следовательно

$$
F(tx)\mid F(ty)\quad\text{и}\quad F(tx)\ne F(ty).
$$

$\square$

### Смысл

Не имеет значения, насколько редки скачки. Достаточно, что они уходят сколь угодно далеко. Масштабирование $x\mapsto tx$ растягивает любой ненулевой промежуток между $x$ и $y$ до тех пор, пока он не захватит один из скачков.

Поэтому cumulative divisibility history оказывается скрытым измерителем ordinary magnitude.

---

# 8. Три следствия collapse

## Следствие 5: cumulative radical

Для

$$
R(n)=\operatorname{rad}(n!)
$$

собственный скачок происходит ровно при простом $n$. Простых бесконечно много, поэтому

$$
\boxed{x<y\Longleftrightarrow\exists t\;\bigl(R(tx)\mid R(ty)\land R(tx)\ne R(ty)\bigr).}
$$

Следовательно, обычный $<$ определим в $(\mathbb N,\times,R)$.

## Следствие 6: cumulative LCM

Для

$$
L(n)=\operatorname{lcm}(1,\ldots,n)
$$

скачки происходят на степенях простых; множество скачков неограниченно. Поэтому $<$ определим в $(\mathbb N,\times,L)$.

## Следствие 7: factorial

Для $F(n)=n!$ собственные скачки происходят при каждом $n\ge2$, так что теорема также применима.

Эти примеры объединяются одним no-go принципом:

$$
\boxed{
\text{unbounded cumulative divisibility information}
+
\text{dilation}
\Longrightarrow
\text{ordinary magnitude}.
}
$$

---

# 9. От ordinary order к сложению

Julia Robinson доказала, что addition положительных натуральных first-order определимо из multiplication и unary successor; в той же работе получаются соответствующие определения через multiplication и order/divisibility variants [2].

После определения $<$ ordinary successor задается формулой

$$
S(x,y)\Longleftrightarrow x<y\land\neg\exists z\,(x<z\land z<y).
$$

Следовательно:

## Следствие 8

Для всякой $F$, удовлетворяющей условиям Dilation-Collapse Theorem,

$$
\boxed{+\in\operatorname{Def}(\mathbb N_{>0},\times,F).}
$$

В частности,

$$
(\mathbb N,\times,R)
$$

уже имеет выразительную силу полной арифметики относительно definability стандартных операций.

---

# 10. Prime-blindness и magnitude-blindness

На этом месте первоначальное слово **prime-blind** требует уточнения.

Функция $R(n)=\operatorname{rad}(n!)$ синтаксически не использует $\mathbb P$, $p_k$, $\pi(n)$ или `nextPrime`. Но само значение $n$ используется как граница обычного начального отрезка $1,\ldots,n$. Ordinary magnitude уже импортирована в определение операции.

Поэтому в этой заметке полезно различать два рабочих понятия:

**Syntactic prime-blindness:** определение не обращается явно к prime order, $p_k$, $\pi$ или nextPrime.

**Structural magnitude-blindness:** расширение не позволяет first-order восстановить ordinary order всех натуральных.

Слово **natural** ниже является методологическим, а не формальным ограничением. Мы не предлагаем внутреннюю классификацию «естественных функций». Практически кандидат должен, по крайней мере:

- не содержать явный prime order или nextPrime;
- не использовать заранее ordinary $<$ или ordinary successor как часть определения;
- не быть cumulative magnitude filtration класса, закрытого Теоремой 4;
- задаваться одной конечной равномерной конструкцией на всех натуральных.

---

# 11. Euler $\varphi$: симметрия уничтожена полностью

Рассмотрим

$$
\mathcal E=(\mathbb N_{>0},\times,\varphi).
$$

На простых

$$
\varphi(p)=p-1.
$$

В отличие от $R$, функция $\varphi$ не образует cumulative divisibility filtration, поэтому Dilation-Collapse Theorem к ней непосредственно неприменима.

Но структура оказывается чрезвычайно жесткой.

## Теорема 9 (Pointwise definability)

Каждый элемент $n\in\mathbb N_{>0}$ определим без параметров в

$$
(\mathbb N_{>0},\times,\varphi).
$$

То есть для каждого фиксированного $n$ существует first-order формула $\delta_n(x)$, имеющая в стандартной структуре единственное решение $x=n$.

### Доказательство

Формулы $\delta_n$ строятся внешней рекурсией по обычному натуральному $n$.

Единица определима мультипликативно.

Предположим, что для всех $m<n$ формулы $\delta_m$ уже построены.

Если $n$ составно, выберем факторизацию

$$
n=ab,
\qquad 1<a,b<n.
$$

Тогда $a$ и $b$ уже определимы, а $n$ задается как их произведение.

Если $n=p$ простое, число $p-1<p$ уже определимо. Среди простых $q$ условие

$$
\varphi(q)=p-1
$$

имеет единственное решение, потому что для простого $q$ имеем $\varphi(q)=q-1$. Поэтому $p$ определим.

Так рекурсивно строится конечная формула для каждого фиксированного $n$. $\square$

## Следствие 10

$$
\boxed{\operatorname{Aut}(\mathbb N_{>0},\times,\varphi)=\{\mathrm{id}\}.}
$$

Pointwise definability сильнее rigidity: каждое число имеет собственное parameter-free first-order имя.

---

# 12. Почему индивидуализация еще не равна ориентации

Следует строго различать утверждения

$$
\forall n\;\exists\delta_n(x)
$$

и

$$
\exists\Theta(x,y)\;\forall p,q\in\mathbb P\;
[\Theta(p,q)\leftrightarrow p<q].
$$

В первом случае для каждого конкретного числа существует своя конечная формула. Во втором требуется **одна** конечная формула, равномерно работающая для бесконечного множества простых.

Поэтому pointwise definability **сама по себе** не дает uniform definability of order.

Для конкретной структуры $(\mathbb N,\times,\varphi)$ мы не утверждаем неопределимость prime order. Статус остается вопросом исследования:

$$
\boxed{<_{\mathbb P}\stackrel{?}{\in}\operatorname{Def}(\mathbb N,\times,\varphi).}
$$

По Теореме 2 эквивалентно спросить

$$
\boxed{S_{\mathbb P}\stackrel{?}{\in}\operatorname{Def}(\mathbb N,\times,\varphi).}
$$

Именно здесь различаются:

$$
\boxed{
\text{symmetry breaking}
\;\neq\;
\text{pointwise individualization}
\;\neq\;
\text{uniform orientation}.
}
$$

---

# 13. Правая граница: Maurin и Bès-Richard

Maurin показывает, что order restricted to primes сохраняет разрешимость [1].

Bès и Richard показывают резкий рост силы при расширении порядка на более богатые multiplicative strata. В частности, их результаты для порядка на primary numbers связывают такое расширение с полной арифметикой и устанавливают неразрешимость ряда более слабых расширений [3].

Это делает различие между

$$
\text{prime order}
$$

и

$$
\text{prime-power order / magnitude information}
$$

структурно существенным, а не косметическим.

---

# 14. Prime successor и enumeration — разные цены

Cegielski, Matiyasevich и Richard исследовали расширения divisibility/multiplication инъекциями натуральных в простые и показали, что такие связи между ordinary indices и prime coordinates способны интерпретировать полную арифметику и приводить к неразрешимости [4].

Поэтому полезно различать

$$
S_{\mathbb P}:\mathbb P\to\mathbb P
$$

и отображение вида

$$
n\mapsto p_n:\mathbb N\to\mathbb P.
$$

Первое остается внутри разрешимого уровня Maurin. Второе непосредственно связывает ordinary magnitude/indexing с prime coordinates и несет значительно больше информации.

---

# 15. Фазовая диаграмма

Полученная картина может быть записана в четырех режимах.

### I. PRIME SYMMETRY

$$
(\mathbb N,\times)
$$

Простые определимы как класс, но свободно переставляются.

### II. POINTWISE INDIVIDUALIZATION / RIGIDITY

$$
(\mathbb N,\times,\varphi)
$$

Каждый элемент индивидуально определим; автоморфизмов нет. Uniform prime orientation пока не установлена.

### III. UNIFORM PRIME ORIENTATION

$$
(\mathbb N,\times,S_{\mathbb P})
\equiv_{\mathrm{def}}
(\mathbb N,\times,<_{\mathbb P}).
$$

Все простые ориентированы в стандартную цепь, но теория остается разрешимой.

### IV. FULL MAGNITUDE

Для cumulative functions типа $R(n)=\operatorname{rad}(n!)$:

$$
(\mathbb N,\times,R)
\Longrightarrow
(\mathbb N,\times,<)
\Longrightarrow
(\mathbb N,+,\times).
$$

Итак:

$$
\boxed{
\text{PRIME SYMMETRY}
\to
\text{POINTWISE INDIVIDUALIZATION}
\to
\text{UNIFORM PRIME ORIENTATION}
\to
\text{FULL MAGNITUDE}.
}
$$

Стрелки здесь показывают концептуальные уровни, а не утверждают, что именно $\varphi$ обязательно лежит строго между соседними уровнями: положение $(\times,\varphi)$ относительно prime orientation является открытым вопросом этой заметки.

---

# 16. Prime-Successor Algebra Problem

После этих результатов исходную задачу можно сформулировать существенно точнее.

> **Prime-Successor Algebra Problem.** Существует ли математически естественная, syntactically prime-blind и structurally magnitude-blind операция $\Omega$ на положительных натуральных, такая что
>
> $$
> S_{\mathbb P}\in\operatorname{Def}(\mathbb N_{>0},\times,\Omega),
> $$
>
> но
>
> $$
> +\notin\operatorname{Def}(\mathbb N_{>0},\times,\Omega)?
> $$

В идеале хотелось бы дополнительно потребовать разрешимость first-order theory такого расширения. Тогда $\Omega$ реализовывала бы естественным способом именно промежуточный уровень Maurin.

---

# 17. Более сильная динамическая версия

First-order definability не равна вычислительной эффективности.

Даже если $S_{\mathbb P}$ определимо, это не означает существования локального алгоритмического шага, который получает $p_{k+1}$ из $p_k$ без прохождения обычной числовой прямой.

Поэтому сохраняется более сильная задача:

найти состояние $X_k$ и операцию $\Omega$, для которых

$$
X_{k+1}=\Omega(X_k),
$$

а новый различимый атом состояния однозначно соответствует $p_{k+1}$, причем вычисление шага не является скрытым `nextPrime`, решетом или последовательным перебором всех натуральных между соседними простыми.

Именно эта версия ближе всего к исходной мечте

$$
\boxed{P_k\oplus1=P_{k+1}.}
$$

Model theory отвечает здесь на вопрос о **необходимой информации**; computational complexity — на другой вопрос, о **цене ее извлечения**.

---

# 18. Статус результатов и осторожность с новизной

Следующие компоненты являются классическими или прямыми следствиями классических результатов:

- permutation symmetry простых в чистой Skolem arithmetic;
- decidability multiplication + order restricted to primes — Maurin [1];
- definability of addition from multiplication + successor — Robinson [2];
- undecidable/arithmetically strong extensions involving richer order on multiplicative strata — Bès-Richard [3];
- сильные расширения divisibility через injections into primes — Cegielski-Matiyasevich-Richard [4].

В настоящей заметке явно выделены и доказаны:

1. finite-support coding, дающий интеропределимость $S_{\mathbb P}$ и $<_{\mathbb P}$ при наличии multiplication;
2. Dilation-Collapse Theorem и его применение к cumulative radical, cumulative LCM и factorial;
3. pointwise definability структуры $(\mathbb N,\times,\varphi)$ посредством внешней рекурсии.

В проведенном рабочем литературном аудите точные формулировки этих трех утверждений не были найдены. Это **не является заявлением математического приоритета**. Утверждения достаточно элементарны, чтобы некоторые из них могли быть известны специалистам как folklore или следствия более общих результатов. Поэтому настоящая версия использует их как доказательное ядро концептуальной заметки, а не как безусловную заявку на абсолютную новизну.

---

# 19. Что в итоге оказалось самым неожиданным

Начальный вопрос звучал почти наивно: можно ли придумать действие, которое играет для простых ту же роль, что $+1$ для натуральных?

Но уже первая симметрия показывает, что простые как multiplicative atoms не имеют встроенных имен.

Затем выясняется, что явный prime successor — все еще довольно слабая информация: он дает весь prime order, но не обрушивает теорию в полную арифметику.

Попытка внести «всего лишь множество уже появившихся простых» через $R(n)=\operatorname{rad}(n!)$ оказывается слишком сильной. Масштабирование извлекает из cumulative history весь ordinary order.

А $\varphi$, напротив, индивидуализирует каждый натуральный элемент, но ставит более тонкий вопрос: достаточно ли бесконечного семейства индивидуальных имен, чтобы существовала одна конечная формула правильной ориентации?

В этом смысле исходная задача трансформируется в более точную:

$$
\boxed{\textbf{можно ли получить ориентацию раньше, чем величину?}}
$$

или, в языке исходной интуиции:

$$
\boxed{\textbf{можно ли узнать, кто следующий, не восстановив сначала всю числовую прямую?}}
$$

Это и есть Prime-Successor Algebra Problem в той форме, к которой привело исследование.

---

# 20. Сопровождающая демонстрация

К статье прилагается самостоятельная HTML-демонстрация, не требующая сервера или внешних библиотек. Она показывает два доказательных механизма:

1. **Finite-support coding:** выбранный конечный отрезок prime-successor chain кодируется одним квадратсвободным натуральным как множеством его простых делителей.
2. **Dilation collapse:** для выбранных $x<y$ демонстрация находит масштаб $t$ и простой jump $j$ функции $R(n)$ с $tx<j\le ty$, после чего prime support $R(tx)$ является собственным подмножеством prime support $R(ty)$.

Демонстрация является иллюстрацией доказательств, а не заменой доказательства.

---

# Благодарности и disclosure

Commander Sol (OpenAI GPT-5.6 Sol) использовался как исследовательский collaborator для формулировки гипотез, проверки логических границ, построения доказательств, литературного triage, программирования демонстрации и подготовки рукописи. Ответственность за публикуемые математические утверждения и окончательную редакцию несет автор.

---

# Литература

[1] F. Maurin, **The Theory of Integer Multiplication with Order Restricted to Primes is Decidable**, *The Journal of Symbolic Logic* 62(1), 123-130 (1997). DOI: **10.2307/2275735**.

[2] J. Robinson, **Definability and Decision Problems in Arithmetic**, *The Journal of Symbolic Logic* 14(2), 98-114 (1949). DOI: **10.2307/2266510**.

[3] A. Bès, D. Richard, **Undecidable Extensions of Skolem Arithmetic**, *The Journal of Symbolic Logic* 63(2), 379-401 (1998). DOI: **10.2307/2586837**.

[4] P. Cegielski, Y. Matiyasevich, D. Richard, **Definability and Decidability Issues in Extensions of the Integers with the Divisibility Predicate**, *The Journal of Symbolic Logic* 61(2), 515-540 (1996). DOI: **10.2307/2275673**.

[5] R. D. King, **Numbers as Data Structures: The Prime Successor Function as Primitive**, arXiv:1104.3056 (2011).

---

## Citation

Malachevsky, Alex. *Размышлизмы о следующем простом с Commander Sol: Prime-Successor Algebra between Symmetry, Rigidity and Full Arithmetic*. Zenodo, 2026. DOI: **10.5281/zenodo.22077920**.
