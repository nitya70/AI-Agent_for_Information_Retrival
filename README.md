# AI-Agent_for_Information_Retrival


1. Open a terminal in the root directory (project_root).
            Run the following command to install dependencies:
            bash
            pip install -r requirements.txt
            Add API Keys:

            Open the .env file located in the root directory.
            Add your API keys for SerpAPI and OpenAI:

                  SERPAPI_KEY=your_serpapi_api_key
                  OPENAI_API_KEY=your_openai_api_key
2. Running the Application
            Launch the Streamlit Dashboard:

            In the terminal, run:
            bash
            Copy code
            streamlit run app/app.py
            This will open the application in your default browser.
            Interacting with the Dashboard:

            Upload CSV:
            Click the "Browse" button to upload a CSV file.
            Ensure the file contains at least one column with the entities you want to query.
            Google Sheets Connection:
            If working with Google Sheets, enter your sheet ID and range (e.g., Sheet1!A1:B10).
            Upload your Google credentials JSON file for authorization.
            Select Query Options:

            Choose the main column from the uploaded file or connected Google Sheet.
            Enter a custom prompt with placeholders, e.g.,:
            plaintext
            Copy code
            Get me the email and address of {company}.
            Run Queries:

            Click the Run Queries button.
            The app will:
            Perform web searches for each entity in the column.
            Extract the requested information using the language model (LLM).
3. Viewing and Exporting Results
View Results:

         Extracted results will be displayed in a table on the dashboard.
         Download Results:

         Click the Download Results as CSV button to save the output.
         Update Google Sheets:

If connected to Google Sheets, click Write to Google Sheets to upload the results directly.
4. Optional Features
      Use Batch Mode for large datasets:
      Specify the batch size to process data in smaller chunks.
      Monitor progress with the progress bar displayed on the dashboard.
      Use advanced query templates to extract multiple fields in a single prompt.




Troubleshooting
      API Errors:
            Ensure valid API keys in the .env file.
            Verify that your API subscription supports the required number of requests.
      Google Sheets Issues:
            Confirm the sheet ID, range, and JSON credentials are correct.
            Check Google Sheets API limits if the app fails to write data back.
      LLM Errors:
            Ensure your OpenAI account has sufficient token allowance.
            Retry queries if failures occur due to temporary outages.




