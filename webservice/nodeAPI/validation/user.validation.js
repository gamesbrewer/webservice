var response = require('./../general/MyResponse'); //common function for every http response inside general folder
var messages = require('./../general/messages'); //common files inside general folder for each error message in app

//create instance of express-validator
const {check,validationResult} = require('express-validator/check');
const {matchedData, sanitize} = require('express-validator/filter');

//function that validate express-validator results
function checkValidationResult(req, res, next) {
    var result = validationResult(req);
    if (!result.isEmpty()) {
        response.createResponse(res, 400,result.array()[0].msg,{}, {}); //response.createResponse is a method of general/MyResponse
    } else {
        next(); //go ahead if request is valid
    }
}

module.exports.checkValidationResult = checkValidationResult;

//function that actually validate request
module.exports.validateAddUser = [
    check('email').isLength({min: 1}).withMessage(messages.EMAIL_REQUIRED).isEmail().withMessage(messages.INVALID_EMAIL),
    check('password').isLength({ min: 1 }).withMessage(messages.PASSWORD_REQUIRED),
    check('confirmPassword').isLength({ min: 1 }).withMessage(messages.CONFIRM_PASSWORD_REQUIRED).isLength({max:6}).withMessage(messages.CONFIRM_PASSWORD_MAX_LENGTH)
        .custom((value, {req}) => {
            if (value !== req.body.password) {
                throw new Error(messages.PASSWORD_AND_CONFIRM_PASSWORD_SAME)
            } else {
                return true;
            }
        }),
];