from flask import Flask
app= Flask(__name__)
app.secret_key ="sneaky"
DATABASE = "gf_schema"
import openai
openai.api_key = 'APIKEY'

