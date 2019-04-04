var mysql = require('mysql'); //require mysql
var oracle = require('oracledb'); //require oracle
var config = require('./config'); //import config file for DB information
var util = require('util');

//create pool connection of MySQL
var poolMySQL = mysql.createPool({
    connectionLimit: 100,
    host: config.MySQLHost,
    user: config.MySQLUser,
    password: config.MySQLPassword,
    database: config.MySQLName
});

//create pool connection of oracle
async function init() {
  const poolOracle = await oracle.createPool({
		poolAlias: 'pool1',
		user: config.OracleUser,
		password: config.OraclePassword,
		connectString: config.OracleConnectString
    }); 
}
module.exports.init = init;

poolMySQL.getConnection((err, connection) => {
    if (err) {
        if (err.code === 'PROTOCOL_CONNECTION_LOST') {
            console.log('Database connection was closed.');
        }
        if (err.code === 'ER_CON_COUNT_ERROR') {
            console.log('Database has too many connections.')
        }
        if (err.code === 'ECONNREFUSED') {
            console.log('Database connection was refused.');
        }
        if (connection) connection.release();
        return
    }
});



try {
    console.log('Initializing database module');
 
    init();
	console.log("hehe", poolOracle);
  } catch (err) {
    console.error(err);
 
    process.exit(1); // Non-zero failure code
  }
/*
poolOracle.then(function(result) {
   console.log("hehe", result) // "Some User token"
   poolOracle.getConnection(function(err, conn) {
      // Use connection from the pool and then release it
   });
})
*/

poolMySQL.query = util.promisify(poolMySQL.query);

module.exports = poolMySQL; //export the pool variable for globally use
