from datetime import datetime

# ============================================
# 1. SIMPLE FUNCTION (NO INPUT, NO OUTPUT)
# ============================================

def print_line():
    print('-' * 35)

print_line()

# ============================================
# 2. FUNCTION WITH ONE INPUT (NO OUTPUT)
# ============================================
def greeting(name):
    print(f'Hello {name}')
   
greeting('Ali')

# ============================================
# 3. FUNCTION WITH MULTIPLE INPUTS (NO OUTPUT)
# ============================================
def full_greeting(first_name, last_name):
    print(f'Hello *{first_name} {last_name}*')

full_greeting('John', 'Doe')
    
# ============================================
# 4. FUNCTION WITH ONE OUTPUT (NO INPUT)
# ============================================
def current_year():
    now = datetime.now()
    this_year = now.year
    return this_year

year = current_year()
print(f'We are in {year}')

# ============================================
# 5. FUNCTION WITH ONE INPUT AND ONE OUTPUT
# ============================================
def circle_surface(radius):
    return 3.14 * radius**2

r = 5
s = circle_surface(r)
print(f'Surface of a circle with radius {r} is {s}')

# ============================================
# 6. FUNCTION WITH MULTIPLE OUTPUTS
# ============================================
def analyze_scores(scores):
    avg = sum(scores)/len(scores)
    s_min = min(scores)
    s_max = max(scores)
    return avg, s_min, s_max

my_scores = [10, 12.5, 20, 16, 18.25]
a, b, c = analyze_scores(my_scores)
print(f'Average: {a}, Min: {b}, Max: {c}')
    
# ============================================
# 7. FUNCTION WITH DEFAULT ARGUMENTS
# ============================================
def user_info(username, country='Iran'):
    print(f'You are {username} from {country}')

user_info('Ali')
user_info('John', 'Nigeria')
user_info(country='Nigeria', username='John')



