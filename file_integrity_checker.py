import os
import hashlib
import time

FOLDER_TO_MONITOR = r"C:\Users\sayan\Downloads"

def compute_hash(path):
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            h.update(f.read())
        return h.hexdigest()
    except:
        return None

file_info = {}

for f in os.listdir(FOLDER_TO_MONITOR):
    path = os.path.join(FOLDER_TO_MONITOR, f)
    if os.path.isfile(path):
        file_info[path] = {
            "hash": compute_hash(path),
            "mtime": os.path.getmtime(path)
        }


print("Monitoring folder:", FOLDER_TO_MONITOR)
print("Press CTRL+C to stop.\n")

while True:
    current_files = {}

    for f in os.listdir(FOLDER_TO_MONITOR):
        path = os.path.join(FOLDER_TO_MONITOR, f)

        if os.path.isfile(path):
            current_hash = compute_hash(path)
            current_mtime = os.path.getmtime(path)
            current_files[path] = True

            if path not in file_info:
                print(f"[NEW FILE]     {path}")
                file_info[path] = {"hash": current_hash, "mtime": current_mtime}

            else:
                old_hash = file_info[path]["hash"]
                old_mtime = file_info[path]["mtime"]

                if current_hash != old_hash or current_mtime != old_mtime:
                    print(f"[MODIFIED]      {path}")
                    file_info[path] = {"hash": current_hash, "mtime": current_mtime}

    for old_path in list(file_info.keys()):
        if old_path not in current_files:
            print(f"[DELETED FILE] {old_path}")
            del file_info[old_path]

    time.sleep(3)
