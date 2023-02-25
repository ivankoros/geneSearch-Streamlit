import streamlit as st
import cowsay
import pandas as pd
import re
from st_keyup import st_keyup
import random

pd.set_option('display.max_colwidth', None)

st.title("Gene Search 🧬")

datasets = [
    "CD IR vs CD Sham Filtered.xlsx",
    "DP IR vs DP Sham Filtered.xlsx",
    "DP Sham vs CD Sham Filtered.xlsx",
]

data_list = [pd.read_excel(file) for file in datasets]

st.sidebar.markdown('''
# Options and info
''')

search_term = st.sidebar.radio('Search for a gene by symbol or name:', ["Symbol", "Name"], index=0)

st.sidebar.markdown('''
### Tips:
* Start entering some characters to look for a gene (Rag, tnf, Itga11...)
* Switch between gene name (**chemokine (C-C motif) receptor 6**) and symbol (**Ccr6**) with buttons
* Click on the column headers to sort the results
* All filtered datasets (*filtered 11/17/2021*) are searched as you type
* Your search isn't case sensitive and is found everywhere (**paR** turns up **Sparcl1**)
* Friendly animals will guide you 🐄
''')

search_term = "Symbol" if search_term == "Symbol" else "Name"


def findthing(name):
    results = []
    for i, data in enumerate(data_list):
        set = data.loc[
            data[search_term].str.contains(name, flags=re.IGNORECASE, regex=True),
            [search_term, "SaR", "Log2f"]
        ]
        if not set.empty:
            set["Dataset"] = datasets[i].replace(" Filtered.xlsx", "")
            set.columns = ["Gene", "Regulation", "Log2f", "Dataset"]
            results.append(set)
    return pd.concat(results, ignore_index=True, sort=False) if results else None


gene = st_keyup("")

if not gene:
    st.text(cowsay.get_output_string("cow", "Enter a gene name or symbol to search :)"))

if gene:
    results = findthing(gene)
    if results is not None:
        st.dataframe(results, use_container_width=True)
    else:
        animal = random.choice(cowsay.char_names)
        st.text(cowsay.get_output_string(animal, f"No results for {gene}"))
