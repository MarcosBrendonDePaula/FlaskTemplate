import re
from datetime import datetime
class Validation:
    
    def __init__(self, rules, error_msg):
        self.rules = rules
        self.error_msg = error_msg

    def validate(self, data={}):
        errors = {}
        failed_rules = {}
        for field, rules in self.rules.items():
            for rule in rules:
                if rule.startswith("min:"):
                    min_length = int(rule.split(":")[1])
                    if len(data[field]) < min_length:
                        errors[field] = {"message": self.error_msg.get(f"{field}.min", "The field does not meet the minimum length requirement.")}
                        failed_rules.setdefault(field, []).append(rule)
                        break
                elif rule.startswith("max:"):
                    max_length = int(rule.split(":")[1])
                    if len(data[field]) > max_length:
                        errors[field] = {"message": self.error_msg.get(f"{field}.max", "The field exceeds the maximum length.")}
                        failed_rules.setdefault(field, []).append(rule)
                        break
                elif rule == "required":
                    if not data.get(field):
                        errors[field] = {"message": self.error_msg.get(f"{field}.required", "The field is required.")}
                        failed_rules.setdefault(field, []).append(rule)
                        break
                elif rule.startswith("type:"):
                    field_type = rule.split(":")[1]
                    if field_type == "int":
                        if not isinstance(data[field], int):
                            try:
                                int(data[field])
                            except ValueError:
                                errors[field] = {"message": self.error_msg.get(f"{field}.type", "The field must be an integer.")}
                                failed_rules.setdefault(field, []).append(rule)
                                break
                    elif field_type == "float":
                        if not isinstance(data[field], float):
                            try:
                                float(data[field])
                            except ValueError:
                                errors[field] = {"message": self.error_msg.get(f"{field}.type", "The field must be a floating point number.")}
                                failed_rules.setdefault(field, []).append(rule)
                                break
                    elif field_type == "string":
                        if isinstance(data[field], (int, float)):
                            errors[field] = {"message": self.error_msg.get(f"{field}.type", "The field must be a string.")}
                            failed_rules.setdefault(field, []).append(rule)
                            break
                    elif field_type == "date":
                        date_format = "%Y-%m-%d"
                        try:
                            datetime.strptime(data[field], date_format)
                        except ValueError:
                            errors[field] = {"message": self.error_msg.get(f"{field}.date", f"The field must be a valid date in the {date_format} format.")}
                            failed_rules.setdefault(field, []).append(rule)
                            break
                elif rule == "email":
                    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
                    if not re.match(pattern, data[field]):
                        errors[field] = {"message": self.error_msg.get(f"{field}.email", "The field must be a valid email address.")}
                        failed_rules.setdefault(field, []).append(rule)
                        break
        return {"is_valid": len(errors) == 0, "errors": errors, "failed_rules": failed_rules, "old":data}