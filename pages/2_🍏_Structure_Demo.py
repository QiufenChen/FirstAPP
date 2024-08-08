#!/usr/bin/env python
# Author  : KerryChen
# File    : visualize_protein_structure.py
# Time    : 2024/8/7 21:47

import py3Dmol
import streamlit as st
from stmol import render_pdb_resn, render_pdb
from stmol import showmol

########################################################################################################################
# prot_str = '1A2C,1BML,1D5M,1D5X,1D5Z,1D6E,1DEE,1E9F,1FC2,1FCC,1G4U,1GZS,1HE1,1HEZ,1HQR,1HXY,1IBX,1JBU,1JWM,1JWS'
# prot_list = prot_str.split(',')
# bcolor = st.color_picker('Pick A Color', '#89cff0')
# protein = st.selectbox('select protein', prot_list)
# style = st.selectbox('style', ['cartoon', 'line', 'cross', 'stick', 'sphere'])
# viewer = py3Dmol.view(query='pdb:'+protein)
# viewer.setStyle({style: {'color': 'spectrum'}})
# viewer.setBackgroundColor(bcolor)
# showmol(viewer, height=700, width=1000)

st.sidebar.header("Structure Demo")
st.header("Visualize Protein Structure", divider="rainbow")

tab1, tab2 = st.tabs(['Example-1 using py3Dmol', 'Example-2 using stmol'])

with tab1:
    with st.echo(code_location='below'):
        # Code Block
        prot_str = '1A2C,1BML,1D5M,1D5X,1D5Z,1D6E,1DEE,1E9F,1FC2,1FCC,1G4U,1GZS,1HE1,1HEZ,1HQR,1HXY,1IBX,1JBU,1JWM,1JWS'
        prot_list = prot_str.split(',')
        bcolor = st.color_picker('Pick A Color', '#89cff0')
        protein = st.selectbox('Select protein', prot_list)
        style = st.selectbox('style', ['cartoon', 'line', 'cross', 'stick', 'sphere'])
        xyzview = py3Dmol.view(query='pdb:' + protein)
        xyzview.setStyle({style: {'color': 'spectrum'}})
        xyzview.setBackgroundColor(bcolor)
        showmol(xyzview, height=500, width=800)


with tab2:
    with st.echo(code_location='below'):
        showmol(render_pdb_resn(viewer=render_pdb(id=protein), resn_lst=['LYS', ]))

# st.sidebar.title("View Settings")
#
# pdb_code = st.sidebar.text_input(
#         label="PDB Code",
#         value="3K8Y",
#     )
#
# hl_resi_list = st.sidebar.multiselect(label="Highlight Residues", options=list(range(1,5000)))
#
# hl_chain = st.sidebar.text_input(label="Highlight Chain", value="A")
#
# label_resi = st.sidebar.checkbox(label="Label Residues", value=True)
#
# surf_transp = st.sidebar.slider("Surface Transparency", min_value=0.0, max_value=1.0, value=0.0)
#
# hl_color = st.sidebar.text_input(label="Highlight Color", value="red")
#
# bb_color = st.sidebar.text_input(label="Backbone Color", value="lightgrey")
# lig_color = st.sidebar.text_input(label="Ligand Color", value="white")
#
# st.markdown(f"## For Example: PDB [{pdb_code.upper()}](https://www.rcsb.org/structure/{pdb_code}) (Chain {hl_chain})")
#
# ### Step 3) Py3Dmol
#
# width = 700
# height = 700
#
# cartoon_radius = 0.2
# stick_radius = 0.2
#
# view = py3Dmol.view(query=f"pdb:{pdb_code.lower()}", width=width, height=height)
#
# view.setStyle({"cartoon": {"style": "oval","color": bb_color,"thickness": cartoon_radius}})
#
# view.addSurface(py3Dmol.VDW, {"opacity": surf_transp, "color": bb_color}, {"hetflag": False})
#
# view.addStyle({"elem": "C", "hetflag": True},
#                 {"stick": {"color": lig_color, "radius": stick_radius}})
#
# view.addStyle({"hetflag": True},
#                     {"stick": {"radius": stick_radius}})
#
# for hl_resi in hl_resi_list:
#     view.addStyle({"chain": hl_chain, "resi": hl_resi, "elem": "C"},
#                     {"stick": {"color": hl_color, "radius": stick_radius}})
#
#     view.addStyle({"chain": hl_chain, "resi": hl_resi},
#                         {"stick": {"radius": stick_radius}})
#
# if label_resi:
#     for hl_resi in hl_resi_list:
#         view.addResLabels({"chain": hl_chain,"resi": hl_resi},
#         {"backgroundColor": "lightgray", "fontColor": "black", "backgroundOpacity": 0.5})
#
# showmol(view, height=height, width=width)