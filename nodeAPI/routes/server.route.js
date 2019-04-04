//create instance of express routes
var routes = express.Router();

routes.get('/state', (req, res, next) => {
    res.status(200).json({ isalive: true })
});

//export express routes
module.exports = routes;
