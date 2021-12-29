import streamlit as st
import yfinance as yf
import pandas as pd
from PIL import Image
import altair as alt

img = Image.open("dna-logo.jpg")
st.image(img, use_column_width=True)

st.write("""
# Dna Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!
***
""")

st.header("Enter DNA sequence")

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG" \
                 "\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC" \
                 "\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT "

sequence = st.text_area("Sequence Input", sequence_input, height=225)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = "".join(sequence)

st.write("""
***
""")

# Prints the input DNA sequence
st.header("INPUT(DNA Query)")
sequence

# DNA nucleotide count
st.header("OUTPUT(DNA Nucleotide Count)")

st.subheader("1. Print dictionary")


def DNA_nucleotide_count(seq):
    d = dict([
        ("A", seq.count("A")),
        ("T", seq.count("T")),
        ("G", seq.count("G")),
        ("C", seq.count("C"))
    ])
    return d


X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X

st.subheader("2. Print text")
st.write("There are " + str(X["A"]) + " adenine (A)")
st.write("There are " + str(X["T"]) + " thymine (T)")
st.write("There are " + str(X["G"]) + " guanine (G)")
st.write("There are " + str(X["C"]) + " cytosine (C)")

st.subheader("3. Display DataFrame")
df = pd.DataFrame.from_dict(X, orient="index")
df = df.rename({0: "Count"}, axis="columns")
df.reset_index(inplace=True)
df = df.rename(columns={"index": "Nucleotide"})
st.write(df)

st.subheader("4. Display Bar Chart")
p = alt.Chart(df).mark_bar().encode(
    x="Nucleotide",
    y="Count"
)

p = p.properties(
    width=alt.Step(70)  # Controls the width of the bar
)
st.write(p)
