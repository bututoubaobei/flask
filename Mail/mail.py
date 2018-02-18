from flask import Flask
from flask_mail import Mail, Message

app=Flask(__name__)
mail=Mail(app)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='qiumingming7@gmail.com'
app.config['MAIL_PASSWORD']='080125qmm'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True


@app.route('/')
def index():
    msg=Message('Hello',sender='qiumingming7@gmail.com',recipients=['mingmingqiu73@gmail.com'])
    msg.body="This is the email body"
    mail.send(msg)
    return 'Sent'

if __name__=='__main__':
    app.run(debug=True)
