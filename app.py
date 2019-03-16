from flask import Flask, request, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'memcached'
app.debug = True

if __name__ == '__main__':
    app.run()


@app.before_request
def session_management():
    session.permanent = True


def calculate_scores():
    listUser = session['user']
    listScore = session['score']
    printScore = session['score']

    session['leaders'] = zip(sorted(printScore, reverse=True),
                             [x for _, x in sorted(zip(listScore, listUser), reverse=True)])


questions = [
        ["My twin lives at the reverse of my house number. The difference between our house numbers ends in two. What are the lowest possible numbers of our house?","19"],
        ["If a hen and a half lay an egg and a half in a day and a half, how many eggs will half a dozen hens lay in half a dozen days?","24"],
        ["A small number of cards has been lost from a complete pack. If I deal among four people, three cards remain. If I deal among three people, two remain and if I deal among five people, two cards remain. How many cards are there?","47"],
        ["What is the smallest whole number that is equal to seven times the sum of its digits?","21"],
        ["Old Granny Adams left half her money to her granddaughter and half that amount to her grandson. She left a sixth to her brother, and the remainder, $1,000, to the dogs home. How much did she leave altogether?","21000"],
        ["What is the smallest number that increases by 12 when it is flipped and turned upside down?","86"]
    ]


@app.route('/')
def index():

    is_user_set = session.get('user', False)

    if(is_user_set):
        return render_template('index.html',question = questions)
    else:
        return render_template('user.html')


@app.route('/check-answer',methods=["POST"])
def check_answer():
    right_answer = questions[session['score'][session['current_user']]][1]
    if right_answer == request.form['answer']:
        session['score'][session['current_user']] += 1
        session['last_answer'] = False
        calculate_scores()
    else:
        session['last_answer'] = request.form['answer']

    return redirect('/')

@app.route('/start-new-game')
def start_new_game():
    return render_template('user.html')


@app.route('/reset')
def reset_game():
    session.clear()
    return redirect('/')



@app.route('/save_user',methods=["POST"])
def save_user():
    is_user_set = session.get('user', False)

    if (is_user_set):
        users = len(session['user'])
        session['user'].append(request.form['username'].capitalize())
        session['score'].append(0)
        session['current_user'] = users
        calculate_scores()

    else:
        session['score'] = [0]
        session['current_user'] = 0
        session['user'] = [request.form['username']]

    return redirect('/')