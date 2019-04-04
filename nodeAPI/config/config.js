module.exports = {
  //jwt token and password hashing
  superSecret : 'xyz@123', // ToDo Change the value
  bcryptSalt : 10, // ToDo Change the value
  
  //mysql db
  MySQLHost : '10.1.12.232',
  MySQLName : 'tableau',
  MySQLUser : 'tableausuperadmin',
  MySQLPassword : 'thisismyboomsticksaidthegreatestmanever',
  
  //oracle db
  OracleUser          : "tableausuperadmin",
  OraclePassword      : "thisismyboomsticksaidthegreatestmanever",
  OracleConnectString : "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=10.1.12.106)(PORT=1521))(CONNECT_DATA =(SERVER=DEDICATED)(SID=HEXP)))"
};
