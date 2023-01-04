from flask import Flask
from flask import request
from .plot_web import plot_xy
from flask import Flask
from collections import defaultdict

app = Flask(__name__)

loss = []
accuracy = []
model_parameters = defaultdict(list)

@app.route('/', methods=['get'])
def show():
    global loss
    global accuracy
    return plot_xy(loss) + \
            plot_xy(accuracy)

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

@app.route('/weight', methods=['get'])
def weight_list():
    parameters = []
    for i in model_parameters.keys():
        parameters.append(f"""
            <a href="weight/{i}">{i}</a>
        """)
    return "<br>".join(parameters)

@app.route('/weight/<name>', methods=['get'])
def weight(name):
    return "<br>".join(model_parameters[name])


@app.route('/weight', methods=['post'])
def receive_weight():
    global model_parameters
    name = request.json['name']
    plot = request.json['plot']
    model_parameters[name].append(plot)

    return 'OK'

if __name__ == "__main__":
    app.run(port=8080)
