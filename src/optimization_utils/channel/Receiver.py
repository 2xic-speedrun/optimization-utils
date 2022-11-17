from flask import Flask
from flask import request
from plot_web import plot
from flask import Flask

app = Flask(__name__)

loss = []
accuracy = []

@app.route('/', methods=['get'])
def show():
    global loss
    global accuracy
    return plot(loss) + \
            plot(accuracy)

@app.route('/', methods=['post'])
def receive():
    print(request.json)
    loss_value = request.json['loss']
    accuracy_value = request.json['accuracy']
    if loss_value is not None:
        loss.append(loss_value)
    if accuracy_value is not None:
        accuracy.append(accuracy_value)
    return 'OK'

if __name__ == "__main__":
    app.run(port=8080)
