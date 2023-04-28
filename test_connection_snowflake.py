@st.experimental_singleton
def init_connection():
return snowflake.connector.connect(user = “XXX”,
authenticator=‘externalbrowser’,
account = “XXX”,
warehouse = “XXX”,
database = “XXX”,
schema = “XXX”)

conn = init_connection()

Perform query.
Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
with conn.cursor() as cur:
cur.execute(query)
return cur.fetchall()

rows = run_query(“SELECT * from XXX;”)
