# [geneSearch-Streamlit](https://ivankoros-genesearch-streamlit-main-3pmql0.streamlit.app/)

### A high-performance Streamlit web app for exploring genome expression data with ease

Optimized for quick access to past and lab-specific published data, geneSearch-Streamlit enables users to unlock valuable mechanistic insights within seconds.

## Features

* **Real-time search**: With a 50ms delay, search results update dynamically as you type - no need for a submission button
* **Flexible query options**: Choose between gene symbols (e.g., "Rag1") or names (e.g., "Recombination activating 1") using radio buttons
* **Case-insensitive & substring search**: Find matches effortlessly, regardless of capitalization or substring location, e.g., "**rAg**" matches "13-3**RAG**fn2"
* **User-friendly guidance**: Cowsay ASCII art provides helpful hints and feedback on missing search results

![newanimation](genesearch-streamlit-animation.gif)

## Tech Stack

* **Streamlit**: Built and hosted entirely with Streamlit
* **Pandas**: Leveraged for data preprocessing and table/dataframe visualization
* **NumPy**: Utilized for efficient data wrangling
* **Markdown**: Integrated for seamless content formatting

## Clone and Run Locally

To run the geneSearch-Streamlit app on your local machine, follow these steps:

1. **Clone the repository**

   Open your terminal or command prompt and run the following command to clone the GitHub repository:
   ```bash
   git clone https://github.com/ivankoros/geneSearch-Streamlit.git
   ```
   
2. **Navigate to the cloned repository**

Change your working directory to the cloned repository folder:
```bash
cd geneSearch-Streamlit
```

3. **Set up a Python virtual environment (Optional, but recommended)**

Create a new virtual environment to avoid package conflicts:
MacOS:
```python
python3 -m venv venv
```
Windows/Linux:
```python
python -m venv venv
```

Activate the virtual environment:

- On Windows:

  ```
  venv\Scripts\activate
  ```
  
- On macOS/Linux:

  ```
  source venv/bin/activate
  ```

4. **Install dependencies**

Install the required packages using the following command:
```python
pip install -r requirements.txt
```


5. **Run the Streamlit app**

Start the app by running the following command:
```python
streamlit run app.py
```

Streamlit will automatically open a new browser window with the app running. If it doesn't, navigate to the provided URL (usually `http://localhost:8501`).
