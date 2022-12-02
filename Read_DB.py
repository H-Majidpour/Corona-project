import pickle


PATH = "statics/DB/data.dat"

def read_db():
    Fin = open(PATH, 'rb')
    Coronavirus_Cases = pickle.load(Fin)
    Deaths = pickle.load(Fin)
    Recovered = pickle.load(Fin)
    Table_info = pickle.load(Fin)

    info_dict = {
        "Coronavirus_Cases" : Coronavirus_Cases,
        "Deaths" : Deaths,
        "Recovered" : Recovered,
        "Table_info" : Table_info
    }

    return info_dict
