import csv
from flask import Flask, render_template, request, redirect, url_for, make_response
from imdbmodels import Imdbuser, db


app = Flask(__name__)
db.create_all()

class filmek():
    def __init__(self, cim, leiras, IMDB):
        self.cim = cim
        self.leiras = leiras
        self.IMDB = IMDB


elso = filmek("The Shawshank Redemption",
              "Two imprisoned men bond over a number of years,"
              "finding solace and eventual redemption "
              "through acts of common decency.",
              "https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=ZWB8PT2QX4FAXCNQB8D8&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1")
masodik = filmek("The Godfather",
                 "The aging patriarch of an organized crime dynasty transfers "
                 "control of his clandestine empire to his reluctant son.",
                 "https://www.imdb.com/title/tt0068646/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=ZWB8PT2QX4FAXCNQB8D8&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_2")
harmadik = filmek("The Godfather: Part II",
                  "The early life and career of Vito Corleone in 1920s New York City is portrayed, "
                  "while his son, Michael, expands and tightens his grip on the family crime syndicate.",
                  "https://www.imdb.com/title/tt0071562/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=ZWB8PT2QX4FAXCNQB8D8&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_3")
negyedik = filmek("The Dark Knight",
                  "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, "
                  "Batman must accept one of the greatest psychological and physical tests of his ability "
                  "to fight injustice.",
                  "https://www.imdb.com/title/tt0468569/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=ZWB8PT2QX4FAXCNQB8D8&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_4")
otodik = filmek("12 Angry Men",
                "A jury holdout attempts to prevent a miscarriage of justice by forcing "
                "his colleagues to reconsider the evidence.",
                "https://www.imdb.com/title/tt0050083/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=ZWB8PT2QX4FAXCNQB8D8&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_5")
hatodik = filmek("Schindler's List",
                 "In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for "
                 "his Jewish workforce after witnessing their persecution by the Nazis.",
                 "https://www.imdb.com/title/tt0108052/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=57QNAAWK9P8J65TW50G6&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_6")
hetedik = filmek("The Lord of the Rings: The Return of the King",
                 "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze "
                 "from Frodo and Sam as they approach Mount Doom with the One Ring.",
                 "https://www.imdb.com/title/tt0167260/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=57QNAAWK9P8J65TW50G6&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_7")
nyolcadik = filmek("Pulp Fiction",
                   "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of "
                   "diner bandits intertwine in four tales of violence and redemption.",
                   "https://www.imdb.com/title/tt0110912/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=57QNAAWK9P8J65TW50G6&pf_rd_"
                   "s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_8")
kilencedik = filmek("Il buono, il brutto, il cattivo",
                    "A bounty hunting scam joins two men in an uneasy alliance against a third in a "
                    "race to find a fortune in gold buried in a remote cemetery.",
                    "https://www.imdb.com/title/tt0060196/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=57QNAAWK9P8J65TW50G6&pf_rd_s="
                    "center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_9")
tizedik = filmek("The Lord of the Rings: The Fellowship of the Ring",
                 "A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring "
                 "and save Middle-earth from the Dark Lord Sauron.",
                 "https://www.imdb.com/title/tt0120737/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=57QNAAWK9P8J65TW50G6&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_10")

filmek = [elso, masodik, harmadik, negyedik, otodik, hatodik, hetedik, nyolcadik, kilencedik, tizedik]


with open("users.csv","r") as regisztral:
    reader = csv.reader(regisztral)
    users = {rows[0]:rows[1] for rows in reader}
    print(users)

@app.route("/")
def index():
    return render_template("table.html")


@app.route("/form", methods=["POST"])
def contact():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in users and users[username] == password:
        response = make_response(render_template("table.html", filmek=filmek, name = username))
        response.set_cookie("username", username)  # cookie változó neve
    else:
        response = render_template("table.html")

    return response

@app.route("/reg", methods=["POST"])
def reg():
    username = request.form.get("regusername")
    password = request.form.get("regpassword")

    user = Imdbuser(name=username, password=password)

    db.add(user)
    db.commit()

    with open("users.csv", "a") as regisztral:
        regisztral.write(username+","+password+"\n")
    response = make_response(render_template("table.html", filmek=filmek, name = username))
    response.set_cookie("username", username)  # cookie változó neve

    return response

@app.route("/logoff", methods=["POST"])
def kilepes():
    response = make_response(render_template("table.html"))
    response.set_cookie("username", expires = 0)
    return response

if __name__ == '__main__':
    app.run()
