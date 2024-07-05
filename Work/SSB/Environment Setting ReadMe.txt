1. 安裝poetry

下載poetry 並將安裝檔設為環境變數
開啟powershell執行poetry

2. 下載方式

開啟powershell輸入以下指令：
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

3. 若有現成的toml檔案，安裝poetry之後，可至toml資料夾，使用powershell執行以下直令：
poetry install
跳過步驟4-7

4. 若無toml檔案，則需運行以下指令：
poetry init

5. 下載Python.exe
https://www.python.org/downloads/release/python-380/
找出執行檔路徑ex:
"C:\Users\ChrisLee\AppData\Local\Programs\Python\Python38\python.exe”

6. 使用powershell執行以下指令
poetry env use  C:\Users\ChrisLee\AppData\Local\Programs\Python\Python38\python.exe

7. 執行poetry add "package"可以安裝套件 ex: poetry add robotframework

