# HATTER-SOL-11 · ORDER_44_R16_TWO_CENTER_SEPARATED

**Status:** closed theorem layer for all two-center cases with `xy notin F`.

Let `F` be a sixteen-edge face-triangulation complement of a 5-regular 3-connected simple plane support. Let `x,y` be the two overloaded vertices and assume `xy` is not an added edge.

By T11.101 the possible center degrees and residual sizes are

`(7,7;2), (8,7;1), (9,7;0), (8,8;0)`.

The proof uses a common reserve-first rule.

## 1. Reserve-first overlap rule

First retriangulate one or two faces at `x` so that `x` falls to degree at most five. If a selected face contains `y`, protect `y`. If a later selected face at `y` meets a first-stage face in a noncentral vertex `w`, choose the triangulations jointly as follows:

- if a first-stage face avoids `y`, ordinary T11.72 is safe; if extra overlap protection is needed, use T11.77 protecting `w`;
- if a first-stage face contains `y` and must also protect `w`, use T11.98: ear off at `x`, give `y` at most one new incidence and `w` at most two;
- use the symmetric rule on the later face at `y` if it contains `x`.

A face avoiding the opposite center has local bound at most two under ordinary ear-off, and a boundary vertex may retain at most one old edge from the opposite center. A face containing the opposite center deletes all old added edges from that center to its other boundary vertices, by facial uniqueness.

Thus, with at most two residual edges, every noncentral vertex on only one repaired face has final degree at most six. At a vertex shared by a first-stage and second-stage repair, either both faces avoid the opposite centers and the bound is `2+2+2=6`, or one face also carries center protection and T11.98 lowers its overlap contribution to at most two, again giving at most six. If both repaired faces are the two common support faces of support-adjacent centers, they meet only in the support edge `xy` and have no noncentral overlap.

This rule will be invoked below without repeating the local bookkeeping.

## 2. Pattern `(7,7)` with two residual edges

Because seven old incidences are distributed over five faces at `x`, choose a face of `x`-load at least two and repair it. Protect `y` if the face contains `y`. Then `x<=5`.

The degree of `y` after this first stage is at most eight. If it is at most six, stop. If it is seven, repair any remaining loaded face at `y`. If it is eight, the first repair can have increased it only by one while deleting no old `y`-incidence; consequently its seven old incidences lie on the other four faces, so one of them has load at least two. Repair such a face.

Use the reserve-first overlap rule. The second stage lowers `y` to at most six and can return at most one incidence to `x`, so `x<=6`. Thus `(7,7;2)` is closed.

## 3. Pattern `(8,7)` with one residual edge

Create reserve at `x` by removing at least three old incidences.

If one face has load at least three, repair it. Otherwise all loads are at most two; since they sum to eight, at least three faces have load two, and two of those are nonconsecutive. Repair such a nonconsecutive pair. At most one selected face can contain `y`, because two common support faces of support-adjacent centers are consecutive and nonadjacent support vertices share at most one face.

Hence `x<=5` after the first stage.

Now `y` has degree at most eight. Repair it exactly as in Section 2: one loaded face if its degree is seven, or a load-at-least-two face if its degree is eight. Apply the overlap rule to all intersections with first-stage faces. The single residual edge cannot raise any local bound above six. Thus `(8,7;1)` is closed.

## 4. Pattern `(9,7)` with no residual edge

Again create reserve at `x` by removing at least three incidences.

If one face has load at least three, use it. Otherwise the loads are exactly `{2,2,2,2,1}`; repair two nonconsecutive load-two faces. This leaves `x<=5`.

The second center is then repaired as in Sections 2--3. There is no residual edge, so every noncentral overlap estimate is strictly below or equal to six. Thus `(9,7;0)` is closed.

## 5. Pattern `(8,8)` with no residual edge

First create reserve at `x`. If one face has load at least three, repair it. Otherwise at least three faces have load two; choose two nonconsecutive load-two faces. Thus at least three old `x`-incidences are removed and `x<=5`.

The first stage can leave `y` with degree at most nine. If `y<=6`, stop. If `y=7` or `8`, remove respectively at least one or two old incidences. If `y=9`, the increase by one means a first-stage common face contributed a protected new incidence while containing no old `y`-diagonal; hence all eight old `y`-incidences lie on at most four remaining faces. One face has load at least two, and if three incidences are required then either one face has load at least three or two nonconsecutive load-two faces exist. Repair accordingly.

When two second-stage faces are used, choose them nonconsecutive, so at most one can contain `x`. Therefore at most one new protected incidence can return to `x`, and `x` remains at most six. The reserve-first overlap rule controls every noncentral intersection.

Thus `(8,8;0)` is closed.

## Theorem T11.108 — all separated-center two-center cases at r=16

Every sixteen-edge augmentation with two overloaded centers not joined by an added edge can be retriangulated to maximum added degree at most six.

### Proof

T11.101 gives exactly the four patterns treated in Sections 2--5. QED.