from flask import Blueprint, render_template, request, redirect, url_for, flash, Markup
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
possibleValues = [503, 521, 541, 557, 563, 613, 631, 641, 653, 661]
    
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



@views.route('/cyberescape')
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
            return redirect(url_for('views.phoneHome'))
            
    return render_template('phone.html',password = secretKey,a=a,b=b, response = response)

@views.route('/phoneHome',methods =['GET','POST'])
def phoneHome():
    response = None
    # Doing this because of two forms on one view, checks which one was used
    if request.method =='POST':
        if "validater" in request.form:
            if request.form['validatePhoto'] != "U2FsdGVkX18099HHwV0FYWBJXXfd4JDKkrhsHwGeD64=":
                response = 'Incorrect Ciphertext'
                flash(response)
            else:
                # assign chall 2 points, steganography
                response = 'Correct Ciphertext.' 
                flash(response)
        elif "aes" in request.form:
            if request.form['password'] != "check_user.php":
                response = 'Incorrect password'
                flash(response)
            else:
                # assign chall 3 points, aes
                response = Markup("Correct password.<br>Access Splunk <a href ='http://52.1.222.178:8000' target='_blank'>here</a><br>Username: ctf<br>Password: EscapeEscap3")
                flash(response)

    return render_template('phoneHome.html')     

@views.route('/Points_Logic', methods=['GET', 'POST'])
def points():
    response=None
    if request.method=='POST':
        timeLeft=request.form.get('timeLeft',type=int)
        hintsUsed=request.form.get('hintsUsed',type=int)
        timeTaken=request.form.get('timeTaken',type=int)
        basePoints=25000
        timeLPenalty = (24 - timeLeft)*500
        hintPenalty = basePoints - ((basePoints-timeLPenalty) * (1-(hintsUsed * 0.08)))
        timeTPenalty = timeTaken *0.03

        points = basePoints - (timeLPenalty + hintPenalty + timeTPenalty)

        response = points

        flash(response)
        
    return render_template('Points_Logic.html', response= response)

@views.route('/intro')
def intro():
    return render_template('intro.html')

@views.route('/winroom', methods=['GET', 'POST'])
def winroom():
    response = None
    if request.method=='POST':
        code1=request.form.get('code1',type=int)
        code2=request.form.get('code2',type=int)
        code3=request.form.get('code3',type=int)
        if(code1==63 and code2==34 and code3==11):
            response = Markup("Correct code<br>Congratulations!")
            flash(response)
            return render_template('winroom.html',flash_message="True")
        else:
            response = 'Incorrect code'
            flash(response)
        
    return render_template('winroom.html',flash_message="False")

@views.route('/')
def home():
    return render_template('index.html')
