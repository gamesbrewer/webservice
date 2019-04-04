import database

#create a todo item
def createTodo(dbtype, title=None, completed=None):
	result = None
	
	if dbtype == 'mysql':
		query = "INSERT INTO tableau.todo_models (title, completed, created_at) values (%s, %s, now())"
		to_filter = []
		to_filter.append(title)
		to_filter.append(completed)
	
		db = database.mysqlDB()
	
		result = db.cur.execute(query, to_filter)
	if dbtype == 'oracle':
		query = "INSERT INTO todo_models (id, title, completed, created_at) values (seq_todo_models.nextval, :s_title, :s_completed, to_date(sysdate,'DD/MM/YYYY'))"

		db = database.oracleDB()
		result = db.cur.execute(query, s_title=title, s_completed=completed)
	return result

#read all todo ||| read todo by id or title
def readTodo(dbtype, id=None, title=None):
	result = None
	
	if dbtype == 'mysql':
		query = "SELECT id, title, completed FROM tableau.todo_models WHERE deleted_at is null"
		to_filter = []
		
		if id or title:
			query = query + " AND"

		if id:
			query += " id=%s "
			to_filter.append(id)

		if id and title:
			query = query + " AND" #

		if title:
			query += " title LIKE %s "
			to_filter.append("%" + title + "%")

		db = database.mysqlDB()
		db.cur.execute(query, to_filter)
		result = db.cur.fetchall()
	if dbtype == 'oracle':
		query = "SELECT id, TO_CHAR(title), completed FROM todo_models WHERE deleted_at is null"
		
		db = database.oracleDB()

		if id:
			query += " AND id=:s_id "
			if not title:
				db.cur.execute(query, s_id=id)

		if title:
			query += " AND title LIKE :s_title "
			title = "%%" + title + "%%"
			if id:
				db.cur.execute(query, s_id=id, s_title=title)
			else:
				db.cur.execute(query, s_title=title)
		
		if not id and not title:
			db.cur.execute(query)

		result = []
		for id, title, completed in db.cur:
			result.append({
			"id": id,
			"title": title,
			"completed": completed
			})

	return result

#update a todo item
def updateTodo(dbtype, id=None, title=None, completed=None):
	if dbtype == 'mysql':
		query = "UPDATE tableau.todo_models SET title=%s, completed=%s, updated_at=now() WHERE id = %s"
		to_filter = []
		to_filter.append(title)
		to_filter.append(completed)
		to_filter.append(id)
		
		db = database.mysqlDB()
		result = db.cur.execute(query, to_filter)
	if dbtype == 'oracle':
		db = database.oracleDB()
		
		query = "UPDATE todo_models SET title=:s_title, completed=:s_completed, updated_at = to_date(sysdate,'DD/MM/YYYY') WHERE id = :s_id"

		db = database.oracleDB()
		result = db.cur.execute(query, s_id=id, s_title=title, s_completed=completed)
		
	return result

#delete a todo item
def deleteTodo(dbtype, id=None):
	if dbtype == 'mysql':
		query = "UPDATE tableau.todo_models SET updated_at=now(), deleted_at=now() WHERE id = %s"
		to_filter = []
		to_filter.append(id)
		
		db = database.mysqlDB()
		result = db.cur.execute(query, to_filter)
	if dbtype == 'oracle':
		query = "UPDATE todo_models SET updated_at=to_date(sysdate,'DD/MM/YYYY'), deleted_at=to_date(sysdate,'DD/MM/YYYY') where id = :s_id"
		
		db = database.oracleDB()
		result = db.cur.execute(query, s_id=id)
	return result