import json,math,pathlib
nominal=10.0; measured=10.01; tol=0.05; u_repeat=0.005; u_cal=0.003
uc=math.sqrt(u_repeat**2+u_cal**2); U=2.0*uc; deviation=abs(measured-nominal); guarded_pass=deviation+U<=tol
expected_uc=math.sqrt(34e-6)
passed=math.isclose(uc,expected_uc,rel_tol=1e-12) and guarded_pass
out={"benchmark":"rss_uncertainty_guardband","engine":"PY-METROLOGY-MVP","nominal_mm":nominal,"measured_mm":measured,"tolerance_mm":tol,"combined_standard_uncertainty_mm":uc,"expanded_uncertainty_k2_mm":U,"guarded_pass":guarded_pass,"passed":passed,"evidence_level":"E2","limitations":["synthetic benchmark","independent uncertainty assumption","not calibrated laboratory measurement"]}
pathlib.Path("artifacts").mkdir(exist_ok=True); pathlib.Path("artifacts/metrology_mvp.json").write_text(json.dumps(out,indent=2),encoding="utf-8"); print(json.dumps(out,indent=2)); raise SystemExit(0 if passed else 1)
