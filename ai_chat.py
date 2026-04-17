import os

from dotenv import load_dotenv
from openai import OpenAI


def get_ai_client():
    """Helper to initialize OpenAI client with latest env vars"""
    load_dotenv()
    return OpenAI(api_key=os.environ.get("OPENAI_API_KEY", ""))


SYSTEM_PROMPT_TEMPLATE = """You are an expert academic AI assistant named "Amrita AI" designed exclusively for Amrita University CSE students.

Student Profile:
- Name: {name}
- Current Semester: {semester}
- Coding Level: {coding_level}
- Specialization Interest: {specialization}
- Primary Career Goal Context: {career_goal_desc}

Your responsibilities:
1. Answer subject-related doubts clearly and with examples
2. Explain complex topics in a beginner-friendly, step-by-step manner if the coding level is Beginner
3. Provide coding help with working examples suited to their coding level
4. Give career guidance aligned with their {specialization} path and their goal: {career_goal_desc}
5. Suggest relevant resources, practice problems, and interview tips
6. Generate practice questions on demand
7. Motivate and guide students on their academic journey

Important rules:
- Keep responses structured with headers if the answer is long
- Focus on Amrita CSE curriculum topics (Semesters 1-8)
- Be encouraging and supportive
- For coding questions, always provide runnable code examples
- For career questions, align advice with the student's specialization: {specialization}
"""


def get_mock_response(user_message: str, user_profile: dict) -> str:
    """Provides a simulated intelligent response when API key is missing."""
    msg = user_message.lower()
    name = user_profile.get("name", "Student")
    spec = user_profile.get("specialization", "CSE")

    if "hello" in msg or "hi" in msg:
        return f"Hello {name}! I'm your Amrita AI Assistant. How can I help you with your Semester {user_profile.get('semester', 1)} subjects or your {spec} career path today?"

    if "career" in msg or "job" in msg or "placement" in msg:
        return f"For a {spec} path at Amrita, I recommend focusing on building a strong GitHub portfolio and maintaining a CGPA above 8.0 for top product companies. Would you like a roadmap?"

    if "coding" in msg or "python" in msg or "java" in msg:
        return "That's a great technical question! In Demo Mode, I can tell you that staying consistent with LeetCode and understanding Data Structures (Semester 3/4) is key for CSE students."

    # Default fallback
    return f"Note: **Demo Mode Active**. To get real-time AI logic, please add your OpenAI API key to the `.env` file. However, as an Amrita AI, I can tell you that Semester {user_profile.get('semester', 1)} is a crucial semester for your {spec} journey!"


def get_ai_response(user_message: str, chat_history: list, user_profile: dict) -> str:
    """
    Get AI response using OpenAI Chat Completion API (or fallback to Mock).
    """
    api_key = os.environ.get("OPENAI_API_KEY", "")

    # Check if we should use Mock mode
    if not api_key or api_key == "your_key_here" or api_key.strip() == "":
        return get_mock_response(user_message, user_profile)

    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(
        name=user_profile.get("name", "Student"),
        semester=user_profile.get("semester", 1),
        coding_level=user_profile.get("coding_level", "Beginner"),
        specialization=user_profile.get("specialization", "Product-Based Companies"),
        career_goal_desc=user_profile.get(
            "career_goal_desc", "I want to be a software engineer."
        ),
    )

    # Build messages context (last 10 messages for context window efficiency)
    messages = [{"role": "system", "content": system_prompt}]

    # Add last 10 chat history messages to maintain context
    recent_history = chat_history[-10:] if len(chat_history) > 10 else chat_history
    for msg in recent_history:
        messages.append({"role": msg["role"], "content": msg["content"]})

    # Add current user message
    messages.append({"role": "user", "content": user_message})

    try:
        client = get_ai_client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=1000,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        error_msg = str(e)
        if "api_key" in error_msg.lower() or "authentication" in error_msg.lower():
            return "❌ Invalid API key. Please check your `.env` file and ensure `OPENAI_API_KEY` is set correctly."
        elif "quota" in error_msg.lower() or "billing" in error_msg.lower():
            return "❌ OpenAI quota exceeded. Please check your OpenAI billing at platform.openai.com."
        else:
            return f"❌ AI service error: {error_msg}. Please try again later."
