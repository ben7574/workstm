import altair as alt
import numpy as np
import pandas as pd

import streamlit as st

# Define questions and options together
questions_and_options = [
    {
        "question": "I have finished a competition or test and I would like some feedback. I would like to have feedback:",
        "options": {
            1: "using graphs of my results.",
            2: "from somebody who talks it through with me.",
            3: "using examples from what I have done.",
            4: "using a written description of my results."
        }
    },
    {
        "question": "I want to suggest fund-raising options for a sports team. I would:",
        "options": {
            1: "list details about different options.",
            2: "question others who have been involved with fundraising.",
            3: "focus on fund-raising options that I know will work.",
            4: "compare graphs of different fund-raising options."
        }
    },
    {
        "question": "I want to learn how to take better photos. I would:",
        "options": {
            1: "use diagrams showing how different camera settings work.",
            2: "ask questions and talk about how to achieve interesting effects.",
            3: "use examples of good and poor photos showing how to improve them.",
            4: "use the written instructions about what to do."
        }
    },
    {
        "question": "I want to find out about a house or an apartment. Before visiting it, I would want:",
        "options": {
            1: "to view a video of the property.",
            2: "a discussion with the owner.",
            3: "a plan showing the rooms and a map of the area.",
            4: "a printed description of the rooms and features."
        }
    },
    {
        "question": "When I am learning I:",
        "options": {
            1: "see patterns in things.",
            2: "like to talk things through.",
            3: "use examples and applications.",
            4: "read books, articles and handouts."
        }
    },
    {
        "question": "When choosing my subjects to study, these are important for me:",
        "options": {
            1: "Working with designs, maps or charts.",
            2: "Communicating with others through discussion.",
            3: "Applying my knowledge in real situations.",
            4: "Using words well in written communications."
        }
    },
    {
        "question": "I want to assemble a wooden table that came in parts (kitset). I would learn best from:",
        "options": {
            1: "diagrams showing each stage of the assembly.",
            2: "advice from someone who has done it before.",
            3: "watching a video of a person assembling a similar table.",
            4: "written instructions that came with the parts for the table."
        }
    },
    {
        "question": "A website has a video showing how to make a special graph or chart. There is a person speaking, some lists and words describing what to do and some diagrams. I would learn most from:",
        "options": {
            1: "seeing the diagrams.",
            2: "listening.",
            3: "watching the actions.",
            4: "reading the words."
        }
    },
    {
        "question": "I have a problem with my knee. I would prefer that the doctor:",
        "options": {
            1: "showed me a diagram of what was wrong.",
            2: "described what was wrong.",
            3: "used a plastic model to show me what was wrong.",
            4: "gave me something to read to explain what was wrong."
        }
    },
    {
        "question": "I need to find the way to a shop that a friend has recommended. I would:",
        "options": {
            1: "use a map.",
            2: "ask my friend to tell me the directions.",
            3: "find out where the shop is in relation to somewhere I know.",
            4: "write down the street directions I need to remember."
        }
    },
    {
        "question": "I want to learn to do something new on a computer. I would:",
        "options": {
            1: "follow the diagrams in a manual or online.",
            2: "talk with people who know about the program.",
            3: "start using it and learn by trial and error.",
            4: "read the written instructions that came with the program."
        }
    },
    {
        "question": "When learning from the Internet I like:",
        "options": {
            1: "interesting design and visual features.",
            2: "audio channels where I can listen to podcasts or interviews.",
            3: "videos showing how to do or make things.",
            4: "interesting written descriptions, lists and explanations."
        }
    },
    {
        "question": "I prefer a presenter or a teacher who uses:",
        "options": {
            1: "diagrams, charts, maps or graphs.",
            2: "question and answer, talk, group discussion, or guest speakers.",
            3: "demonstrations, models or practical sessions.",
            4: "handouts, books, or readings."
        }
    },
    {
        "question": "After reading a play, I need to do a project. I would prefer to:",
        "options": {
            1: "act out a scene from the play.",
            2: "read a speech from the play.",
            3: "draw or sketch a scene from the play.",
            4: "write about the play."
        }
    },
    {
        "question": "I want to find out more about a tour that I am going on. I would:",
        "options": {
            1: "use a map and see where the places are.",
            2: "talk with the person who planned the tour or others who are going on the tour.",
            3: "watch videos to see if there are things I like.",
            4: "read about the tour on the itinerary."
        }
    },
    {
        "question": "I want to learn how to play a new board game or card game. I would:",
        "options": {
            1: "use the diagrams that explain the various stages, moves and strategies in the game.",
            2: "listen to somebody explaining it and ask questions.",
            3: "watch others play the game before joining in.",
            4: "read the instructions."
        }
    }]

# Learning styles mapping
learning_styles = {
    1: "Visual",
    2: "Aural",
    3: "Tactile/Kinesthetic",
    4: "Read/Write"
}


            # Display a custom message based on the highest and second-highest learning styles
            # ... (your code for custom message based on the top two results)

# ... (previous code)
# Function to calculate the learning style
# Function to calculate the learning style
def calculate_learning_style(answers):
    results = {"Visual": 0, "Aural": 0, "Tactile/Kinesthetic": 0, "Read/Write": 0}
    for answer in answers:
        # Directly map answer to learning style
        if answer in learning_styles:
            results[learning_styles[answer]] += 1
    return results

# ... (your calculate_learning_style function here)

# Initialize session state
st.session_state.setdefault('current_question', 0)
st.session_state.setdefault('answers', [0] * len(questions))

# Title of the app
st.title('Learning Style Test')

# Display only the current question
current_q_and_o = questions_and_options[st.session_state.current_question]
question = current_q_and_o["question"]
options = current_q_and_o["options"]

# Use a form to ensure answers are submitted before moving to the next question
with st.form(key=f'question_{st.session_state.current_question}'):
    st.session_state.answers[st.session_state.current_question] = st.radio(
        question, 
        list(options.keys()), 
        format_func=lambda x: options[x]
    )
    submitted = st.form_submit_button('Next')

    if submitted:
        if st.session_state.current_question < len(questions_and_options) - 1:
            # Move to the next question
            st.session_state.current_question += 1
        else:
            # Calculate and display the results after the last question
            result = calculate_learning_style(st.session_state.answers)
            st.subheader("Your Learning Style Preferences:")
            for style, count in result.items():
                st.write(f"{style}: {count}")

            # Sort the learning styles by count in descending order
            sorted_styles = sorted(result.items(), key=lambda x: x[1], reverse=True)

            # Extract the top two learning styles
            top_style = sorted_styles[0]
            second_top_style = sorted_styles[1]

            # Display a custom message based on the highest and second-highest learning styles
            message = f"You have the highest count in {top_style[0]} learning ({top_style[1]} counts) and the second-highest in {second_top_style[0]} learning ({second_top_style[1]} counts)."
            
            # You can add more specific advice or career guidance based on top_style[0] and second_top_style[0]
            # For example:
            if top_style[0] == "Visual" and second_top_style[0] == "Aural":
                message += " This combination is suitable for careers that involve visual and auditory skills, such as graphic design or music production."
            # Add more conditions as needed for other combinations

            st.subheader("Custom Career Advice Based on Learning Style:")
            st.write(message)
