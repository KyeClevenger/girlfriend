from flask_app import app
from flask import render_template, redirect, request, session, jsonify
from flask_app.models.user_model import User
from flask_app.models.robot_model import Robot
import openai
import json
# from elevenlabs import generate, play

def generate_and_play_audio(text, voice, model):
    audio = generate(text=text, voice=voice, model=model)
    play(audio)

if __name__ == "__main__":
    # Define the text, voice, and model
    text = "Hello! 你好! Hola! नमस्ते! Bonjour! こんにちは! مرحبا! 안녕하세요! Ciao! Cześć! Привіт! வணக்கம்!"
    voice = "Bella"
    model = "eleven_multilingual_v2"

    # Generate and play the audio
    generate_and_play_audio(text, voice, model)


@app.route('/robots/chatroom')
def bot():
    return render_template('chatroom.html')

@app.route('/ask', methods=['POST'])
def ask_chatbot():
    print(request.form)
    user_message = request.form['user_message']
    print(user_message)
    response = get_chatbot_response(user_message)
    print(response)
    return jsonify({'response': response})

def get_chatbot_response(user_message):
    prompt = f'You: {user_message}\nPartner:'
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
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