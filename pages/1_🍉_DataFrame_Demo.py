import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from stmol import showmol, render_pdb_resn, render_pdb
import py3Dmol
# import pymysql as mysql

st.set_page_config(page_title="Dataframe Demo", page_icon="📈")
st.header("Dataframe Demo", divider="rainbow")
st.sidebar.header("Dataframe Demo")
st.write("""This demo demonstrates using Streamlit+Python to read tables from a MySQL 
            database and perform some simple analysis operations.""")

# # 数据库连接配置
# db_config = {
#     'user': 'root',
#     'password': 'tanlab4049',
#     'host': 'localhost',
#     'port': 3306,
#     'database': 'test'
# }

# # 连接数据库
# cnx = mysql.connect(**db_config)

# # SQL 查询语句, 查询user表
# query = "SELECT * FROM ak4"

# 执行SQL并读取数据
# df = pd.read_sql(query, con=cnx)

df = pd.read_csv(r'../files/AK4.csv')
df.columns = ['Accession', 'Description', 'Gene', 'MW [kDa]', 'Control', 'Case']

urls = []
prefix = "https://alphafold.com/entry/"
for idx in df['Accession']:
    url = prefix + idx
    urls.append(url)
df["Link"] = urls

##################################################################################

# 在展示数据表格之前添加介绍文本
st.markdown("""
### Tabel Introduction
The table example shown below is protein mass spectrometry data read from a local MySQL database. 
The table includes the following columns:
- **Accession**:  UniProt ID of protein.
- **Description**:  Description of protein.
- **Gene**:  Gene names corresponding to proteins.
- **MW [kDa]**:  Molecular weight of protein (in kDa).
- **Control**:  Measurement values of the control group.
- **Case**:  Measurement values of the treatment group.

You can perform specific data analysis operations by selecting the corresponding columns, let's embark on this interesting journey!
""", unsafe_allow_html=True)

st.subheader("Display Our Table", divider="rainbow")
if st.checkbox('Show total dataframe'):
    st.write(df)

# 添加交互式组件
uniprot_id_click = st.selectbox("What protein have you chosen:", df['Accession'].unique())
# 根据选择的uniprot_id筛选数据
selected_protein = df[df['Accession'] == uniprot_id_click]
expander = st.expander("Display detailed information", expanded=True)
with expander:
    # 确保Link是有效的URL
    link = selected_protein['Link'].iloc[0]
    # 创建一个可点击的链接
    st.markdown(f'More details: {link}')



########################################################################################################################
st.subheader("Display Molecular Weights", divider="rainbow")
mol_weight = df['MW [kDa]']
median_value = mol_weight.median()

plt.figure(figsize=(10, 6), dpi=600)
sns.kdeplot(mol_weight, fill=True, color='green', label='Density')
plt.axvline(median_value, color='red', linestyle='--', label=f'Median: {median_value}')
plt.title('Density Plot of Molecular Weights', fontsize=15, fontweight='bold')  # 设置图形标题
plt.xlabel('Molecular Weight (kDa)', fontsize=15, fontweight='bold')  # 设置x轴标签
plt.ylabel('Density', fontsize=15, fontweight='bold')  # 设置y轴标签
plt.legend()
st.pyplot(plt)


########################################################################################################################
st.subheader("Calculate the Log2 Fold Change", divider="rainbow")
options = st.multiselect('Please select control group and treatment group:', ['Accession', 'Description', 'Gene',
                                                                              'MW [kDa]', 'Control', 'Case', 'Link'])
print(options)
st.write('You selected:', options)
filter_df = df[options]
st.write(filter_df)


###########################################################################################################
st.markdown("""Please choose whether to calculate Log2 fold change?""")
cal_fold_change = st.checkbox('Calculate Log2 fold change')
if cal_fold_change:
    if (df['Control'] == 0).any():
        st.warning("There is a value of 0 in the Control column, unable to calculate fold change.")
    else:
        filter_df['Log2 Fold Change'] = np.log2(filter_df['Case'] / filter_df['Control'])
        st.write(filter_df)

# cnx.close()

