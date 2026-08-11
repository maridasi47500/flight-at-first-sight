
mkdir templates 
python3 scaffold.py airport name city_id:references
python3 scaffold.py user username phone email country_id:references password listener:radio musician:radio favorite_genre_id:references musicalinstrument_id:references artist_composer_or_band_id:references
python3 scaffold.py musical_genre name
python3 scaffold.py artist_composer_or_band name
python3 scaffold.py photos airport_id:references pic:file description
python3 scaffold.py musicalinstrument name
python3 scaffold.py person name email phone country_id:references musicalinstrument_id:references oracle:radio
python3 scaffold.py photoshavepeople person_id:references photos_id:references
python3 scaffold.py country name
python3 scaffold.py city name country_id:references
