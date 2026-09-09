/-
Axiom audit for the partial proof.  Nothing here may report `sorryAx`:
Proof.lean is entirely `sorry`-free, and the project's single `sorry` is the
conjecture in Statement.lean.

    lake env lean AuditProof.lean
-/
import Proof

open AICR0004

#print axioms AICR0004.sum_rmass
#print axioms AICR0004.SD_le_one
#print axioms AICR0004.sum_pos_part_eq_SD
#print axioms AICR0004.distGame_apply_true
#print axioms AICR0004.distGame_toReal
#print axioms AICR0004.distAdv_eq
#print axioms AICR0004.distAdv_le_SD
#print axioms AICR0004.distAdv_mapTest
#print axioms AICR0004.isGreatest_distAdv
#print axioms AICR0004.distGame_viewDist
#print axioms AICR0004.extGame_eq_distGame
#print axioms AICR0004.extAdv_le_SD_views
#print axioms AICR0004.extAdv_mapDist
#print axioms AICR0004.isGreatest_extAdv
#print axioms AICR0004.predGame_toReal
#print axioms AICR0004.predAdv_le_maxMass
