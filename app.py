from flask import Flask
from task_controller import task_controller
from data import df

app = Flask(__name__)

@app.route('/reset', methods=['GET'])
def reset():
    try:
        df.iloc[0:0]
        df.to_csv('data.csv', index=True)
        return {
            'code': 200,
            'status': 'success',
            'message': 'Data reset complete.'
        }
    except:
        return {
            'code': 500,
            'status': 'error',
            'message': 'Error: Unable to reset data.'
        }

app.register_blueprint(task_controller)

if __name__ == '__main__':
    app.run(debug=True)
