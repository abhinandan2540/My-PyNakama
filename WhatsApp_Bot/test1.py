from flask import Flask, request
from googlesearch import search
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/", methods=["POST"])
def whatsapp_bot():
    user_msg = request.values.get("Body", '').lower()
    response = MessagingResponse()
    q = user_msg+"google.com"

    search_result = []
    for i in search(q, num_results=5):
        search_result.append(i)

    msg = response.message(f"Generating results for {user_msg}")
    for result in search_result:
        msg = response.message(result)

    return str(response)


if __name__ == "__main__":
    app.run(debug=True)
