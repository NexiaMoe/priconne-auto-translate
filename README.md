# priconne-auto-translate

Auto translate textbox from Japanese to English or Indonesia

## How to use

- Install python first, Anaconda is recommended 
- Install python depedency with command: ```pip install -r requirement.txt```
- Install tesseract for windows, [Download here](https://digi.bib.uni-mannheim.de/tesseract/), select `tesseract-ocr-w64-setup-v5.0.0-alpha.20210811.exe`
- Download japanese datapack at this repository
- Copy trainneddata file to `C:\Program Files\Tesseract-OCR\tessdata`
- Run Princess Connect Re:Dive
- Run run.py with command : `python run.py --data fast --translate googleDict` or just `python run.py`

## Available command

`--data`

select japanese detection datapack.\
- `fast` is lightweight but not accurate.
- `medium` is not light but not heavy either, fairly accurate.
- `best` is heavy but it is very accurate. default is best

`--translate`

Select translator endpoint.\
- `azure` using bing translate, need API key, free is limited 2 millions of character
- `ibm` using IBM Translate, not really accurate.
- `googleModule` using googletrans module, not accurate, IP maybe blocked if too many request
- `googleDict` using google dictionary endpoint, somewhat accurate. Default is googleDict

## PR is wellcome!

Yes, I need your help to improve this program. My code is messy but at least it work.\
If there any improvement, PR is always open!

## Issue

Please open issue if there is any bug or have question!

## ToDo
- [ ] Overlay to the game.
- [ ] Improve performance with multithreading / multiprocessing
