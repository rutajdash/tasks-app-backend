from flask import request, Blueprint
from data import df

task_controller = Blueprint('task_controller', __name__, url_prefix='/task')

@task_controller.route('/<int:task_id>', methods=['GET'])
def get(task_id):
    try:
        if (task_id >= len(df) or task_id < 0 or df.empty == True or df.iloc[task_id].isnull().values.any() == True):
            return {
                'code': 404,
                'status': 'error',
                'message': 'Task not found.'
            }
        
        return {
            'code': 200,
            'status': 'success',
            'data': df.loc[task_id].to_dict()
        }
    except:
        return {
            'code': 500,
            'status': 'error',
            'message': 'Error: Unable to get task.'
        }

@task_controller.route('/all', methods=['GET'])
def list():
    try:
        return {
            'code': 200,
            'status': 'success',
            'data': df.to_dict('index')
        }
    except:
        return {
            'code': 500,
            'status': 'error',
            'message': 'Error: Unable to list tasks.'
        }

@task_controller.route('', methods=['POST'])
def add():
    try:
        data = request.get_json()

        if (data['task'] == ''):
            return {
                'code': 400,
                'status': 'error',
                'message': 'Task cannot be empty.'
            }
        
        if (data['status'] != 'incomplete' and data['status'] != 'complete'):
            return {
                'code': 400,
                'status': 'error',
                'message': 'Status is not valid.'
            }

        df.loc[len(df.index)] = [data['task'], data['status']]
        df.to_csv('data.csv', index=True)

        return {
            'code': 200,
            'status': 'success',
            'message': 'Task added successfully.'
        }
    except:
        return {
            'code': 500,
            'status': 'error',
            'message': 'Error: Unable to add task.'
        }

@task_controller.route('/<int:task_id>/description', methods=['PUT'])
def update_status(task_id):
    try:
        data = request.get_json()

        if (task_id >= len(df) or task_id < 0 or df.empty == True or df.iloc[task_id].isnull().values.any() == True):
            return {
                'code': 404,
                'status': 'error',
                'message': 'Task not found.'
            }

        if (data['task'] == ''):
            return {
                'code': 400,
                'status': 'error',
                'message': 'Task cannot be empty.'
            }

        df.loc[df.index == task_id, 'task'] = data['task']
        df.to_csv('data.csv', index=True)

        return {
            'code': 200,
            'status': 'success',
            'message': 'Task updated successfully.'
        }
    except:
        return {
            'code': 500,
            'status': 'error',
            'message': 'Error: Unable to update task.'
        }

@task_controller.route('/<int:task_id>/status', methods=['PUT'])
def update_task(task_id):
    try:
        data = request.get_json()

        if (task_id >= len(df) or task_id < 0 or df.empty == True or df.iloc[task_id].isnull().values.any() == True):
            return {
                'code': 404,
                'status': 'error',
                'message': 'Task not found.'
            }

        if (data['status'] != 'incomplete' and data['status'] != 'complete'):
            return {
                'code': 404,
                'status': 'error',
                'message': 'Status is not valid.'
            }

        df.loc[df.index == task_id, 'status'] = data['status']
        df.to_csv('data.csv', index=True)

        return {
            'code': 200,
            'status': 'success',
            'message': 'Task updated successfully.'
        }
    except:
        return {
            'code': 500,
            'status': 'error',
            'message': 'Error: Unable to update task.'
        }

@task_controller.route('/<int:task_id>', methods=['DELETE'])
def delete(task_id):
    try:
        if (task_id >= len(df) or task_id < 0 or df.empty == True or df.iloc[task_id].isnull().values.any() == True):
            return {
                'code': 404,
                'status': 'error',
                'message': 'Task not found.'
            }

        df.drop(task_id, inplace=True)
        df.to_csv('data.csv', index=True)

        return {
            'code': 200,
            'status': 'success',
            'message': 'Task deleted successfully.'
        }
    except:
        return {
            'code': 500,
            'status': 'error',
            'message': 'Error: Unable to delete task.'
        }
