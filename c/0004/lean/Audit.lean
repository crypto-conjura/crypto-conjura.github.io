/-
Axiom audit.  Not part of the statement; run it to confirm that the only
declaration in `Statement.lean` resting on `sorryAx` is the conjecture
itself, and that every sanity lemma rests on nothing beyond Lean's three
standard axioms.

    lake env lean Audit.lean

Expected: `sorryAx` appears on the first line and on no other.
-/
import Statement

open Conjura0004

#print axioms Conjura0004.lhl_public_seed
#print axioms Conjura0004.predAdv_nonneg
#print axioms Conjura0004.predAdv_le_one
#print axioms Conjura0004.predAdv_mem_unitInterval
#print axioms Conjura0004.extAdv_le_one
#print axioms Conjura0004.neg_one_le_extAdv
#print axioms Conjura0004.extAdv_eq_zero_of_subsingleton
