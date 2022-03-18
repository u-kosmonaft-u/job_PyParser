# job_PyParser
Parsing job api for $ work
##Instuctions to use
1. Download repository:
    ```
    git clone https://github.com/u-kosmonaft-u/job_PyParser.git
    ```
2. Add configs:
    ```
    vim config.yml
    ```
    Make sure all fields are written
    
    - The section `log` is responsible for the path to the log file
    and name of the file. Make sure you write down the full or
    relative path to the file, including its name. For example like so:
    ```
    log:
      path: /var/log/pyParser_jobs.log
    ```
   - The database section is responsible for the name of the file database. You can leave the default
   - The section `telegram` is responsible for telegram api keys and chat_id. You can get these 
   values from the respective bots in the telergram app
   
   - The section `job` is responsible for the name of the vacancy
   for which there will be a request to the HeadHunter api and subsequently parsed
3. Create virtual environment
    ```
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
4. Run the app
   ```
    python3 main.py
    ```