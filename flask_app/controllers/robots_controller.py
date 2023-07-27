from flask_app import app
from flask import render_template, redirect, request, session, jsonify
from flask_app.models.user_model import User
from flask_app.models.robot_model import Robot
import openai
import json
openai.api_key = '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'


@app.route('/robots/chatroom')
def bot():
    return render_template('chatroom.html')

@app.route('/ask', methods=['POST'])
def ask_chatbot():
    user_message = request.form['user_message']
    response = get_chatbot_response(user_message)
    return jsonify({'response': response})

def get_chatbot_response(user_message):
    prompt = f'You: {user_message}\nChatGPT:'
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        stop=['\n']
    )
    print("print from python", response)
    return response.choices[0].text.strip()


@app.route('/robots')
def robot():
    if 'user_id' not in session:
        return redirect('/')
    data ={
        'id': session['user_id']
    }
    logged_user = User.get_by_id(data)
    robot = Robot.get_all()
    return render_template('robot.html', logged_user=logged_user, robot=robot)


@app.route('/robots/partner')
def robot_partner():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('robot_partner.html')


@app.route('/robots/avatar')
def robot_avatar():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('robot_avatar.html')

@app.route('/robots/chatroom', methods=["POST"])
def chatroom():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('chatroom.html')

# @app.route('/robots/avatar', methods=['POST'])
# def robot_avatar():
#     if 'user_id' not in session:
#         return redirect('/')
#     if not Robot.is_valid(request.form):
#         return redirect('/robots/avatar')
#     robot_data = {
#         **request.form,
#         'user_id': session['user_id']
#     }
#     Robot.create(robot_data)
#     return redirect('/robots')

# @app.route('/robot/<int:id>/view')
# def view_one_robot(id):
#     if 'user_id' not in session:
#         return redirect('/')
#     data = {
#         'id': id
#     }
#     one_robot = Robot.get_one(data)
#     return render_template("robot.html", one_robot=one_robot)

# @app.route('/robot/<int:id>/delete')
# def delete_robot(id):
#     data = {
#         'id': id
#     }
#     this_robot = Robot.get_one(data)
#     if this_robot.user_id != session['user_id']:
#         flash('not yours, you cant edit')
#         flash("No no buddy, you can't delete this!")
#         return redirect('/robots')
        
#     Robot.delete(data)
#     return redirect('/robots')

# @app.route('/robot/<int:id>/edit')
# def edit_robot_form(id):
#     if 'user_id' not in session:
#         return redirect('/')
#     data ={
#         'id': id
#     }
#     one_robot = Robot.get_one(data)
#     if one_robot.user_id !=session['user_id']:
#         flash('not yours, you cant edit')
#         return redirect('/robots')
#     return render_template('robot.html', one_robot=one_robot)

# @app.route('/robots/<int:id>/update', methods=['POST'])
# def update_robot(id):
#     if 'user_id' not in session:
#         return redirect('/')
#     if not Robot.is_valid(request.form):
#         return redirect(f'/robots/{id}/edit')
#     data = {
#         **request.form,
#         'id': id
#     }

#     one_robot = Robot.get_one(data)
#     if one_robot.user_id != session['user_id']:
#         flash('not yours, you cant edit')
#         return redirect('/robots')
        
#     Robot.update(data)
#     return redirect('/robots')


# @app.route("/robots/chatroom", methods=["POST"])
# def search():
#     question = request.form.get("question")
#     answer = get_wikipedia_answer(answer)
#     print(answer)
#     return render_template("chatroom.html", question=question, answer=answer)

# @app.route('/robots/chatroom', methods=['POST'])
# def chat():
#     return render_template('chatroom.html')

# @app.route('/robots/chatroom')
# def index():
#     return render_template('chatroom.html')

# @app.route('/ask', methods=['POST'])
# def ask():
#     question = request.form['question']
    
#     try:
#         # Make the request to GPT-3 API
#         response = openai.Completion.create(
#             engine="text-davinci-002",  # Update engine if needed, check OpenAI docs
#             prompt=question,
#             max_tokens=150,
#             stop=["\n"]  # To limit the response to a single paragraph
#         )
        
#         answer = response['choices'][0]['text'].strip()
#         return answer
        
#     except Exception as e:
#         return f"Error: {e}"