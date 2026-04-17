"""database.py — DB initialization and seeding for Amrita CSE Navigator"""
from models import db, Subject, Elective
from data import CURRICULUM, CAREER_MAP, ELECTIVE_MAP


def init_db(app):
    """Initialize the database and seed data."""
    with app.app_context():
        db.create_all()
        _seed_subjects()
        _seed_electives()
        print("[SUCCESS] Database initialized and seeded successfully.")


def _seed_subjects():
    """Seed subject table from CURRICULUM data (skip if already seeded)."""
    if Subject.query.count() > 0:
        return
    for semester, subjects in CURRICULUM.items():
        for s in subjects:
            career = CAREER_MAP.get(s["name"], s.get("career", "Builds core knowledge"))
            subject = Subject(
                semester=semester,
                subject_name=s["name"],
                career_relevance=career,
            )
            db.session.add(subject)
    db.session.commit()
    print(f"[SUCCESS] Seeded {Subject.query.count()} subjects.")


def _seed_electives():
    """Seed elective table (skip if already seeded)."""
    if Elective.query.count() > 0:
        return
    for spec, electives in ELECTIVE_MAP.items():
        for e in electives:
            elective = Elective(
                specialization=spec,
                elective_name=e["name"],
                description=e.get("desc", ""),
            )
            db.session.add(elective)
    db.session.commit()
    print(f"[SUCCESS] Seeded {Elective.query.count()} electives.")
