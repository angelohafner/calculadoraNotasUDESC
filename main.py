import numpy as np
import streamlit as st

st.title("Calculadora dos Alunos de Engenharia")
number = st.number_input("Insert a number")
number = int(number)
nota = []
for ii in range(number):
    nota.append(st.number_input(f"digite a nota {ii}:"))

nota = np.array(nota)
media_notas = nota.sum() / len(nota)
st.write(f"soma das notas = {media_notas}")

nota_minima = (5 - media_notas*0.6) / 0.4
st.write(f"nota minima exame = {nota_minima}")
