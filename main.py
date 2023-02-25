import streamlit as st
import cowsay
import pandas as pd
import re
from st_keyup import st_keyup
import random
from deta import Deta

API_KEY = st.secrets["API_KEY"]

# importing datasets
deta = Deta(API_KEY)
drive = deta.Drive("1")


@st.cache_resource
def get_file_names(_drive):
    result = _drive.list()
    all_files = result.get("names")
    paging = result.get("paging")
    last = paging.get("last") if paging else None

    while (last):
        result = _drive.list(last=last)
        all_files += result.get("names")
        paging = result.get("paging")
        last = paging.get("last") if paging else None

    return all_files


@st.cache_data
def get_dataframes(_drive, xl_names):
    dfs = []
    for xl_name in xl_names:
        large_file = _drive.get(xl_name)
        with open(xl_name, "wb+") as f:
            for chunk in large_file.iter_chunks(4096):
                f.write(chunk)

        df = pd.read_excel(xl_name, engine="openpyxl")
        dfs.append(df)

    return dfs


@st.cache_data
def load_data():
    file_names = get_file_names(drive)
    data_list = get_dataframes(drive, file_names)
    return file_names, data_list


file_names, data_list = load_data()

# Streamlit App
st.title("Gene Search 🧬")

# data_list = [pd.read_excel(file) for file in datasets]

st.sidebar.markdown('''
# Options and info
''')

search_term = st.sidebar.radio('Search for a gene by symbol or name:', ["Symbol", "Name"], index=0)

st.sidebar.markdown('''
### Tips:
* Start entering some characters to look for a gene (Rag, tnf, Itga11...)
* Switch between gene name (**chemokine (C-C motif) receptor 6**) and symbol (**Ccr6**) with buttons
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
            set["Dataset"] = file_names[i].replace(" Filtered.xlsx", "")
            set.columns = ["Gene", "Regulation", "Log2f", "Dataset"]
            results.append(set)
    return pd.concat(results, ignore_index=True, sort=False) if results else None


gene = st_keyup("", debounce=0.1)

if not gene:
    st.text(cowsay.get_output_string("cow", "Enter a gene name or symbol to search :)"))

if gene:
    results = findthing(gene)
    if results is not None:
        st.table(results)
    else:
        #animal = random.choice(cowsay.char_names)
        animal = "stegosaurus"
        st.text(cowsay.get_output_string(animal, f"No results for {gene}"))
