mkdir -p ~/.streamlit/
echo "
[general]n
email = "olaide_abiola87@yahoo.com"n
" > ~/.streamlit/credentials.toml
echo "
[server]n
headless = truen
enableCORS=falsen
port = $PORTn
" > ~/.streamlit/config.toml
