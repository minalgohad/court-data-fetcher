# # from flask import Flask, render_template, request
# # from scraper import fetch_case_data
# # import sqlite3
# # from flask import jsonify

# # app = Flask(__name__)

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/submit', methods=['POST'])
# # def submit():
# #     case_type = request.form['case_type']
# #     case_number = request.form['case_number']
# #     year = request.form['year']

# #     data = fetch_case_data(case_type, case_number, year)

# #     conn = sqlite3.connect('database.db')
# #     c = conn.cursor()
# #     c.execute('CREATE TABLE IF NOT EXISTS queries (case_type TEXT, case_number TEXT, year TEXT, result TEXT)')
# #     c.execute("INSERT INTO queries (case_type, case_number, year, result) VALUES (?, ?, ?, ?)",
# #               (case_type, case_number, year, str(data)))
# #     conn.commit()
# #     conn.close()

# #     # return render_template('result.html', data=data)
# #     return jsonify(data)

# # if __name__ == '__main__':
# #     app.run(debug=True)
# from flask import Flask, render_template, request, jsonify
# from scraper import fetch_case_data
# import sqlite3

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     try:
#         # Read JSON from JavaScript fetch body
#         data_json = request.get_json()
#         case_type = data_json['case_type']
#         case_number = data_json['case_number']
#         year = data_json['year']

#         # Fetch data from scraper
#         data = fetch_case_data(case_type, case_number, year)

#         # Save to database
#         conn = sqlite3.connect('database.db')
#         c = conn.cursor()
#         c.execute('CREATE TABLE IF NOT EXISTS queries (case_type TEXT, case_number TEXT, year TEXT, result TEXT)')
#         c.execute("INSERT INTO queries (case_type, case_number, year, result) VALUES (?, ?, ?, ?)",
#                   (case_type, case_number, year, str(data)))
#         conn.commit()
#         conn.close()

#         return jsonify(data)  # Return JSON to JavaScript
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from scraper import fetch_case_data  # Make sure this file/function exists
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data_json = request.get_json()
        case_type = data_json['case_type']
        case_number = data_json['case_number']
        year = data_json['year']

        data = fetch_case_data(case_type, case_number, year)

        # Save to database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS queries (case_type TEXT, case_number TEXT, year TEXT, result TEXT)')
        c.execute("INSERT INTO queries (case_type, case_number, year, result) VALUES (?, ?, ?, ?)",
                  (case_type, case_number, year, str(data)))
        conn.commit()
        conn.close()

        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
