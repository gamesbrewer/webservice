#import flask framework
from flask import Flask
from flask import request
from flask import jsonify

#import api
from api import todo

#set up config
app = Flask(__name__)
api_oracle_todo = '/api/v1/oracle/todo/'
api_mysql_todo = '/api/v1/mysql/todo/'

#setup routes
#---------------------------------------------------------------------------------------
#create todo
@app.route(api_oracle_todo, methods=['POST'])
def postOracleTodo():
	if not request.json or not 'title' in request.json:
		return jsonify("error encountered")
	param_title = request.json['title']
	param_completed = request.json['completed']
	return jsonify(todo.createTodo('oracle', param_title, param_completed))

@app.route(api_mysql_todo, methods=['POST'])
def postMysqlTodo():
	if not request.json or not 'title' in request.json:
		return jsonify("error encountered")
	param_title = request.json['title']
	param_completed = request.json['completed']
	return jsonify(todo.createTodo('mysql', param_title, param_completed))

#read todo
@app.route(api_oracle_todo, methods=['GET'])
def getOracleTodo(param_id = None, param_title = None):
	if 'id' in request.json:
		param_id = request.json['id']
	if 'title' in request.json:
		param_title = request.json['title']
	return jsonify(todo.readTodo('oracle', param_id, param_title))

@app.route(api_mysql_todo, methods=['GET'])
def getMysqlTodo(param_id = None, param_title = None):
	if 'id' in request.json:
		param_id = request.json['id']
	if 'title' in request.json:
		param_title = request.json['title']
	return jsonify(todo.readTodo('mysql', param_id, param_title))

#update todo
@app.route(api_oracle_todo, methods=['PUT'])
def putOracleTodo():
	if not request.json or not 'id' in request.json:
		return jsonify("error encountered")
	param_id = request.json['id']
	param_title = request.json['title']
	param_completed = request.json['completed']
	return jsonify(todo.updateTodo('oracle', param_id, param_title, param_completed))

@app.route(api_mysql_todo, methods=['PUT'])
def putMysqlTodo():
	if not request.json or not 'id' in request.json:
		return jsonify("error encountered")
	param_id = request.json['id']
	param_title = request.json['title']
	param_completed = request.json['completed']
	return jsonify(todo.updateTodo('mysql', param_id, param_title, param_completed))

#delete todo
@app.route(api_oracle_todo, methods=['DELETE'])
def deleteOracleTodo():
	if not request.json or not 'id' in request.json:
		return jsonify("error encountered")
	param_id = request.json['id']
	return jsonify(todo.deleteTodo('oracle', param_id))
	
@app.route(api_mysql_todo, methods=['DELETE'])
def deleteMysqlTodo():
	if not request.json or not 'id' in request.json:
		return jsonify("error encountered")
	param_id = request.json['id']
	return jsonify(todo.deleteTodo('mysql', param_id))

#---------------------------------------------------------------------------------------
#start the app
app.run(host='0.0.0.0', port=5000,debug=True)