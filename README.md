# Bass-Treble-Booster
A pythonic script to add a layer of bass or treble over songs.

## Installation
This script uses a library called `pydub`. You can install it either in a virtualenv or pip install it directly.

`pip install pydub numpy` for direct installation of the library.

For virtualenv in the home folder:
```
# make virtualenv
cd ~
virtualenv pydub

# activate virtualenv
source ~/pydub/bin/activate
pip install pydub numpy
```

### Clone and run:
```
git clone https://github.com/nsidn98/Bass-Treble-Booster.git
cd Bass-Treble-Booster
python BassBooster.py
```

This will add a layer of bass in the file `No_roots.mp3` and save it as `No_roots_bass_boost.mp3`.

You can change the `accentuate_db` and the `attenuate_db` parameter to your liking. Do not increase `accentuate_db` too much as it makes it worse:P

## Recommendations to try out with bass boosting:
* [Strobe (Sparkee Remix)](https://www.youtube.com/watch?v=cytyAgu9-bA&ab_channel=Davie504) played by Davie504
* [The Happiest Days of Our Lives](https://www.youtube.com/watch?v=VyTarjUjNMQ) by Pink Floyd
* [Attention](https://www.youtube.com/watch?v=nfs8NYg7yQM) by Charlie Puth
* [Another One Bites the Dust](https://www.youtube.com/watch?v=rY0WxgSXdEE) by Queen
* [Can't Stop](https://www.youtube.com/watch?v=BfOdWSiyWoc) by RHCP


## Reference

[Pydub Library](https://github.com/jiaaro/pydub) by [James Robert](https://github.com/jiaaro)
