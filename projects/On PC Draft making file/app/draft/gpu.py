"""GPU temperature guard for a card with weak cooling. Silent no-op when nvidia-smi is missing."""
import subprocess
import time


def temperature():
    try:
        out = subprocess.run(["nvidia-smi", "--query-gpu=temperature.gpu", "--format=csv,noheader,nounits"],
                             capture_output=True, text=True, timeout=5).stdout.strip().splitlines()
        return int(out[0]) if out else None
    except Exception:
        return None


def wait_if_hot(cfg, log=print):
    if not cfg.get("guard", True):
        return
    t = temperature()
    if t is None or t < cfg["pause_above_c"]:
        return
    log(f"GPU at {t}C, pausing until it drops below {cfg['resume_below_c']}C ...")
    while True:
        time.sleep(15)
        t = temperature()
        if t is None or t < cfg["resume_below_c"]:
            log("GPU cooled down, continuing.")
            return
