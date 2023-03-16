from flask import render_template  # Remove: import Flask
import connexion
import user as sheduled_user
import event as sheduled_event

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")


@app.route("/")
def home():
    user = sheduled_user.read_all()
    event = sheduled_event.read_all()
    return render_template("home.html", user=user, event=event)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
