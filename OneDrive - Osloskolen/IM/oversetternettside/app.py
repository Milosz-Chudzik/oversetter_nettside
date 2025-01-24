from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="10.2.2.219",
    user="min",
    password="passord",
    database="oversetter"
)
    
 
cursor = mydb.cursor()

cursor.execute('''
    create table IF NOT EXISTS brukere (
        user_id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
        email varchar(255) NOT NULL unique,
        passord varchar(255) NOT NULL
    );
''')

cursor.execute('''
    create table IF NOT EXISTS ytelser (
        ytelse_id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
        ytelse_navn varchar(255) NOT NULL,
        beskrivelse text NOT NULL
    );
''')

cursor.execute('''
        create table IF NOT EXISTS bestillinger (
        bestilling_id int AUTO_INCREMENT primary key NOT NULL,
        bestillingsdato datetime NOT NULL,
        user_id int NOT NULL,
        ytelse_id int NOT NULL,
        FOREIGN KEY (user_id) REFERENCES brukere(user_id),
        FOREIGN KEY (ytelse_id) REFERENCES ytelser(ytelse_id)
    );
''')

mydb.commit()

    
@app.route('/')
def home():
    return "dette er hjemmesiden"

@app.route("/login", methods=["GET", "POST"])
def login():
    
    if request.method == "POST":
        brukernavn = request.form["brukernavn"]
        passord = request.form["passord"]
        
        try:
            query = "SELECT passord FROM bruker WHERE brukernavn = %s"
            cursor.execute(query, (brukernavn,))
            result = cursor.fetchone()

            if result:
                stored_passord = result[0]
                if passord == stored_passord:
                    return f"Velkommen, {brukernavn}!"  
                else:
                    return "Feil passord. Prøv igjen."
            else:
                return "Bruker ikke funnet."
        except mysql.connector.Error as err:
            return f"Feil under innlogging: {err}"
    return render_template('logginn.html')

@app.route("/registrer", methods=["GET", "POST"])
def register_user():
    print("registrer")
    if request.method == "POST":
        print("hei")
        email = request.form['email']
        passord = request.form["passord"]
        print(cursor)
        try:
            sql = "INSERT INTO brukere (email, passord) VALUES (%s, %s)"
            cursor.execute(sql,(email, passord))

            mydb.commit()
            return render_template("bestill.html")
        #except mysql.connector.Error as err:
         #   return f"Feil under registrering: {err}"
        except Exception as error:
            print(error)



    
    return render_template("registrer.html")
       
            
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=2222)

