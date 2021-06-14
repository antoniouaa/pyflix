from pyflix import create_app


if __name__ == "__main__":
    app = create_app()
    app.run(host="192.168.0.58", port=5000, load_dotenv=True)
