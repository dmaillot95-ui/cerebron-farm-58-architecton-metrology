import subprocess,sys,json,pathlib
r=subprocess.run([sys.executable,"worker/metrology_mvp.py"],check=False); assert r.returncode==0
x=json.loads(pathlib.Path("artifacts/metrology_mvp.json").read_text()); assert x["passed"] is True and x["guarded_pass"] is True
