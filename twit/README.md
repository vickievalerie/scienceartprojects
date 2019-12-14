## Twitter Musician

In this project, the instuments are played by twitter live feed. Different sounds are made according
to the keywords present in the twitter livestream.

## Configuring

In order for this application to work, you would need twitter app key / consumer key and secrets. You
can obtain those from twitter API by registering your own application at http://dev.twitter.com. Rename
the file `keys_sample.txt` into `keys.txt`, and fill in the values there (`keys.txt` file is not checked
into git for your convenience).

## Running

You need to make sure you have all right python dependencies installed by running

```
pip install -r requirements.txt
```

Afther that you can start the project and enjoy!
```
python ttwit.py
```
