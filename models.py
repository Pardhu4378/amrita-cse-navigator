"""models.py — SQLAlchemy database models for Amrita CSE Navigator"""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    semester = db.Column(db.Integer, nullable=False, default=1)
    cgpa = db.Column(db.Float, nullable=True)
    coding_level = db.Column(db.String(50), default="Beginner")
    career_goal_desc = db.Column(db.Text, nullable=True)
    specialization = db.Column(db.String(50), default="Product-Based Companies")

    progress = db.relationship("Progress", backref="user", lazy=True, cascade="all, delete-orphan")
    chat_history = db.relationship("ChatHistory", backref="user", lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "semester": self.semester,
            "cgpa": self.cgpa,
            "coding_level": self.coding_level,
            "career_goal_desc": self.career_goal_desc,
            "specialization": self.specialization,
        }


class Subject(db.Model):
    __tablename__ = "subjects"
    id = db.Column(db.Integer, primary_key=True)
    semester = db.Column(db.Integer, nullable=False)
    subject_name = db.Column(db.String(200), nullable=False)
    career_relevance = db.Column(db.Text, nullable=True)

    progress = db.relationship("Progress", backref="subject", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "semester": self.semester,
            "subject_name": self.subject_name,
            "career_relevance": self.career_relevance,
        }


class Elective(db.Model):
    __tablename__ = "electives"
    id = db.Column(db.Integer, primary_key=True)
    specialization = db.Column(db.String(100), nullable=False)
    elective_name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)


class Progress(db.Model):
    __tablename__ = "progress"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"), nullable=False)
    status = db.Column(db.String(20), default="Not Started")  # Not Started / In Progress / Completed


class ChatHistory(db.Model):
    __tablename__ = "chat_history"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    message = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
