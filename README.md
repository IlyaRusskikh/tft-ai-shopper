# tft-ai-shopper
tft-ai-shopper provides automatic purchasing selected champions units from list by pre trained YOLOv8 model.
## Requirements
- Windows >= 10
- GPU with CUDA [(check list here)](https://ru.wikipedia.org/wiki/CUDA "(check list here)")
- Python >= 3.12.3 (it might work with older versions)
- Added Python to PATH
- 1920x1080 resolution

## How to install
1. Download and unpack this repository or clone it  `git clone https://github.com/IlyaRusskikh/tft-ai-shopper`
2. Open project folder and launch the terminal
3. Create virtual enviroment `python -m venv .venv`
4. Install dependences `.venv\Scripts\pip install -r requirements.txt`
5. Define CUDA version installed `nvidia-smi` 
6. [Select defined CUDA version](https://pytorch.org/get-started/locally/ "Select defined CUDA version") and copy command
7. Install pytorch libraries with `.venv\Scripts\`+`copied command`

## How to use
Just launch start.bat from folder root and enjoy!

## Settings
There is some variables, that you can change in `settings.txt` inside `source` folder:
- model - name of pre trained model inside `source\models` folder
- wish_list - name of file inside `source\wish_lists` with array of units names to purchase, which can be filled by names from `source\all_names`
- wish_list_refresh_value - amount of loops before wish_list will be updated during executuion the programm
- conf - lower value of ai confidence that programm accepts as true during detection
- beforeclick_delay - amount of seconds, that will be waited after moving cursor on necessary unit
- afterclick_delay - amount of seconds, that will be waited after click on necessary unit

## Tips
- You can edit wish_list during execution of programm, but if you want to change wish_list file name in settings, you need to restart app
- You can add new model and change file name in settings (needs to restart the app)
- You can use this app legitly, because it is has not access to game memory
