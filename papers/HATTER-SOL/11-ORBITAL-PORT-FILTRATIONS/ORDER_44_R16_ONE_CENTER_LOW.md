# HATTER-SOL-11 · ORDER_44_R16_ONE_CENTER_LOW

**Status:** closed theorem layer for one-center degrees `8<=d<=12`.

Let `F` be a sixteen-edge face-triangulation complement of a 5-regular 3-connected simple plane support. Assume exactly one vertex `x` is overloaded. Put `d=d_F(x)` and `q=16-d`; let `Q` be the `q` off-center edges. For `q<=8`, T11.95 gives at most one off-center vertex of degree at least five.

## T11.104a — degree 8, q=8

Some face at `x` has old load at least two. If such a face avoids the unique hot vertex, apply T11.72 at `x`.

Otherwise every load-at-least-two face contains the hot vertex `y`. At most two support faces contain both `x,y`, while the other three have load at most one. Hence the common faces carry at least five old `x`-incidences, so one common face `C` has load at least three.

Ear off `C` at `y`. Then `y` receives no new diagonal and `d(x)<=8-3+2=7`. If the load of `C` is at least four, stop. If it is exactly three, the remaining five old `x`-incidences lie on four faces, so one further face `D` has load at least two. Ear off `D` at `x`; if `D` is consecutive to `C`, use T11.97 to protect their unique noncentral overlap vertex. Then `x<=5`. At the overlap vertex the two repair contributions are at most `2+1`, while at most three off-center edges avoid `y`, so the degree is at most six. Thus `(8,8)` is closed.

## T11.104b — degree 9, q=7

If some face has load at least three, repair it at `x`; protect the unique hot vertex if necessary. A degree-five hot vertex is safe. If its outside degree is six, the six relevant off-center edges form a star and a single secondary repair at the hot center removes one remaining old star edge. If this secondary face also contains `x`, protect `x`; if that would leave `x` above six, then the two common faces contain too little old `x`-load, forcing at least five old incidences onto the three noncommon faces, one of which has load at least two. One final noncommon repair at `x` finishes.

If no face has load three, the loads are `{2,2,2,2,1}`. Choose two nonconsecutive load-two faces. They have no noncentral overlap and the hot vertex can lie on at most one. Repair both, protecting the hot vertex if needed. The center falls to degree five, leaving enough reserve for any secondary hot-center repair. Thus `(9,7)` is closed.

## T11.104c — degree 10, q=6

We need to remove four incidences. If one face has load at least four, use it. Otherwise some nonconsecutive pair has combined load at least four because the five nonconsecutive pair-loads sum to `20`.

Repair the selected face or pair. A hot vertex lies on at most one face of a selected nonconsecutive pair. If its degree is five, protect it and finish. If its degree is six, the off-center graph is a six-edge star; a single secondary repair at the hot center removes a remaining star edge. If that face meets `x`, protect `x`; if no reserve remains, the same load-count argument as in T11.104b supplies one final noncommon face of load at least two. Thus `(10,6)` is closed.

## T11.104d — degree 11, q=5

We need to remove five incidences. Either one face has load at least five, or a nonconsecutive pair has combined load at least five because the average nonconsecutive pair-load is `22/5`.

The only hot off-center graph is a five-edge star. Its center can lie on at most one face of a selected nonconsecutive pair. Protect it there and use ordinary ear-off on the other selected face. The hot vertex remains at degree at most six and all other off-center vertices have degree at most one. Thus `(11,5)` is closed.

## T11.104e — degree 12, q=4

We need to remove six incidences. If one face has load at least six, repair it. If one nonconsecutive pair has combined load at least six, repair that pair.

Assume neither occurs. Then every nonconsecutive pair has sum at most five. A cyclic five-tuple of nonnegative integer loads summing to twelve under this restriction is, up to rotation, `(3,3,2,2,2)` with the two threes consecutive. Indeed an entry at least four would force both nonconsecutive partners low enough that the cyclic inequalities sum to total at most eleven; with all entries at most three, sum twelve forces exactly two threes, and they must be consecutive.

Repair the two consecutive load-three faces. They share one support edge `xw`. On both faces use T11.97, ear-off at `x` and protect `w`. Hence `w` gets at most one new diagonal from each face, while every other noncentral vertex lies on at most one repaired face and gets at most two. Since `Delta(Q)<=4`, all final degrees are at most six. The center loses exactly six and falls to degree six.

Therefore every one-center case `8<=d<=12` is repairable to maximum added degree six.