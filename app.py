'''THIS IS THE PAGE THAT WILL INITIALIZE OUR APP IN HEROKU, AND DO OTHER COOL STUFF TOO IN A FEW DAYS OR SO '''

# LETS GO

def create_app():
    """
    Function to deploy heroku application.
    Contains assorment of functions which control the inputs and outputs
    of interractive web application.
    """
    app = Flask(__name__)
    load_model = load('finalized_model.sav')
    # as easy as changing path to /form and make a link to it in main page
    @app.route('/')
    def form():
        return render_template('form.html')\