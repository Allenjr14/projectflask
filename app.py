from flask import Flask , redirect , url_for, render_template , request , session , flash , jsonify , json
from datetime import  timedelta


app = Flask (__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=10)

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        flash("login successful!")
        user = request.form["allen"]
        session["user"]= user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login1.html")

@app.route("/user>")
def user():
    if "user" in session:
        user = session["user"]
        flash("Already logged in!")
        return render_template("user.html", user =user)
    else:
        flash("You are not logged in !")
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    session.pop("user", None)
    flash(f"logout successfull","{user}")
    return redirect(url_for("login"))



@app.route("/sod",methods=['GET'])
def jsondata1():
    data1 =  {
        "job_id": 1,
        "job_title": "Software Engineer",
        "company": "Tech Solutions Inc.",
        "required_skills": ["JavaScript", "React", "Node.js"],
        "location": "San Francisco",
        "job_type": "Full-Time",
        "experience_level": "Intermediate"
    }
    print("software engineer")
    return data1

@app.route("/dus",methods=['GET'])
def jsondata2():
    data2 =  {
        "job_id": 2,
        "job_title": "Data Scientist",
        "company": "Data Analytics Corp.",
        "required_skills": ["Python", "Data Analysis", "Machine Learning"],
        "location": "Remote",
        "job_type": "Full-Time",
        "experience_level": "Intermediate"
    }
    print("Data scientist")
    return data2

@app.route("/fd",methods=['GET'])
def jsondata3():
    data3 ={
        "job_id": 3,
        "job_title": "Frontend Developer",
        "company": "Creative Designs LLC",
        "required_skills": ["HTML", "CSS", "JavaScript", "Vue.js"],
        "location": "New York",
        "job_type": "Part-Time",
        "experience_level": "Junior"
    }
    print("Frontend Developer")
    return data3

@app.route("/bd",methods=['GET'])
def jsondata4():
    data4 ={
        "job_id": 4,
        "job_title": "Backend Developer",
        "company": "Web Services Co.",
        "required_skills": ["Python", "Django", "REST APIs"],
        "location": "Chicago",
        "job_type": "Full-Time",
        "experience_level": "Senior"
    }
    print("Backend Developer")
    return data4

@app.route("/ml",methods=['GET'])
def jsondata5():
    data5 ={
        "job_id": 5,
        "job_title": "Machine Learning Engineer",
        "company": "AI Innovations",
        "required_skills": ["Python", "Machine Learning", "TensorFlow"],
        "location": "Boston",
        "job_type": "Full-Time",
        "experience_level": "Intermediate"
    }
    print("Machine learning engnieer")
    return data5

@app.route("/de",methods=['GET'])
def jsondata6():
    data6 ={
        "job_id": 6,
        "job_title": "DevOps Engineer",
        "company": "Cloud Networks",
        "required_skills": ["AWS", "Docker", "Kubernetes"],
        "location": "Seattle",
        "job_type": "Full-Time",
        "experience_level": "Senior"
    }
    print("DevOps Engineer")
    return data6

@app.route("/fsd",methods=['GET'])
def jsondata7():
    data7 = {
        "job_id": 7,
        "job_title": "Full Stack Developer",
        "company": "Startup Hub",
        "required_skills": ["JavaScript", "Node.js", "Angular", "MongoDB"],
        "location": "Austin",
        "job_type": "Full-Time",
        "experience_level": "Intermediate"
    }
    print("Full Stack Developer")
    return data7


@app.route("/displaydata",methods=['GET'])
def displaydata():
    print("These are the jobs which are currently available....")
    data13 = {
        "datacom": 
        [
        {
            "job_id": 1,
            "job_title": "Software Engineer",
            "company": "Tech Solutions Inc.",
            "required_skills": ["JavaScript", "React", "Node.js"],
            "location": "San Francisco",
            "job_type": "Full-Time",
            "experience_level": "Intermediate"
        },
        {
            "job_id": 2,
            "job_title": "Data Scientist",
            "company": "Data Analytics Corp.",
            "required_skills": ["Python", "Data Analysis", "Machine Learning"],
            "location": "Remote",
            "job_type": "Full-Time",
            "experience_level": "Intermediate"
        },
        {
            "job_id": 3,
            "job_title": "Frontend Developer",
            "company": "Creative Designs LLC",
            "required_skills": ["HTML", "CSS", "JavaScript", "Vue.js"],
            "location": "New York",
            "job_type": "Part-Time",
            "experience_level": "Junior"
        },
        {
            "job_id": 4,
            "job_title": "Backend Developer",
            "company": "Web Services Co.",
            "required_skills": ["Python", "Django", "REST APIs"],
            "location": "Chicago",
            "job_type": "Full-Time",
            "experience_level": "Senior"
        },
        {
            "job_id": 5,
            "job_title": "Machine Learning Engineer",
            "company": "AI Innovations",
            "required_skills": ["Python", "Machine Learning", "TensorFlow"],
            "location": "Boston",
            "job_type": "Full-Time",
            "experience_level": "Intermediate"
        },
        {
            "job_id": 6,
            "job_title": "DevOps Engineer",
            "company": "Cloud Networks",
            "required_skills": ["AWS", "Docker", "Kubernetes"],
            "location": "Seattle",
            "job_type": "Full-Time",
            "experience_level": "Senior"
        },
        {
            "job_id": 7,
            "job_title": "Full Stack Developer",
            "company": "Startup Hub",
            "required_skills": ["JavaScript", "Node.js", "Angular", "MongoDB"],
            "location": "Austin",
            "job_type": "Full-Time",
            "experience_level": "Intermediate"
        },
        {
            "job_id": 8,
            "job_title": "Data Analyst",
            "company": "Finance Analytics",
            "required_skills": ["SQL", "Python", "Tableau"],
            "location": "New York",
            "job_type": "Full-Time",
            "experience_level": "Junior"
        },
        {
            "job_id": 9,
            "job_title": "Quality Assurance Engineer",
            "company": "Reliable Software",
            "required_skills": ["Selenium", "Java", "Testing"],
            "location": "San Francisco",
            "job_type": "Contract",
            "experience_level": "Intermediate"
        },
        {
            "job_id": 10,
            "job_title": "Systems Administrator",
            "company": "Enterprise Solutions",
            "required_skills": ["Linux", "Networking", "Shell Scripting"],
            "location": "Remote",
            "job_type": "Full-Time",
            "experience_level": "Senior"
        }
        ]
    }
    return data13



if __name__ =="__main__":
    app.run(debug=True) 