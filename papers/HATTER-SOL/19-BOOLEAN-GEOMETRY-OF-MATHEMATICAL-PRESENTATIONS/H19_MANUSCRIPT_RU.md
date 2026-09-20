# HATTER-SOL-19

# Булева геометрия математических представлений

## Наблюдаемость, скрытие и повторное проявление структуры в компиляции и FPGA-реализации

Автор: Alex Malachevsky  
AI research collaborator: Commander Sol · Hatter Sol  
Статус: publication candidate  
Дата: 20 сентября 2026 г.

## Аннотация

Исследуется конечное семейство математически мотивированных представлений одной и той же вычислительной задачи и вопрос о том, какие различия между представлениями остаются видимыми после Booleanization, synthesis, technology mapping и физической FPGA-реализации.

Замороженное E0-семейство:

\[
D=\mathrm{DIRECT12},\qquad
P=\mathrm{PREFIX19},\qquad
N=\mathrm{NIELSEN12}.
\]

Все три реализации имеют одинаковую семантику, один и тот же 305-узловой decision DAG, одинаковую fault-модель, одинаковую registered shell и общий 2561-векторный regression contract, но различаются исходной математической факторизацией.

Для compiler stage \(i\) и наблюдателя \(O\) вводится

\[
M_a\sim_{i,O}M_b
\iff
O(C_i(M_a))=O(C_i(M_b)),
\]

и соответствующее разбиение семейства presentations.

На generic Yosys flow DIRECT12 и PREFIX19 различимы на source level, совпадают по reported cell histogram после proc/opt и techmap, а после abc-fast снова различимы. Детерминированность compiler tower даёт no-resurrection statement для полного compiler state: если complete states совпали, более поздняя детерминированная стадия не может снова их разделить.

На Cyclone V, Quartus II 13.1, 5CEFA7F23C6, joint measured physical profile даёт

\[
\mathcal P_{\rm CV}^{\rm joint}
=
\{\{D,P\},\{N\}\}.
\]

Независимая репликация на Gowin GW5A-25A, Gowin Education IDE 1.9.9Beta-4, даёт тот же post-P&R quotient:

\[
\mathcal P_{\rm GW}^{\rm joint}
=
\{\{D,P\},\{N\}\}.
\]

Основной результат - двухвендорный конечный experiment о повторении partition shape, а не универсальный закон FPGA-cost.

## 1. Формальная модель

Пусть

\[
M=(X,Y,Q,G,\lambda,\delta,\omega)
\]

- конечное адаптивное представление. Оно индуцирует функцию

\[
\Phi_M:X\to Y.
\]

В H19 сравниваются только presentations с одним и тем же внешним E0-контрактом.

Canonical temporal realization вычисляет observer текущего decision node и обновляет состояние. Full spatial realization вычисляет поддерживаемые observers параллельно и реализует decision DAG сетью combinational selectors. Поэтому

\[
D_{\rm query}\ne D_{\rm Boolean}\ne L_{\rm transaction}.
\]

В presentation-preserving discipline \(\Pi_{\rm DAG}\) каждый observer инстанцируется один раз, одинаковые DAG nodes разделяются как в source, а каждый нетерминальный node даёт selector. До downstream rewriting:

\[
S_{\rm gen}(M)
=
\sum_{q_i\in Q_{\rm used}}S(q_i)
+
\sum_{v\in V_{\rm nt}}s_{\rm sel}(r_v,b)
+
S_{\rm shell}.
\]

Это construction accounting, не lower bound на минимальную Boolean circuit complexity.

## 2. Контролируемое семейство

DIRECT12 использует 24 permutation-composition nodes при maximum composition depth 3.

PREFIX19 использует 19 shared composition nodes при том же depth 3:

\[
24\to19.
\]

NIELSEN12 использует mixed source profile

\[
18\ \text{shear}
+
3\ \text{inverse}
+
6\ \text{direct commutator compositions}.
\]

Все три RTL variants используют один 305-node decision DAG и проходят общий 2561-transaction regression.

## 3. Observer-induced partitions

На стадии \(i\) complete compiler state обозначается \(C_i(M)\). Наблюдатель

\[
O:C_i\to Z_O
\]

индуцирует equivalence

\[
M_a\sim_{i,O}M_b
\]

и partition

\[
\mathcal P_{i,O}=\mathcal F/{\sim_{i,O}}.
\]

Если \(O_a=f\circ O_b\), то \(O_b\) не менее различающий:

\[
O_a\preceq O_b
\Longrightarrow
\mathcal P_{i,O_a}\preceq\mathcal P_{i,O_b}.
\]

Эта order theory используется как язык и не заявляется как самостоятельная новизна.

## 4. No-resurrection для complete state

Пусть

\[
C_{i+1}(M)=F_i(C_i(M))
\]

и flow детерминирован. Если

\[
C_i(M_1)=C_i(M_2),
\]

то

\[
C_{i+1}(M_1)=C_{i+1}(M_2).
\]

Следовательно exact-state visibility не может иметь переход \(0\to1\).

Поэтому позднее повторное различение coarse observer означает, что различие раньше было скрыто, а не уничтожено.

## 5. Generic compiler trajectory

Source composition count:

\[
24\ne19.
\]

После Yosys proc/flatten/opt:

\[
D=4919,\qquad P=4919
\]

reported cells с одинаковым cell histogram.

После generic techmap:

\[
D=63719,\qquad P=63719.
\]

Но wire totals различаются:

\[
7732\ne7582,
\qquad
17674\ne17531.
\]

После abc-fast:

\[
D=60374,\qquad
P=60383,\qquad
N=68406.
\]

Таким образом для D/P coarse survival word:

\[
\boxed{1001}.
\]

Family-level partitions:

\[
\mathcal P_{\rm proc}
=
\{\{D,P\},\{N\}\},
\]

\[
\mathcal P_{\rm techmap}
=
\{\{D,P\},\{N\}\},
\]

\[
\mathcal P_{\rm ABC}
=
\{\{D\},\{P\},\{N\}\}.
\]

## 6. Latent partition gap

Пусть \(\mathcal P_i^{\rm full}\) - partition по complete state, а \(\mathcal P_i^O\) - по observer. Тогда

\[
\mathcal P_i^{\rm full}\preceq\mathcal P_i^O.
\]

Для

\[
Q(\mathcal P)=\sum_{B\in\mathcal P}\binom{|B|}{2}
\]

определим

\[
L_i(O)=Q(\mathcal P_i^O)-Q(\mathcal P_i^{\rm full}).
\]

Для cell-histogram observer:

\[
\boxed{
L_{\rm cellhist}:1\to1\to0.
}
\]

## 7. Cyclone-V laboratory

Target: 5CEFA7F23C6. Tool: Quartus II 13.1. Reference clock: 100 MHz.

| Presentation | ALM | Reg | DSP | Fmax MHz | Data delay ns | Levels | Cell ns | Routing ns |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DIRECT12 | 10627 | 69 | 48 | 28.52 | 34.827 | 30 | 13.556 | 21.270 |
| PREFIX19 | 10627 | 69 | 48 | 28.52 | 34.827 | 30 | 13.556 | 21.270 |
| NIELSEN12 | 12017 | 69 | 48 | 27.50 | 36.212 | 31 | 14.026 | 22.182 |

Следовательно

\[
\boxed{
\mathcal P_{\rm CV}^{\rm joint}
=
\{\{D,P\},\{N\}\}.
}
\]

D/P совпадают по всем восьми заранее объявленным physical coordinates. Это equality measured profile, не routed-state identity.

## 8. Gowin laboratory

Target: GW5A-LV25MG121NC1/I0. Tool: Gowin Education IDE 1.9.9Beta-4. Clock contract: 100 MHz, period 10 ns.

### Synthesis

| Presentation | Logic | LUT | ALU | Reg | DSP |
| --- | ---: | ---: | ---: | ---: | ---: |
| DIRECT12 | 19376 | 18882 | 494 | 69 | 28 |
| PREFIX19 | 19376 | 18882 | 494 | 69 | 28 |
| NIELSEN12 | 21221 | 20729 | 492 | 69 | 28 |

### Post-P&R

| Presentation | P&R | Logic | LUT | ALU | Reg | CLS | DSP | Fmax MHz | Levels | WNS ns | Setup TNS ns |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DIRECT12 | PASS | 19628 | 18882 | 746 | 69 | 10150 | 28 | 16.276 | 49 | -51.440 | -644.501 |
| PREFIX19 | PASS | 19628 | 18882 | 746 | 69 | 10150 | 28 | 16.276 | 49 | -51.440 | -644.501 |
| NIELSEN12 | PASS | 21448 | 20729 | 719 | 69 | 10941 | 28 | 16.599 | 49 | -50.243 | -628.206 |

Все variants завершили placement, routing, timing analysis и bitstream generation, но 100 MHz timing target не закрыт.

Следовательно

\[
\boxed{
\mathcal P_{\rm GW}^{\rm joint}
=
\{\{D,P\},\{N\}\}.
}
\]

## 9. Cross-vendor result

Основной физический результат:

\[
\boxed{
\mathcal P_{\rm CV}^{\rm joint}
=
\mathcal P_{\rm GW}^{\rm joint}
=
\{\{D,P\},\{N\}\}.
}
\]

Полная измеренная trajectory:

\[
\{\{D,P\},\{N\}\}_{\rm proc}
\to
\{\{D,P\},\{N\}\}_{\rm techmap}
\to
\{\{D\},\{P\},\{N\}\}_{\rm ABC}
\to
\begin{cases}
\{\{D,P\},\{N\}\}_{\rm CycloneV},\\
\{\{D,P\},\{N\}\}_{\rm Gowin}.
\end{cases}
\]

Это observer-relative re-coarsening.

## 10. Multidimensional physical cost

NIELSEN12 физически крупнее на обоих targets, но timing direction различается: на Cyclone V Fmax ниже D/P, а на Gowin немного выше.

Следовательно из этих данных не следует universal scalar ordering presentations.

## 11. Reproducibility

Cyclone-V и Gowin laboratories содержат SHA-256 provenance manifests по 33 ключевых run artifacts каждая.

Hashes фиксируют byte-level provenance конкретных локальных runs, но не доказывают deterministic rerouting across machines, seeds или future tool versions.

## 12. Prior-art boundary

Классическими являются branching programs, BDDs и decision-tree/circuit comparisons [Wegener 2000; Wegener 1986; Bryant 1986], translation validation и verified compilation [Pnueli et al. 1998; Necula 2000; Leroy 2009], equality saturation [Tate et al. 2009].

Поэтому H19 не заявляет novelty для partition lattices, observational equivalence, semantic preservation, branching-program/circuit comparisons, equality saturation и unrestricted lower bounds.

H19-specific contribution:

\[
\boxed{
\text{controlled E0 presentations}
+
\text{compiler observer atlas}
+
\text{nonmonotone visibility}
+
\text{two-vendor replicated physical quotient}.
}
\]

## 13. Ограничения и non-claims

Результат ограничен одной semantic task family, тремя presentations, двумя FPGA vendors, конкретными tool versions/options и declared observers.

Не утверждаются:

1. equality full compiler state D/P;
2. equality routed netlists;
3. equality bitstreams;
4. universal cross-technology invariance;
5. globally optimal presentation;
6. technology-independent scalar cost;
7. unrestricted circuit lower bound.

## 14. Заключение

Для frozen E0 family получено

\[
\boxed{
\mathcal P_{\rm CycloneV}^{\rm joint}
=
\mathcal P_{\rm Gowin}^{\rm joint}
=
\{\{DIRECT12,PREFIX19\},\{NIELSEN12\}\}.
}
\]

Вместе с deterministic no-resurrection statement это поддерживает conceptual distinction

\[
\boxed{
\text{наблюдаемое забывание}
\ne
\text{уничтожение структуры}.
}
\]

Hardware image математического presentation целесообразно описывать trajectory observer-induced partitions, а не одним scalar resource value.

## References

1. Ingo Wegener. Branching Programs and Binary Decision Diagrams: Theory and Applications. SIAM, 2000. DOI 10.1137/1.9780898719789.
2. Ingo Wegener. Time-space trade-offs for branching programs. Journal of Computer and System Sciences 32(1), 1986, 91-96. DOI 10.1016/0022-0000(86)90004-8.
3. Randal E. Bryant. Graph-Based Algorithms for Boolean Function Manipulation. IEEE Transactions on Computers C-35(8), 1986, 677-691. DOI 10.1109/TC.1986.1676819.
4. Amir Pnueli, Michael Siegel, Eli Singerman. Translation Validation. TACAS 1998, 151-166. DOI 10.1007/BFb0054170.
5. George C. Necula. Translation Validation for an Optimizing Compiler. PLDI 2000, 83-94. DOI 10.1145/349299.349314.
6. Xavier Leroy. Formal Verification of a Realistic Compiler. Communications of the ACM 52(7), 2009, 107-115. DOI 10.1145/1538788.1538814.
7. Ross Tate, Michael Stepp, Zachary Tatlock, Sorin Lerner. Equality Saturation: A New Approach to Optimization. POPL 2009, 264-276. DOI 10.1145/1480881.1480915.
8. Clifford Wolf, Johann Glaser. Yosys - A Free Verilog Synthesis Suite. Austrochip 2013, 47-52.
9. Robert K. Brayton, Alan Mishchenko. ABC: An Academic Industrial-Strength Verification Tool. CAV 2010, 24-40. DOI 10.1007/978-3-642-14295-6_5.
