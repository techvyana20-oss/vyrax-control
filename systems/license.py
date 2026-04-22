import json, os, hashlib

CONFIG = "config.json"
VALID_KEYS = ["TECHVYANA2.0-A9F2-3KX1-ZQ8M"]

def _hash(k):
    return hashlib.sha256(k.encode()).hexdigest()

def _load():
    if not os.path.exists(CONFIG):
        return {}
    try:
        with open(CONFIG) as f:
            return json.load(f)
    except:
        return {}

def _save(d):
    with open(CONFIG, "w") as f:
        json.dump(d, f, indent=4)

def license_check():
    cfg = _load()
    if "license" in cfg:
        return True

    key = input("Enter License Key: ").strip()
    if key in VALID_KEYS:
        cfg["license"] = _hash(key)
        _save(cfg)
        print("✔ Activated")
        return True
    else:
        print("❌ Invalid Key")
        return False
