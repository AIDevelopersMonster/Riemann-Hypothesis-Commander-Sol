# HATTER-SOL-18 · H18-03
# Почему возникли два компонента 32+32: Higman invariant и канонический подъём в SL(2,7)

**Статус:** CLOSED exact finite layer + literature identification.

## 1. Что было загадкой после H18-02

Nielsen graph на 114 H17 states, порождённый стандартными moves

\[
(A,B)\mapsto(B,A),\qquad
(A,B)\mapsto(A^{-1},B),\qquad
(A,B)\mapsto(AB,B),
\]

распался на четыре connected components:

\[
36,\ 32,\ 32,\ 14.
\]

Коммутатор

\[
K=[A,B]
\]

объяснял три сектора лишь частично:

- \(36\): class \(3A\);
- \(32\): class \(4A\);
- \(32\): class \(4A\);
- \(14\): classes \(7A/7B\).

Поэтому два компонента \(32+32\) выглядели как скрытое дополнительное расщепление внутри одного и того же projective class \(4A\).

Оно действительно скрыто **не в PSL(2,7), а на один этаж выше**.

---

## 2. Канонический commutator lift

Каждый элемент

\[
A\in PSL(2,7)
\]

имеет два determinant-one lift-а

\[
\widetilde A,\ -\widetilde A\in SL(2,7).
\]

То же для \(B\).

Но commutator не зависит от выбора знаков:

\[
[-\widetilde A,\widetilde B]
=
[\widetilde A,-\widetilde B]
=
[\widetilde A,\widetilde B].
\]

Поэтому projective pair \((A,B)\) определяет **канонический** элемент

\[
\widetilde K
=
[\widetilde A,\widetilde B]
\in SL(2,7).
\]

Следовательно, определено число

\[
\boxed{
\tau(A,B)=\operatorname{tr}(\widetilde K)\in\mathbb F_7.
}
\]

Это и есть trace form of the Higman invariant.

---

## 3. Exact H17 decomposition

Новый сертификат непосредственно на 114 canonical H17 states даёт:

\[
\boxed{
\tau=6:\ 36,
\qquad
\tau=4:\ 32,
\qquad
\tau=3:\ 32,
\qquad
\tau=5:\ 14.
}
\]

И каждый из этих четырёх trace fibers является **ровно одним connected Nielsen component**.

То есть:

\[
\boxed{
\text{Nielsen component}
\iff
\tau\text{-fiber}
}
\]

в нашей конечной \(q=7\) лаборатории.

---

## 4. Откуда именно берётся 32+32

Самая важная строка:

\[
\boxed{
\tau=3\ \longrightarrow\ 32\text{ states},
\qquad
\tau=4=-3\pmod7\ \longrightarrow\ 32\text{ states}.
}
\]

При этом оба trace values проектируются в один и тот же PSL class:

\[
\boxed{
\tau=3,\ 4
\quad\mapsto\quad
K\in4A.
}
\]

Почему?

Для \(C\in SL(2,7)\) с trace \(\pm3\) lift имеет order \(8\). После факторизации по центральному

\[
\{\pm I\}
\]

его образ в \(PSL(2,7)\) имеет order \(4\).

Но \(C\) и \(-C\) представляют **один projective element**, а их traces противоположны:

\[
\operatorname{tr}(-C)=-\operatorname{tr}(C).
\]

Поэтому projective class \(4A\) забывает знак подъёма:

\[
3\sim -3=4\pmod7.
\]

А commutator of lifts этот знак не забывает.

Именно поэтому две Nielsen worlds выглядят одинаково на уровне обычного class \(4A\), но различаются на уровне \(SL(2,7)\):

\[
\boxed{
4A^{(+)}:\tau=3,
\qquad
4A^{(-)}:\tau=4.
}
\]

Это не два новых conjugacy classes в PSL. Это два **lift sectors** одного projective commutator class.

---

## 5. Полная таблица четырёх миров

| Canonical lift trace \(\tau\) | H17 states | PSL commutator observation |
|---:|---:|---|
| \(6=-1\) | 36 | \(3A\) |
| \(3\) | 32 | \(4A\) |
| \(4=-3\) | 32 | \(4A\) |
| \(5=-2\) | 14 | \(7A/7B\) |

Для order-7 sector inversion exchanges \(7A\leftrightarrow7B\), поэтому extended Higman invariant naturally keeps them in one 14-state Nielsen world.

---

## 6. Чьё это свойство

Здесь важно отделить известную математику от нашей H18 реализации.

### Классическая часть

Для generating pairs of a two-generator group, extended conjugacy class of the commutator is invariant under Nielsen transformations. Это классический **Higman invariant**, названный по D. G. Higman.

Для \(SL(2,q)\) и \(PSL(2,q)\) trace of the commutator даёт особенно удобную форму этого invariant.

Darryl McCullough и Marcus Wanderley систематически исследовали Nielsen equivalence generating pairs of \(SL(2,q)\) and \(PSL(2,q)\). Их работа показывает, в частности, что для \(q=7\) возможные trace invariants generating pairs равны

\[
\boxed{\{3,4,5,6\}},
\]

и их computational classification was verified for \(q\le101\).

Позднейшие работы формулируют для \(PSL(2,q)\) именно canonical commutator lift

\[
PSL(2,q)^2\to SL(2,q)
\]

и trace invariant \(\tau\).

### Что является H18-результатом

Мы **не заявляем открытие Higman/trace invariant**.

Наш результат:

1. обнаружить расщепление \(36+32+32+14\) независимо внутри H17 114-state model;
2. точно идентифицировать два загадочных 32-state components как fibers

\[
\tau=3,\qquad\tau=4;
\]

3. встроить этот классический invariant в H17/H18 language of orbit tomography, adaptive queries and hardware states;
4. дать standalone exact certificate, который вычисляет lift invariant непосредственно из canonical H17 model.

---

## 7. Почему числа 32 и 32 всё равно интересны

Инвариант объясняет **почему они не соединяются Nielsen moves**.

Равенство cardinalities

\[
32=32
\]

сертификат подтверждает точно, но само по себе мы не объявляем новым общим theorem.

На уровне generating ordered pairs каждый H17 state содержит 168 inner-conjugate pairs, поэтому два sectors содержат:

\[
32\cdot168=5376
\]

generating pairs каждый.

Вместе projective \(4A\)-sector содержит

\[
10752
\]

generating pairs и делится canonical lift sign ровно пополам:

\[
5376+5376.
\]

Это сильная конечная симметрия \(q=7\), но для общей семьи \(PSL(2,q)\) размеры trace fibers являются отдельным counting question.

---

## 8. Ещё один контроль: outer automorphism

Для \(q=7\) field automorphism trivial, а nontrivial outer automorphism приходит из

\[
PGL(2,7)/PSL(2,7)\cong C_2.
\]

В H18 certificate он действует на 114 inner-conjugacy states как

\[
57
\]

двухциклов без fixed vertices и сохраняет \(\tau\).

После quotient по этому outer symmetry размеры становятся:

\[
\boxed{
18,\ 16,\ 16,\ 7.
}
\]

То есть:

\[
36\to18,\qquad
32\to16,\qquad
32\to16,\qquad
14\to7.
\]

Именно такие four T-system sizes for \(PSL(2,7)\) встречаются в ранее опубликованной combinatorial literature.

Это независимый sanity check того, что H18 graph попал в классическую Nielsen/T-system structure, а не создал искусственное разбиение из-за наших orbit IDs.

---

## 9. Что это меняет для «вращения слов»

Теперь видно фундаментальное ограничение.

Если мы меняем words только посредством Nielsen/Aut\((F_2)\) dynamics, то \(\tau\) не изменяется:

\[
\boxed{
\tau(\alpha\cdot(A,B))=\tau(A,B).
}
\]

Следовательно, Nielsen dynamics никогда не перебросит state между четырьмя trace worlds.

Особенно:

\[
\tau=3
\not\leftrightarrow
\tau=4
\]

никаким набором обычных Nielsen moves.

Это значит, что динамика слов живёт **внутри** этих компонентов.

---

## 10. Новая идея для adaptive tomography

Наш текущий H17 class observer видит projective conjugacy classes.

Для commutator он видит:

\[
3A,\ 4A,\ 7A,\ 7B,
\]

но в \(4A\)-sector теряет lift sign.

Можно добавить один observer другого типа:

\[
\boxed{
q_{\rm lift}(A,B)
=
\operatorname{tr}([\widetilde A,\widetilde B]).
}
\]

Он мгновенно различает:

\[
4A^{(+)}
\quad\text{и}\quad
4A^{(-)}.
\]

Следующий H18 вопрос становится очень конкретным:

> насколько уменьшится adaptive decision complexity, если разрешить не только projective class queries, но и один canonical lift-trace query?

Это уже новое сочетание классического invariant и нашей adaptive tomography.

---

## 11. Источники

1. D. McCullough, M. Wanderley, **Nielsen Equivalence of Generating Pairs of SL(2,q)**, Glasgow Mathematical Journal 55 (2013), 481-509. DOI: 10.1017/S0017089512000675.
2. J. Boschheidgen, B. Klopsch, A. Thillaisundaram, **Generating pairs of projective special linear groups that fail to lift**, Mathematische Nachrichten 293 (2020), 1251-1258. DOI: 10.1002/mana.201900354.
3. Anton Prowse, **Generalized Operations on Hypermaps**, PhD thesis, University of Southampton, 2006; reports four \(PSL(2,7)\) T-systems of sizes \(16,16,18,7\).

---

## 12. Certificate

Run:

\`\`\`text
python certificates/h18_higman_trace_lift_certificate.py
\`\`\`

Expected terminal statement:

\`\`\`text
KEY: the two 32-state 4A components are tau=3 and tau=4=-3
PASS: the 32+32 split is exactly the canonical SL(2,7) commutator-trace split
\`\`\`
