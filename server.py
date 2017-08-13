from flask import Flask, render_template, redirect, request, session
import jinja2
import csv

app = Flask(__name__)


@app.route('/')
def route_index():
    with open("data.csv", mode='r') as data:
        reader = csv.reader(data, delimiter=',')
        table = list(reader)
        print(table)

    return render_template('list.html', data=table)


@app.route('/story')
def route_edit():
    note_text = None
    return render_template('form.html')


@app.route('/story/<int:post_id>')
def show_post(post_id):
    return render_template('form.html')


@app.route('/save-note', methods=['POST'])
def route_save():
    print('POST request received!')
    # session['note'] = request.form['note']
    # session['note2'] = request.form['note2']
    # print(session['note'])
    # print(session['note2'])
    headers = []
    for header in request.form:
        headers.append(header)
    print(headers)
    values = [request.form.getlist(h)[0] for h in headers]
    print(values)
    with open("data.csv", "r") as csv_file:
        fileObject = csv.reader(csv_file)
        row_count = sum(1 for row in fileObject)
        print(row_count)
    values.insert(0, row_count+1)
    print(values)

    with open("data.csv", "a", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(values)

    return redirect('/')


if __name__ == "__main__":
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
    )
