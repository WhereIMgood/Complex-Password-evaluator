from colorama import init, Fore
import password_generator

init()

special_chars_ = "@/.;:§!?_-|{}#&[]()=''``+*µ¤$£²"
special_chars_list = list(special_chars_)

def Evaluate(password):
    default_points = 10
    points = 0

    complexity_factors = [
        (len(password) >= 8, 2),
        (any(char in special_chars_list for char in password), 3),
        (sum(1 for char in password if char.isdigit()) >= 2, 2),
        (sum(1 for char in password if char.isupper()) >= 2, 2),
    ]

    for condition, weight in complexity_factors:
        if condition:
            points += weight

    common_password_patterns = [
        "letmein", "welcome", "monkey", "1234", "password", "admin", "123456", "qwerty", "abc123", "12345",
        "iloveyou", "sunshine", "football", "password1", "qwertyui", "12345678", "welcome1", "1234567", "superman",
        "password123", "letmein1", "iloveyou1", "starwars", "123123", "test123", "trustno1", "shadow", "123321",
        "123qwe", "welcome123", "welcome1234", "123abc", "12345qwert", "1234567890", "password1234", "1234abcd",
        "abcdef", "123456789", "admin123", "letmein123", "qazwsx", "password12", "letmein12", "letmein12345",
        "admin1234", "1234password", "monkey123", "sunshine1", "football1", "password12345", "qwerty123", "welcome12345",
        "qwertyuiop", "12345abc", "starwars123", "123456abc", "password12345", "iloveyou123", "password123456",
        "12345qwerty", "test1234", "trustno1", "shadow123", "12345test", "1234qwer", "qwerty1234", "123abc123",
        "1234qaz", "iloveyou1234", "letmein123456", "admin12345", "superman123", "welcome123456", "password1234567",
        "123456789a", "password12345678", "iloveyou12345", "starwars1234", "test12345", "qwertyuiop123", "abcdef123",
        "admin123456", "password123456789", "welcome1234567", "123456789012", "sunshine123", "football123", "adminadmin",
        "password1234567890", "letmein1234567", "1234qwerasdf", "trustno1", "shadow12345", "letmeinpassword", "123456qwerty",
        "passwordiloveyou", "123abc456", "123qwe789", "welcome12345678", "qwerty12345", "12345abcdef", "starwars12345",
        "test123456", "adminadmin123", "password1234567", "qwertyuiop1234", "123456789a", "password12345678", "iloveyou123456",
        "letmein12345678", "admin1234567", "superman12345", "welcome123456789", "1234567890123", "sunshine1234", "football1234",
        "qwerty123456", "password12345678900", "letmeinpassword123", "123456qwerty123", "iloveyou1234567", "123abc4567",
        "123qwe7890", "welcome1234567890", "qwerty1234567", "12345abcdefg", "starwars123456", "test12345678", "adminadmin12345",
        "hello", "1234", "12345", "1234567", "12345678", "123456789", "hi","Hi", "helloworld", "password"
    ]
    found_patterns = []

    for pattern in common_password_patterns:
        if pattern in password.lower():
            found_patterns.append(pattern)

    if found_patterns:
        found_patterns_str = ', '.join(found_patterns)
        print(Fore.YELLOW + f"SECURITY WARNING: Common patterns found in your password: {found_patterns_str}")
        points -= 4
        print(Fore.BLUE + f"We recommend using this password: " + Fore.GREEN + str(password_generator.gen(25)))
    strength_levels = {
        "Weak": [0, 2],
        "Normal": [2, 4],
        "Medium": [4, 6],
        "Strong": [6, 10]
    }

    strength_level = "Weak"
    for level, (lower_bound, upper_bound) in strength_levels.items():
        if lower_bound <= points <= upper_bound:
            strength_level = level
            break

    color_ = Fore.GREEN
    if strength_level == "Weak":
        color = Fore.RED
    if strength_level == "Normal":
        color = Fore.YELLOW
    if strength_level == "Medium":
        color = Fore.BLUE
    if strength_level == "Strong":
        color = Fore.GREEN
    print(Fore.BLUE + f"Strength Level: {color+strength_level}.")
    percentage_strength = (points / default_points) * 100
    print(f"\nPercentage of Strength: {percentage_strength}%")

Evaluate(input("Enter a password to evaluate: "))
