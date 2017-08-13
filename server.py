from flask import Flask, render_template, redirect, request, session
import jinja2
import csv

app = Flask(__name__)


@app.route('/')
def route_index():
    with open("data.csv", mode='r') as data:
        reader = csv.reader(data, delimiter=',')
        table = list(reader)
        # print(table)

    return render_template('list.html', data=table)


@app.route('/story')
def route_edit():
    note_text = None
    return render_template('form.html', data=None, button="Create")


@app.route('/story/<int:post_id>')
def show_post(post_id):
    csv_data = []
    with open("data.csv", "r") as csv_file:
        table = csv.reader(csv_file)
        for row in table:
            csv_data.append(row)
    # print(csv_data)
    print(post_id)

    return render_template('form.html', data=row, button="Update", post_id=post_id)


@app.route('/save-note', methods=['POST'])
def route_save():
    print('POST request received!')
    headers = []
    for header in request.form:
        headers.append(header)
    values = [request.form.getlist(h)[0] for h in headers]
    result = []
    with open("data.csv", "r") as csv_file:
        table = csv.reader(csv_file, delimiter=',')
        row_count = sum(1 for row in table)
    with open("data.csv", "r") as csv_file:
        table = csv.reader(csv_file, delimiter=',')
        for row in table:
            result.append(row)
        # print(len(values))
    print("values: ", values)
    if len(values) == 7:
        print("lofasz")
        print(result)
        for i, row in enumerate(result):
            print("result i : ", result[i])
            # print(row)
            print(row[0], values[0])
            if row[0] == values[0]:
                result[i] = values
        print(result)
        with open("data.csv", "w") as filee:
            for record in result:
                row = ','.join(record)
                filee.write(row + "\n")
    else:
        print("lofasz2")
        values.insert(0, row_count + 1)
        with open("data.csv", "a", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(values)
    result=[]
    return redirect('/')


if __name__ == "__main__":
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
    )
