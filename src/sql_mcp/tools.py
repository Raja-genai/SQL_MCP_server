from fastmcp import FastMCP
from .database import conn
mcp = FastMCP()
cursor = conn.cursor()
import re
@mcp.tool()
def execute_sql(query:str):
    '''This function helps to execute an sql query'''
    try:
        cursor.execute(query)
    except Exception as e:
        return f"An unexpected error occured: {e}"
        
    return "Query executed successfully"

@mcp.tool()
def list_tables():
    try:
        cursor.execute("SELECT name FROM sqlite_schema WHERE type='table' AND name NOT LIKE 'sqlite_%';")
        tables = cursor.fetchall()
        return[table[0] for table in tables]
    except Exception as e:
        return f"Unexpected Error occured {e}"

@mcp.tool()
def describe_table(table_name:str):
    '''This function allows you to get schema of given table name'''
    query=f'PRAGMA table_info ("{table_name}") ;'
    cursor.execute(query)
    return cursor.fetchall()

@mcp.tool()
def execute_select(query:str):
    '''Execute SELECT Queries and returns rows'''
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        return f"An Unexpected error occured {e}"