# Bit-Byte Meme Generator


Simple python script that generates bit-byte memes in english and farsi.

## Installation
```
pipenv install
pip install -r requirements.txt
```

## Usage
```
python main.py --language fa/en
```


## Post On Twitter
You can post all generated memes on twiiter using `--twitter` switch.
make sure that all listed envs are set correctly
* TOKEN
* TOKEN_SECRET
* CONSUMER
* CONSUMER_SECRET

It will post all memes in a single thread.

```
python main.py --twitter
```

## Todo

* GUI
