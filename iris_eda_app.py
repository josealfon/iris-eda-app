import streamlit as st 
import pandas as pd

def main():
	""" A simple Iris EDA App """

	st.title("Iris EDA App with streamlit")
	st.subheader("Streamlit is Cool")
	df1 = pd.DataFrame({
  		'first column': [1, 2, 3, 4],
  		'second column': [10, 20, 30, 40]
})
	df1

if __name__ == '__main__':
	main()