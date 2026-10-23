from flask import Flask, render_template, request, redirect, url_for, session, flash
import os


from flask import Flask

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret")


# ---------------- FILE UPLOAD ----------------
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("home.html")

# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("home"))
    return render_template("dashboard.html")

# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["user"] = request.form.get("username")
        return redirect(url_for("dashboard"))
    return render_template("login.html")

# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        session["user"] = request.form.get("username")
        return redirect(url_for("dashboard"))
    return render_template("register.html")

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

# ---------------- CAREER TEST ----------------
questions = [
    {
        "question": "Which do you like?",
        "options": {
            "tech": "Computers",
            "medical": "Helping people",
            "law": "Debating",
            "creative": "Design"
        }
    }
]

career_map = {
    "tech": "Web Development",
    "medical": "MBBS",
    "law": "LLB",
    "creative": "Graphic Design"
}

@app.route("/career-test", methods=["GET", "POST"])
def career_test():
    if "user" not in session:
        return redirect(url_for("home"))

    result = None

    if request.method == "POST":
        answer = request.form.get("q0")
        result = career_map.get(answer, "No result")

    return render_template("career_test.html", questions=questions, result=result)

# ---------------- LEARNING PAGE ----------------
@app.route("/learn")
def learn():
    if "user" not in session:
        return redirect(url_for("home"))

    resources = {
        "Python": "https://www.w3schools.com/python/",
        "HTML": "https://www.w3schools.com/html/",
        "JavaScript": "https://www.w3schools.com/js/",
        "Machine Learning": "https://www.w3schools.com/python/python_ml_getting_started.asp"
    }

    return render_template("learn.html", resources=resources)

# ---------------- RESUME UPLOAD (MAIN FEATURE) ----------------
@app.route("/resume", methods=["GET", "POST"])
def resume():
    if "user" not in session:
        return redirect(url_for("home"))

    if request.method == "POST":
        file = request.files.get("resume")

        if file and file.filename != "":
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
            flash("✅ Resume uploaded successfully!", "success")
        else:
            flash("❌ Upload failed!", "danger")

        return redirect(url_for("resume"))

    return render_template("resume.html")

# ---------------- LINKEDIN PLACEHOLDER ----------------
@app.route("/linkedin", methods=["GET", "POST"])
def linkedin():
    if "user" not in session:
        return redirect(url_for("home"))

    if request.method == "POST":
        file = request.files.get("resume")

        if file and file.filename != "":
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
            flash("✅ Resume uploaded! (LinkedIn API not connected)", "success")
        else:
            flash("❌ Upload failed!", "danger")

        return redirect(url_for("linkedin"))

    return render_template("linkedin.html")

# ---------------- AI CAREER PREDICTOR ----------------
@app.route("/predict", methods=["GET", "POST"])
def predict():
    if "user" not in session:
        return redirect(url_for("home"))

    result = None

    if request.method == "POST":
        tech = int(request.form.get("tech", 0))
        medical = int(request.form.get("medical", 0))
        law = int(request.form.get("law", 0))
        creative = int(request.form.get("creative", 0))

        scores = {
            "Web Development": tech,
            "MBBS": medical,
            "LLB": law,
            "Graphic Design": creative
        }

        result = max(scores, key=scores.get)

    return render_template("predict.html", result=result)

# ---------------- ROADMAP GRAPH ----------------
@app.route("/roadmap-graph")
def roadmap_graph():
    if "user" not in session:
        return redirect(url_for("home"))
    return render_template("roadmap_graph.html")

# ---------------- DEGREE ROADMAP ----------------
@app.route("/degree-roadmap")
def degree_roadmap_route():
    if "user" not in session:
        return redirect(url_for("home"))
    return render_template("degree_roadmap.html")

# ---------------- SAFE PLACEHOLDER ----------------
@app.route("/feature")
def feature():
    if "user" not in session:
        return redirect(url_for("home"))
    return "<h2>🚧 Feature Coming Soon</h2>"

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)