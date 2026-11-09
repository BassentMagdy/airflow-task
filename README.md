create codespace
Machine Type: 4-core

run
    
    echo -e "AIRFLOW_UID=$(id -u)" > .env

then
    
    mkdir -p ./dags ./logs ./plugins

then
    
    docker compose up -d

expose the 8080 port and click on link

username and password are airflow
