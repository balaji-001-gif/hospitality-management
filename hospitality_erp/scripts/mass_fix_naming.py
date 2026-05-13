import os
import json
from datetime import datetime

def fix_naming_series(app_path):
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    for root, dirs, files in os.walk(app_path):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r") as f:
                        data = json.load(f)
                    
                    if data.get("doctype") == "DocType":
                        changed = False
                        
                        # 1. Fix naming_series field
                        if data.get("autoname") == "naming_series:":
                            naming_series_field = None
                            for field in data.get("fields", []):
                                if field.get("fieldname") == "naming_series":
                                    naming_series_field = field
                                    break
                            
                            if naming_series_field:
                                if naming_series_field.get("fieldtype") != "Series":
                                    naming_series_field["fieldtype"] = "Series"
                                    changed = True
                                
                                if naming_series_field.get("reqd") != 1:
                                    naming_series_field["reqd"] = 1
                                    changed = True
                                
                                options = naming_series_field.get("options", "")
                                if options:
                                    first_option = options.split("\n")[0].strip()
                                    if not naming_series_field.get("default"):
                                        naming_series_field["default"] = first_option
                                        changed = True
                        
                        # 2. Fix naming_rule
                        if data.get("naming_rule") and "Naming Series" in data.get("naming_rule"):
                            if data["naming_rule"] != 'By "Naming Series" field':
                                data["naming_rule"] = 'By "Naming Series" field'
                                changed = True

                        if changed:
                            # 3. Bump dates to force sync
                            data["modified"] = now_str
                            # data["creation"] = now_str # Keep original creation if possible, but modified is enough
                            
                            print(f"Fixed {data.get('name')} in {file_path}")
                            with open(file_path, "w") as f:
                                json.dump(data, f, indent=1, sort_keys=False)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    fix_naming_series(os.getcwd())
