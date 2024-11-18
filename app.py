import streamlit as st
import pandas as pd
from backend.google_sheets import fetch_google_sheet
from backend.web_search import search_query
from backend.llm_processing import process_with_llm

st.title("AI Agent for Information Retrieval")

# Upload a CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
data = None
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Preview of Uploaded Data:")
    st.dataframe(data)

# Google Sheets Connection
sheet_id = st.text_input("Enter Google Sheet ID (optional):")
range_name = st.text_input("Enter range (e.g., Sheet1!A1:D):")
if sheet_id and range_name:
    credentials_file = st.file_uploader("Upload Google Credentials JSON")
    if credentials_file:
        try:
            google_data = fetch_google_sheet(sheet_id, range_name, credentials_file)
            st.write("Data from Google Sheet:")
            st.dataframe(pd.DataFrame(google_data))
        except Exception as e:
            st.error(f"Error fetching Google Sheet: {e}")

# Main column selection
if data is not None or sheet_id:
    main_column = st.selectbox("Select the primary column for queries:", data.columns if data is not None else [])
    query_template = st.text_input("Enter your query template (e.g., 'Get me the email of {company}')")

    if st.button("Run Queries"):
        if main_column and query_template:
            results = []
            for entity in data[main_column] if data is not None else google_data[0]:
                query = query_template.replace("{company}", entity)
                search_results = search_query(query)
                llm_input = f"""
                Extract the required information for '{entity}' based on the query template:
                "{query_template}". 
                Web results:
                {search_results}
                """
                extracted_info = process_with_llm(llm_input)
                results.append({"Entity": entity, "Extracted Info": extracted_info})
            
            results_df = pd.DataFrame(results)
            st.write("Results:")
            st.dataframe(results_df)

            csv_file = results_df.to_csv(index=False)
            st.download_button("Download Results as CSV", csv_file, "results.csv")
