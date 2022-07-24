# Pipepine to cleanup Cars data (autos.csv)
## Follow The Following Steps to Run the Script
#### Disclaimer:
- This tutorial is for Mac
- At the time of this tutorial, the python version is 3.9
- My virtual env name is ```pipeline_pacmann``` as the folder name suggested

## Steps By Steps:
1. Create python virtual env using python venv ```python3 -m venv <your_virtual_envname>```
2. Navigate to the folder named ```<your_virtual_envname>```
3. Activate the virtual env by running ```source/bin/activate```
4. Install dependencies from ```requirements.txt``` to run the script using: ```<your_virtual_envname>/bin/python3.9 -m pip3 install -r requirements.txt```
5. Make sure the csv file required (```autos.csv```) for cleaning up is under the same directory as the ```<your_virtual_envname>``` folder. **Not inside, but under the _**SAME**_ directory.**
6. Run the script from the terminal by: ```<your_virtual_envname>/bin/python3.9 script.py```