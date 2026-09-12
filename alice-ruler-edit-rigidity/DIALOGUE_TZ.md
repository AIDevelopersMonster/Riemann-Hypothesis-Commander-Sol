# ТЗ ДЛЯ НОВОГО ДИАЛОГА
## Alice Throws Away the Ruler III — Edit-Distance Rigidity for Steiner Triple Systems

**Repository:** `AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol`  
**Branch:** `research/alice-ruler-edit-rigidity`  
**Parent publication:** *Alice Throws Away the Ruler II — Phase Rigidity in Steiner Triple Systems*  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.22722951  
**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196

---

# 0. Роль нового диалога

Ты — ведущий исследователь ветки `research/alice-ruler-edit-rigidity`.

Не пересказывай предыдущую статью как конечный результат. Используй её как доказанный вход и атакуй следующий уровень:

> **можно ли из малой плотности anti-mitre-дефектов вывести не только почти чистый локальный фазовый профиль, но и малое расстояние всей Steiner triple system до настоящей projective/Hall модели?**

Работай как математический исследователь, а не как редактор обзора.

Правила:

1. Не объявляй теорему без доказательства.
2. Любой внешний stability/removal/property-testing theorem сначала проверяй на точное соответствие нашим объектам и нормировкам.
3. Сначала пытайся опровергнуть сильную формулировку: trades, embeddings, switched constructions, sparse perturbations, wrong-order examples.
4. Если общий projective/Hall theorem слишком силён, изолируй сильнейший честно доказуемый подрезультат.
5. Сохраняй промежуточный научный статус в этой ветке, чтобы другой диалог мог продолжить без потери контекста.
6. Не делай промежуточные PDF. PDF нужен только после нового публикационного порога.
7. Сам сигнализируй, когда появляется результат уровня отдельной публикации.

---

# 1. Доказанный вход из Article II

Пусть `S` — `STS(v)`.

Для каждой независимой (неколлинеарной) тройки `tau` определена локальная фаза:

- `P`, если `<tau> ~= S_7` (Fano/projective closure);
- `H`, если `<tau> ~= S_9` (affine/Hall closure);
- `D`, иначе.

Число независимых троек

```math
N=\frac{v(v-1)(v-3)}6.
```

Фазовые плотности:

```math
\rho_P=|P|/N,\qquad
\rho_H=|H|/N,\qquad
\rho_D=|D|/N.
```

Граф `G_ind(S)` имеет вершинами независимые тройки и соединяет две тройки, если они имеют ровно две общие точки.

Доказано:

```math
\deg G_{ind}=3(v-4),
```

```math
\mu_2(G_{ind})\ge v-3,
```

и фазовая изопериметрия

```math
(v-3)q\left(1-\frac qN\right)
\le s+3(v-4)|D|,
```

где

```math
q=\min\{|P|,|H|\},\qquad s=e(P,H).
```

Для classical anti-mitre configuration `C_A` Král–Máčajová–Pór–Sereni с числом копий `c_A` доказано

```math
|D|\le 56c_A,
```

а также существует абсолютная константа `C_I`, такая что

```math
s\le C_Iv|D|.
```

Отсюда следует опубликованная theorem:

```math
\boxed{
\min\{\rho_P,\rho_H\}
\le C\frac{c_A}{N}
}
```

для абсолютной константы `C`.

То есть при

```math
\varepsilon:=c_A/N\to0
```

имеем

```math
\rho_D=O(\varepsilon),
```

и одна из чистых фаз имеет плотность

```math
1-O(\varepsilon).
```

**Это только phase-profile stability. Edit-distance theorem пока не доказана.**

---

# 2. Обязательная терминологическая коррекция

Не путать два разных объекта:

- `C_A` = configuration #4 в пятиблочной таблице Danziger et al.;
- mirror residual `R_7` = configuration #7.

Они не изоморфны, но их счётчики удовлетворяют

```math
c_A=2r_7.
```

Поэтому completion coordinate предыдущей статьи

```math
\alpha=\frac{r_7}{6P(v)}
      =\frac{c_A}{12P(v)}
```

имеет тот же zero set:

```math
\alpha=0\iff c_A=0.
```

Также не смешивать термин `anti-mitre configuration C_A` из Král et al. с литературой об `anti-mitre Steiner triple systems`, где словом anti-mitre называют STS без обычных mitre-конфигураций.

---

# 3. Новая метрика: сначала определить объект теоремы

Пусть

```math
b(v)=\frac{v(v-1)}6
```

— число блоков любой `STS(v)`.

Для двух STS на одном маркированном множестве `X` определить нормированное блочное расстояние, например

```math
d_{blk}(S,T)
:=\frac{|\mathcal B(S)\triangle\mathcal B(T)|}{2b(v)}.
```

Оно лежит в `[0,1]`; множитель `2` выбран потому, что обе системы имеют одинаковое число блоков.

Для изоморфно-инвариантного расстояния:

```math
d_{iso}(S,T)
:=\min_{\pi\in Sym(X)}d_{blk}(S,\pi T).
```

Для семейства моделей `\mathcal F_v`:

```math
d(S,\mathcal F_v)
:=\inf_{T\in\mathcal F_v} d_{iso}(S,T).
```

Перед любой основной теоремой проверить, что выбранная нормировка действительно удобна. Если другая метрика лучше для доказательства — можно заменить, но зафиксировать её явно.

---

# 4. Главная гипотеза ветки

Исследовать существование функции

```math
F(\varepsilon)\to0
\qquad (\varepsilon\to0)
```

такой, что малая нормированная `C_A`-плотность

```math
c_A/N\le\varepsilon
```

вынуждает структурную близость к одному из exact zero-defect классов.

Рабочая форма:

```math
\min\bigl\{
 d(S,\mathcal P_v),
 d(S,\mathcal H_v)
\bigr\}
\le F(\varepsilon),
```

где

- `\mathcal P_v` — projective Steiner triple systems соответствующего порядка;
- `\mathcal H_v` — Hall triple systems соответствующего порядка.

**Не считать эту формулу истинной заранее.**

Нужно либо:

1. доказать её с правильными спектральными/порядковыми оговорками;
2. найти контрпример;
3. определить правильную ослабленную формулировку.

---

# 5. Критическая развилка: projective branch и Hall branch нельзя смешивать

Предыдущая theorem даёт почти чистую фазу, но две ветви имеют разную алгебраическую природу.

## 5.1 Projective-dominant branch — ПЕРВЫЙ ПРИОРИТЕТ

Если

```math
\rho_P=1-O(\varepsilon),
```

то почти все независимые тройки порождают `S_7`.

Связать STS со Steiner loop:

- добавить новый элемент `0`;
- положить `x\circ0=0\circ x=x`;
- `x\circ x=0`;
- при `x\ne y` положить `x\circ y=x\oplus y`, где `x\oplus y` — третья точка STS-блока.

Для projective STS этот loop должен быть elementary abelian `2`-group, то есть операция ассоциативна и изоморфна сложению в `\mathbb F_2^m`.

### Главный локальный мост P-ветки

Нужно строго выяснить:

> насколько множество `D\cup H` контролирует число неассоциативных троек
>
> ```math
> (x\circ y)\circ z\ne x\circ(y\circ z)?
> ```

Идеальная лемма:

```math
\Pr_{x,y,z}[\text{associativity fails}]
\le K(1-\rho_P)
```

или двусторонняя оценка с абсолютными константами.

Если такой мост закрывается, искать и применять **stability of partially associative multiplication tables**: почти ассоциативная таблица должна быть близка к операции настоящей группы.

Но необходимо доказать дополнительно, что полученная группа совместима с:

- коммутативностью;
- exponent `2`;
- размером `v+1`;
- исходной STS после удаления `0`.

Только после этого можно получить близость к projective STS.

### Первый возможный сильный результат

Conditional/projective theorem вида:

> если `P` — доминирующая фаза и `v+1` имеет допустимую projective форму, то
>
> ```math
> d(S,\mathcal P_v)\le F_P(\varepsilon),
> ```
>
> где `F_P(\varepsilon)->0`.

Даже этот односторонний theorem уже может быть отдельной публикацией.

---

## 5.2 Hall-dominant branch — ВТОРОЙ ПРИОРИТЕТ

Если

```math
\rho_H=1-O(\varepsilon),
```

почти все независимые тройки порождают `S_9`.

Перевести STS в Steiner quasigroup `(X,*)`:

```math
x*x=x,
```

а для `x\ne y`, `x*y` — третья точка соответствующего блока.

Hall triple systems соответствуют distributive Steiner quasigroups; точное identity-представление необходимо перепроверить по первоисточнику.

### Главный локальный мост H-ветки

Вывести из `\rho_H=1-O(\varepsilon)` количественную оценку числа нарушений distributive law, например

```math
x*(y*z)=(x*y)*(x*z)
```

и симметричного/right distributive варианта.

Нужно получить оценку вида

```math
\Pr[\text{distributive identity fails}]
\le K_H(1-\rho_H).
```

После этого исследовать stability theorem для finite distributive Steiner quasigroups / Latin squares / quasigroup identities.

**Не предполагать, что Hall-модель единственна.** Расстояние должно быть до семейства Hall STS, а не до одного канонического объекта, пока не доказано обратное.

---

# 6. Отдельная проблема порядка

Нельзя молча предполагать, что `v` уже принадлежит exact projective или Hall spectrum.

Нужно отдельно исследовать:

1. какие порядки допустимы для exact projective STS;
2. какие порядки допустимы для Hall STS;
3. может ли существовать последовательность STS неправильных порядков с
   `c_A/N -> 0`;
4. или малая `C_A`-плотность ниже абсолютного порога уже вынуждает точную принадлежность порядка одному из допустимых спектров.

Возможны три сценария:

- **order rigidity:** достаточно малая ошибка заставляет точный правильный порядок;
- **asymptotic order rigidity:** порядок лишь близок к допустимому спектру;
- **no order rigidity:** существуют counterexamples неправильного порядка.

Эта часть должна быть доказана или явно вынесена в hypothesis основного theorem.

---

# 7. Первым делом искать контрпримеры

Перед попыткой глобального доказательства провести destructive audit.

## 7.1 Steiner trades

Взять projective/Hall модель и выполнить малый Steiner trade.

Для каждого семейства trades оценить одновременно:

```math
\Delta_{edit},
\qquad
c_A,
\qquad
1-\rho_P,
\qquad
1-\rho_H.
```

Цель — понять оптимально возможный порядок функции `F(epsilon)`.

Например, проверить, возможны ли масштабы

```math
F(\varepsilon)=O(\varepsilon),
O(\sqrt\varepsilon),
```

или линейная stability заведомо ложна.

## 7.2 Большие подсистемы / embeddings

Проверить конструкции, в которых большая projective/Hall subsystem сидит внутри общей STS.

Не предполагать, что большая subsystem может занимать `(1-o(1))v` точек: использовать реальные embedding restrictions для Steiner systems.

## 7.3 Piecewise/glued constructions

Искать системы, где разные области carrier имеют разные локальные законы, но boundary мала.

Phase-isoperimetry предыдущей статьи уже запрещает простой макроскопический `P/H` split без дефекта, но это не исключает более тонкие algebraic gluing counterexamples.

## 7.4 Wrong-order sequences

Особенно важно проверить, существуют ли STS порядков, удалённых от exact projective/Hall spectra, но с `c_A/N=o(1)`.

Если да — unconditional edit theorem в текущем виде ложна.

---

# 8. Рабочие пакеты

## WP0 — Literature and theorem audit

Найти и проверить:

- exact characterization projective STS through Steiner loops / associativity;
- Hall STS through distributive Steiner quasigroups;
- stability of partially associative finite operations;
- quasigroup/Latin-square property testing and removal theorems;
- stability of algebraic identities in finite quasigroups;
- Steiner trades and subsystem embedding restrictions;
- любые уже существующие structural stability results для STS.

Каждый найденный theorem фиксировать в таблице:

| source | exact assumptions | conclusion | usable here? | missing bridge |
|---|---|---|---|---|

## WP1 — Local identity bridge, projective side

Выразить ассоциатор Steiner loop через closure type тройки.

Цель:

```math
\#\{(x,y,z):[x,y,z]\ne0\}
\le K_P N_{bad}
```

с `N_bad` контролируемым через `|H|+|D|` или напрямую `c_A`.

## WP2 — Approximate Boolean-group reconstruction

Если loop почти ассоциативен:

1. получить nearby group operation;
2. заставить её быть abelian exponent 2;
3. сравнить multiplication-table distance с block edit-distance STS;
4. получить явную `F_P(epsilon)`.

## WP3 — Local identity bridge, Hall side

Связать failure distributivity с non-H roots.

## WP4 — Approximate distributive-quasigroup reconstruction

Либо найти готовый stability theorem, либо доказать специальную версию для Steiner quasigroups.

## WP5 — Order rigidity

Определить минимальные дополнительные assumptions, без которых theorem ложна.

## WP6 — Computational falsification

Для малых STS:

- вычислять `c_A`;
- `(rho_P,rho_H,rho_D)`;
- associativity/distributivity failure rates;
- exact/minimal edit-distance до model family там, где enumeration доступна.

Компьютерный поиск используется как falsifier и constant/exponent detector, не как замена proof.

---

# 9. Definition of success

Ветка считается научно успешной при любом из следующих результатов.

### Success A — Projective reconstruction theorem

Доказана функция `F_P(epsilon)->0` для projective-dominant branch.

### Success B — Hall reconstruction theorem

Доказана аналогичная функция для Hall-dominant branch.

### Success C — Full dichotomy stability

Доказано

```math
\min\{d(S,\mathcal P_v),d(S,\mathcal H_v)\}
\le F(c_A/N),
```

с корректными order assumptions.

### Success D — Sharp obstruction / counterexample

Построена последовательность, показывающая ложность естественной сильной формулировки, и доказана правильная replacement theorem.

### Success E — Quantitative local-to-algebraic bridge

Даже если полный edit theorem не закрывается, строгая theorem, связывающая phase defect с associativity/distributivity defect в associated loop/quasigroup, может быть самостоятельным публикационным результатом.

---

# 10. Publication discipline

Не публиковать как theorem:

- heuristic proximity;
- numerical evidence without proof;
- generic removal lemma без проверки, что она сохраняет STS/Latin constraints;
- distance to a model of wrong order;
- Hall closeness to a single canonical model без uniqueness theorem;
- claim `F(epsilon)=O(epsilon)` без lower-bound examples.

Перед публикацией обязательны:

1. explicit metric definition;
2. theorem assumptions including order;
3. full proof of local-to-algebraic bridge;
4. exact statement of any imported stability theorem;
5. counterexample/trade audit;
6. bibliography/priority audit;
7. RU/EN synchronization;
8. no claim stronger than proved edit notion.

---

# 11. Первый удар нового диалога

Начни **не** с общей theorem.

Первый вопрос:

> Для associated Steiner loop `L(S)=X cup {0}`, как точно связаны projective phase `P` независимой тройки и associativity of `circ` on ordered triples?

Сделай следующее:

1. выпиши associator identities для distinct/non-distinct `x,y,z`;
2. классифицируй их по closure `<x,y,z>`;
3. докажи или опровергни, что `P`-root эквивалентен associativity на всей локальной подтаблице, порождённой root;
4. получи количественную формулу/неравенство между `1-rho_P` и global associativity-failure density;
5. только после этого подбирай внешний stability theorem для almost-associative multiplication tables;
6. сохрани результат в ветке как `notes/PROJECTIVE_ASSOCIATOR_BRIDGE.md` и обнови `STATUS.md`.

Если этот мост закрывается с хорошей нормировкой, projective edit-rigidity становится главной линией ветки.

---

# 12. Формат ответа нового диалога

Новый диалог должен работать итеративно:

- сначала коротко зафиксировать текущее доказанное состояние;
- затем наносить один конкретный математический удар;
- явно отделять theorem / lemma / conjecture / failed attempt;
- после каждого существенного результата сохранять конспективный handoff в GitHub branch;
- не спрашивать разрешения на рутинное продолжение;
- при достижении publication threshold самостоятельно сообщить об этом.

**Стартовая команда пользователю после загрузки этого ТЗ:**

> Открой ветку `research/alice-ruler-edit-rigidity`, прочитай `alice-ruler-edit-rigidity/DIALOGUE_TZ.md` и опубликованную родительскую работу `alice-ruler-incidence/`. Начинай с `PROJECTIVE_ASSOCIATOR_BRIDGE`: выведи точную связь между локальной P-фазой и ассоциативностью associated Steiner loop, сначала пытаясь найти контрпример к наивной эквивалентности. Сохраняй каждый закрытый шаг в ветке.
