# Import python packages
import streamlit as st
# from snowflake.snowpark.functions import col
import requests

# Write directly to the app
st.title(":cup_with_straw: Zenas Atheleisure Store! :cup_with_straw:")
st.write(
    "Choose the item from the list!"
)

name_on_order = st.text_input("Name on Order:")
st.write("The name on your order will be:", name_on_order)

my_cnx = st.connection("snowflake")
session = my_cnx.session()
# my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'), col('SEARCH_ON'))
# st.dataframe(data=my_dataframe, use_container_width=True)
# st.stop()

# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),
# CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)
