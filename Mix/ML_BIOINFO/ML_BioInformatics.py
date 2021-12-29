import pandas as pd
import numpy as np
import seaborn as sns
sns.set(style="ticks")
import matplotlib.pyplot as plt
from chembl_webresource_client.new_client import new_client
from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski

#########PART1##########
# # Target search for coronavirus
# # Basically like searching coronavirus in the search bar of the chembl website
# target = new_client.target
# target_query = target.search("coronavirus")
# targets = pd.DataFrame.from_dict(target_query)
# # print(targets)
#
# # Select and retrieve bioactivity data for SARS coronavirus 3C-like
# # proteinase(5th entry)
# selected_target = targets.target_chembl_id[4]
# # print(selected_target)
#
# # Only retrieve bioactivity data for coronavirus 3C-like proteinase (CHEMBL3927)
# activity = new_client.activity
# res = activity.filter(target_chembl_id=selected_target).filter(standard_type="IC50")
# df = pd.DataFrame.from_dict(res)
# # print(df.head(3))
# # print(df.standard_type.unique())
#
# # Saving the resulting bioactivity data to CSV file
# df.to_csv("ML_BINFO_bioacti_data.csv", index=False)
# print("Successfully written to the file")
#
# # Handling missing data
# df_2 = df[df.standard_value.notna()]
# # print(df_2)
#
# # Data pre-processing of the bioactivity data
# bioactivity_class = []
# for i in df_2.standard_value:
#     if float(i) >= 10000:
#         bioactivity_class.append("Inactive")
#     elif float(i) <= 1000:
#         bioactivity_class.append("Active")
#     else:
#         bioactivity_class.append("Intermediate")
#
# # Gets the three columns and converts them to a dataframe
# selection = ["molecule_chembl_id", "canonical_smiles", "standard_value"]
# df_3 = df_2[selection]
#
# # Concatenating the df_3 and bioactivity_class (as a series) together
# df_4 = pd.concat([df_3, pd.Series(bioactivity_class).rename("bioactivity_class")], axis=1)
# df_4.to_csv("ML_BINFO_bioacti_prepro_data.csv", index=False)
# print("Successfully written to the file")

#########PART2##########
df = pd.read_csv("ML_BINFO_bioacti_prepro_data.csv")


def lipinski(smiles, verbose=False):
    moldata = []
    for elem in smiles:
        mol = Chem.MolFromSmiles(elem)
        moldata.append(mol)

    base_data = np.arange(1, 1)
    i = 0
    for mol in moldata:
        desc_molwt = Descriptors.MolWt(mol)
        desc_mol_logp = Descriptors.MolLogP(mol)
        desc_numh_donors = Lipinski.NumHDonors(mol)
        desc_numh_acceptors = Lipinski.NumHAcceptors(mol)

        row = np.array([desc_molwt,
                        desc_mol_logp,
                        desc_numh_donors,
                        desc_numh_acceptors])

        if i == 0:
            base_data = row
        else:
            base_data = np.vstack([base_data, row])
        i = i + 1

    column_names = ["MW", "LogP", "NumHDonors", "NumHAcceptors"]
    descriptors = pd.DataFrame(data=base_data, columns=column_names)

    return descriptors


df_lipinski = lipinski(df.canonical_smiles)
df_combined = pd.concat([df, df_lipinski], axis=1)


# Convert IC50 to PIC50
def pIC50(input):
    pIC50 = []

    for i in input["standard_value_norm"]:
        molar = i * (10 ** -9)
        pIC50.append(-np.log10(molar))

    input["pIC50"]  = pIC50
    x = input.drop("standard_value_norm", 1)

    return x


def norm_value(input):
    norm = []

    for i in input["standard_value"]:
        if i > 100000000:
            i = 100000000
        norm.append(i)

    input["standard_value_norm"] = norm
    x = input.drop("standard_value", 1)

    return x


df_norm = norm_value(df_combined)
df_final = pIC50(df_norm)

# Removing the "Intermediate" bioactivity class
df_2class = df_final[df_final.bioactivity_class != "Intermediate"]

# # Frequency plot of the bioactivity classes
# plt.figure(figsize=(5.5, 5.5))
# sns.countplot(x="bioactivity_class", data=df_2class, edgecolor="black")
# plt.xlabel("Bioactivity Class", fontsize=14, fontweight="bold")
# plt.ylabel("Frequency", fontsize=14, fontweight="bold")

# # Scatter plot of MW versus LogP
# plt.figure(figsize=(6, 6))
# sns.scatterplot(x="MW", y="LogP", data=df_2class, hue="bioactivity_class", size="pIC50", edgecolor="black", alpha=0.7)
# plt.xlabel("MW", fontsize=14, fontweight="bold")
# plt.ylabel("LogP", fontsize=14, fontweight="bold")
# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)

# Box Plots pIC50 value
plt.figure(figsize=(5.5, 5.5))
sns.boxplot(x="bioactivity_class", y="pIC50", data=df_2class)
plt.xlabel("Bioactivity Class", fontsize=14, fontweight="bold")
plt.ylabel("pIC50 Value", fontsize=14, fontweight="bold")

plt.show()