mkdir -p -/.streamlit/
echo "\
[general]\n\
email= \"your-email@domani.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless=true\n\
enableCORS=false\n\
port = $port\n\
" > ~/.streamlit/config.toml