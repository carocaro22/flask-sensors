from flask import Flask, render_template, request
import plotter
import model
from model import add_temperature, get_all_data, get_all_times
from JsonParser import parse_json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        content = request.get_json()
        temp = parse_json(content)
        add_temperature(temp)
        x_labels = get_all_times()
        y = get_all_data()
        plot_url = plotter.plot(x_labels, y)
        temperatures = model.session.query(model.Temperature).order_by(model.Temperature.id).all()
        return render_template('graph.html', plot_url=plot_url, temperatures=temperatures)
    x = get_all_times()
    y = get_all_data()
    plot_url = plotter.plot(x, y)
    temperatures = model.session.query(model.Temperature).order_by(model.Temperature.id).all()
    return render_template('graph.html', plot_url=plot_url, temperatures=temperatures)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3333, debug=True)
