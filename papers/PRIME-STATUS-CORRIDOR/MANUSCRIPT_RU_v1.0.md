---
title: "Размышлизмы о коридоре статуса простых с Commander Sol"
subtitle: "От точной простоты без порядка к арифметике, рождаемой мощностью"
author: "Alex Malachevsky"
date: "31 августа 2026"
lang: ru-RU
---

**Версия:** 1.0  
**ORCID:** 0009-0008-6009-3196  
**Репозиторий:** AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol  
**Исследовательская ветка:** `research/prime-status-corridor`  
**DOI публикации:** ожидает присвоения Zenodo

## Аннотация

Мы вводим фактор мультипликативного моноида положительных целых, который в точности сохраняет простоту, но стирает почти всю информацию о показателях степеней и весь числовой порядок простых атомов. Для целого $n$ фактор сохраняет только конечный набор его простых делителей и один бит, отмечающий, встречается ли какой-либо простой множитель со степенью не меньше двух. Индуцированная операция замкнута, неединичные неприводимые элементы совпадают с обычными простыми, а любая перестановка простых продолжается до автоморфизма. Это даёт точную левую границу коридора определимости: статус «простое/составное» сохраняется, тогда как порядок простых и отношение следующего простого исчезают.

Далее структура возвращается контролируемыми слоями. Фиксированные конгруэнтностные раскраски и явные непериодические блочные отношения уменьшают симметрию, но не восстанавливают глобальный порядок. Даже отношение, совпадающее с истинным prime-successor на всех рёбрах, кроме не более чем четырёх, может не определять сам successor. После добавления истинного successor внутренняя система конечных supports делает полученную first-order структуру эффективно эквивалентной слабой монадической логике второго порядка над помеченным successor-словом. Поэтому последовательность остатков последовательных нечётных простых modulo $4$ превращается в конкретную задачу теории бесконечных слов; решение её монадической теории, в частности, решало бы вопрос о бесконечной повторяемости каждого фиксированного конечного residue-pattern.

Главный переход — finite-carrier arithmetic jump. Если доступно сложение координат простых, конечные carriers определяют делимость координат, после чего классическая теорема Джулии Робинсон даёт умножение. Ещё геометричнее: одно лишь равенство мощностей конечных supports уже определяет сложение координат через сравнение длин конечных интервалов. Поэтому порядок сам по себе разрешим, equicardinality сама по себе разрешима, но их комбинация интерпретирует полную арифметику. Перенос теоремы Алексиса Бэса даёт точную ноль-один границу для всех чистых support-cardinality relations: каждое такое отношение либо уже weak-monadically определимо из порядка, либо немедленно даёт сложение и умножение. Для унарных предикатов мощности support точной границей является eventual periodicity.

**Ключевые слова:** простые числа; арифметика Сколема; определимость; слабая монадическая логика второго порядка; WS1S; конечные множества; группы автоморфизмов; отношения мощности; последовательные простые; интерпретация арифметики.

## 1. Введение

Мультипликативная структура положительных целых помнит простое разложение каждого числа, но сама по себе не выделяет обычный числовой порядок простых. Поэтому мультипликативная арифметика естественно ставит вопрос, сколько информации действительно нужно для различения трёх логически разных ресурсов:

1. **простота** — является ли элемент простым или составным;
2. **координаты простых** — обычный порядок и отношение successor на простых;
3. **арифметика координат** — сложение и умножение индексов простых.

В этой работе вопрос ставится конструктивно:

> Можно ли сжать мультипликативную информацию так, чтобы в точности сохранить статус «простое/составное», уничтожить координатный порядок простых, а затем определить, какие дополнительные отношения возвращают порядок и какие пересекают границу полной арифметики?

Ниже сохраняется только множество простых делителей и один square-defect bit. Это существенно меньше полного вектора показателей степеней. Тем не менее такой фактор отличает каждое простое от каждого составного, одновременно оставляя все простые атомы полностью симметричными.

Классический фундамент здесь велик. Арифметика Сколема и перестановки простых хорошо изучены [7]; слабая монадическая successor-арифметика разрешима методом автоматов Бюхи–Элгота–Трахтенброта [1]; Семёнов дал критерий разрешимости монадических теорий фиксированных бесконечных слов [6,8]; Робинсон доказала определимость сложения и умножения из successor и делимости [3]; Феферман и Воут установили разрешимость order-free equicardinality setting [2]; Бэс доказал резкую теорему о новых cardinality-expansions слабого монадического порядка [5]. Ни один из этих классических ингредиентов не заявляется как новый.

Вклад настоящей работы — **Prime-Status Corridor**, единый фактор, в котором эти классические механизмы располагаются на одной шкале определимости и связываются явными теоремами. Основная последовательность показана на рисунке 1.

![Рисунок 1. Коридор статуса простых. Точная простота сохраняется на полностью симметричной левой границе; истинный successor возвращает порядок, оставаясь в weak-monadic режиме; equinumerosity конечных supports синхронизирует длины интервалов и запускает арифметику.](assets/prime_status_corridor.png){width=100%}

В частности, доказана следующая цепочка.

- Однобитовый фактор точно сохраняет простоту, но имеет группу автоморфизмов $\operatorname{Sym}(\mathbb P)$ на простых атомах.
- Любая фиксированная конечная конгруэнтностная фаза оставляет бесконечные внутрицветовые перестановки простых, поэтому порядок и true successor не определимы.
- Явные непериодические блочные отношения могут уменьшать симметрию, не возвращая порядок.
- Совпадение с true successor с плотностью $1$ не гарантирует определимость successor.
- True successor вместе с внутренними конечными множествами фактора приводит ровно к задаче о помеченном weak-monadic word.
- Даже максимальная повторяемость всех конечных бинарных pattern не вынуждает coordinate addition.
- Coordinate addition вместе с finite-set carrier определяет делимость, а значит и умножение.
- Equinumerosity конечных supports уже определяет coordinate addition.
- Для всего класса pure support-cardinality relations теорема Бэса даёт ноль-один границу: новой промежуточной cardinality-фазы нет.

Работа посвящена определимости и логической мощности. Не утверждается, что отображение в фактор вычисляется быстрее факторизации: структурное сжатие результата разложения не является алгоритмическим способом дешёво получить этот результат.

## 2. Prime-Status Quotient

Пусть $\mathbb P$ — множество обычных простых, а $\mathbb N_{>0}$ — положительные целые.

### Определение 2.1 (support и square defect)

Для $n\ge 1$ положим

$$
S(n)=\{p\in\mathbb P:p\mid n\},
\qquad
Q(n)=\begin{cases}
0,&n\text{ squarefree},\\
1,&\exists p\in\mathbb P\;p^2\mid n.
\end{cases}
\qquad \mathrm{(1)}
$$

и определим

$$
\Xi(n)=(S(n),Q(n)).
\qquad \mathrm{(2)}
$$

Обозначим образ $\Xi$ через $\mathfrak P_0$.

### Определение 2.2 (индуцированное произведение)

Для конечных множеств простых $A,B$ и битов $e,d\in\{0,1\}$ положим

$$
(A,e)\star(B,d)
=
\left(A\cup B,\;e\vee d\vee[A\cap B\ne\varnothing]\right).
\qquad \mathrm{(3)}
$$

Состояние $(\varnothing,1)$ исключается, поскольку оно не лежит в образе $\Xi$.

### Предложение 2.3 (фактор-гомоморфизм)

Для всех $a,b\in\mathbb N_{>0}$

$$
\Xi(ab)=\Xi(a)\star\Xi(b).
\qquad \mathrm{(4)}
$$

#### Доказательство

Имеем $S(ab)=S(a)\cup S(b)$. В произведении $ab$ возникает квадрат простого тогда и только тогда, когда повтор уже был в $a$, повтор уже был в $b$ или один и тот же простой входит в оба support. Это в точности Boolean rule из (3). ∎

### Предложение 2.4 (точная простота)

Для $n>1$

$$
n\text{ простое}
\iff
|S(n)|=1\land Q(n)=0.
\qquad \mathrm{(5)}
$$

#### Доказательство

Если $n=p$ простое, то $S(n)=\{p\}$ и $Q(n)=0$. Обратно, если $|S(n)|=1$, то $n=p^k$. Условие $Q(n)=0$ исключает $k\ge2$, следовательно $k=1$. ∎

### Следствие 2.5

Неединичные неприводимые элементы $\mathfrak P_0$ — ровно состояния

$$
(\{p\},0),\qquad p\in\mathbb P.
\qquad \mathrm{(6)}
$$

#### Доказательство

Singleton squarefree state нельзя получить произведением двух неединичных состояний. Любой squarefree composite support разбивается на объединение двух непустых proper supports, а

$$
(\{p\},1)=(\{p\},0)\star(\{p\},0).
\qquad \mathrm{(7)}
$$

∎

## 3. Полная симметрия простых

### Теорема 3.1

Каждая перестановка $\sigma:\mathbb P\to\mathbb P$ единственным образом продолжается до автоморфизма $\mathfrak P_0$ по правилу

$$
(A,e)\longmapsto(\sigma A,e).
\qquad \mathrm{(8)}
$$

И наоборот, любой автоморфизм $\mathfrak P_0$ индуцирует перестановку простых атомов. Поэтому

$$
\operatorname{Aut}(\mathfrak P_0)\cong\operatorname{Sym}(\mathbb P).
\qquad \mathrm{(9)}
$$

#### Доказательство

Операция $\star$ зависит только от объединения, непустоты пересечения и defect bits; всё это сохраняется любой перестановкой prime labels. Обратно, автоморфизм сохраняет определимое множество неединичных неприводимых элементов, то есть prime atoms. Каждый элемент фактора однозначно задаётся конечным support и defect bit, поэтому перестановка атомов однозначно задаёт весь автоморфизм. ∎

### Следствие 3.2

Обычный числовой порядок простых и true prime-successor не определимы в $\mathfrak P_0$.

#### Доказательство

Любое определимое отношение инвариантно относительно автоморфизмов. Транспозиция двух prime atoms сохраняет $\mathfrak P_0$, но в общем случае разрушает обычный порядок и successor. ∎

Это левая граница коридора: точная простота уже есть, а координаты простых отсутствуют.

## 4. Конечная периодическая фаза не возвращает порядок

Зафиксируем $M\ge2$. Для reduced residue classes $r\pmod M$ добавим unary colours

$$
C_r(p)\iff p\equiv r\pmod M,
\qquad (p,M)=1,
\qquad \mathrm{(10)}
$$

а конечное множество простых, делящих $M$, рассматриваем отдельно.

### Теорема 4.1 (Finite Phase Wall)

Каждый reduced residue class содержит бесконечно много простых. Поэтому

$$
\operatorname{Aut}(\mathfrak P_M)
\supseteq
\prod_r\operatorname{Sym}(\mathbb P_r).
\qquad \mathrm{(11)}
$$

В частности, стандартный prime order и true prime successor остаются неопределимыми.

#### Доказательство

По теореме Дирихле в каждом reduced residue class бесконечно много простых. Любая перестановка внутри каждого цветового класса сохраняет unary colours и продолжается до автоморфизма фактора по теореме 3.1. Такая перестановка может перемещать простой сколь угодно далеко в числовом порядке, поэтому ни order, ни true successor не могут быть инвариантными. ∎

Тот же аргумент применим к любому фиксированному конечному relational enrichment, чьё ограничение на tuples простых зависит только от конечной residue-information modulo фиксированного $M$.

## 5. Непериодическое разрушение симметрии без глобального порядка

Для одного residue class $r$ перечислим простые по величине:

$$
p_{r,1}<p_{r,2}<p_{r,3}<\cdots.
\qquad \mathrm{(12)}
$$

Добавим ориентированное парное отношение

$$
R_2(p_{r,2j-1},p_{r,2j}).
\qquad \mathrm{(13)}
$$

Оно непериодично относительно обычной числовой координаты простых и запрещает произвольные перестановки отдельных атомов. Однако целые ориентированные пары одного цвета всё ещё свободно переставимы.

### Предложение 5.1

В расширении с $R_2$ ни глобальный prime order, ни true prime successor не определимы.

#### Доказательство

Возьмём две ориентированные пары одного цвета и поменяем пары местами как блоки. Это сохраняет фактор, residue colours и $R_2$, но меняет числовые позиции четырёх prime atoms. Следовательно order и true successor не инвариантны. ∎

Таким образом, симметрия может строго уменьшаться без восстановления координатного порядка.

## 6. Почти полный successor всё ещё может не определять successor

Пусть $S$ — true prime successor. Выберем два далёких prime atoms $x,y$ одного цвета и удалим все $S$-рёбра, инцидентные $x$ или $y$. Удаляется не более четырёх рёбер.

### Теорема 6.1 (Finite-Injury Obstruction)

Существует отношение $E$, отличающееся от true prime successor не более чем на четырёх рёбрах, такое что true prime successor не определим из фактора, конечной phase colouring и $E$.

#### Доказательство

После удаления рёбер $x$ и $y$ изолированы относительно $E$. Транспозиция $x\leftrightarrow y$, фиксирующая остальные atoms, сохраняет $E$, цвета и quotient structure. Но true successor при этой транспозиции не сохраняется. ∎

Следовательно agreement с true successor с плотностью $1$ не является достаточным reconstruction criterion. Существенна не плотность рёбер сама по себе, а глобальная stitching geometry.

## 7. Внутренние конечные множества

Далее удобно перейти к нечётным простым, исключив $2$ как отдельный тривиальный parity layer.

### Лемма 7.1 (squarefree carriers)

Squarefree quotient elements образуют определимую копию всех конечных множеств prime atoms.

#### Доказательство

Для любого непустого состояния $(A,e)$

$$
(A,e)\star(A,e)=(A,1).
\qquad \mathrm{(14)}
$$

Поэтому непустой элемент squarefree тогда и только тогда, когда он не идемпотентен. Единица обрабатывается отдельно. Для любого конечного множества prime atoms $A$ существует squarefree state $(A,0)$. ∎

### Лемма 7.2 (равенство supports)

Для quotient elements $x,y$

$$
\operatorname{supp}(x)=\operatorname{supp}(y)
\iff
x\star x=y\star y.
\qquad \mathrm{(15)}
$$

#### Доказательство

Squaring сохраняет support и заменяет defect bit любого непустого состояния на $1$. Для unit обе стороны равенства также согласованы. ∎

### Лемма 7.3 (membership)

Для prime atom $p$ и squarefree carrier $X$ отношение $p\in X$ first-order определимо.

#### Доказательство

Достаточно потребовать, чтобы добавление $p$ не меняло support:

$$
(p\star X)\star(p\star X)=X\star X.
\qquad \mathrm{(16)}
$$

По лемме 7.2 это эквивалентно $p\in\operatorname{supp}(X)$. ∎

Таким образом quotient содержит внутренний weak-monadic finite-set channel.

## 8. True successor даёт помеченное weak-monadic word

Добавим true prime successor $S$ на нечётных prime atoms и перечислим

$$
q_0=3,q_1=5,q_2=7,\ldots,
\qquad S(q_i,q_{i+1}).
\qquad \mathrm{(17)}
$$

При необходимости добавим конечное число unary colours $C_1,\ldots,C_t$.

### Теорема 8.1 (Weak-Monadic Interpretation)

First-order theory структуры

$$
(\mathfrak P_0^{\rm odd};\star,S,C_1,\ldots,C_t)
\qquad \mathrm{(18)}
$$

эффективно взаимно переводится со слабой монадической логикой второго порядка над labelled successor word

$$
(\mathbb N;\operatorname{Succ},C_1^w,\ldots,C_t^w),
\qquad \mathrm{(19)}
$$

где set variables пробегают конечные subsets позиций.

#### Доказательство

По разделу 7 first-order quantification по squarefree quotient elements даёт quantification по произвольным конечным subsets prime positions. Обратно, каждый quotient element кодируется конечным множеством и одним Boolean defect tag. Операция $\star$ задаётся через union, nonempty intersection и два tags; successor и colours переводятся непосредственно. Это даёт эффективный перевод формул в обе стороны, с обычной two-sorted coding set/position variables. ∎

### Следствие 8.2

Без дополнительного colour word теория разрешима как классическая WS1S.

### Лемма 8.3 (order становится определимым)

Successor order на indices prime atoms first-order определим в quotient с $S$.

#### Доказательство

Для atoms $x,y$ потребуем существование конечного carrier $X$, содержащего $x$ и $y$, такого что каждый включённый atom, кроме $y$, имеет свой $S$-successor также в $X$. Если $x\le y$, конечный interval от $x$ до $y$ является witness. Если $x>y$, forward closure из $x$ никогда не закончится в $y$ и потребует бесконечного множества, невозможного для finite carrier. ∎

Итак, prime order появляется раньше арифметики.

## 9. Mod-4 prime word как number-theoretic frontier

Определим binary word

$$
w_4(n)=
\begin{cases}
0,&q_n\equiv1\pmod4,\\
1,&q_n\equiv3\pmod4.
\end{cases}
\qquad \mathrm{(20)}
$$

Для каждого конечного binary word $u=u_0\ldots u_{k-1}$ формула $\operatorname{Occ}_u(y)$, утверждающая, что block длины $k$, начинающийся в $y$, равен $u$, first-order определима из successor и colours.

### Теорема 9.1 (recurrence-query lower bound)

Если weak monadic theory слова $w_4$ разрешима, то существует алгоритм, который для каждого конечного binary word $u$ решает, встречается ли $u$ бесконечно много раз в $w_4$.

#### Доказательство

Эффективно построим предложение

$$
\rho_u:=\forall x\,\exists y\,(x<y\land\operatorname{Occ}_u(y)).
\qquad \mathrm{(21)}
$$

Оно истинно тогда и только тогда, когда $u$ встречается сколь угодно далеко, то есть бесконечно много раз. Decision procedure для WMSO theory $w_4$ решал бы истинность $\rho_u$. ∎

Теорема Shiu даёт произвольно длинные одноцветные runs в каждом reduced residue class [4], но общий recurrence spectrum предписанных смешанных residue-patterns остаётся за пределами текущих безусловных результатов теории простых [9,10]. Поэтому теорема 9.1 — barrier statement, а не доказательство undecidability.

## 10. Finite-Carrier Arithmetic Jump

Определим coordinate addition на atoms:

$$
\operatorname{Add}_{\rm idx}(q_i,q_j,q_k)
\iff i+j=k.
\qquad \mathrm{(22)}
$$

### Теорема 10.1

В

$$
(\mathfrak P_0^{\rm odd};\star,S,\operatorname{Add}_{\rm idx})
\qquad \mathrm{(23)}
$$

coordinate divisibility first-order определима.

#### Доказательство

Пусть $q_0$ обозначает coordinate zero. Для $a>0$ определим $a\mid b$ существованием finite carrier $X$, удовлетворяющего:

1. $q_0\in X$ и $q_b\in X$;
2. каждый atom из $X$ не превосходит $q_b$;
3. если $q_t\in X$ и $t<b$, то atom $q_{t+a}$ также лежит в $X$.

Если $a\mid b$, witness — конечная progression

$$
\{q_0,q_a,q_{2a},\ldots,q_b\}.
\qquad \mathrm{(24)}
$$

Обратно, closure из $0$ вынуждает все кратные $a$ до bound $b$. Если $b$ не кратно $a$, последний вынужденный multiple ниже $b$ требует следующий multiple выше $b$, противореча condition 2. При $a=0$ определяем $0\mid b$ тогда и только тогда, когда $b=0$. ∎

### Теорема 10.2 (Arithmetic Jump)

Coordinate multiplication определимо, а complete theory expansion (23) неразрешима.

#### Доказательство

Джулия Робинсон доказала, что addition и multiplication first-order определимы из successor и divisibility на натуральных числах [3]. Применяя её фиксированные defining formulas к atom-index copy, получаем ordinary first-order arithmetic. Следовательно complete theory интерпретирует истинную арифметику и неразрешима. ∎

### Следствие 10.3

Coordinate addition не определимо в uncoloured successor layer $\mathfrak P_0^{\rm odd}+S$, поскольку этот layer имеет разрешимую WS1S theory.

## 11. Максимальная локальная recurrence недостаточна

Для каждого $n\ge1$ пусть $B_n$ — concatenation в lexicographic order всех binary words длины не более $n$. Определим

$$
w_*=B_1B_2B_3\cdots.
\qquad \mathrm{(25)}
$$

Каждое finite binary word входит как отдельный block во все достаточно большие $B_n$, поэтому встречается в $w_*$ бесконечно много раз.

### Теорема 11.1 (Maximal-Recurrence Separation)

Существует computable binary word, в котором каждое конечное binary word встречается бесконечно много раз, но coordinate addition не WMSO-определимо.

#### Доказательство

Слово $w_*$ computable. Его recurrence indicator для regular factor languages recursive: если regular language $L$ пуст, recurrent factor из $L$ отсутствует; если $L$ непуст, то $L$ содержит некоторое конечное слово, а всякое finite word встречается в $w_*$ бесконечно много раз. По критерию Семёнова MSO theory $w_*$ разрешима [6,8]. Если бы coordinate addition было определимо, теорема 10.2 интерпретировала бы full arithmetic и противоречила разрешимости. ∎

Следовательно

$$
\boxed{
\text{maximal finite-pattern recurrence}
\not\Rightarrow
\text{coordinate addition}.
}
\qquad \mathrm{(26)}
$$

Искомый ресурс — некоторый вид global synchronization, а не просто богатство локальных факторов.

## 12. Equinumerosity как primitive synchronizer

Добавим на finite squarefree carriers отношение

$$
\operatorname{EqCard}(X,Y)
\iff |X|=|Y|.
\qquad \mathrm{(27)}
$$

### Теорема 12.1 (Equinumerosity Synchronization)

В

$$
(\mathfrak P_0^{\rm odd};\star,S,\operatorname{EqCard})
\qquad \mathrm{(28)}
$$

coordinate addition first-order определимо.

#### Доказательство

Для atoms $a\le b$ пусть $\operatorname{Interval}(a,b,X)$ означает, что $X$ — ровно множество atoms в half-open interval $[a,b)$:

$$
\forall u\bigl(\operatorname{At}(u)\to
[u\in X\leftrightarrow(a\le_Su\land u<_Sb)]\bigr).
\qquad \mathrm{(29)}
$$

Для

$$
x=q_i,\qquad y=q_j,\qquad z=q_k
\qquad \mathrm{(30)}
$$

имеем

$$
|[x,z)|=k-i,
\qquad
|[q_0,y)|=j.
\qquad \mathrm{(31)}
$$

Поэтому

$$
i+j=k
\iff
x\le_S z\land |[x,z)|=|[q_0,y)|.
\qquad \mathrm{(32)}
$$

Оба intervals представлены finite squarefree carriers, а равенство их мощностей выражается через EqCard. Следовательно $\operatorname{Add}_{\rm idx}$ first-order определимо. ∎

### Следствие 12.2

$$
\operatorname{EqCard}
\Longrightarrow
\operatorname{Add}_{\rm idx}
\Longrightarrow
\operatorname{Div}_{\rm idx}
\Longrightarrow
\operatorname{Mul}_{\rm idx}.
\qquad \mathrm{(33)}
$$

Следовательно EqCard expansion интерпретирует full arithmetic.

## 13. Два tame-ингредиента, wild вместе

### Предложение 13.1

$\mathfrak P_0^{\rm odd}+S$ имеет разрешимую complete theory.

Это следствие 8.2.

### Предложение 13.2

Order-free structure $\mathfrak P_0^{\rm odd}+\operatorname{EqCard}$ имеет разрешимую complete theory.

#### Обоснование

Феферман и Воут доказали разрешимость weak monadic logic чистого equality setting с equicardinality конечных множеств [2]; Бэс явно использует этот результат как decidability of $\operatorname{WMSO}(\mathbb N,\operatorname{EqCard})$ without $<$ [5]. Prime-Status operation на finite supports определима через set-theoretic union/intersection information и один finite defect tag, поэтому quotient интерпретируется в этом разрешимом setting.

### Теорема 13.3 (Interaction Law)

$$
\boxed{
\text{order alone tame; EqCard alone tame; order+EqCard wild}.
}
$$

#### Доказательство

Первые два утверждения следуют из предложений 13.1–13.2. Для совместного expansion теорема 12.1 определяет coordinate addition, а теоремы 10.1–10.2 дают divisibility, multiplication и интерпретацию full arithmetic. ∎

Суть перехода: order превращает равенство мощностей конечных sets в равенство длин интервалов, то есть в coordinate translation.

## 14. Ноль-один граница для pure cardinality synchronizers

Пусть $R(X_1,\ldots,X_n)$ зависит только от tuple

$$
(|X_1|,\ldots,|X_n|).
$$

Такое отношение будем называть **pure cardinality synchronizer**.

Бэс доказал для WMSO над $(\mathbb N,<)$, что если cardinality relation $R$ не определимо уже в base weak-monadic order structure, то в expansion определимы и $+$, и $\times$ [5].

### Теорема 14.1 (Transferred Cardinality Dichotomy)

Для каждого pure cardinality synchronizer $R$ на Prime-Status finite carriers выполняется ровно одна из альтернатив:

1. $R$ уже определимо в successor/order Prime-Status layer, не добавляет definability power и сохраняет decidability;
2. $R$ определяет coordinate addition и coordinate multiplication, поэтому expansion неразрешим.

#### Доказательство

По теореме 8.1 successor Prime-Status structure предоставляет в точности weak-monadic finite-set variables над упорядоченными atom positions. Применяем теорему Бэса к $R$ и переводим полученные coordinate relations обратно на atom sort. ∎

### Следствие 14.2 (unary wall)

Для unary predicate

$$
R_A(X)\iff |X|\in A,
\qquad A\subseteq\mathbb N,
\qquad \mathrm{(34)}
$$

$R_A$ tame тогда и только тогда, когда $A$ ultimately periodic.

Поэтому фиксированные congruence conditions на support size tame, тогда как простота мощности support, squareness, powers of two и любой другой non-ultimately-periodic unary size law вызывают arithmetic collapse.

Это нельзя смешивать с nonperiodic **position colours**. Непериодическое infinite word на successor positions может иметь разрешимую monadic theory [6]. Та же непериодичность, помещённая на **support cardinalities**, wild по теореме Бэса. Значит, место хранения информации не менее существенно, чем сама информация.

## 15. Связь с классической мультипликативной и монадической арифметикой

Prime-Status Quotient следует понимать как контролируемый reduct мультипликативной информации, а не как замену арифметике Сколема. Современная model theory $\operatorname{Th}(\mathbb N,\cdot)$ подчёркивает структурную роль squarefree elements и сильную симметрию prime coordinates [7]. Наш quotient намеренно схлопывает все положительные exponents выше единицы в один defect bit. Поэтому novelty claim не относится к существованию supports, radicals или prime permutations.

Weak-monadic часть аргумента также классическая. Теорема Бюхи даёт decidability WS1S [1], а теорема Семёнова объясняет, почему некоторые непериодические computable words всё же имеют разрешимую monadic theory [6,8]. Prime-Status construction добавляет алгебраический механизм, который интернализует finite-set variables непосредственно внутри quotient.

Cardinality boundary также опирается на классическую теорему. Результат Бэса уже содержит абстрактную WMSO dichotomy для cardinality relations [5]. Специфика настоящей работы в том, что one-bit Prime-Status quotient после восстановления successor точно попадает в условия этой теоремы. Поэтому абстрактная логическая дихотомия превращается в конкретную фазовую границу мультипликативной prime-status algebra.

## 16. Ограничения и открытые задачи

Результаты намеренно останавливаются на чёткой публикационной границе.

1. **Точная monadic theory слова $w_4$ здесь не решена.** Recurrence-query reduction не доказывает undecidability.
2. **Не утверждается, что каждый конечный residue pattern встречается среди consecutive primes.** Такие pattern остаются предметом активной аналитической теории чисел [9,10].
3. **EqCard достаточен, но глобальная минимальность не доказана.** Более слабый non-cardinality synchronizer может уже определять coordinate addition.
4. **Density не классифицирует successor reconstruction.** Finite-injury example — obstruction, а не полная characterization.
5. **Не показано, что вычисление $\Xi(n)$ проще факторизации $n$.** Quotient сжимает multiplicative state после того, как factor information уже известно.
6. **Не заявляется исчерпывающий приоритет.** Novelty statement относится к combined corridor architecture и доказанному внутри неё theorem package.

Эти вопросы естественно образуют программу продолжения и не являются пробелами в доказанной цепочке.

## 17. Заключение

Prime-Status Quotient даёт резкое разделение между простотой, координатами простых и арифметикой координат. Сохраняя только finite prime support и один square-defect bit, он в точности сохраняет различие «простое/составное». Но все prime atoms остаются свободно переставимы, поэтому обычный prime order исчезает полностью.

Finite congruence phases и явные непериодические block relations уменьшают симметрию, не возвращая порядок. Даже почти полный successor может сохранять residual automorphism obstruction. True successor наконец восстанавливает order, потому что quotient способен внутри себя хранить конечные paths, однако uncoloured structure остаётся только WS1S и потому разрешима.

Арифметика возникает, когда появляется global synchronization resource, связывающий длины конечных интервалов. Equinumerosity finite supports достаточно: order непосредственно превращает её в coordinate addition, а finite carrier затем усиливает addition до divisibility и multiplication. Теорема Бэса показывает, что явление не специфично для EqCard: среди pure support-cardinality relations нет genuinely new intermediate layer.

Коридор можно суммировать формулой

$$
\boxed{
\text{точная простота}
\;<\;
\text{конечная фаза}
\;<\;
\text{порядок простых}
\;<\;
\text{синхронизация мощности}
\Longrightarrow
\text{полная арифметика координат}.
}
\qquad \mathrm{(35)}
$$

Тем самым выявляется не только способ уничтожения арифметики сжатием, но и конкретный механизм её повторного появления.

## Раскрытие использования ИИ

Commander Sol, исследовательский collaborator на базе языковой модели OpenAI, использовался для генерации гипотез, исследования доказательств, поиска контрпримеров, литературного triage, формализации, проектирования hostile audits и подготовки рукописи. Указанный человек-автор несёт ответственность за публикацию, отбор утверждений и окончательные математические формулировки. Все классические результаты, использованные в доказательствах, явно атрибутированы оригинальным или современным источникам.

## Доступность данных и кода

Для математических доказательств статьи экспериментальный dataset не требуется. Research notes, hostile audits, publication sources и companion visualization поддерживаются в публичном репозитории `AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol`, ветка `research/prime-status-corridor`. После резервирования/публикации Zenodo сюда следует внести окончательный DOI.

## Литература

[1] J. R. Büchi, "Weak Second-Order Arithmetic and Finite Automata," *Mathematical Logic Quarterly* 6 (1960), 66-92. DOI: 10.1002/malq.19600060105.

[2] S. Feferman and R. L. Vaught, "The First Order Properties of Products of Algebraic Systems," *Fundamenta Mathematicae* 47 (1959), 57-103. DOI: 10.4064/fm-47-1-57-103.

[3] J. Robinson, "Definability and Decision Problems in Arithmetic," *The Journal of Symbolic Logic* 14(2) (1949), 98-114. DOI: 10.2307/2266510.

[4] D. K. L. Shiu, "Strings of Congruent Primes," *Journal of the London Mathematical Society* 61(2) (2000), 359-373. DOI: 10.1112/S0024610799007863.

[5] A. Bès, "Expansions of MSO by Cardinality Relations," *Logical Methods in Computer Science* 9(4:18) (2013), 1-17. DOI: 10.2168/LMCS-9(4:18)2013.

[6] D. Kuske, J. Liu, and A. Moskvina, "Infinite and Bi-infinite Words with Decidable Monadic Theories," *Logical Methods in Computer Science* 14(3:9) (2018). DOI: 10.23638/LMCS-14(3:9)2018.

[7] A. Stonestrom, "Some Model Theory of $\operatorname{Th}(\mathbb N,\cdot)$," *Mathematical Logic Quarterly* 68(3) (2022), 288-303. DOI: 10.1002/malq.202100049.

[8] A. L. Semenov, "Logical Theories of One-Place Functions on the Set of Natural Numbers," *Mathematics of the USSR-Izvestiya* 22(3) (1984), 587-618. DOI: 10.1070/IM1984v022n03ABEH001456.

[9] R. J. Lemke Oliver and K. Soundararajan, "Unexpected Biases in the Distribution of Consecutive Primes," *Proceedings of the National Academy of Sciences* 113(31) (2016), E4446-E4454. DOI: 10.1073/pnas.1605366113.

[10] C. F. Lau, "Residue Class Patterns of Consecutive Primes," arXiv:2409.12819 (2024), version consulted for the current pattern frontier. DOI: 10.48550/arXiv.2409.12819.
