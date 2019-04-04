package main

import (
    "fmt"
    "database/sql"
    _ "gopkg.in/goracle.v2"
)
 
func main(){
 
    db, err := sql.Open("goracle", "tableausuperadmin/thisismyboomsticksaidthegreatestmanever@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=10.1.12.106)(PORT=1521))(CONNECT_DATA =(SERVER=DEDICATED)(SID=HEXP)))")
    if err != nil {
        fmt.Println(err)
        return
    }
    defer db.Close()
     
    //rows,err := db.Query("select sysdate from dual")
	rows,err := db.Query("select title, completed from todo_models")
    if err != nil {
        fmt.Println("Error running query")
        fmt.Println(err)
        return
    }
	
    defer rows.Close()
 
	var columns []string
    columns, err = rows.Columns()
    if err != nil {
        fmt.Println("rows.Columns() failed.\n\t%s\n", err.Error())
    }
    for i, c := range columns {
        fmt.Println("ahahaha %3d %s\n", i, c)
		fmt.Println("end haha\n")
    }
 
    var thedate string
	var completeds string
    for rows.Next() {
        rows.Scan(&thedate, &completeds)
		if err = rows.Scan(&thedate, &completeds); err != nil {
			break
		}
		fmt.Printf("The date is: %s\n", thedate)
    }
    
}
