import requests
import hashlib

while True:
    password = input(" Enter your password (or 'quit' to exit):")

    if password.lower() in ['quit', 'exit', 'q', 'bye'] :
        print("Exiting password checker. Stay safe!")
        break

    strength = 0
    feedback = []

    if any(char.isdigit() for char in password):
        strength += 1
    else:
        feedback.append(" -Add at least one number")
    if any(char.isupper() for char in password):
        strength += 1
    else :
        feedback.append(" -Add at least one uppercase letter")
    if any(char.islower() for char in password):
        strength += 1
    else :
        feedback.append (" -Add at least one lowercase letter")
    if any(char in "!@#$%^&*()_+-=~`.,;:<>?/" for char in password):
        strength += 1
    else :
        feedback.append(" -Add at least one special character")
    if len(password) < 8:
        feedback.append(f" -Password should be at least 8 characters long (current length: {len(password)})")

    print("\n PASSWORD ANALYSIS: ")
    print(f" -Password Length: {len(password)} characters")
    print(f" -Types used: {strength}/4 character types")

    if len(password) < 8:
        if strength <= 2:
            rating = "VERY WEAK"
        elif strength == 3:
            rating = "WEAK"
        else:
            rating = "MEDIUM"
    else:
        if strength == 1:
            rating  = "WEAK"
        elif strength == 2:
            rating = "MEDIUM"
        elif strength == 3:
            rating = "STRONG"
        else:
            rating = "VERY STRONG"

    print(f" -Password Strength: {rating}")

    if feedback:
        print("\n SUGGESTIONS TO IMPROVE YOUR PASSWORD: ")
        for item in feedback:
            print(f" {item}")
    else:
        print("\n Your password is excellent!")


    with open("common_list/10k-most-common.txt", "r") as file:
        passwordList = file.read().splitlines()

    def check_common_password(password, passwordList):
        password_lower = password.lower()
        for rank , cmn_password in enumerate(passwordList , start = 1):
            if cmn_password == password_lower :
                return {
                    "is_common" : True,
                    "rank" : rank ,
                    "message" : f" -rank #{rank} most common password !"
                    }
        return {
                "is_common" : False,
                "rank" : None,
                "message" :" -password is not in common passwords list"
                }

    result = check_common_password(password , passwordList)
    print(" \n CHECK PASSWORD IN COMMON LIST:")
    print(result["message"])
    if result ["is_common"] and result ["rank"] <= 10:
        print("This is in the TOP 10 most common passwords!!!" )

    def check_pwned_password(password):
        try:
            hashed = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

            prefix = hashed[:5]
            suffix = hashed[5:]

            url = f"https://api.pwnedpasswords.com/range/{prefix}"
            headers = {
                'User-Agent': 'PasswordStrengthChecker/1.0 (Python Script)'
            }
            response = requests.get(url , headers=headers , timeout=5)

            if response.status_code == 200:
                for line in response.text.splitlines():
                    hash_suffix , count = line.split(':')
                    if hash_suffix == suffix:
                        return int(count)
                return 0
            else:
                print(f"API returned status code: {response.status_code}")
                return -1
        
        except requests.exceptions.Timeout:
            print("API request timed out.")
            return -1
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return -1
        except Exception as e:
            print(f"Unexpected error: {e}")
            return -1
    
    print("\n CHECK PASSWORD AGAINST PWNED DATABASE:")

    count = check_pwned_password(password)
    if count > 0:
        print(f" -BREACHED! Found {count} times! \n")
    elif count == 0:
        print("  -Not found in any breaches! \n")
    else:
        print(" -Check failed (API error) \n ")