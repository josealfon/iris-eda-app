import streamlit as st 
import pandas as pd

def get_data():
    #return pd.read_csv('https://datahub.io/core/gdp/r/gdp.csv')
    return pd.read_csv('~/streamlit/gdp.csv')

def main():
	""" A simple Iris EDA App """

	st.title("Iris EDA App with streamlit")
	st.subheader("Streamlit is Cool")
	df1 = pd.DataFrame({
  		'first column': [1, 2, 3, 4],
  		'second column': [10, 20, 30, 40]
})
	df1

	'# World GDP'

	df = get_data()
	df["Value"] = "$" + (df["Value"].astype(float)/1000000).round(2).astype(str) + "MM"
	min_year = int(df['Year'].min())
	max_year = int(df['Year'].max())

	countries = df['Country Name'].unique()

	'## By country'
	country = st.selectbox('Country', countries)
	df[df['Country Name'] == country]


	'## By year'
	year = st.slider('Year', min_year, max_year)
	df[df['Year'] == year]

	st.sidebar.header('About')
	st.sidebar.text('This is Streamlit Tuto')

	# Functions
	@st.cache
	def run_multiple():
		return range(100)
	st.write(run_multiple())

if __name__ == '__main__':
	main()