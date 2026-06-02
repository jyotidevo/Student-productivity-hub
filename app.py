from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/attendance", methods=["GET", "POST"])
def attendance():

    percentage = None
    status = ""

    if request.method == "POST":
        attended = int(request.form["attended"])
        total = int(request.form["total"])

        percentage = (attended / total) * 100

        if percentage >= 75:
            status = "✅ Good Attendance"
        else:
            status = "⚠️ Attendance Below 75%"

    return render_template(
        "attendance.html",
        percentage=percentage,
        status=status
    )

if __name__ == "__main__":
    app.run(debug=True)