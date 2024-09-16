'''import streamlit as st

# Initialize the leaderboard as an empty dictionary
leaderboard = {}

# Function to display the leaderboard
def display_leaderboard():
    # Sort the leaderboard by score in descending order
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)

    st.write("### Leaderboard")
    st.write("-------------------")
    for rank, (player, score) in enumerate(sorted_leaderboard, start=1):
        st.write(f"{rank}. {player} - {score} points")
    st.write("-------------------")

# Function to update the leaderboard
def update_leaderboard(player, score):
    if player in leaderboard:
        leaderboard[player] += score
    else:
        leaderboard[player] = score

# Streamlit user interface
st.title("Leaderboard Application")

# Input fields for adding players and their scores
player_name = st.text_input("Player Name")
player_score = st.number_input("Score", min_value=0, step=1)

# Button to add/update the player's score
if st.button("Add/Update Score"):
    if player_name:
        update_leaderboard(player_name, player_score)
        st.success(f"Updated {player_name}'s score to {leaderboard[player_name]} points.")
    else:
        st.error("Please enter a player's name.")

# Display the leaderboard
display_leaderboard()

# Optional reset button
if st.button("Reset Leaderboard"):
    leaderboard.clear()
    st.info("Leaderboard has been reset.")'''
import streamlit as st
import pandas as pd

# Load the CSV file into a DataFrame
file_path = "fake_data.csv"  # Change this to your path if necessary
data = pd.read_csv(file_path)

# Initialize the leaderboard as an empty dictionary
leaderboard = {}

# Function to display the leaderboard
def display_leaderboard():
    # Sort the leaderboard by score in descending order
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)

    st.write("### Leaderboard")
    st.write("-------------------")
    for rank, (player, score) in enumerate(sorted_leaderboard, start=1):
        st.write(f"{rank}. {player} - {score} points")
    st.write("-------------------")

# Function to update the leaderboard
def update_leaderboard(player, score):
    if player in leaderboard:
        leaderboard[player] += score
    else:
        leaderboard[player] = score

# Streamlit user interface
st.title("Leaderboard Application")

# Load the data from the CSV file into the leaderboard
if st.button("Load Data"):
    for index, row in data.iterrows():
        update_leaderboard(row['Name'], row['Score'])
    st.success("Data loaded successfully!")

# Display the leaderboard
display_leaderboard()

# Optional reset button
if st.button("Reset Leaderboard"):
    leaderboard.clear()
    st.info("Leaderboard has been reset.")