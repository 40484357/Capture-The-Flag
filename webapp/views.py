from flask import Blueprint, render_template, request, redirect, url_for, flash
import hashlib, random, time
passwords = []
with open('webapp\static\cyberA-Z.txt') as f:
    words = f.readlines()
    passwords = [x.strip().lower() for x in words]

passLength = len(passwords) - 1
selection = random.randint(0, passLength)
selected = passwords[selection]
password = hashlib.md5(selected.encode()) 

# Diffie-Hellman Key Exchange start
N = 604931 
G = 30672

# List of potential a and b values
possibleValues = [101, 103, 107,    109,    113,    127,    131,    137,    139,    149,    151,    157,    163,    167,    173,
179, 181,    191,    193,    197,    199,    211,    223,    227,    229,    233,    239,    241,    251,    257,    263,    269,    271,    277,    281,
283,    293,    307,    311,    313,    317,    331,    337,    347,    349,    353,    359,    367,    373,    379,    383,    389,    397,    401,    409,
419,    421,    431,    433,    439,    443,    449,    457,    461,    463,    467,    479,    487,    491,    499,    503,    509,    521,    523,    541,
547,    557,    563,    569,    571,    577, 587,    593,    599,    601,    607,    613,    617,    619,    631,    641,    643,    647,    653,    659,
661,    673,    677,    683,    691,    701,    709,    719,    727,    733,    739,    743,    751,    757,    761,    769,    773,    787,    797,    809,
811,    821,    823,    827,    829,    839,    853,    857,    859,    863,    877,    881,    883,    887,    907,    911,    919,    929,    937,    941,
947,    953,    967,    971,    977,    983,    991,    997]
    
# Need to select two random unique values from the list
possibleValuesLength = len(possibleValues) - 1
primeSelection1 = random.randint(0, possibleValuesLength)
prime1 = possibleValues[primeSelection1]

# Remove the first value from the list and decrease the length of the list by 1
possibleValues.pop(primeSelection1)
possibleValuesLength -= 1

# Select the second value from the list
primeSelection2 = random.randint(0, possibleValuesLength)
prime2 = possibleValues[primeSelection2]
    
a = prime1 #variable
b = prime2 #variable
A = pow(G,a) % N
B = pow(G,b) % N
secretKey = pow(B,a) % N
print("A: ", A)
print("B: ", B)
print("Secret Key: ", secretKey)

views = Blueprint('views', __name__)



@views.route('/')
def landing():
    passLength = len(passwords) - 1
    selection = random.randint(0, passLength)
    selected = passwords[selection]
    password = hashlib.md5(selected.encode())
    print(password.hexdigest())
    print(passLength)
    return render_template('cyberescape.html')

@views.route('/laptop', methods=['GET', 'POST'])
def laptop():
    print(selected)
    response = None
    if request.method=='POST':
        if request.form['answer'] != selected:
            response = 'wrong password, try again'
            flash(response)
        else:
            return redirect('/desktop')
            
    return render_template('laptop.html',password = password.hexdigest(), response = response)
    
@views.route('/desktop', methods=['GET', 'POST'])
def desktop():
    ip = "85.50.46.53"
    response = None
    if request.method == 'POST':
        if request.form['answer'] != ip:
            response = 'not quite try again'
            flash(response)
            return render_template('desktop.html', response = response)
            
        else:
            response = "That's the IP, but where does it go?"
            flash(response)
            return render_template('desktop.html', response = response)

    return render_template('desktop.html')


@views.route('/phone', methods=['GET', 'POST'])
def phone():
    response = None
    if request.method=='POST':
        secretKeyGuess=request.form.get('answer', type=int)
        #secretKeyGuess = int(request.form['answer'])
        if secretKeyGuess != secretKey:
            response = 'wrong password, try again'
            flash(response)
        else:
            # Redirect to the next page
            return redirect(url_for('views.laptop'))
            
    return render_template('phone.html',password = secretKey,a=a,b=b, response = response)

@views.route('/Points_Logic')
def points():
    return render_template('Points_Logic.html')
