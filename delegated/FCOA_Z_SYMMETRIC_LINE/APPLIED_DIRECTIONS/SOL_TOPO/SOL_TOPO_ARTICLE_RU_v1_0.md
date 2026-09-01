# Тени каналов слияния на знаковом одномерном носителе FCOA: препятствие кос и барьер когерентности

**Версия:** 1.0 — исправленная предпубликационная рукопись  
**Дата:** 2026-09-01  
**Программа:** SOL-TOPO / прикладные направления FCOA-Z  
**База:** FCOA-Z v1.1, DOI `10.5281/zenodo.22169264`  
**Статус:** ПУБЛИКАЦИОННЫЙ ПОРОГ ДОСТИГНУТ / HOSTILE AUDIT ПРОЙДЕН / ФИЗИЧЕСКИЕ ПРЕТЕНЗИИ ИСКЛЮЧЕНЫ

---

## Аннотация

Мы исследуем, насколько далеко знаковая одномерная Fixed-Carrier Oriented Algebra (FCOA-Z) может воспроизвести структурные особенности, которые в теории неабелевых энионов описываются каналами слияния, деревьями слияния, ассоциаторами и косами. Цель намеренно ограничена: никакого физического отождествления знаков, отражения или выходов FCOA с энионными зарядами не предполагается.

На каждом фиксированном радиальном уровне три существующих терминальных типа `E_n^+`, `E_n^*` и `E_n^times` образуют трёхсимвольный алфавит, который точно кодирует **носитель** multiplicity-free правил слияния Ising. В частности, двухканальный носитель правила `sigma x sigma = 1 + psi` представляется двухэлементным типизированным выходным слоем `{E_n^+,E_n^times}`. Консервативное правило в mixed-sector реализует этот носитель, не меняя ни одной унаследованной same-sign ячейки FCOA.

Далее возникают три жёстких препятствия. Во-первых, каждая примитивная операция FCOA остаётся функциональной, поэтому одна ячейка не может внутренне возвращать прямую сумму двух каналов. Во-вторых, терминальные выходы не входят обратно в старую сигнатуру операций, поэтому деревья повторного слияния и `F`-ходы недоступны. В-третьих, неупорядоченное конфигурационное пространство конечного числа попарно различных точек на строгой прямой стягиваемо; следовательно, одномерная геометрия носителя имеет тривиальную фундаментальную группу и не может породить неабелеву braid-memory.

Hostile audit промежуточной LC2-конструкции выявляет дополнительное структурное различие. Split-output reflection действует на **зеркальный provenance** `E_n^alpha <-> bar E_n^alpha`, тогда как Ising-ассоциатор смешивает различные **типы fusion-channel** `E_n^+` и `E_n^times`. Эти две бинарные степени свободы нельзя отождествлять. Отсюда следует block-diagonal no-go для channel mixing: reflection/provenance-операторы, порождённые проверенной выходной структурой FCOA, не могут дать Ising-Hadamard на fusion-channel factor.

Наконец, мы показываем, что single-fiber LC2 с unary endomorphisms не способен даже сформулировать категорный pentagon без дополнительного tensor/fusion-tree address layer. После добавления этого слоя и выбора Ising fusion ring стандартная классификация Tambara-Yamagami и Ising-категорий оставляет две monoidal completion и четыре braiding на каждой, всего восемь braided Ising categories. Эти классы когерентности являются дополнительными данными, а не следствиями текущей знаковой прямой.

Итоговая лестница ресурсов имеет вид

\[
\boxed{
\text{знаковая прямая}
<
\text{типизированные каналы}
<
\text{provenance-fiber}
<
\text{линейное смешивание каналов}
<
\text{fusion-tree composition}
<
\text{monoidal class}
<
\text{braided class}.
}
\tag{1}
\]

Основной вклад состоит в точной positive-negative границе: FCOA-Z поддерживает конечные тени fusion-channel, но coherent non-Abelian anyon structure требует независимых композиционных и когерентностных ресурсов.

---

## 1. Область утверждений

Формальный вопрос статьи таков:

\[
\boxed{
\text{могут ли mixed-sector взаимодействия FCOA и типизированные outputs кодировать fusion-channel structure,}
}
\tag{2}
\]

и, если да,

\[
\boxed{
\text{какие дополнительные ресурсы необходимы до появления }F/R\text{-когерентности и braid-memory?}
}
\tag{3}
\]

Сопоставление исключительно структурное. Мы **не** отождествляем

- две ветви FCOA с particle/antiparticle charge;
- отражение FCOA с CPT, обменом или braiding;
- mixed-sign cell с аннигиляцией;
- output type с физическим superselection sector;
- конечный output-fiber с квантовым Hilbert space, пока линейная структура явно не добавлена.

---

## 2. Используемые данные FCOA-Z

Знаковый носитель:

\[
B^{\pm}
=
\{P_0\}
\sqcup
\{P_n^+:n\ge1\}
\sqcup
\{P_n^-:n\ge1\},
\tag{4}
\]

с отражением

\[
\nu(P_0)=P_0,
\qquad
\nu(P_n^+)=P_n^-,
\qquad
\nu(P_n^-)=P_n^+.
\tag{5}
\]

На унаследованной положительной лучевой части имеются терминальные outputs

\[
P_n^+\oplus P_n^+=E_n^+,
\tag{6}
\]

\[
P_n^+\otimes P_0=E_n^*\qquad(n\ge2),
\tag{7}
\]

и

\[
P_n^+\otimes P_n^+=E_n^\times\qquad(n\ge2).
\tag{8}
\]

Negative-negative cells задаются отражением после выбора lift для terminal outputs. Mixed sectors

\[
(P_i^+,P_j^-),
\qquad
(P_i^-,P_j^+)
\tag{9}
\]

остаются единственной base-base областью, не определённой унаследованной positive table и simultaneous reflection.

Терминальные значения `E_n^alpha` являются sinks: общих правил, позволяющих им снова входить в `oplus` или `otimes`, нет.

---

## 3. Ising fusion data как целевой шаблон

Используем простые метки

\[
\mathcal I=\{1,\psi,\sigma\}
\tag{10}
\]

и multiplicity-free Ising fusion rules

\[
1\times a=a\times1=a,
\qquad
\psi\times\psi=1,
\qquad
\psi\times\sigma=\sigma\times\psi=\sigma,
\tag{11}
\]

\[
\boxed{\sigma\times\sigma=1+\psi.}
\tag{12}
\]

Пусть `N_ab^c` — fusion multiplicities. Тогда

\[
N_{\sigma\sigma}^{1}=N_{\sigma\sigma}^{\psi}=1.
\tag{13}
\]

Fusion support сам по себе ещё не образует fusion category: требуются iterated fusion spaces, `F`-moves, `R`-symbols и pentagon/hexagon coherence.

---

## 4. Точное конечное кодирование fusion support

Фиксируем `n>=2` и определяем

\[
O_n=\{E_n^+,E_n^*,E_n^\times\}.
\tag{14}
\]

Вводим биекцию

\[
\chi_n(1)=E_n^+,
\qquad
\chi_n(\sigma)=E_n^*,
\qquad
\chi_n(\psi)=E_n^\times.
\tag{15}
\]

Для `a,b in I` положим

\[
\Phi_n(a,b)
=
\{\chi_n(c):N_{ab}^c=1\}.
\tag{16}
\]

### Теорема 4.1 — Вложение fusion support

Для всех `a,b,c in I`

\[
\boxed{
N_{ab}^c=1
\iff
\chi_n(c)\in\Phi_n(a,b).
}
\tag{17}
\]

В частности,

\[
\boxed{
\Phi_n(\sigma,\sigma)=\{E_n^+,E_n^\times\}.
}
\tag{18}
\]

### Доказательство

По определению (16) fiber является образом множества всех ненулевых fusion channels при биекции (15). Инъективность предотвращает слияние разных каналов, а сюръективность сопоставляет каждой выбранной terminal type ровно одну простую Ising label. Равенство (18) следует из (12)-(13). `QED`.

### Ограничение

Теорема кодирует support, но не произвольную multiplicity. При `N_ab^c>1` одной метки `E_n^alpha` недостаточно для различения basis states.

---

## 5. Консервативная mixed-sector реализация

Используем shared terminal reflection lift и для всех `n>=2` задаём

\[
P_n^+\oplus P_n^-=E_n^+,
\qquad
P_n^-\oplus P_n^+=E_n^+,
\tag{19}
\]

\[
P_n^+\otimes P_n^-=E_n^\times,
\qquad
P_n^-\otimes P_n^+=E_n^\times.
\tag{20}
\]

Другие undefined cells не открываются. Для base pair `(x,y)` определим bundled terminal channel set

\[
\mathcal C(x,y)
=
\{\omega(x,y):\omega\in\{\oplus,\otimes\},\ \omega(x,y)\text{ terminal}\}.
\tag{21}
\]

### Теорема 5.1 — Консервативная двухканальная реализация

Расширение (19)-(20) сохраняет каждую legacy FCOA cell и simultaneous reflection, причём

\[
\boxed{
\mathcal C(P_n^+,P_n^-)
=
\mathcal C(P_n^-,P_n^+)
=
\{E_n^+,E_n^\times\}.
}
\tag{22}
\]

### Доказательство

Все новые ячейки лежат в ранее свободном mixed sector (9), поэтому ни одно унаследованное значение не меняется. Правило единообразно по radial depth, reflection меняет местами два ordered mixed pairs, а shared terminal lift фиксирует значения. Формула (22) непосредственно следует из (19)-(21). `QED`.

Результат `1D-CLOSED` на уровне one-step support. Но два результата получаютcя объединением **двух разных primitive operation symbols**, что слабее одного intrinsic fusion product с двумя каналами.

---

## 6. Препятствия функциональности и re-entry

### Теорема 6.1 — Single-operation channel obstruction

Примитивная binary operation FCOA является partial function

\[
\omega:D_\omega\to Y.
\tag{23}
\]

Поэтому одна input cell не может одновременно иметь два различных terminal values. Следовательно, никакая неизменённая primitive operation не реализует (12) как intrinsic direct-sum-valued fusion law.

### Доказательство

Функциональность означает единственность значения на каждой определённой паре. Два разных значения противоречат определению функции. `QED`.

### Теорема 6.2 — Terminal-sink obstruction

При текущей terminal semantics невозможно построить faithful depth-two fusion tree только старыми операциями.

### Доказательство

После первого шага

\[
x\,\omega\,y=E_n^\alpha
\tag{24}
\]

второй fusion step требует ячейку вида

\[
E_n^\alpha\,\omega'\,z
\quad\text{или}\quad
z\,\omega'\,E_n^\alpha.
\tag{25}
\]

Общего re-entry нет. Следовательно, intermediate channel не участвует в следующем fusion step и сравнение parenthesizations через `F`-move невозможно. `QED`.

---

## 7. Препятствие braid topology на строгой прямой

Пусть

\[
\operatorname{Conf}_m(\mathbb R)
=
\{(x_1,\ldots,x_m):x_i\ne x_j\text{ при }i\ne j\}
\tag{26}
\]

и

\[
C_m(\mathbb R)
=
\operatorname{Conf}_m(\mathbb R)/S_m.
\tag{27}
\]

### Теорема 7.1 — Стягиваемость неупорядоченных конфигураций на прямой

Для всех `m>=1`

\[
\boxed{C_m(\mathbb R)\text{ стягиваемо}.}
\tag{28}
\]

Следовательно,

\[
\boxed{\pi_1(C_m(\mathbb R))=0.}
\tag{29}
\]

### Доказательство

Каждая неупорядоченная конфигурация имеет единственного sorted representative

\[
x_1<x_2<\cdots<x_m.
\tag{30}
\]

Поэтому `C_m(R)` гомеоморфно открытому chamber

\[
\Delta_m=\{(x_1,\ldots,x_m)\in\mathbb R^m:x_1<\cdots<x_m\},
\tag{31}
\]

который выпуклый и потому стягиваемый. `QED`.

В плоскости фундаментальная группа соответствующего unordered configuration space является braid group `B_m`. Следовательно, strict one-dimensional geometry сама не порождает anyonic braid topology.

---

## 8. Corrigendum к промежуточной LC2-конструкции

В промежуточном отчёте `SOL_TOPO_LC2_REFLECTION_BRAID_v0_2.md` был активирован split terminal orbit

\[
E_n^\alpha\longleftrightarrow\bar E_n^\alpha
\tag{32}
\]

и корректно установлено, что после free linearization reflection swap `J` и provenance sign `S` удовлетворяют

\[
J^2=S^2=I,
\qquad
JS=-SJ.
\tag{33}
\]

Следовательно, на этом **provenance orbit** возникает локальный Hadamard-type duality

\[
H_{pr}=\frac{J+S}{\sqrt2}.
\tag{34}
\]

Алгебраическое утверждение (33)-(34) сохраняется.

Отзывается только интерпретация, согласно которой (34) уже является Ising fusion-channel associator.

Причина — type mismatch. В v0.1 fusion dictionary использовано

\[
1\leftrightarrow E_n^+,
\qquad
\psi\leftrightarrow E_n^\times,
\tag{35}
\]

то есть channel degree of freedom есть `E^+ versus E^times`. Reflection же действует как `E^alpha versus bar E^alpha` **внутри фиксированного terminal type**.

Корректное разложение:

\[
\boxed{
H_n\cong H_{ch}\otimes H_{pr},
}
\tag{36}
\]

где

\[
H_{ch}=\operatorname{span}\{|1\rangle,|\psi\rangle\},
\qquad
H_{pr}=\operatorname{span}\{|+\rangle,|-\rangle\}.
\tag{37}
\]

Старые reflection/provenance operators действуют на втором factor, Ising associator — на первом.

Corrigendum не затрагивает Теоремы 4.1, 5.1, 6.1, 6.2 и 7.1.

---

## 9. Разделение channel/provenance

На исправленном four-state space старые output operators имеют вид

\[
J_{old}=I_{ch}\otimes X_{pr},
\qquad
S_{old}=I_{ch}\otimes Z_{pr}.
\tag{38}
\]

Поэтому любая algebra, порождённая ими вместе с type-preserving scalars/projectors, block-diagonal относительно

\[
H_n=H_n^+\oplus H_n^\times.
\tag{39}
\]

### Теорема 9.1 — Typed-sort channel-mixing obstruction

Если отсутствует primitive map между terminal sorts `E^+` и `E^times`, каждый generated output operator сохраняет channel blocks. Следовательно, Ising channel Hadamard

\[
H_{ch}
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}
\tag{40}
\]

не порождается проверенной reflection/provenance algebra.

### Доказательство

Каждый разрешённый generator сохраняет terminal type. Суммы и композиции block-diagonal operators остаются block-diagonal. Матрица (40) имеет ненулевые cross-channel entries. `QED`.

Минимально нужен хотя бы один cross-type channel mixer, например

\[
X_{ch}|1\rangle=|\psi\rangle,
\qquad
X_{ch}|\psi\rangle=|1\rangle.
\tag{41}
\]

Такого primitive в FCOA-Z нет.

---

## 10. Pentagon expressibility barrier

Категорный associator имеет вид

\[
\alpha_{a,b,c}:(a\otimes b)\otimes c
\to
a\otimes(b\otimes c).
\tag{42}
\]

Pentagon сравнивает композиции между пятью parenthesizations fourfold tensor product.

### Теорема 10.1 — Single-fiber LC2 не формулирует pentagon внутренне

Теория, содержащая только active finite fibers `H_q` и unary endomorphisms `H_q -> H_q`, не может внутренне сформулировать pentagon equation без tensor/fusion-tree composition layer.

### Доказательство

Pentagon требует binary tensor product на labels, parenthesized fusion-tree objects, tensoring morphisms with identities и canonical source/target matching между reassociation paths. В family of unrelated fibers с unary endomorphisms этих typed constructions нет. Поэтому сами члены pentagon equation не определены. `QED`.

Минимальный coherence-address resource:

\[
\boxed{
\text{labels}
+
\text{binary fusion composition}
+
\text{parenthesization addresses}
+
\text{functorial action on morphisms}.
}
\tag{43}
\]

Это compositional memory, а не дополнительная spatial coordinate.

---

## 11. Условная coherent completion

Чтобы понять остаточную свободу после добавления tensor layer, формально выбираем Ising fusion ring (11)-(12). Invertible sector

\[
G=\{1,\psi\}\cong\mathbb Z_2
\tag{44}
\]

даёт `Z_2` Tambara-Yamagami fusion rules.

Классификация Tambara-Yamagami использует symmetric nondegenerate bicharacter `chi` и scalar `tau`, где

\[
\tau^2=\frac1{|G|}.
\tag{45}
\]

Для `G=Z_2` nondegeneracy вынуждает

\[
\chi(\psi,\psi)=-1,
\tag{46}
\]

поэтому

\[
\tau=\frac{\varepsilon}{\sqrt2},
\qquad
\varepsilon\in\{+1,-1\}.
\tag{47}
\]

### Теорема 11.1 — Две monoidal completion

После выбора Ising fusion ring и настоящего tensor/fusion-tree layer существует ровно две fusion-category equivalence classes. В стандартном skeletal gauge nontrivial channel associator имеет вид

\[
\boxed{
F^{\sigma\sigma\sigma}_{\sigma}
=
\frac{\varepsilon}{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix},
\qquad
\varepsilon=\pm1.
}
\tag{48}
\]

Это стандартная классификация Tambara-Yamagami/Ising, а не новый FCOA theorem.

Для фиксированной Ising fusion category Drinfeld, Gelaki, Nikshych и Ostrik получают четыре braided structures. Если `zeta` — braiding eigenvalue на trivial channel, то

\[
\zeta^2+\zeta^{-2}=\lambda,
\qquad
\lambda^2=2,
\tag{49}
\]

а на втором `sigma x sigma` channel eigenvalue равен `zeta^{-3}`. Для обеих fusion categories вместе braided equivalence classes параметризуются восемью roots

\[
\boxed{\zeta^8=-1.}
\tag{50}
\]

Итого существует восемь braided Ising categories.

Projective channel ratio

\[
t=\zeta^{-4}
\tag{51}
\]

даёт из (50)

\[
\boxed{t=\pm i.}
\tag{52}
\]

Именно поэтому абстрактный двухмерный braid template из v0.2 выбрал `t=±i`: он восстановил projective relative phase, но не полную categorical braiding class.

---

## 12. Теорема независимости когерентности

### Теорема 12.1 — Minimum-resource no-go

Проверенная FCOA-Z line, её terminal alphabet, split reflection и conservative LC2 linear activation не определяют единственной pentagon/hexagon-complete Ising structure.

Точнее:

1. без fusion-tree/tensor layer pentagon внутренне не формулируется;
2. без cross-type channel mixer Ising channel associator не порождается;
3. после добавления Ising fusion ring и tensor layer pentagon оставляет две inequivalent monoidal completion;
4. каждая monoidal completion допускает четыре braided structures;
5. line reflection действует на provenance и не выбирает ни один из этих categorical classes.

### Доказательство

Пункты 1 и 2 следуют из Теорем 10.1 и 9.1. Пункты 3 и 4 — из стандартных `Z_2` Tambara-Yamagami и Ising braided-category classifications, суммированных в разделе 11. Пункт 5 следует из factor separation (36)-(38). `QED`.

Следовательно,

\[
\boxed{
\text{full non-Abelian coherence не выводится из line completion + reflection + typed outputs.}
}
\tag{53}
\]

Это no-go theorem о **порождении**, а не утверждение, что FCOA не способна нести явно добавленный braided fusion-category layer.

---

## 13. Лестница ресурсов

| Уровень | Ресурс | Что появляется | Что ещё отсутствует |
|---|---|---|---|
| R0 | signed FCOA line | root, две ветви, reflection, mixed-sector freedom | fusion semantics |
| R1 | typed terminal outputs | channel alphabet и one-step support shadow | multiplicity spaces, re-entry |
| R2 | split output provenance | mirror-pair internal fiber | channel mixing |
| R3 | linear/additive activation | superposition-capable fibers | typed cross-channel maps |
| R4 | cross-type channel mixer | возможен `1/psi` reassociation | fusion-tree coherence |
| R5 | tensor/fusion-tree address | pentagon становится формулируем | выбор coherence class |
| R6 | monoidal coherence class | fusion category | braiding/twist choice |
| R7 | braided coherence class | full `F/R` braided data | physical realization остаётся отдельным вопросом |

Недостающие ресурсы выше R3 являются internal compositional data и не требуют второй spatial coordinate.

---

## 14. Hostile audit

Финальная рукопись проверена против следующих ошибочных усилений.

### 14.1 `+/-` не является particle/antiparticle

Такое физическое отождествление нигде не используется.

### 14.2 Несколько outputs не означают quantum superposition

Конечное множество labels не содержит amplitudes, inner product или coherent phase. Линейная структура должна быть добавлена явно.

### 14.3 Две primitive operations не являются одним fusion product

Правила (19)-(22) дают bundled support shadow. Operation tag заранее выбирает output.

### 14.4 Reflection не является braiding

Configuration space строгой прямой имеет тривиальную фундаментальную группу. Reflection — involution carrier, не braid generator.

### 14.5 Provenance Hadamard v0.2 не является Ising channel `F`

Это центральное corrigendum. Численно одинаковые matrices действуют на разных typed factors.

### 14.6 Braid polynomial не выводит full Ising category

Условие `t=±i` классифицирует projective relative phase в одном abstract 2D braid template, но не фиксирует fusion-category sign, common braiding phase, twist или полный pentagon/hexagon package.

### 14.7 Standard classification — prior art

Tambara-Yamagami и classification of Ising braided categories используются только для описания остаточной свободы после доказанного FCOA-specific obstruction.

---

## 15. Граница новизны

Не являются новыми:

- Ising fusion rules;
- braid-group representations of non-Abelian anyons;
- Tambara-Yamagami classification;
- две Ising fusion categories;
- восемь braided Ising equivalence classes;
- стандартные Ising `F/R` matrices.

FCOA-specific contribution состоит в совокупности четырёх результатов:

1. точное typed-output encoding one-step Ising fusion support в существующем terminal alphabet FCOA;
2. conservative mixed-sector realization без изменения legacy table;
3. strict-line braid-topology obstruction и terminal-reentry obstruction;
4. channel/provenance separation theorem и minimum-resource barrier, объясняющие, почему line reflection и split fibers не порождают full Ising coherence.

Следовательно, это structural embedding/no-go note, а не новая физическая модель энионов.

---

## 16. Заключение

На one-step уровне FCOA-Z уже содержит достаточно terminal type structure, чтобы кодировать support простого неабелева fusion rule:

\[
\boxed{
\sigma\times\sigma=1+\psi
\quad\rightsquigarrow\quad
\{E_n^+,E_n^\times\}.
}
\tag{54}
\]

Но каждое продвижение к coherent anyon-like theory выявляет отдельный недостающий ресурс. Function-valued operations блокируют intrinsic direct sums; terminal sinks блокируют fusion trees; строгая одномерная geometry блокирует braid topology; reflection действует на provenance, а не fusion channel; pentagon требует отсутствующий tensor/fusion-tree address layer.

После добавления этого categorical layer стандартная классификация показывает, что coherence всё равно содержит независимые monoidal и braided choices.

Самое сильное корректное заключение:

\[
\boxed{
\text{FCOA-Z поддерживает тени fusion-channel, но не порождает non-Abelian anyon coherence.}
}
\tag{55}
\]

Минимально необходимая дополнительная архитектура:

\[
\boxed{
\text{cross-type channel mixing}
+
\text{fusion-tree/tensor composition}
+
\text{monoidal/braided coherence data}.
}
\tag{56}
\]

С пространственной точки зрения вывод остаётся консервативным: конечная внутренняя categorical memory может быть размещена над одномерным носителем, но genuine geometric braiding не выводится из самой прямой.

---

## Литература

1. D. Tambara, S. Yamagami, **Tensor Categories with Fusion Rules of Self-Duality for Finite Abelian Groups**, *Journal of Algebra* **209** (1998), 692–707. DOI: `10.1006/jabr.1998.7558`.
2. V. Drinfeld, S. Gelaki, D. Nikshych, V. Ostrik, **On braided fusion categories I**, *Selecta Mathematica* **16** (2010), 1–119. DOI: `10.1007/s00029-010-0017-z`. Appendix B посвящён Ising categories.
3. C. Nayak, S. H. Simon, A. Stern, M. Freedman, S. Das Sarma, **Non-Abelian Anyons and Topological Quantum Computation**, *Reviews of Modern Physics* **80** (2008), 1083–1159. DOI: `10.1103/RevModPhys.80.1083`.
4. J. Preskill, **Lecture Notes for Physics 219: Quantum Computation**, Chapter 9, *Topological Quantum Computation*.
5. J. S. Birman, **Braids, Links, and Mapping Class Groups**, Annals of Mathematics Studies 82, Princeton University Press, 1974.
6. **FCOA-Z v1.1**, базовая рукопись программы и построение signed line, DOI: `10.5281/zenodo.22169264`.

---

## Revision note

Эта рукопись заменяет физическую интерпретацию `SOL_TOPO_LC2_REFLECTION_BRAID_v0_2.md`, сохраняя корректные локальные reflection/provenance matrix calculations. Формальная поправка вынесена в `CORRIGENDUM_SOL_TOPO_v0_2.md`.