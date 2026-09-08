# Предписанная стабилизаторная опора в фиксированно-носительной ориентированной алгебре
## Wreath-когерентность, сжатие разбиений и точное орбитальное разделение

**Автор:** Alex Malachevsky  
**Серия:** Commander Sol / Fixed-Carrier Oriented Algebra  
**Статус:** публикационный черновик v0.9  
**Дата:** 2026-09-01

---

## Аннотация

Fixed-Carrier Oriented Algebra (FCOA) изучает, каким образом типизированные частичные операции на фиксированном активном носителе могут сохранять структурную информацию в геометрии своих значений после стирания вспомогательной структуры носителя. В настоящей работе используется базовое определение FCOA и каноническая конструкция из A. Malachevsky, Zenodo DOI **10.5281/zenodo.22164246**. Мы используем величину предписанной стабилизаторной опоры

\[
m_G(H;S)=\min\{|F|:F\subseteq S,\ \operatorname{Stab}_G(F)=H\},
\]

не заявляя приоритет на саму абстрактную идею точного стабилизатора подмножества, а вводя её как ресурсную меру точной остаточной симметрии в FCOA-памяти значений. Для imprimitive wreath-действий получен ряд точных результатов. Если транзитивная группа \(A\leq\operatorname{Sym}(\Lambda)\) степени \(t\) независимо действует на \(b\) изоморфных ветвях, то на множестве упорядоченных межветвевых клеток \(S_\times\) точная цена одной общей внутренней фазы равна

\[
m_{A\wr S_b}(\Delta A\times S_b;S_\times)=b(b-1)t.
\]

Для произвольного разбиения ветвей \(\mathcal P\) с размерами блоков \(n_1,\ldots,n_c\) точная цена памяти, одновременно сохраняющей само разбиение и одну общую внутреннюю фазу внутри каждого блока, равна

\[
m_G(H_{\mathcal P};S_\times)=t\sum_{j=1}^c n_j(n_j-1).
\]

Если же внутренние фазы должны оставаться независимыми и требуется помнить только разбиение, каждая выбранная пара ветвей обязана нести полный \(t^2\)-слой. Задача точно редуцируется к минимизации числа дуг в петлесвободном ориентированном отношении, автоморфизмная группа которого совпадает с конкретным стабилизатором разбиения \(K_{\mathcal P}\). Доказывается дихотомия надгрупп: всякая лишняя симметрия либо содержит запрещённую межблочную транспозицию точек, либо реализует единственную особую возможность — macro-swap объединения singleton-блоков с одним небинарным блоком той же мощности. Отсюда получается точная взвешенная Orbital XOR-Separation Program с \(O(k^2)\) переменными, где \(k\) — число различных размеров блоков. Теория демонстрирует реальное complement compression и ресурсную немонотонность: семантически более сильная phase-coherent память может требовать меньше FCOA-клеток, чем память только разбиения.

---

## 1. Введение

В задачах алгебраического кодирования часто требуется уничтожить часть симметрии, сохранив заранее заданную остаточную группу. В классической теории групп перестановок к этой теме примыкают regular sets, distinguishing colorings, relation groups, 2-closure, orbital digraphs, point-determining graphs и задачи минимальных графовых реализаций заданной группы автоморфизмов.

Здесь рассматривается более узкая постановка. Активный носитель и его ambient action фиксированы заранее. Значения типизированной частичной операции выделяют некоторое подмножество клеток фиксированного \(G\)-множества \(S\). Требуется минимальная опора, setwise stabilizer которой равен **ровно** заданной подгруппе \(H\leq G\).

Основной организующий инвариант:

\[
\boxed{
 m_G(H;S)=\min\{|F|:F\subseteq S,\ \operatorname{Stab}_G(F)=H\}.
}
\tag{1}
\]

Если такого \(F\) нет, полагаем \(m_G(H;S)=\infty\).

В FCOA эта величина измеряет **стоимость памяти в значениях операции**. Скрытое соединение или разбиение используется при назначении значений, после чего удаляется из сигнатуры носителя. Должна остаться такая value geometry, чья активная группа автоморфизмов равна требуемой остаточной симметрии.

Статья состоит из трёх уровней.

1. **Фазовая когерентность.** Тонкое диагональное отношение связывает независимые branch-actions и даёт точные формулы опоры.
2. **Память только разбиения.** Если внутренние фазы должны остаться независимыми, диагональные отношения запрещены; приходится выбирать полные внутренние волокна, и задача редуцируется к sparse directed relation на метках ветвей.
3. **Точное орбитальное разделение.** Для произвольного типа разбиения exactness характеризуется конечным набором запрещённых транспозиций и не более чем одним singleton macro-swap, после чего задача становится конечной взвешенной булевой программой.

---

## 2. Общие редукции

### Предложение 2.1 — Редукция к объединению орбит

Если \(G\) действует на конечном множестве \(S\), \(H\leq G\) и

\[
H\leq\operatorname{Stab}_G(F),
\]

то \(F\) является объединением \(H\)-орбит.

#### Доказательство

Для любого \(x\in F\) и любого \(h\in H\) имеем \(hx\in F\), поэтому \(Hx\subseteq F\). ∎

Следовательно,

\[
m_G(H;S)
=
\min\left\{
\sum_{O\in\mathcal A}|O|:
\mathcal A\subseteq\operatorname{Orb}_H(S),
\operatorname{Stab}_G\!\left(\bigcup_{O\in\mathcal A}O\right)=H
\right\}.
\tag{2}
\]

### Предложение 2.2 — Редукция по нормальной подгруппе

Пусть \(H\triangleleft G\), \(Q=G/H\), а \(\Omega=H\backslash S\) — множество \(H\)-орбит с весом \(w(O)=|O|\). Тогда

\[
\boxed{
 m_G(H;S)=
\min\left\{
\sum_{O\in A}w(O):
A\subseteq\Omega,
\operatorname{Stab}_Q(A)=1
\right\}.
}
\tag{3}
\]

#### Доказательство

\(H\)-инвариантные подмножества \(S\) взаимно однозначно соответствуют подмножествам \(\Omega\). Нормальность \(H\) даёт действие \(Q\) на \(\Omega\), причём

\[
\operatorname{Stab}_G(F)/H
\cong
\operatorname{Stab}_Q(A).
\]

Поэтому exact stabilizer \(H\) эквивалентен тривиальному стабилизатору в \(Q\). ∎

### Следствие 2.3 — Формула индекса два

Если \([G:H]=2\), а \(q\) — нетривиальный элемент \(G/H\), то

\[
\boxed{
 m_G(H;S)=
\min\{|O|:O\in H\backslash S,\ qO\neq O\}.
}
\tag{4}
\]

Семивершинный пример \(D_8\to V_4\) является частным случаем этой формулы.

---

## 3. Wreath-геометрия ветвей

Пусть

\[
|\Lambda|=t\ge2,
\]

а \(A\leq\operatorname{Sym}(\Lambda)\) транзитивна.

Берём \(b\ge2\) изоморфных ветвей. Активный носитель:

\[
X=[b]\times\Lambda.
\tag{5}
\]

Ambient group:

\[
G=A\wr S_b=A^b\rtimes S_b.
\tag{6}
\]

Элемент записывается как

\[
g=(\sigma_1,\ldots,\sigma_b;\pi).
\]

Множество ordered cross-branch клеток:

\[
S_\times
=
\{((r,i),(s,j)):r\neq s\},
\tag{7}
\]

и

\[
|S_\times|=b(b-1)t^2.
\tag{8}
\]

---

## 4. Глобальная фазовая когерентность

Определим equality fiber

\[
F_=
=
\{((r,i),(s,i)):r\neq s\}.
\tag{9}
\]

Тогда

\[
|F_=|=b(b-1)t.
\tag{10}
\]

Положим

\[
\Delta A
=
\{(\sigma,\ldots,\sigma):\sigma\in A\}
\tag{11}
\]

и

\[
H=\Delta A\times S_b.
\tag{12}
\]

### Теорема 4.1 — Стабилизатор глобальной когерентности

\[
\boxed{
\operatorname{Stab}_G(F_=)=H.
}
\tag{13}
\]

#### Доказательство

Любой элемент \(H\) сохраняет равенство внутренних координат. Обратно, если

\[
g=(\sigma_1,\ldots,\sigma_b;\pi)
\]

сохраняет \(F_=\), то для любых \(r\neq s\) и \(i\in\Lambda\) образ клетки

\[
((r,i),(s,i))
\]

должен снова иметь равные внутренние координаты. Поэтому

\[
\sigma_r(i)=\sigma_s(i)
\]

для всех \(i\), откуда \(\sigma_r=\sigma_s\). Все внутренние компоненты совпадают, а \(\pi\) произвольна. ∎

### Теорема 4.2 — Точная цена глобальной когерентности

\[
\boxed{
 m_G(H;S_\times)=b(b-1)t.
}
\tag{14}
\]

#### Доказательство

Верхняя граница достигается на \(F_=\).

Пусть теперь \(F\subseteq S_\times\) имеет стабилизатор ровно \(H\). По Предложению 2.1 оно \(H\)-инвариантно. На фиксированной ordered pair разных ветвей внутреннее выбранное отношение является объединением диагональных \(A\)-орбит в \(\Lambda^2\).

Любая ненулевая диагональная \(A\)-орбита имеет размер не меньше \(t\): её проекция на первую координату является ненулевым \(A\)-инвариантным подмножеством \(\Lambda\), следовательно равна всему \(\Lambda\), а размеры волокон постоянны и положительны.

Пустое или полное внутреннее отношение оставило бы независимые branch-actions и дало бы stabilizer строго больше \(H\). Поэтому на каждой ordered branch pair требуется непустое собственное диагональное отношение, стоимость которого не меньше \(t\). Всего ordered branch pairs — \(b(b-1)\). ∎

### Следствие 4.3

Число различных coherence states равно

\[
[G:H]=|A|^{b-1},
\tag{15}
\]

а semantic information

\[
I_{\rm coh}=(b-1)\log_2|A|.
\tag{16}
\]

---

## 5. Произвольное разбиение ветвей

Пусть

\[
\mathcal P=\{B_1,\ldots,B_c\},
\tag{17}
\]

\[
|B_j|=n_j,
\qquad
\sum_jn_j=b.
\tag{18}
\]

Пусть

\[
m_d=|\{j:n_j=d\}|.
\tag{19}
\]

Тогда branch stabilizer:

\[
K_{\mathcal P}
\cong
\prod_{d\ge1}(S_d\wr S_{m_d}).
\tag{20}
\]

Внутренняя group с одной phase на каждый блок:

\[
A^{\mathcal P}
=
\{(\sigma_1,\ldots,\sigma_b):
\sigma_r=\sigma_s\text{ внутри каждого }B_j\}
\cong A^c.
\tag{21}
\]

Target residual group:

\[
H_{\mathcal P}=A^{\mathcal P}\rtimes K_{\mathcal P}.
\tag{22}
\]

Canonical coherence fiber:

\[
F_{\mathcal P}
=
\{((r,i),(s,i)):r\neq s,\ r,s\text{ в одном блоке }\mathcal P\}.
\tag{23}
\]

### Теорема 5.1 — Точная цена произвольной partition+phase coherence

\[
\boxed{
 m_G(H_{\mathcal P};S_\times)
=t\sum_{j=1}^cn_j(n_j-1).
}
\tag{24}
\]

#### Доказательство

**Верхняя граница.** Мощность (23) равна правой части (24). Проекция на branch pairs восстанавливает disjoint union полных loopless directed cliques по блокам, а сохранение внутреннего equality fiber схлопывает независимые \(A\)-действия внутри каждого non-singleton блока до диагонального \(A\). Поэтому stabilizer равен \(H_{\mathcal P}\).

**Нижняя граница.** Пусть \(F\) имеет stabilizer ровно \(H_{\mathcal P}\). Для каждого размера \(d\ge2\) restriction на ordered pairs ветвей внутри size-\(d\) блока задаётся одним диагонально-\(A\)-инвариантным relation

\[
R_d\subseteq\Lambda^2.
\]

На cross-block клетках действуют независимые \(A\times A\), а потому всякий \(H_{\mathcal P}\)-инвариантный internal fiber там пуст или полон.

Если \(R_d\) пуст или полон, можно применить ненулевой элемент \(A\) только к одной ветви одного size-\(d\) блока. Этот лишний элемент сохранит все выбранные клетки, что противоречит exact residual group. Значит \(R_d\) непуст и собственен.

Каждая ненулевая диагональная \(A\)-орбита имеет размер не менее \(t\). Ordered branch pairs внутри блоков size class \(d\) ровно

\[
m_dd(d-1).
\]

Суммирование даёт

\[
|F|\ge t\sum_{d\ge2}m_dd(d-1)
=t\sum_jn_j(n_j-1).
\]

Граница достигается canonical equality fiber. ∎

### Следствие 5.2 — Equal-block ladder

Если \(b=cn\) и все \(c\) блоков имеют размер \(n\), то

\[
\boxed{m_G(H_{c,n};S_\times)=b(n-1)t.}
\tag{25}
\]

При \(n=1\) имеем \(m=0\); при \(n=b\) — \(m=b(b-1)t\).

---

## 6. Почему complement recovery не работает для phase coherence

Даже если последний блок разбиения восстанавливается как множество по дополнению к остальным, это не заставляет его независимое действие

\[
A^{n_j}
\]

схлопнуться до диагонального \(A\).

Поэтому

\[
\boxed{
\text{восстановление принадлежности блоку}
\not\Rightarrow
\text{восстановление внутренней фазы}.
}
\tag{26}
\]

Эта граница отделяет full coherence от следующей задачи.

---

## 7. Память только разбиения

Теперь внутренние branch phases должны остаться независимыми. Target group:

\[
J_{\mathcal P}=A^b\rtimes K_{\mathcal P}.
\tag{27}
\]

Пусть

\[
\Omega_b=\{(r,s):r\neq s\}
\tag{28}
\]

— ordered branch-pair set.

### Лемма 7.1 — Full-fiber lemma

Если \(F\subseteq S_\times\) является \(J_{\mathcal P}\)-инвариантным, то для каждой ordered branch pair \((r,s)\) внутренний слой

\[
\{((r,i),(s,j)):i,j\in\Lambda\}
\]

либо выбран целиком, либо не выбран вовсе.

#### Доказательство

Независимые факторы \(A_r\times A_s\) транзитивны на \(\Lambda^2\). ∎

Следовательно, \(F\) является полным lift некоторого branch-level relation

\[
R\subseteq\Omega_b.
\]

### Теорема 7.2 — Точная partition-only редукция

Определим

\[
\widehat R
=
\{((r,i),(s,j)):(r,s)\in R,\ i,j\in\Lambda\}.
\tag{29}
\]

Тогда

\[
\boxed{
\operatorname{Stab}_G(\widehat R)
=A^b\rtimes\operatorname{Aut}(R).
}
\tag{30}
\]

Если

\[
d(\mathcal P)
=
\min\{|R|:\operatorname{Aut}(R)=K_{\mathcal P}\},
\tag{31}
\]

то

\[
\boxed{
 m_G(J_{\mathcal P};S_\times)=t^2d(\mathcal P).
}
\tag{32}
\]

#### Доказательство

Base group \(A^b\) сохраняет каждый полный internal fiber. Branch permutation сохраняет \(\widehat R\) тогда и только тогда, когда сохраняет \(R\). Лемма 7.1 показывает, что других допустимых supports нет. ∎

---

## 8. Точные семейства partition-only памяти

### Теорема 8.1 — Два блока

Для \(p>q\ge2\):

\[
\boxed{d(p,q)=q(q-1).}
\tag{33}
\]

Для \(p>1=q\):

\[
\boxed{d(p,1)=p.}
\tag{34}
\]

Для двух равных блоков \(n,n\):

\[
\boxed{d(n,n)=2n(n-1).}
\tag{35}
\]

#### Доказательство

При \(p>q\) orbitals группы \(S_p\times S_q\) имеют веса

\[
p(p-1),\ q(q-1),\ pq,\ pq.
\]

Для \(q\ge2\) минимальная положительная orbit — clique меньшего блока. При \(q=1\) минимальна directed star веса \(p\). При равных блоках partition stabilizer есть \(S_n\wr S_2\), и within-block orbital веса \(2n(n-1)\) меньше cross-block orbital веса \(2n^2\). ∎

### Теорема 8.2 — Один non-singleton block плюс singleton class

Для типа \((n,1^m)\):

\[
\boxed{
 d(n,1^m)
=
\min\{n(n-1),\ nm,\ m(m-1)\text{ при }m\ge2\}.
}
\tag{36}
\]

### Теорема 8.3 — Три попарно различных блока

Если

\[
p>q>r\ge1,
\]

то

\[
\boxed{d(p,q,r)=qr.}
\tag{37}
\]

#### Доказательство

Directed complete bipartite relation от \(q\)-блока к \(r\)-блоку содержит \(qr\) дуг. Tail class, head class и isolated complement имеют размеры \(q,r,p\), которые попарно различны, поэтому automorphism group равна \(S_p\times S_q\times S_r\).

Ни один более дешёвый single orbital не отделяет все три класса: внутренний orbital меньшего блока выделяет только один класс, оставляя два остальных в одной полной symmetric complement-class. Следовательно, \(qr\) точно. ∎

Это первый бесконечный класс настоящего complement compression: крупнейший \(p\)-блок вообще не участвует в support.

---

## 9. Orbitals произвольного типа разбиения

Для каждого size class \(d\ge2\) с \(m_d>0\) введём within-block orbital \(W_d\) веса

\[
w(W_d)=m_dd(d-1).
\tag{38}
\]

При \(m_d\ge2\) введём equal-size cross-block orbital \(E_d\) веса

\[
w(E_d)=m_d(m_d-1)d^2.
\tag{39}
\]

Для разных sizes \(d\neq e\) введём directed orbital \(C_{d\to e}\) веса

\[
w(C_{d\to e})=m_dm_e de.
\tag{40}
\]

Все \(K_{\mathcal P}\)-инвариантные loopless directed relations являются объединениями этих orbitals.

Пусть

\[
Q(\mathcal P)=\{O_1,\ldots,O_q\}
\tag{41}
\]

и

\[
R(y)=\bigcup_{y_i=1}O_i,
\qquad y_i\in\{0,1\}.
\tag{42}
\]

---

## 10. Дихотомия надгрупп стабилизатора разбиения

Пусть \(S\) — объединение всех singleton-блоков.

Транспозиция двух точек лежит в \(K_{\mathcal P}\) ровно тогда, когда точки лежат либо в одном non-singleton block, либо обе в \(S\). Остальные транспозиции назовём **запрещёнными межблочными транспозициями**.

### Теорема 10.1 — Partition-Overgroup Dichotomy

Пусть

\[
K_{\mathcal P}\le L\le S_b.
\]

Если \(L>K_{\mathcal P}\), то выполняется хотя бы одно:

1. \(L\) содержит запрещённую межблочную транспозицию точек;
2. \(|S|\) совпадает с размером некоторого non-singleton блока, и \(L\) содержит permutation, переводящую \(S\) целиком на такой блок.

#### Доказательство

Возьмём \(g\in L\setminus K_{\mathcal P}\) и non-singleton block \(B\). Так как \(\operatorname{Sym}(B)\le K_{\mathcal P}\), все транспозиции внутри \(B\) лежат в \(K_{\mathcal P}\); после сопряжения через \(g\) все транспозиции внутри \(g(B)\) лежат в \(L\).

Если \(g(B)\) пересекает два partition blocks и хотя бы один из них non-singleton, одна из таких транспозиций становится запрещённой. Поэтому при отсутствии запрещённых транспозиций всякое block image, не лежащее в одном non-singleton блоке, должно лежать внутри \(S\).

Если \(g(B)\subsetneq S\), возьмём \(x\in g(B)\), \(y\in S\setminus g(B)\). Транспозиция \((xy)\) лежит в \(K_{\mathcal P}\), а её сопряжение через \(g^{-1}\) даёт запрещённую транспозицию между точкой \(B\) и точкой вне \(B\). Значит

\[
g(B)=S,
\]

и \(|B|=|S|\).

Если же \(g(B)\) лежит внутри non-singleton блока \(C\), собственное включение также даёт запрещённую транспозицию после обратного сопряжения. Поэтому \(g(B)=C\), и размеры блоков равны.

Применяем тот же аргумент к \(g^{-1}\). Если ни один блок не обменивается с \(S\), то \(S\) сохраняется, а все non-singleton blocks переставляются лишь внутри одинаковых size classes. Все такие действия уже лежат в \(K_{\mathcal P}\), противоречие. ∎

### Лемма 10.2 — Double coset для macro-mover

Пусть \(s=|S|\ge2\), и имеются non-singleton blocks \(B_1,\ldots,B_{m_s}\) размера \(s\). Определим macro-set

\[
\mathcal M=\{S,B_1,\ldots,B_{m_s}\}.
\]

Фиксируем одну permutation \(\tau\), обменивающую \(S\) и \(B_1\) биекцией и сохраняющую остальные blocks setwise. Тогда всякий допустимый macro-mover лежит в

\[
\boxed{K_{\mathcal P}\tau K_{\mathcal P}.}
\tag{43}
\]

#### Доказательство

На \(\mathcal M\) группа \(K_{\mathcal P}\) индуцирует полный стабилизатор выделенной macro-point \(S\), то есть \(S_{m_s}\le S_{m_s+1}\). У point stabilizer в полной symmetric group ровно два double cosets: сам stabilizer и permutations, двигающие выделенную точку. Следовательно, любой macro-mover имеет macro decomposition

\[
\bar g=\bar k_1\bar\tau\bar k_2.
\]

После lift \(\bar k_1,\bar k_2\) в \(K_{\mathcal P}\) остаются только permutations внутри partition blocks и разрешённые permutations блоков одинакового размера. Они также лежат в \(K_{\mathcal P}\). ∎

---

## 11. Exact recognition theorem

### Теорема 11.1

Для \(K_{\mathcal P}\)-инвариантного relation \(R\subseteq\Omega_b\):

\[
\boxed{
\operatorname{Aut}(R)=K_{\mathcal P}
}
\tag{44}
\]

тогда и только тогда, когда:

1. ни одна representative forbidden cross-block transposition не сохраняет \(R\);
2. если singleton macro-swap размерно возможен, одна фиксированная canonical permutation \(\tau\) его типа не сохраняет \(R\).

#### Доказательство

Необходимость очевидна. Для достаточности предположим, что оба теста выполнены, но \(\operatorname{Aut}(R)>K_{\mathcal P}\). По Теореме 10.1 либо имеется forbidden transposition, что противоречит первому тесту, либо имеется macro-mover \(g\). По Лемме 10.2

\[
g=k_1\tau k_2
\]

с \(k_1,k_2\in K_{\mathcal P}\). Так как \(K_{\mathcal P}\le\operatorname{Aut}(R)\), отсюда \(\tau\in\operatorname{Aut}(R)\), противоречие второму тесту. ∎

---

## 12. Orbital XOR-Separation Program

Для forbidden permutation \(\pi\) строим graph \(\Gamma_\pi\) на orbital indices \(1,\ldots,q\). Соединяем \(i,j\), если существует ordered pair \(z\in O_i\), для которой

\[
\pi z\in O_j,
\qquad i\neq j.
\tag{45}
\]

### Лемма 12.1

\[
\pi\in\operatorname{Aut}(R(y))
\iff
 y_i=y_j
\text{ для всех }ij\in E(\Gamma_\pi).
\tag{46}
\]

Следовательно, \(\pi\) разрушена тогда и только тогда, когда

\[
\bigvee_{ij\in E(\Gamma_\pi)}(y_i\oplus y_j)=1.
\tag{47}
\]

### Теорема 12.2 — Точная булева программа

\[
\boxed{
\begin{aligned}
\text{минимизировать }&\sum_{i=1}^q |O_i|y_i,\\
\text{при условиях }&
\bigvee_{ij\in E(\Gamma_\pi)}(y_i\oplus y_j)=1
\quad\text{для каждой representative forbidden }\pi,\\
&y_i\in\{0,1\}.
\end{aligned}}
\tag{48}
\]

Оптимум программы равен \(d(\mathcal P)\).

#### Доказательство

Каждый \(K_{\mathcal P}\)-invariant relation однозначно кодируется orbital bit-vector \(y\). По Теореме 11.1 exact automorphism group равна \(K_{\mathcal P}\) тогда и только тогда, когда разрушены все representative forbidden symmetries. Лемма 12.1 переводит это в OR-of-XOR constraints, а objective равен числу выбранных ordered pairs. ∎

---

## 13. Размер exact solver

Пусть

\[
D=\{d:m_d>0\},
\qquad k=|D|.
\tag{49}
\]

Число orbital variables:

\[
q
=
 k(k-1)
+|\{d\ge2:m_d>0\}|
+|\{d:m_d\ge2\}|,
\tag{50}
\]

поэтому

\[
q\le k^2+k.
\tag{51}
\]

Representative forbidden transposition types не больше

\[
\binom{k}{2}
+|\{d\ge2:m_d\ge2\}|,
\tag{52}
\]

плюс максимум один macro-swap.

Так как

\[
1+2+\cdots+k\le b,
\]

то

\[
k=O(\sqrt b).
\tag{53}
\]

Таким образом произвольный конечный partition type сводится к компактной exact optimization problem, размер которой определяется прежде всего числом различных block sizes.

Классификацию вычислительной сложности этой специальной программы мы оставляем открытой. NP-hardness не заявляется.

---

## 14. Anonymous terminal values

Для двух anonymous output values возможен дополнительный swap двух fibers.

Для global coherence special fiber имеет размер

\[
b(b-1)t,
\]

а complement —

\[
b(b-1)t(t-1).
\]

Равенство требует \(t=2\), а реальный wreath swap возможен только при \(b=2\).

Для arbitrary partition coherence равенство fibers требует

\[
2\sum_jn_j(n_j-1)=b(b-1)t.
\tag{54}
\]

Поскольку

\[
\sum_jn_j(n_j-1)\le b(b-1),
\]

это снова приводит только к global binary case

\[
\boxed{b=2,\ t=2.}
\tag{55}
\]

Это и есть ранее найденная уникальная 4+4 anomaly, устраняемая одной canonical root-anchor cell, после чего получаем exact anonymous support \(9\).

---

## 15. Ресурсная немонотонность

Partition+phase memory сильнее, чем partition-only:

\[
H_{\mathcal P}\le J_{\mathcal P}.
\tag{56}
\]

Но она может быть дешевле по support.

Для двух equal blocks размера \(n\ge2\):

\[
m_G(J_{\mathcal P};S_\times)=2n(n-1)t^2,
\tag{57}
\]

а

\[
m_G(H_{\mathcal P};S_\times)=2n(n-1)t.
\tag{58}
\]

Поэтому

\[
\boxed{
\frac{m_G(J_{\mathcal P};S_\times)}{m_G(H_{\mathcal P};S_\times)}=t.
}
\tag{59}
\]

Причина в admissible geometry: partition-only invariance содержит independent \(A\times A\), поэтому выбранная branch pair обязана нести весь \(t^2\)-fiber; phase coherence позволяет использовать тонкую диагональ размера \(t\).

---

## 16. Компьютерная верификация

Exact solver и независимый verifier находятся в репозитории проекта.

Для всех integer partitions при

\[
2\le b\le7
\]

были перебраны все \(K_{\mathcal P}\)-invariant orbital unions и независимо вычислены их полные automorphism groups прямым перебором \(S_b\).

Во всех случаях:

\[
\boxed{
\text{новый recognition criterion}
\iff
\operatorname{Aut}(R)=K_{\mathcal P}.
}
\tag{60}
\]

Верификация поддерживает доказательство, но не заменяет его.

---

## 17. Граница с классической литературой

Регулярные множества и setwise stabilizers являются классическими объектами. Gluck исследовал trivial set-stabilizers; современная работа Sabatini рассматривает также нетривиальные stabilizers с контролируемой структурой.

Distinguishing theory минимизирует число цветов. Chan изучал direct и wreath product actions. Alikhani–Soltani рассматривают subgroup-relative distinguishing number, где surviving symmetry требуется лишь содержать в заданной группе или, эквивалентно в их формулировке, label-preserving elements должны лежать в \(H\). Здесь же требуется exact equality stabilizer и минимизируется support weight.

Relation-group и 2-closure theory дают классическую основу бинарных relational representations. Наша partition-only задача является фиксированно-действующей weighted orbital-subselection problem внутри этой классической рамки.

Point-determining/twin-free theory объясняет локальную интуицию forbidden transpositions. Новизна не относится к самому понятию twins; специфичен exact partition-stabilizer criterion с singleton macro-swap completion и FCOA resource interpretation.

---

## 18. Заключение

Получена точная теория prescribed residual symmetry для рассматриваемой FCOA-Z ветви.

Глобальная coherence:

\[
\boxed{b(b-1)t.}
\]

Произвольная partition+phase coherence:

\[
\boxed{t\sum_jn_j(n_j-1).}
\]

Partition-only memory:

\[
\boxed{t^2d(\mathcal P).}
\]

А \(d(\mathcal P)\) точно вычисляется через finite Orbital XOR-Separation Program.

Тем самым окончательно разделяются три ресурса:

\[
\boxed{
\text{мощность output alphabet}
\quad\neq\quad
\text{стоимость support}
\quad\neq\quad
\text{число semantic states}.
}
\]

Именно это разделение является центральным результатом данной FCOA-Z работы.

---

## Литература

1. A. Malachevsky, *Fixed-Carrier Oriented Algebra (FCOA): Definition, Typed Partial Operations, Carrier Erasure, and the Canonical M0 Baseline*, Zenodo, 2026. DOI: `10.5281/zenodo.22164246`.
2. A. Malachevsky, *Reflections on How a Ray Becomes an Axis: And why old operations reveal new local laws after a second direction appears*, Zenodo, 2026. DOI: `10.5281/zenodo.22171473`.
3. D. Gluck, *Trivial Set-Stabilizers in Finite Permutation Groups*, Canadian Journal of Mathematics 35 (1983), 59–67. DOI: `10.4153/CJM-1983-005-2`.
4. M. Chan, *The distinguishing number of the direct product and wreath product action*, Journal of Algebraic Combinatorics 24 (2006), 331–345. DOI: `10.1007/s10801-006-0006-7`.
5. S. Alikhani, S. Soltani, *The distinguishing number of groups based on the distinguishing number of subgroups*, Journal of Information and Optimization Sciences 43 (2022), 311–321. DOI: `10.1080/02522667.2021.2003011`; arXiv:1701.00141.
6. F. Dalla Volta, J. Siemons, *Orbit equivalence and permutation groups defined by unordered relations*, Journal of Algebraic Combinatorics 35 (2012), 547–564. DOI: `10.1007/s10801-011-0313-5`.
7. M. Grech, A. Kisielewicz, *Orbit closed permutation groups, relation groups, and simple groups*, Journal of Algebraic Combinatorics 57 (2023). DOI: `10.1007/s10801-022-01214-2`.
8. M. W. Liebeck, C. E. Praeger, J. Saxl, *On the 2-Closures of Finite Permutation Groups*, Journal of the London Mathematical Society 37 (1988), 241–252. DOI: `10.1112/jlms/s2-37.2.241`.
9. D. P. Sumner, *Point determination in graphs*, Discrete Mathematics 5 (1973), 179–187. DOI: `10.1016/0012-365X(73)90109-X`.
10. R. C. Entringer, L. D. Gassman, *Line-critical point determining and point distinguishing graphs*, Discrete Mathematics 10 (1974), 43–55. DOI: `10.1016/0012-365X(74)90019-3`.
11. P. Hell, C. Hernández-Cruz, *Point determining digraphs, {0,1}-matrix partitions, and dualities in full homomorphisms*, Discrete Mathematics 338 (2015), 1755–1762. DOI: `10.1016/j.disc.2014.12.001`.
12. D. J. McCarthy, L. V. Quintas, *A stability theorem for minimum edge graphs with given abstract automorphism group*, Transactions of the AMS 208 (1975), 27–39. DOI: `10.1090/S0002-9947-1975-0369148-4`.
13. L. Babai, A. J. Goodman, L. Lovász, *Graphs with Given Automorphism Group and Few Edge Orbits*, European Journal of Combinatorics 12 (1991), 185–203. DOI: `10.1016/S0195-6698(13)80085-6`.
14. L. Babai, A. J. Goodman, *Subdirectly Reducible Groups and Edge-Minimal Graphs with Given Automorphism Group*, Journal of the London Mathematical Society 47 (1993), 417–432. DOI: `10.1112/jlms/s2-47.3.417`.
15. D. Deligeorgaki, *Smallest graphs with given automorphism group*, Journal of Algebraic Combinatorics 56 (2022), 609–633. DOI: `10.1007/s10801-022-01125-2`.
16. L. Sabatini, *On stabilizers in finite permutation groups*, Bulletin of the London Mathematical Society, 2026. DOI: `10.1112/blms.70201`.
