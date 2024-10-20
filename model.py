from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key


GOOGLE_API_KEY = os.getenv("GOOGLE_API")
print(GOOGLE_API_KEY)
genai.configure(api_key=GOOGLE_API_KEY)

## Function To Load Google Gemini Model and provide queries as response



prompt=[
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database has tables with various columns. The table name will be provided in the question.
    For example,
    Example 1 - How many entries of records are present in table users?, 
    the SQL command will be something like this: SELECT COUNT(*) FROM users;
    Example 2 - Tell me all the students studying in Data Science class in table students?, 
    the SQL command will be something like this: SELECT * FROM students WHERE CLASS="Data Science";
    The SQL code should not have ``` in the beginning or end and should not include the word 'sql'.
    """
]



def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text


def read_sql_data(db,qry):
    con = sqlite3.Connection(db)
    cur = con.cursor()
    cur.execute(qry)
    data = cur.fetchall()
    con.commit()
    con.close()
    return data


question = "How many rows are in the users table?"
sql_query = get_gemini_response(prompt=prompt,question=question)
print(f"Decoded Query: {sql_query}")
data = read_sql_data(db="sample.db",qry=sql_query) 
print(f"Data from query: {data}")
