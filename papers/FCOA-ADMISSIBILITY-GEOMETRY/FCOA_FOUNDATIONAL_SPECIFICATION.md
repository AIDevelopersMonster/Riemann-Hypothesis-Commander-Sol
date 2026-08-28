# FCOA — Foundational Mathematical Specification

**Русское название:** Базовая математическая спецификация FCOA  
**Status:** canonical working foundation  
**Purpose:** зафиксировать сам математический объект FCOA отдельно от исследовательских веток G1/G2/G3/G4 и Arithmetic Leakage  
**Compatibility:** не изменяет опубликованную цепочку `M0 -> G1 -> G2`; консолидирует уже принятые соглашения и явно отмечает незаполненные части

---

## 1. Где FCOA находится в обычной математической классификации

В самом широком смысле алгебра изучает операции над элементами множеств. FCOA относится к этой общей области, но ее естественный формальный дом — не группа, кольцо или поле и не обычная тотальная одно-сортная универсальная алгебра.

Ближайшая стандартная форма:

\[
\boxed{
\text{many-sorted partial algebra}
+
\text{oriented carrier presentation}
+
\text{first-order relational reducts}.
}
\]

Главные отличия от обычного школьного `+`/`x`:

1. операции могут быть **частичными**;
2. порядок аргументов структурно значим;
3. область определенности операции является частью информации;
4. результат может уходить из активного носителя в отдельный terminal/output sort;
5. внешний порядок носителя может использоваться при построении, а затем стираться при Carrier-Erasure Test;
6. никакие законы коммутативности, ассоциативности, дистрибутивности, существования нуля, единицы или обратных не предполагаются без отдельного доказательства.

Поэтому слово `Algebra` в FCOA означает **алгебраическую структуру с операциями на фиксированном носителе**, а не утверждение, что структура является кольцом, полем, полугруппой и т. п.

---

## 2. FCOA — это класс структур, а не одна заранее полностью заполненная таблица

### Definition 2.1 — abstract FCOA datum

Базовый FCOA-объект задается данными

\[
\mathfrak F=
\bigl(
B,\preceq;\;\mathcal O;\;\Omega
\bigr),
\]

где:

- \(B\) — **fixed active carrier**;
- \(\preceq\) — ориентация/порядок, доступный на стадии построения;
- \(\mathcal O\) — семейство дополнительных output sorts;
- \(\Omega\) — конечная сигнатура частичных операций фиксированной арности.

Каждая бинарная операция имеет тип

\[
\omega:B\times B\rightharpoonup B\sqcup O_1\sqcup\cdots\sqcup O_t.
\]

Символ \(\rightharpoonup\) означает, что операция **не обязана быть определена на каждой паре**.

Аргументы являются позиционными:

\[
\omega(x,y)
\quad\text{и}\quad
\omega(y,x)
\]

— разные клетки таблицы. Role-sensitivity не утверждает автоматически, что их значения различны; она запрещает заранее отождествлять эти роли.

### Definition 2.2 — oriented presentation and erased reduct

Ориентированная презентация хранит \(\preceq\):

\[
\mathfrak F^{\rm or}=(B,\preceq;\mathcal O;\Omega).
\]

Операционный reduct после стирания ориентации:

\[
\mathfrak F^\circ=(B;\mathcal O;\Omega).
\]

Центральный вопрос memory programme:

> Какие отношения, использованные для построения, остаются восстанавливаемыми/FO-определимыми в \(\mathfrak F^\circ\)?

---

## 3. Каноническая натуральная база

Для основной линии принимается натуральный активный носитель

\[
\boxed{B=\mathbb N_0=\{0,1,2,\ldots\}.}
\]

Символьная запись проекта

\[
P_0,P_1,P_2,\ldots
\]

есть просто переименование натуральной базы:

\[
\iota(n)=P_n.
\]

Мы сохраняем запись \(P_n\), когда важно визуально отделить **элемент FCOA** от обычного натурального числа.

### Firewall 3.1 — обычная арифметика не входит автоматически

Использование \(\mathbb N_0\) как множества **не добавляет** в сигнатуру обычные

\[
+_{\mathbb N},\qquad \times_{\mathbb N}.
\]

Индекс \(n\) является внешней координатой/метаязыком, пока соответствующая арифметика не доказана восстанавливаемой внутри reduct.

На стадии генерации разрешено пользоваться фиксированной ориентацией

\[
0<1<2<\cdots
\]

и локальными successor/predecessor rules, если их provenance явно объявлен. После стирания порядка их внутреннее восстановление является отдельной теоремой, а не предпосылкой.

---

## 4. Конечные truncations и бесконечный master object

Для вычислений и конечной model-theoretic программы используем

\[
B_N=\{0,1,\ldots,N\}
\]

или эквивалентно

\[
X_N=\{P_0,\ldots,P_N\},\qquad N\ge3.
\]

Канонический бесконечный baseline определяется как согласованное объединение всех M0-правил:

\[
\mathfrak F^{\omega}_{M0}
=\bigcup_{N\ge3}\mathfrak F^{N}_{M0}
\]

в смысле стабильной таблицы на всех уже существующих аргументах.

Это **определение master table**, но не перенос конечных FO-теорем на бесконечный предел. Например, конечная rigidness или конечная recoverability не превращаются автоматически в uniform FO theorem на \(\omega\).

---

## 5. Output sorts: почему результат не обязан оставаться натуральным

FCOA использует orthogonal/terminal outputs. Чтобы вся конструкция оставалась буквально основанной на натуральных координатах, их можно представить tagged copies натурального множества:

\[
E^+=\{(+,n):n\ge1\},
\]

\[
E^\ast=\{(\ast,n):n\ge2\},
\]

\[
E^\times=\{(\times,n):n\ge2\}.
\]

В проектной записи:

\[
(+,n)=E_n^+,
\qquad
(\ast,n)=E_n^\ast,
\qquad
(\times,n)=E_n^\times.
\]

Эти множества дизъюнктны с активным носителем \(B\).

Дополнительные branch-specific terminal symbols, например \(\Omega\) или \(\Omega_\pm\), образуют отдельные конечные output sorts.

### Fixed rule 5.1 — terminality

По умолчанию элементы \(E^+,E^\ast,E^\times\) и свежие \(\Omega\)-outputs **не являются входами** базовых операций.

То есть выражения вида

\[
E_i^+\oplus x,
\qquad
x\otimes E_j^\times,
\qquad
\Omega\otimes x
\]

не имеют значения, пока отдельная исследовательская ветка явно не введет соответствующее typed rule.

Это не пробел в таблице, а принятая terminal-output дисциплина.

---

## 6. Канонический M0 baseline на натуральном носителе

В базовой сигнатуре имеются два частичных бинарных символа

\[
\oplus,\qquad\otimes.
\]

Их названия исторические и **не означают обычные натуральные сложение и умножение**.

### 6.1 Operation `oplus`

Тип:

\[
\oplus:B\times B\rightharpoonup B\sqcup E^+.
\]

Для каждого \(n\ge1\):

\[
\boxed{0\oplus n=n,}
\tag{A1}
\]

\[
\boxed{n\oplus0=n-1,}
\tag{A2}
\]

\[
\boxed{n\oplus n=E_n^+.}
\tag{A3}
\]

В проектной записи:

\[
P_0\oplus P_n=P_n,
\]

\[
P_n\oplus P_0=P_{n-1},
\]

\[
P_n\oplus P_n=E_n^+.
\]

Все остальные base-base клетки **UNDEF**.

В частности:

\[
0\oplus0=\mathrm{UNDEF},
\]

и для \(m,n>0,\ m\ne n\):

\[
m\oplus n=\mathrm{UNDEF}.
\]

### 6.2 Operation `otimes`

Тип:

\[
\otimes:B\times B
\rightharpoonup
B\sqcup E^\ast\sqcup E^\times.
\]

Для \(n\ge1\):

\[
\boxed{0\otimes n=0.}
\tag{M1}
\]

Для \(n\ge2\):

\[
\boxed{n\otimes0=E_n^\ast,}
\tag{M2}
\]

\[
\boxed{1\otimes n=n\otimes1=n,}
\tag{M3}
\]

\[
\boxed{n\otimes n=E_n^\times.}
\tag{M4}
\]

Все остальные base-base клетки **UNDEF**.

Особенно:

\[
0\otimes0=\mathrm{UNDEF},
\]

\[
1\otimes0=\mathrm{UNDEF},
\qquad
1\otimes1=\mathrm{UNDEF},
\]

и для различных \(m,n\ge2\):

\[
m\otimes n=\mathrm{UNDEF}.
\]

---

## 7. Что эти операции делают структурно

### 7.1 `oplus` — boundary/predecessor baseline

`oplus` фиксирует сильную асимметрию границы:

- \(0\) действует слева как локальная identity на положительных base points;
- справа тот же \(0\) вызывает predecessor shift;
- диагональ выводит результат в orthogonal sort.

Поэтому

\[
0\oplus n=n
\quad\text{но}\quad
n\oplus0=n-1.
\]

Это operation с сильной boundary-mediated order memory. В конечном M0 ее automorphism group уже trivial.

### 7.2 `otimes` — symmetry-rich baseline

`otimes` специально оставляет generic sector

\[
G=\{2,3,4,\ldots\}
\]

максимально exchangeable на M0-уровне:

- \(0\) — левый absorber на положительных points;
- \(1\) — локальная two-sided identity для generic points \(n\ge2\);
- справа \(0\) отправляет generic point в индивидуальный orthogonal output;
- generic off-diagonal cells оставлены пустыми.

На конечном truncation

\[
G_N=\{2,\ldots,N\}
\]

это дает базовую symmetry

\[
\operatorname{Aut}(\otimes_{M0})\cong S_{N-1}.
\]

Именно поэтому `otimes` стало основным лабораторным operation для G1/G2/G3/G4: новые structural memories можно измерять относительно известного symmetry baseline.

---

## 8. UNDEF, OUT и «мы еще не решили» — три разные вещи

### UNDEF

`UNDEF` означает:

> В текущей математической структуре эта пара **не входит в domain operation**.

`UNDEF` не является элементом носителя и не является специальным значением операции.

### OUT

`OUT` применяется только при анализе конечной truncation глобально заданного rule, когда требуемый результат существует в master family, но лежит за текущей конечной границей.

`OUT` также не является operation value.

### OPEN

`OPEN` означает:

> Проект пока не принял никакого канонического правила для этой области в будущих расширениях.

Клетка может быть `UNDEF` в M0 и одновременно быть **доступна для открытия в новой ветке**. Тогда новая ветка создает другую структуру; она не «исправляет пропуск» в M0.

---

## 9. Полная карта M0-клеток и их назначение

| Operation sector | Current status | Purpose |
|---|---|---|
| \(0\oplus n,\ n\ge1\) | **F** | left-boundary identity-like role |
| \(n\oplus0,\ n\ge1\) | **F** | predecessor / boundary direction |
| \(n\oplus n,\ n\ge1\) | **F** | orthogonal diagonal output |
| \(0\oplus0\) | **F = UNDEF in M0** | preserve singular boundary; no zero law assumed |
| \(m\oplus n,\ m,n>0,m\ne n\) | **F = UNDEF in M0 / O for future branches** | leaves generic additive sector uncommitted |
| \(0\otimes n,\ n\ge1\) | **F** | left absorber role |
| \(n\otimes0,\ n\ge2\) | **F** | right-boundary orthogonal output |
| \(1\otimes n=n\otimes1,\ n\ge2\) | **F** | local generic identity role |
| \(n\otimes n,\ n\ge2\) | **F** | orthogonal generic diagonal |
| \(0\otimes0\) | **F = UNDEF in M0** | boundary singularity |
| \(1\otimes0\) | **F = UNDEF in M0** | keeps left/right role distinction |
| \(1\otimes1\) | **F = UNDEF in M0** | no global identity axiom |
| \(m\otimes n,\ m,n\ge2,m\ne n\) | **F = UNDEF in M0 / O for extensions** | preserves generic \(S_\infty\)-type exchangeability in master baseline |
| any terminal output used as input | **F = typed UNDEF** | outputs are terminal unless a new branch changes the type system |

---

## 10. Что НЕ является законом FCOA

Следующие утверждения **не входят в определение FCOA**:

\[
x\oplus y=y\oplus x,
\]

\[
(x\oplus y)\oplus z=x\oplus(y\oplus z),
\]

\[
x\otimes y=y\otimes x,
\]

\[
(x\otimes y)\otimes z=x\otimes(y\otimes z),
\]

\[
x\otimes(y\oplus z)=
(x\otimes y)\oplus(x\otimes z).
\]

Не предполагаются также глобальные neutral elements, inverses, closure on the base sort или ordinary arithmetic interpretation.

Если какое-либо привычное свойство встречается на части domain, это локальный факт конкретной operation table, а не автоматически переносимый алгебраический закон.

---

## 11. Derived objects: что мы измеряем, но не добавляем как primitive symbols

Для каждой partial operation \(\star\) рассматриваются:

### Domain

\[
D_\star=\{(x,y):x\star y\text{ defined}\}.
\]

### Left/right translations

\[
L_a^\star(x)=a\star x,
\qquad
R_a^\star(x)=x\star a.
\]

### Commutation locus

\[
\operatorname{Comm}_\star
=\{(x,y):x\star y,y\star x\text{ defined and equal}\}.
\]

### Association spectrum

Для triples различаем:

`EQ`, `NEQ`, `LEFT`, `RIGHT`, `NONE`

в зависимости от definedness и равенства двух bracketings.

### Automorphism group

\[
\operatorname{Aut}(\mathfrak F^\circ)
\]

измеряет structural symmetry reduct.

Все эти объекты являются diagnostics/invariants; они не считаются новой памятью, пока не внесены в signature отдельным правилом.

---

## 12. Branches are extensions, not hidden parts of the base algebra

### M0 — canonical baseline

Это именно таблица Sections 6–9.

### G1 — external relation

Добавляется внешний skeleton

\[
A\subseteq G^2,
\]

но M0-operation table не меняется.

### G2 — domain compilation

Вводится fresh terminal \(\Omega\) и открываются successor-oriented generic cells

\[
n\otimes_1(n+1)=\Omega,
\qquad n\ge2.
\]

Reverse/nonadjacent cells остаются undefined.

### G3/G4

Это отдельные post-publication extensions, исследующие value geometry, bounded-output amplification и order recovery. Их cells **не входят в canonical M0**.

### Arithmetic-Leakage constructions

Finite-state markers, EqGap, generated addition, BIT-history, digit/CRT carriers и другие AL-constructions — это further structures/interpretations над FCOA programme. Они не должны задним числом превращаться в базовые операции FCOA.

---

## 13. Status ledger базовой математики

### **F — Fixed**

1. натуральный active carrier \(B=\mathbb N_0\) и finite truncations;
2. внешняя координатная запись \(P_n\leftrightarrow n\);
3. ordinary `+` and `times` on indices are not internal primitives;
4. partiality and positional argument roles;
5. M0 rules (A1)–(A3), (M1)–(M4);
6. unspecified M0 base cells are UNDEF, not guessed by analogy;
7. orthogonal outputs are typed/terminal;
8. domain geometry is structural data;
9. external orientation and erased operational reduct are distinguished;
10. new cells/rules create an extension/checkpoint, not a silent completion of M0.

### **W — Working architectural conventions**

1. `FCOA = Fixed-Carrier Oriented Algebra` as programme terminology;
2. semicolon notation \(F^\sigma(x;y)\) to emphasize argument roles;
3. `sigma(x,y) in {<,=,>}` as convenient branch-selection architecture where applicable;
4. the exact minimal abstract axiom package common to every future object called “FCOA”.

### **O — Open foundational choices**

1. whether any generic off-diagonal \(\oplus\)-law should ever become canonical beyond M0;
2. whether any generic off-diagonal \(\otimes\)-law should ever become canonical rather than branch-specific;
3. whether terminal outputs should remain permanently terminal in the broadest FCOA class or whether nested-output algebras form a formally named subclass;
4. whether the infinite master object itself, rather than the coherent finite family, should be the primary semantic object;
5. whether a preferred minimal signature should contain orientation as a primitive relation or only as generator provenance;
6. whether FCOA should ultimately be axiomatized as one category/class of partial algebras or retained as a programme of explicitly specified families;
7. which representation transformations should count as the “same” FCOA object for resource comparisons.

These items are genuinely open and must not be silently fixed by future examples.

---

## 14. Minimal canonical notation going forward

Use

\[
\boxed{
\mathfrak F_{M0}^{\omega}
=(B,\mathcal E;\oplus,\otimes)
}
\]

for the infinite natural-carrier baseline, where

\[
B=\mathbb N_0,
\qquad
\mathcal E=E^+\sqcup E^\ast\sqcup E^\times.
\]

Use

\[
\boxed{
\mathfrak F_{M0}^{N}
}
\]

for its finite truncation with active carrier \(B_N\).

When orientation is retained explicitly, write

\[
\mathfrak F_{M0}^{\omega,\rm or}
=(B,<,\mathcal E;\oplus,\otimes).
\]

When orientation is erased, write

\[
\mathfrak F_{M0}^{\omega,\circ}
=(B,\mathcal E;\oplus,\otimes).
\]

Branch names such as G2/G4 must appear as subscripts/superscripts or separate structure symbols; they are not silently folded into \(\mathfrak F_{M0}\).

---

## 15. Why this specification is needed

Research on order memory, rigidity, arithmetic leakage and representation dimension only makes sense if the reference object is stable.

The canonical backend is therefore:

\[
\boxed{
\text{natural active carrier}
\to
\text{sparse M0 partial operations}
\to
\text{typed orthogonal outputs}
\to
\text{explicitly named extensions}
\to
\text{erasure / definability / cost tests}.
}
\]

The **frontier** may change from week to week. This document is intended to keep the **object being studied** fixed unless an explicit foundational revision is made.

---

## 16. Claim discipline

This specification does not claim novelty for partial algebras, many-sorted structures, universal algebra, relational reducts, automorphism methods or first-order interpretations separately.

Its role is internal mathematical normalization of the FCOA programme: exactly which carrier is used, exactly which base operation cells are fixed, exactly which cells are undefined, what counts as an extension, and which classical algebraic laws are deliberately not assumed.