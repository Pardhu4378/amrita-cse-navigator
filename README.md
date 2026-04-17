# Amrita CSE Navigator – AI Academic & Career Companion

A curriculum-aware intelligent platform exclusively for Amrita University CSE students (2023 onwards curriculum).

## Features
- **Semester Roadmap**: Complete 8-semester curriculum for Amrita CSE 2023+.
- **Career Mapping**: Understand why each subject matters for your dream career path (AI, Cyber Security, etc.).
- **Elective Engine**: Personalized elective recommendations semester-wise.
- **AI Chat Assistant**: Built-in AI for doubt solving, coding help, and career guidance in English or Telugu.
- **Video Courses**: Curated YouTube courses with filters for programming and explanation languages.
- **Progress Tracking**: Visual progress bars and status management per subject.

## Tech Stack
- **Backend**: Python (Flask) + SQLAlchemy (SQLite)
- **Frontend**: HTML5 + CSS3 (Modern Glassmorphism Theme) + Bootstrap 5
- **AI**: OpenAI API (GPT models)

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd AmritaCSENavigator
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   - Copy `env.example` to `.env`
   - Add your [OpenAI API Key](https://platform.openai.com) in the `.env` file.

4. **Run the Application**:
   ```bash
   python app.py
   ```
   Open `http://127.0.0.1:5000` in your browser.

## Customization

### Adding New Semesters or Electives
1. Open `data.py`.
2. Update the `CURRICULUM` dictionary to add or modify semester subjects.
3. Update `ELECTIVE_MAP` for new specializations.
4. The database will auto-seed these changes on the next run.

### Updating Course Videos
1. Open `data.py`.
2. Locate the `SUBJECT_DETAILS` dictionary.
3. Add or update the list of topics and YouTube embed links.
