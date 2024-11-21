from config import create_app
from routes import init_routes

app, state = create_app()

init_routes(app, state)

if __name__ == "__main__":
    app.run(debug=True, port=3000)