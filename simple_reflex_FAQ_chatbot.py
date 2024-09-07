from flask import Flask

app = Flask(__name__)

@app.route('/')

#Function that responds to requests

def simpleReflexChatbot(user_input):
    user_input = user_input.lower()
    for keword in information:
       if keword == user_input:
           return information[keword]
    return "Sorry Not Found"

# A dictionary to store the data about specific keywords
information = {
    "name" : "FAST NUCES",
    "location" : "Industrial Estate, Hayatabad Peshawar",
    "admissions date": "July to mid August every year",
    "staff" : "Qualified Staff",
    "programs" : " 1. BSCS \n 2. BSSE \n 3. BSAI",
    "contact" : "0911223344",
    "grading" : "sucks"
}


#function call
user_input = input("Ask a Question: ")
response = simpleReflexChatbot(user_input)
print(response)


#App running using flask via internal server on port address 5000
app.run(host="0.0.0.0" , port=5000)
