import streamlit as st
from json import loads
import pandas as pd

st.markdown(
    '''
    # EXIBIDOR DE ARQUIVOS 
    
    '''
)

arquivo= st.file_uploader(
    'Uploder Arquivo',
    type = ['json','py','png','jpg','csv','wav']
)

if arquivo:
    match arquivo.type.split('/'):
        case 'image', 'jpeg' | 'png':
            st.image(arquivo)
        case 'text', 'csv':
            df = pd.read_csv(arquivo)
            st.dataframe(df)
            st.line_chart(df)
        case 'application', _:
            st.json(loads(arquivo.read()))
        case 'text', 'x-python':
            st.code(arquivo.read().decode())
        case 'audio', _:
            st.audio(arquivo)

else:
    st.error("Arquivo nao encontrado")