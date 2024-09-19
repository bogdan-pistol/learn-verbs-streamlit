import csv
import random
import streamlit as st

# Load verbs from the CSV file
@st.cache
def load_verbs():
    verbs = []
    with open('german_verbs.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            verbs.append(row)
    return verbs

verbs = load_verbs()

# Initialize session state variables
if 'correct_count' not in st.session_state:
    st.session_state.correct_count = 0
if 'total_count' not in st.session_state:
    st.session_state.total_count = 0
if 'current_verb' not in st.session_state:
    st.session_state.current_verb = None
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
if 'show_result' not in st.session_state:
    st.session_state.show_result = False

def pick_random_verb():
    st.session_state.current_verb = random.choice(verbs)
    st.session_state.show_result = False
    st.session_state.user_answers = {
        'Infinitive': '',
        'Präteritum': '',
        'Partizip Perfekt': ''
    }

def evaluate_answers():
    verb = st.session_state.current_verb
    user_answers = st.session_state.user_answers

    correct_infinitive = verb['Infinitive'].strip()
    correct_prateritum = verb['Präteritum'].strip()
    correct_partizip_perfekt = verb['Partizip Perfekt'].strip()

    infinitive = user_answers['Infinitive'].strip()
    prateritum = user_answers['Präteritum'].strip()
    partizip_perfekt = user_answers['Partizip Perfekt'].strip()

    is_infinitive_correct = infinitive.lower() == correct_infinitive.lower()
    is_prateritum_correct = prateritum.lower() == correct_prateritum.lower()
    is_partizip_correct = partizip_perfekt.lower() == correct_partizip_perfekt.lower()

    if is_infinitive_correct and is_prateritum_correct and is_partizip_correct:
        st.success("Correct!")
        st.session_state.correct_count += 1
    else:
        st.error("Incorrect!")
        st.write("### Correct Answers:")
        if not is_infinitive_correct:
            st.write(
                f"**Infinitive:** Your answer: *{infinitive}* | Correct: *{correct_infinitive}*"
            )
        else:
            st.write(f"**Infinitive:** *{correct_infinitive}*")
        if not is_prateritum_correct:
            st.write(
                f"**Präteritum:** Your answer: *{prateritum}* | Correct: *{correct_prateritum}*"
            )
        else:
            st.write(f"**Präteritum:** *{correct_prateritum}*")
        if not is_partizip_correct:
            st.write(
                f"**Partizip Perfekt:** Your answer: *{partizip_perfekt}* | Correct: *{correct_partizip_perfekt}*"
            )
        else:
            st.write(f"**Partizip Perfekt:** *{correct_partizip_perfekt}*")

st.title("German Verb Conjugation Practice")

# Start or Next Verb Button
if st.button('Start' if st.session_state.current_verb is None else 'Next Verb'):
    pick_random_verb()

# Display the current verb if one is selected
if st.session_state.current_verb:
    verb = st.session_state.current_verb
    english = verb['English']

    st.header(f"Translate: **{english}**")

    # Input fields for user answers in columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.session_state.user_answers['Infinitive'] = st.text_input(
            "Infinitive", st.session_state.user_answers.get('Infinitive', '')
        )
    with col2:
        st.session_state.user_answers['Präteritum'] = st.text_input(
            "Präteritum", st.session_state.user_answers.get('Präteritum', '')
        )
    with col3:
        st.session_state.user_answers['Partizip Perfekt'] = st.text_input(
            "Partizip Perfekt", st.session_state.user_answers.get('Partizip Perfekt', '')
        )

    # Submit Button
    if st.button('Submit'):
        st.session_state.show_result = True
        st.session_state.total_count += 1
        evaluate_answers()

# Display the score
st.write(f"**Score:** {st.session_state.correct_count}/{st.session_state.total_count}")

if st.session_state.total_count > 0:
    progress = st.session_state.correct_count / st.session_state.total_count
    st.progress(progress)

if st.button('Reset Score'):
    st.session_state.correct_count = 0
    st.session_state.total_count = 0
    st.write("Score has been reset.")