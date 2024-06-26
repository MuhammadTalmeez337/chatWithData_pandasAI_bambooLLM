import streamlit as st 
import pandas as pd 
from pandasai import SmartDataframe
from pandasai.llm import BambooLLM

llm = BambooLLM(api_key='$2a$10$1XGK3zalu3yyVXEBAQDr4.g9s8.LZWy.pJ5.FRZ07tOcPR1qXMOEe')

st.set_page_config(
    page_title="Chat with Data",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Set title for the Streamlit application
st.title("Chat with your data")

st.image('charts for sreamlit.png', caption='PowerBI Dashboard')

# Function to chat with CSV data
def chat_with_csv(df,query):
    # Initialize SmartDataframe with DataFrame and LLM configuration
    pandas_ai = SmartDataframe(df, config={"llm": llm})
    # Chat with the DataFrame using the provided query
    result = pandas_ai.chat(query)
    return result


# Upload multiple CSV files
input_csvs = st.sidebar.file_uploader("Upload your Data files", type=['csv'], accept_multiple_files=True)

# Check if CSV files are uploaded
if input_csvs:
    # Select a CSV file from the uploaded files using a dropdown menu
    selected_file = st.selectbox("Select your Data file", [file.name for file in input_csvs])
    selected_index = [file.name for file in input_csvs].index(selected_file)

    #load and display the selected csv file 
    st.info("Files uploaded successfully")
    data = pd.read_csv(input_csvs[selected_index])
    st.dataframe(data.head(3),use_container_width=True)

    #Enter the query for analysis
    #st.info("Chat Below")
    input_text = st.text_area("Enter the query")

    #Perform analysis
    if st.button("Chat with data"):
        if input_text:
            st.info("Your Query: "+ input_text)
            with st.spinner("Generating response..."):
                result = chat_with_csv(data,input_text)
                st.success(result)
