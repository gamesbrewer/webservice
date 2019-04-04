var response = require('./../general/MyResponse');
var messages = require('./../general/messages');
var config = require('./../config/config');

module.exports = {
    listClient: async (req, res) => {
        //list all user
        var query = "SELECT * FROM users";

        try{
            var user = await connection.query(query);
        } catch (err) {
            console.error("Error occurred : ", err.message);
            response.createResponse(res,500,err.message,{},{});
        }
		
        response.createResponse(res, 200, messages.CLIENT_LISTED_SUCCESS, {user}, {});
    },
};
