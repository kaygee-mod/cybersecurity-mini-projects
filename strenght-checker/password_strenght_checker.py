import re 

def check_strenght(password):
    if len(password) <8:
        return "weak: Too short"
    if not re.search ( r"[A-Z]", password):
     return "weak: Missing uppercase letter"
    if not re.search (r"[a-z]", password):
       return "weak: Missing lowercase letter"
    if not re.search (r"[0-9]", password):
     return "weak: Mising number"
    if not re.search(r"[!@#$%^&*()<>?\":{}|<>]", password):
       return "weak: Missing Special character"
    return "Strong password"

if __name__ == "__main__":
   print("===Password Strenght Checker ===")
   pwd = input("Enter a password to check :")
   print(check_strenght(pwd))
       

    