import os
import hashlib
import tkinter as tk
from tkinter import filedialog, ttk, messagebox

class FileIntegrityChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("File Integrity Checker")
        self.root.geometry("750x500")
        self.root.resizable(False, False)

        self.folder_path = tk.StringVar()
        self.file_hashes = {}

        self.build_gui()

    def build_gui(self):
        frame = ttk.LabelFrame(self.root, text="Select Folder", padding=10)
        frame.pack(fill="x", padx=10, pady=10)

        ttk.Entry(frame, textvariable=self.folder_path, width=60).pack(side="left", padx=5)
        ttk.Button(frame, text="Browse", command=self.browse_folder).pack(side="left", padx=5)

        ttk.Button(self.root, text="Create Baseline Hashes", command=self.create_baseline).pack(pady=10)
        ttk.Button(self.root, text="Check Integrity", command=self.check_integrity).pack(pady=5)

        # Treeview for results
        columns = ("file", "status")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        self.tree.heading("file", text="File Path")
        self.tree.heading("status", text="Status")

        self.tree.column("file", width=500)
        self.tree.column("status", width=200)

        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

    def browse_folder(self):
        path = filedialog.askdirectory()
        if path:
            self.folder_path.set(path)

    def get_hash(self, filepath):
        sha = hashlib.sha256()
        try:
            with open(filepath, "rb") as f:
                while True:
                    chunk = f.read(4096)
                    if not chunk:
                        break
                    sha.update(chunk)
        except:
            return None
        return sha.hexdigest()

    def create_baseline(self):
        folder = self.folder_path.get()

        if not os.path.isdir(folder):
            messagebox.showerror("Error", "Invalid folder selected!")
            return

        self.file_hashes = {}

        for root, dirs, files in os.walk(folder):
            for file in files:
                full_path = os.path.join(root, file)
                file_hash = self.get_hash(full_path)
                if file_hash:
                    self.file_hashes[full_path] = file_hash

        messagebox.showinfo("Success", "Baseline hashes created successfully!")

    def check_integrity(self):
        folder = self.folder_path.get()

        if not self.file_hashes:
            messagebox.showwarning("Warning", "Create baseline first!")
            return

        self.tree.delete(*self.tree.get_children())

        current_files = {}

        for root, dirs, files in os.walk(folder):
            for file in files:
                full_path = os.path.join(root, file)
                file_hash = self.get_hash(full_path)
                current_files[full_path] = file_hash

        # Check for modifications & new files
        for file, new_hash in current_files.items():
            if file not in self.file_hashes:
                self.tree.insert("", "end", values=(file, "NEW FILE"))
            else:
                if new_hash != self.file_hashes[file]:
                    self.tree.insert("", "end", values=(file, "MODIFIED"))

        # Check deleted files
        for old_file in self.file_hashes.keys():
            if old_file not in current_files:
                self.tree.insert("", "end", values=(old_file, "DELETED"))

        messagebox.showinfo("Done", "Integrity check complete!")

# Run GUI
root = tk.Tk()
app = FileIntegrityChecker(root)
root.mainloop()
