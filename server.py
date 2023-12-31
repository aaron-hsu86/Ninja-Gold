from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ninja_money'

@app.route('/')
def welcome():
    # set 'gold' value for initial launch
    if 'gold' not in session:
        session['gold'] = 0
        session['activity_log'] = []
        session['activity'] = ''
        session['turn_count'] = 15
    
    return render_template('index.html')

@app.route('/process_money', methods=['post'])
def process_money():
    gold = random.randint(int(request.form['min-gold']), int(request.form['max-gold']))
    session['gold'] += gold
    location = request.form['location']

    if gold > 0:
        session['activity_log'] += [f'<p style="color:green">Earned {gold} gold from the {location}!</p>']
    elif gold < 0:
        session['activity_log'] += [f'<p style="color:red">Lost {gold} gold from the {location}!</p>']
    else:
        session['activity_log'] += [f'<p style="color:red">You win some, you lose some. Today, you broke even at the casino.</p>']

    session['activity'] = " ".join(list(reversed(session['activity_log'])))
    session['turn_count'] -= 1

    return redirect('/')

@app.route('/process_money/old_code')
def old_process():

    # original method, but wrote hidden method above afterwards. Kept this for educational purposes
    # if 'farm' in request.form:
    #     gold = random.randint(10,20)
    #     session['gold'] += gold
    #     session['activity_log'] += [f'<p style="color:green">Earned {gold} gold from farm!</p>']
    # elif 'cave' in request.form:
    #     gold = random.randint(5,10)
    #     session['gold'] += gold
    #     session['activity_log'] += [f'<p style="color:green">Earned {gold} gold from cave!</p>']
    # elif 'house' in request.form:
    #     gold = random.randint(2,5)
    #     session['activity_log'] += [f'<p style="color:green">Earned {gold} gold from house!</p>']
    #     session['gold'] += gold
    # elif 'casino' in request.form:
    #     gamble = random.randint(-50,50)
    #     session['gold'] += gamble
    #     if gamble > 0:
    #         session['activity_log'] += [f'<p style="color:green">Earned {gamble} gold from the casino!</p>']
    #     elif gamble < 0:
    #         session['activity_log'] += [f'<p style="color:red">Lost {gamble} gold from the casino!</p>']
    #     else:
    #         session['activity_log'] += [f'<p style="color:red">You win some, you lose some. Today, you broke even at the casino.</p>']
    
    # original hidden method. final/condensed version above
    # if request.form['which_form'] == 'farm':
    #     gold = random.randint(10,20)
    #     session['gold'] += gold
    #     session['activity_log'] += [f'<p style="color:green">Earned {gold} gold from farm!</p>']
    # elif request.form['which_form'] == 'cave':
    #     gold = random.randint(5,10)
    #     session['gold'] += gold
    #     session['activity_log'] += [f'<p style="color:green">Earned {gold} gold from cave!</p>']
    # elif request.form['which_form'] == 'house':
    #     gold = random.randint(2,5)
    #     session['activity_log'] += [f'<p style="color:green">Earned {gold} gold from house!</p>']
    # elif request.form['which_form'] == 'casino':
    #     gamble = random.randint(-50,50)
    #     session['gold'] += gamble
    #     if gamble > 0:
    #         session['activity_log'] += [f'<p style="color:green">Earned {gamble} gold from the casino!</p>']
    #     elif gamble < 0:
    #         session['activity_log'] += [f'<p style="color:red">Lost {gamble} gold from the casino!</p>']
    #     else:
    #         session['activity_log'] += [f'<p style="color:red">You win some, you lose some. Today, you broke even at the casino.</p>']

    return redirect('/')

@app.route('/restart')
def restart_session():
    session.clear()
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)

