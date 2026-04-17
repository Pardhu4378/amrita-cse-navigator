"""app.py — Main Flask application for Amrita CSE Navigator"""
import os
from flask import (
    Flask, render_template, request, redirect, url_for,
    session, jsonify, flash
)
from dotenv import load_dotenv
from models import db, User, Subject, Elective, Progress, ChatHistory
from database import init_db
from ai_chat import get_ai_response
from data import CURRICULUM, CAREER_MAP, ELECTIVE_MAP, ELECTIVE_ROADMAP, get_subject_details

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "amrita-cse-navigator-secret-2024")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# ─── Helpers ─────────────────────────────────────────────────────────────────

def get_current_user():
    user_id = session.get("user_id")
    if user_id:
        return User.query.get(user_id)
    return None


def get_user_progress_stats(user):
    """Calculate overall and per-semester progress percentages."""
    all_subjects = Subject.query.all()
    total = len(all_subjects)
    if total == 0:
        return {"overall": 0, "by_semester": {}}

    completed_count = 0
    by_semester = {}

    for sem in range(1, 9):
        sem_subjects = Subject.query.filter_by(semester=sem).all()
        sem_total = len(sem_subjects)
        sem_completed = 0
        for s in sem_subjects:
            prog = Progress.query.filter_by(user_id=user.id, subject_id=s.id).first()
            if prog and prog.status == "Completed":
                sem_completed += 1
                completed_count += 1
        by_semester[sem] = {
            "total": sem_total,
            "completed": sem_completed,
            "pct": int((sem_completed / sem_total) * 100) if sem_total > 0 else 0,
            "in_progress": 0,
        }
        # Count in-progress for each semester
        for s in sem_subjects:
            prog = Progress.query.filter_by(user_id=user.id, subject_id=s.id).first()
            if prog and prog.status == "In Progress":
                by_semester[sem]["in_progress"] += 1

    overall_pct = int((completed_count / total) * 100)
    return {"overall": overall_pct, "by_semester": by_semester}


# ─── Routes ──────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    user = get_current_user()
    if user:
        return redirect(url_for("dashboard"))
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user" in session or "user_id" in session:
        return redirect(url_for("dashboard"))
        
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        if not username:
            flash("Please enter your email or name.", "danger")
            return redirect(url_for("login"))
            
        # Match user by name (case-insensitive for convenience)
        existing_user = User.query.filter(User.name.ilike(f"%{username}%")).first()
        
        # If they don't exist, create a default profile so the dashboard doesn't break
        if not existing_user:
            existing_user = User(
                name=username, semester=1, 
                coding_level="Beginner",
                specialization="Product-Based Companies",
                career_goal_desc=""
            )
            db.session.add(existing_user)
            db.session.commit()
            
        session["user_id"] = existing_user.id
        session["user"] = username
        flash(f"Welcome, {username}!", "success")
        return redirect(url_for("dashboard"))

    return render_template("login.html")



@app.route("/profile", methods=["GET", "POST"])
def profile():
    user = get_current_user()
    
    # If user exists and it's just a GET request, normally they shouldn't see onboarding again
    if user and request.method == "GET" and not request.args.get("edit"):
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        semester = int(request.form.get("semester", 1))
        # Optional fields from wizard
        coding_level = request.form.get("coding_level", "Beginner")
        specialization = request.form.get("specialization", "Product-Based Companies")
        career_goal_desc = request.form.get("career_goal_desc", "").strip()

        if not name:
            flash("Please enter your name.", "danger")
            return redirect(url_for("profile"))

        if user:
            user.name = name
            user.semester = semester
            user.coding_level = coding_level
            user.specialization = specialization
            user.career_goal_desc = career_goal_desc
        else:
            user = User(
                name=name, semester=semester, 
                coding_level=coding_level,
                specialization=specialization,
                career_goal_desc=career_goal_desc
            )
            db.session.add(user)

        db.session.commit()
        session["user_id"] = user.id
        flash(f"Welcome, {user.name}! Your profile has been saved.", "success")
        return redirect(url_for("dashboard"))

    return render_template("profile.html", user=user,
                           specializations=list(ELECTIVE_MAP.keys()))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/dashboard")
def dashboard():
    user = get_current_user()
    if not user:
        return redirect(url_for("profile"))

    current_sem_subjects = Subject.query.filter_by(semester=user.semester).all()
    next_sem = user.semester + 1 if user.semester < 8 else None
    next_sem_subjects = Subject.query.filter_by(semester=next_sem).all() if next_sem else []
    progress_stats = get_user_progress_stats(user)

    # Get progress for each current subject
    subject_progress = {}
    for s in current_sem_subjects:
        prog = Progress.query.filter_by(user_id=user.id, subject_id=s.id).first()
        subject_progress[s.id] = prog.status if prog else "Not Started"

    return render_template(
        "dashboard.html",
        user=user,
        current_sem_subjects=current_sem_subjects,
        next_sem_subjects=next_sem_subjects,
        next_sem=next_sem,
        progress_stats=progress_stats,
        subject_progress=subject_progress,
        career_map=CAREER_MAP,
    )


@app.route("/semester")
def semester():
    user = get_current_user()
    if not user:
        return redirect(url_for("profile"))

    all_data = {}
    total_subjects_count = 0
    for sem in range(1, 9):
        subjects = Subject.query.filter_by(semester=sem).all()
        total_subjects_count += len(subjects)
        sub_list = []
        for s in subjects:
            prog = Progress.query.filter_by(user_id=user.id, subject_id=s.id).first()
            sub_list.append({
                "subject": s,
                "status": prog.status if prog else "Not Started",
            })
        all_data[sem] = sub_list

    return render_template("semester.html", user=user, all_data=all_data,
                           total_subjects_count=total_subjects_count,
                           curriculum=CURRICULUM)


@app.route("/specialization")
def specialization():
    user = get_current_user()
    if not user:
        return redirect(url_for("profile"))

    spec = user.specialization
    electives = Elective.query.filter_by(specialization=spec).all()
    roadmap = ELECTIVE_ROADMAP.get(spec, {})

    return render_template("specialization.html", user=user, electives=electives,
                           roadmap=roadmap, all_specs=list(ELECTIVE_MAP.keys()),
                           elective_map=ELECTIVE_MAP)


@app.route("/courses")
def courses():
    user = get_current_user()
    if not user:
        return redirect(url_for("profile"))

    sem_filter = request.args.get("semester", "all")

    if sem_filter == "all":
        subjects = Subject.query.order_by(Subject.semester).all()
    else:
        subjects = Subject.query.filter_by(semester=int(sem_filter)).order_by(Subject.semester).all()

    subject_progress = {}
    for s in subjects:
        prog = Progress.query.filter_by(user_id=user.id, subject_id=s.id).first()
        subject_progress[s.id] = prog.status if prog else "Not Started"

    return render_template(
        "courses.html",
        user=user,
        subjects=subjects,
        sem_filter=sem_filter,
        subject_progress=subject_progress,
        semesters=range(1, 9),
    )


@app.route("/subject/<int:subject_id>")
def subject_detail(subject_id):
    user = get_current_user()
    if not user:
        return redirect(url_for("profile"))

    subject = Subject.query.get_or_404(subject_id)

    details = get_subject_details(subject.subject_name)
    topics = details["topics"]
    video_url = details.get("video_url", "https://www.youtube.com/embed/rfscVS0vtbw")

    prog = Progress.query.filter_by(user_id=user.id, subject_id=subject_id).first()
    current_status = prog.status if prog else "Not Started"

    career_reason = CAREER_MAP.get(subject.subject_name, subject.career_relevance or "")

    return render_template(
        "subject.html",
        user=user,
        subject=subject,
        topics=topics,
        video_url=video_url,
        current_status=current_status,
        career_reason=career_reason,
    )


@app.route("/progress")
def progress():
    user = get_current_user()
    if not user:
        return redirect(url_for("profile"))

    progress_stats = get_user_progress_stats(user)
    all_subjects_by_sem = {}
    for sem in range(1, 9):
        subjects = Subject.query.filter_by(semester=sem).all()
        sub_list = []
        for s in subjects:
            prog = Progress.query.filter_by(user_id=user.id, subject_id=s.id).first()
            sub_list.append({
                "subject": s,
                "status": prog.status if prog else "Not Started",
            })
        all_subjects_by_sem[sem] = sub_list

    return render_template("progress.html", user=user,
                           progress_stats=progress_stats,
                           all_subjects_by_sem=all_subjects_by_sem)


@app.route("/chat")
def chat():
    user = get_current_user()
    if not user:
        return redirect(url_for("profile"))

    history = ChatHistory.query.filter_by(user_id=user.id).order_by(ChatHistory.timestamp).all()
    return render_template("chat.html", user=user, history=history)


# ─── API Endpoints ────────────────────────────────────────────────────────────

@app.route("/api/chat", methods=["POST"])
def api_chat():
    user = get_current_user()
    if not user:
        return jsonify({"error": "Not logged in"}), 401

    data = request.get_json()
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    # Build chat history context from DB
    history_records = (
        ChatHistory.query.filter_by(user_id=user.id)
        .order_by(ChatHistory.timestamp)
        .limit(20)
        .all()
    )
    chat_history = []
    for record in history_records:
        chat_history.append({"role": "user", "content": record.message})
        chat_history.append({"role": "assistant", "content": record.response})

    # Get AI response
    ai_response = get_ai_response(user_message, chat_history, user.to_dict())

    # Save to DB
    chat_record = ChatHistory(
        user_id=user.id,
        message=user_message,
        response=ai_response,
    )
    db.session.add(chat_record)
    db.session.commit()

    return jsonify({"response": ai_response})


@app.route("/api/progress/update", methods=["POST"])
def api_progress_update():
    user = get_current_user()
    if not user:
        return jsonify({"error": "Not logged in"}), 401

    data = request.get_json()
    subject_id = data.get("subject_id")
    status = data.get("status")

    valid_statuses = ["Not Started", "In Progress", "Completed"]
    if status not in valid_statuses:
        return jsonify({"error": "Invalid status"}), 400

    subject = Subject.query.get(subject_id)
    if not subject:
        return jsonify({"error": "Subject not found"}), 404

    prog = Progress.query.filter_by(user_id=user.id, subject_id=subject_id).first()
    if prog:
        prog.status = status
    else:
        prog = Progress(user_id=user.id, subject_id=subject_id, status=status)
        db.session.add(prog)

    db.session.commit()

    # Recalculate progress stats
    stats = get_user_progress_stats(user)
    return jsonify({"success": True, "overall": stats["overall"]})


@app.route("/api/chat/clear", methods=["POST"])
def api_chat_clear():
    user = get_current_user()
    if not user:
        return jsonify({"error": "Not logged in"}), 401
    ChatHistory.query.filter_by(user_id=user.id).delete()
    db.session.commit()
    return jsonify({"success": True})


# ─── Entry Point ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    init_db(app)
    print("[START] Amrita CSE Navigator running at http://127.0.0.1:5050")
    app.run(debug=True, port=5050)
