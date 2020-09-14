"""
    Script to add a layer of bass or treble
"""
from pydub import AudioSegment
import numpy as np
      
def bass_line_freq(track):
    sample_track = list(track)
    # c-value
    est_mean = np.mean(sample_track)
    # a-value
    est_std = 3 * np.std(sample_track) / (np.sqrt(2))
    bass_factor = int(round((est_std - est_mean) * 0.005))
    return bass_factor

def bass_boost(filepath:str, bass:bool = True, accentuate_db:float = 2, attenuate_db:float = 0):
    """
        Add bass or treble
        Parameters:
        -----------
        filepath: str
            The filepath to the .mp3 file
        bass: bool
            True for bass boost 
            False for treble boost
        accentuate_db: float
            Amount of boosting in dB
        attenuate_db: float
            Amount of boosting in dB
    """
    filename = '_'.join(filepath.split('.')[:-1]) # remove .mp3
    print('Sampling the Audio...')
    sample = AudioSegment.from_mp3(filepath)
    print('Filtering the Audio...')
    if bass:
        filtered = sample.low_pass_filter(bass_line_freq(sample.get_array_of_samples()))
    else:
        filtered = sample.high_pass_filter(bass_line_freq(sample.get_array_of_samples()))
    print('Boosting...')
    boosted = (sample - attenuate_db).overlay(filtered + accentuate_db)
    print('Writing the file...')
    if bass:
        boosted.export(filename + '_bass_boost.mp3',format = 'mp3')
    else:
        boosted.export(filename + '_treble_boost.mp3',format = 'mp3')
            


if __name__ == "__main__":
    bass_boost('No_Roots.mp3', bass = True, accentuate_db = 2, attenuate_db = 0)