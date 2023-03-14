# geneSearch-Streamlit

### A streamlit web app to access and browse genome expression past, lab-specific published data to enable mechanistic insights.
* Pandas and NumPy-wrangled data is piped through a customized, efficiently-cached Streamlit web app to allow for lightning-fast search of both gene symbols and names 

## Functionality
* No submission button - searches come up dynamically (0.05s delay) as you type
* Select radio buttons to search by gene symbol "Rag1" or name "Recombination activating 1"
* Capitalization & string location is ignored for simple, partial searches - "**rAg**" could turn up "13-3**RAG**fn2" 
* Cowsay ASCII inform where/what to type and on missing search results

## Tools used
* Created fully in Streamlit, hosted with Streamlit
* Data and process querying with Streamlit
* Pandas for preprocessing and table/dataframe visualization
* Integrated Markdown

![image](https://user-images.githubusercontent.com/61260021/223280646-a8e70d87-1e9c-48f2-adc3-b6b544ad2d85.png)
