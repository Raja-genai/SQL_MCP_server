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
        conn.commit()
        return "Query executed successfully"
    except Exception as e:
        return f"An unexpected error occured: {e}"
        
    

@mcp.tool()
def list_tables():
    '''Get all the tables in your Database'''
    try:
        cursor.execute("SELECT name FROM sqlite_schema WHERE type='table' AND name NOT LIKE 'sqlite_%';")
        tables = cursor.fetchall()
        return[table[0] for table in tables]
    except Exception as e:
        return f"Unexpected Error occured {e}"

@mcp.tool()
def describe_table(table_name:str):
    '''This function allows you to get schema of given table name'''
    try:
        query=f'PRAGMA table_info ("{table_name}") ;'
        cursor.execute(query)
        columns =cursor.fetchall()
        if not columns:
            return f"Table {table_name} doesn't exist"
        result = []
        for col in columns:
            result.append({
                "column": col[1],
                "type": col[2],
                "nullable": not bool(col[3]),
                "default": col[4],
                "primary_key": bool(col[5])
            })
        return result
    except Exception as e:
        return f"An Unexpected Error Occured {e}"

@mcp.tool()
def execute_select(query:str):
    '''Execute SELECT Queries and returns rows'''
    try:
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        
        result = []
        for row in rows:
            result.append(dict(zip(columns, row)))
        return result
    except Exception as e:
        return f"An Unexpected error occured {e}"
    
@mcp.tool()
def insert_data(table_name:str,data:dict):
    '''Insert Data into the table'''
    try:
        columns = ",".join(data.keys())
        placeholders = ",".join(["?"]*len(data))
        query =f"""
        INSERT INTO {table_name} ({columns})
        VALUES ({placeholders})
        """
        values = tuple(data.values())
        cursor.execute(query,values)
        conn.commit()
        return {
            "message":"Data Inserted Successfully",
            "row_id": cursor.lastrowid
        }    
    except Exception as e:
        return f"An Unexpected error occured {e}"
    
@mcp.tool()
def update_data(table_name:str,data:dict,condition:str):
    '''Update data in the Table'''
    try:
        
        if not data:
            return "No data provided to update"
        if not condition.strip():
            return "Condition cannot be empty"
        set_clause = ",".join(
            [f"{key}=?" for key in data.keys()]
        )
        query = f"""
        UPDATE {table_name} 
        SET {set_clause}
        WHERE {condition}
        """
        values= tuple(data.values())
        cursor.execute(query,values)
        conn.commit()
        return{
            "message":"Data Updated Successfully",
            "rows_updated":cursor.rowcount
        }
    except Exception as e:
        return f"An Unexpected error Occured {e}"
    

@mcp.tool()
def delete_data(table_name:str,condition:str):
    '''Delete Data from your table'''
    try:
        if not condition:
           return "Condition cannot be empty."
        query=f"""
        DELETE FROM {table_name}
        WHERE {condition}
        """
        cursor.execute(query)
        conn.commit()
        return {
            "message":"Data Deleted Successfully",
            "row_deleted":cursor.rowcount
        }
    except Exception as e:
        return f"An Unexpected error occured {e}"