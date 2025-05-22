import os
import ast

def scan_repo(repo_path):
    summary = {
        "modules":[],
        "functions":[],
        "classes":[],
        "docstrings":[],
        "requirements":[],
        "readme_exists":False,
        "license_exists":False,
    }

    for root, dirs, files in os.walk(repo_path):
        for filename in files:
            file_path = os.path.join(root,filename)

            if filename.endswith(".py"):
                summary["modules"].append(file_path)
                with open(file_path, "r", encoding="utf-8") as f:
                    try:
                        node = ast.parse(f.read(), filename = filename)
                        for n in ast.iter_child_nodes(node):
                            if isinstance(n, ast.ClassDef):
                                summary["classes"].append(n.name)
                                doc = ast.get_docstring(n)
                                if doc:
                                    summary["docstrings"].append({"type":"class","name":n.name, "doc":doc})
                            elif isinstance(n,ast.FunctionDef):
                                summary["functions"].append(n.name)
                                doc = ast.get_docstring(n)
                                if doc:
                                    summary["docstrings"].append({"type":"functionn","name":n.name, "doc":doc})
                        
                        module_doc = ast.get_docstring(node)
                        if module_doc:
                            summary["docstrings"].append("type":"module","name":filename, "doc":module_doc)

                    
                    except Exception as e:
                        print(f"Error parsing {file_path}: {e}")

            elif filename == "requirements.txt":
                with open(file_path,"r", encoding="utf-8") as f:
                    summary['requirements'] = [line.strip() for line in f if line.strip() and not line.startswith("#")]
            
            elif filename.lower() in ["main.py","app.py","run.py"]:
                summary["scripts"].append(file_path)
            
            elif filename.lower() == "readme.md":
                summary["readme_exists"] = True
            
            elif filename.lower().startswith("license"):
                summary["license_exists"] = True
            
    return summary