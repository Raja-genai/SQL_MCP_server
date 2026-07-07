# Raja SQL MCP

![PyPI](https://img.shields.io/pypi/v/raja-sql-mcp)
![Python](https://img.shields.io/pypi/pyversions/raja-sql-mcp)
![License](https://img.shields.io/github/license/Raja-genai/SQL_MCP)

An MCP (Model Context Protocol) server for interacting with SQLite databases. This server provides tools to inspect database schemas, execute SQL queries, and perform CRUD operations, making it easy to integrate databases with AI agents and LLM-powered applications.

---

## Features

✅ Execute SQL queries

✅ List all tables in the database

✅ Inspect table schemas

✅ Execute SELECT queries

✅ Insert data dynamically

✅ Update existing records

✅ Delete records safely

✅ SQLite-based (no external database server required)

---

## Installation

```bash
pip install raja-sql-mcp
```

---

## Running the Server

```bash
sql-mcp
```

Or during development:

```bash
uv run python -m src.sql_mcp.main
```

---

## MCP Inspector Configuration

### Transport

```text
STDIO
```

### Command

```text
uv
```

### Arguments

```text
run python -m src.sql_mcp.main
```

### Working Directory

```text
/path/to/SQL_MCP
```

---

## Available Tools

### `list_tables()`

Returns all tables in the database.

Example:

```python
list_tables()
```

---

### `describe_table(table_name)`

Returns the schema of the specified table.

Example:

```python
describe_table("users")
```

---

### `execute_sql(query)`

Executes SQL queries such as:

- CREATE TABLE
- INSERT
- UPDATE
- DELETE
- DROP TABLE
- ALTER TABLE

Example:

```python
execute_sql("""
CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")
```

---

### `execute_select(query)`

Executes SELECT queries and returns rows.

Example:

```python
execute_select(
    "SELECT * FROM users"
)
```

---

### `insert_data(table_name, data)`

Insert records dynamically.

Example:

```python
insert_data(
    "users",
    {
        "name": "Raja",
        "age": 21
    }
)
```

---

### `update_data(table_name, data, condition)`

Update existing records.

Example:

```python
update_data(
    "users",
    {
        "age": 22
    },
    "id = 1"
)
```

---

### `delete_data(table_name, condition)`

Delete records matching a condition.

Example:

```python
delete_data(
    "users",
    "id = 1"
)
```

---

## Example Workflow

Create a table:

```python
execute_sql("""
CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")
```

Insert data:

```python
insert_data(
    "users",
    {
        "name": "Raja",
        "age": 20
    }
)
```

Query data:

```python
execute_select(
    "SELECT * FROM users"
)
```

Update data:

```python
update_data(
    "users",
    {
        "age": 21
    },
    "id = 1"
)
```

Delete data:

```python
delete_data(
    "users",
    "id = 1"
)
```

---

## Project Structure

```text
SQL_MCP/
│
├── src/
│   └── sql_mcp/
│       ├── __init__.py
│       ├── database.py
│       ├── tools.py
│       └── main.py
│
├── README.md
├── LICENSE
├── pyproject.toml
└── uv.lock
```

---

## Use Cases

- AI Database Agents
- Cursor-like Coding Assistants
- LLM-powered CRUD Applications
- Database Automation
- Schema Inspection Tools
- SQL Learning and Experimentation

---

## License

MIT License © 2026 Anna Vamsi Krishna Raja