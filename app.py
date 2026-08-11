from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_airport", methods=["GET","POST"])
def add_one_airport():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescity= query_db("select * from city")

        one_user = query_db("insert into airport (name,city_id) values (:name,:city_id)",hey)
        user = query_db('select * from airport')

        return render_template("airportform.html", airports=user, one_user=one_user, the_title="add new airport", touslescity=touslescity)


    touslescity= query_db("select * from city")

    user = query_db('select * from airport')
    one_user = query_db("select * from airport limit 1", one=True)
    return render_template("airportform.html", airports=user, one_user=one_user, the_title="add new airport", touslescity=touslescity)

@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        touslesfavorite_genre= query_db("select * from favorite_genre")

        touslesmusicalinstrument= query_db("select * from musicalinstrument")

        touslesartist_composer_or_band= query_db("select * from artist_composer_or_band")

        one_user = query_db("insert into user (username,phone,email,country_id,password,listener,musician,favorite_genre_id,musicalinstrument_id,artist_composer_or_band_id) values (:username,:phone,:email,:country_id,:password,:listener,:musician,:favorite_genre_id,:musicalinstrument_id,:artist_composer_or_band_id)",hey)
        user = query_db('select * from user')

        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['username','phone','email','country_id','password','listener','musician','favorite_genre_id','musicalinstrument_id','artist_composer_or_band_id']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry, touslesfavorite_genre=touslesfavorite_genre, touslesmusicalinstrument=touslesmusicalinstrument, touslesartist_composer_or_band=touslesartist_composer_or_band)


    touslescountry= query_db("select * from country")

    touslesfavorite_genre= query_db("select * from favorite_genre")

    touslesmusicalinstrument= query_db("select * from musicalinstrument")

    touslesartist_composer_or_band= query_db("select * from artist_composer_or_band")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry, touslesfavorite_genre=touslesfavorite_genre, touslesmusicalinstrument=touslesmusicalinstrument, touslesartist_composer_or_band=touslesartist_composer_or_band)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['username','phone','email','country_id','password','listener','musician','favorite_genre_id','musicalinstrument_id','artist_composer_or_band_id']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['username','phone','email','country_id','password','listener','musician','favorite_genre_id','musicalinstrument_id','artist_composer_or_band_id']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_musical_genre", methods=["GET","POST"])
def add_one_musical_genre():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into musical_genre (name) values (:name)",hey)
        user = query_db('select * from musical_genre')

        return render_template("musical_genreform.html", musical_genres=user, one_user=one_user, the_title="add new musical_genre")


    user = query_db('select * from musical_genre')
    one_user = query_db("select * from musical_genre limit 1", one=True)
    return render_template("musical_genreform.html", musical_genres=user, one_user=one_user, the_title="add new musical_genre")

@app.route("/add_one_artist_composer_or_band", methods=["GET","POST"])
def add_one_artist_composer_or_band():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into artist_composer_or_band (name) values (:name)",hey)
        user = query_db('select * from artist_composer_or_band')

        return render_template("artist_composer_or_bandform.html", artist_composer_or_bands=user, one_user=one_user, the_title="add new artist_composer_or_band")


    user = query_db('select * from artist_composer_or_band')
    one_user = query_db("select * from artist_composer_or_band limit 1", one=True)
    return render_template("artist_composer_or_bandform.html", artist_composer_or_bands=user, one_user=one_user, the_title="add new artist_composer_or_band")

@app.route("/add_one_photos", methods=["GET","POST"])
def add_one_photos():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['pic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename


        touslesairport= query_db("select * from airport")

        one_user = query_db("insert into photos (airport_id,pic,description) values (:airport_id,:pic,:description)",hey)
        user = query_db('select * from photos')

        return render_template("photosform.html", photoss=user, one_user=one_user, the_title="add new photos", touslesairport=touslesairport)


    touslesairport= query_db("select * from airport")

    user = query_db('select * from photos')
    one_user = query_db("select * from photos limit 1", one=True)
    return render_template("photosform.html", photoss=user, one_user=one_user, the_title="add new photos", touslesairport=touslesairport)

@app.route("/add_one_musicalinstrument", methods=["GET","POST"])
def add_one_musicalinstrument():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into musicalinstrument (name) values (:name)",hey)
        user = query_db('select * from musicalinstrument')

        return render_template("musicalinstrumentform.html", musicalinstruments=user, one_user=one_user, the_title="add new musicalinstrument")


    user = query_db('select * from musicalinstrument')
    one_user = query_db("select * from musicalinstrument limit 1", one=True)
    return render_template("musicalinstrumentform.html", musicalinstruments=user, one_user=one_user, the_title="add new musicalinstrument")

@app.route("/add_one_person", methods=["GET","POST"])
def add_one_person():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        touslesmusicalinstrument= query_db("select * from musicalinstrument")

        one_user = query_db("insert into person (name,email,phone,country_id,musicalinstrument_id,oracle) values (:name,:email,:phone,:country_id,:musicalinstrument_id,:oracle)",hey)
        user = query_db('select * from person')

        return render_template("personform.html", persons=user, one_user=one_user, the_title="add new person", touslescountry=touslescountry, touslesmusicalinstrument=touslesmusicalinstrument)


    touslescountry= query_db("select * from country")

    touslesmusicalinstrument= query_db("select * from musicalinstrument")

    user = query_db('select * from person')
    one_user = query_db("select * from person limit 1", one=True)
    return render_template("personform.html", persons=user, one_user=one_user, the_title="add new person", touslescountry=touslescountry, touslesmusicalinstrument=touslesmusicalinstrument)

@app.route("/add_one_photoshavepeople", methods=["GET","POST"])
def add_one_photoshavepeople():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesperson= query_db("select * from person")

        touslesphotos= query_db("select * from photos")

        one_user = query_db("insert into photoshavepeople (person_id,photos_id) values (:person_id,:photos_id)",hey)
        user = query_db('select * from photoshavepeople')

        return render_template("photoshavepeopleform.html", photoshavepeoples=user, one_user=one_user, the_title="add new photoshavepeople", touslesperson=touslesperson, touslesphotos=touslesphotos)


    touslesperson= query_db("select * from person")

    touslesphotos= query_db("select * from photos")

    user = query_db('select * from photoshavepeople')
    one_user = query_db("select * from photoshavepeople limit 1", one=True)
    return render_template("photoshavepeopleform.html", photoshavepeoples=user, one_user=one_user, the_title="add new photoshavepeople", touslesperson=touslesperson, touslesphotos=touslesphotos)

@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into country (name) values (:name)",hey)
        user = query_db('select * from country')

        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")


    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_city", methods=["GET","POST"])
def add_one_city():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into city (name,country_id) values (:name,:country_id)",hey)
        user = query_db('select * from city')

        return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from city')
    one_user = query_db("select * from city limit 1", one=True)
    return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)

