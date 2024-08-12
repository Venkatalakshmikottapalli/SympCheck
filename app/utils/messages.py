# app/utils/messages.py

BOT_MESSAGES = {
    "welcome": (
        "Hello there! 👋 I'm here to help you check your health. "
        "I can assist you in identifying potential diseases based on the symptoms you provide."
    ),
    "ask_symptom": (
        "Let's get started! Please share your first symptom with me:"
    ),
    "next_symptom": (
        "Got it! What’s your next symptom?"
    ),
    "extra_symptoms": (
        "Please enter more symptoms to help me diagnose you accurately, or press 'Submit' if you're ready."
    ),
    "max_symptoms": (
        "You've reached the maximum number of symptoms. Just hit 'Submit' when you're ready for your diagnosis."
    ),
    "already_selected": (
        "It looks like you've already selected that symptom. Please choose a different one."
    ),
    "prediction_result": (
        "You might have: {}. ⚠️ This prediction is generated by an AI model. Please do not solely rely on it for medical decisions."
    ),
    "reset_intro": (
        "Let’s start fresh!. I can help you identify potential diseases based on the symptoms you provide. "
        "Please enter your symptom again:"
    ),
}