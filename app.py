from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/cgpa", methods=["GET", "POST"])
def cgpa():
    result = None

    if request.method == "POST":
        cgpas = []

        for i in range(1, 9):
            value = request.form.get(f"sem{i}")
            if value:
                cgpas.append(float(value))

        if len(cgpas) > 0:
            result = sum(cgpas) / len(cgpas)

    return render_template("cgpa.html", result=result)


@app.route("/placement", methods=["GET", "POST"])
def placement():
    readiness = None
    status = ""

    if request.method == "POST":

        dsa = int(request.form["dsa"])
        aptitude = int(request.form["aptitude"])
        mock = int(request.form["mock"])
        resume = request.form["resume"]

        dsa_score = min((dsa / 200) * 100, 100)
        aptitude_score = min((aptitude / 20) * 100, 100)
        mock_score = min((mock / 10) * 100, 100)

        resume_score = 100 if resume == "yes" else 0

        readiness = (dsa_score + aptitude_score + mock_score + resume_score) / 4

        if readiness >= 80:
            status = "🟢 Excellent Placement Readiness"
        elif readiness >= 60:
            status = "🟡 Good Progress"
        else:
            status = "🔴 Need More Preparation"

    return render_template("placement.html", readiness=readiness, status=status)


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

    return render_template("attendance.html", percentage=percentage, status=status)


if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)