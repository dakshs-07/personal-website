from flask import render_template
from content import SITE_CONTENT
from services import get_stats, get_cars
from analytics import highlight_stat, car_count
from utils import title_case

def register_routes(app):

    @app.route("/")
    def home():
        stats = get_stats()
        featured = highlight_stat(stats)
        cars = get_cars()
        return render_template(
            "home.html",
            content=SITE_CONTENT,
            stats=stats,
            featured=featured,
            cars=cars,
            car_count=car_count(cars)
        )

    @app.route("/about")
    def about():
        return render_template(
            "about.html",
            bio=SITE_CONTENT["bio"],
            name=title_case(SITE_CONTENT["name"])
        )

    @app.route("/cars")
    def cars_page():
        cars = get_cars()
        return render_template(
            "cars.html",
            cars=cars
        )
