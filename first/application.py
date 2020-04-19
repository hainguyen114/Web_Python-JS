import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *
from flask.json import jsonify

app = Flask(__name__)

# engine = create_engine(os.getenv('DATABASE_URL'))
# db = scoped_session(sessionmaker(bind=engine))
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    # flights = db.execute("SELECT * FROM flights").fetchall()
    flights = Flight.query.all()
    return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""

    # Get form information.
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")

    # Make sure the flight exists.
    flight = Flight.query.get(flight_id)
    # if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0:
    if flight is None:
        return render_template("error.html", message="No such flight with that id.")

    # Add passenger.
    # db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
    #             {"name": name, "flight_id": flight_id})
    # db.commit()
    flight.add_passenger(name)
    return render_template("success.html")

@app.route("/flights")
def flights():
    """Lists all flights."""
    # flights = db.execute("SELECT * FROM flights").fetchall()
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """Lists details about a single flight."""

    # Make sure flight exists.
    # flight = db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).fetchone()
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight.")

    # Get all passengers.
    # passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
    #                          {"flight_id": flight_id}).fetchall()
    passengers = flight.passengers
    return render_template("flight.html", flight=flight, passengers=passengers)

@app.route("/api/flights/<int:flight_id>")
def flight_api(flight_id):
    flight = Flight.query.get(flight_id)
    
    if flight is None:
        return jsonify({"error" : "Invalid flight_id"}), 422

    passengers = flight.passengers
    names = []
    for passenger in passengers:
        names.append(passenger.name)
    return jsonify({
            "origin": flight.origin,
            "destination": flight.destination,
            "duration": flight.duration,
            "passengers": names
            })