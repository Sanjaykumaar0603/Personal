import soundfile as sf
import librosa
from pydub import AudioSegment
import numpy as np
from scipy.signal import correlate
from scipy.signal import butter, lfilter
import random
import os
from pydub.playback import play
class BeatMatcher:
    def __init__(self, audio_path1, audio_path2, output_path1, output_path2):
        self.audio_path1 = audio_path1
        self.audio_path2 = audio_path2
        self.output_path1 = output_path1
        self.output_path2 = output_path2

    def match_beats(self):
        audio1, sr1 = librosa.load(self.audio_path1)
        audio2, sr2 = librosa.load(self.audio_path2)

        # Perform beat tracking
        tempo1, beat_frames1 = librosa.beat.beat_track(y=audio1, sr=sr1)
        tempo2, beat_frames2 = librosa.beat.beat_track(y=audio2, sr=sr2)

        # Calculate time-stretching factor
        stretch_factor = tempo1 / tempo2

        # Apply time-stretching to match beats
        audio1_stretched = librosa.effects.time_stretch(y=audio1, rate=stretch_factor)
        audio2_stretched = librosa.effects.time_stretch(y=audio2, rate=stretch_factor)

        sf.write(self.output_path1, audio1_stretched, sr1)
        sf.write(self.output_path2, audio2_stretched, sr2)
class ScaleMatcher:
    def __init__(self, audio_path1, audio_path2, output_path1, output_path2, pitch_shift_amount=10):
        self.audio_path1 = audio_path1
        self.audio_path2 = audio_path2
        self.output_path1 = output_path1
        self.output_path2 = output_path2
        self.pitch_shift_amount = pitch_shift_amount

    def match_scale(self):
        audio1 = AudioSegment.from_wav(self.audio_path1)
        audio2 = AudioSegment.from_wav(self.audio_path2)

        # Apply pitch shift
        audio_transposed1 = audio1.set_frame_rate(int(audio1.frame_rate * (2 ** (self.pitch_shift_amount / 12.0))))
        audio_transposed2 = audio2.set_frame_rate(int(audio2.frame_rate * (2 ** (self.pitch_shift_amount / 12.0))))

        audio_transposed1.export(self.output_path1, format='wav')
        audio_transposed2.export(self.output_path2, format='wav')
        
class AudioManipulator:
    def __init__(self, audio_file_path):
        self.audio = AudioSegment.from_file(audio_file_path)

    def increase_volume(self, gain_in_db):
        self.audio = self.audio + gain_in_db

    def save(self, output_path):
        self.audio.export(output_path, format="wav")
'''class PhaseAligner:
    def __init__(self, audio_path1, audio_path2, output_path1, output_path2):
        self.audio_path1 = audio_path1
        self.audio_path2 = audio_path2
        self.output_path1 = output_path1
        self.output_path2 = output_path2

    def align_phase(self):
        signal1, _ = librosa.load(self.audio_path1)
        signal2, _ = librosa.load(self.audio_path2)

        # Perform cross-correlation
        correlation = correlate(signal1, signal2, mode='same')

        # Find the lag with maximum correlation
        lag = np.argmax(correlation) - len(signal1) + 1

        # Apply phase alignment
        signal1_aligned = np.roll(signal1, -lag)
        signal2_aligned = np.roll(signal2, -lag)

        sf.write(self.output_path1, signal1_aligned, len(signal1))
        sf.write(self.output_path2, signal2_aligned, len(signal2))'''


class PhaseAlignment:
    def __init__(self, input_audio_path1, input_audio_path2, output_audio_path1, output_audio_path2):
        self.input_audio_path1 = input_audio_path1
        self.input_audio_path2 = input_audio_path2
        self.output_audio_path1 = output_audio_path1
        self.output_audio_path2 = output_audio_path2
        
    def align_phases(self):
        # Load the audio files
        audio1, sr1 = librosa.load(self.input_audio_path1, sr=None)
        audio2, sr2 = librosa.load(self.input_audio_path2, sr=None)

        # Ensure both audio signals have the same sample rate
        if sr1 != sr2:
            raise ValueError("Sample rates of input audio files must be the same.")

        # Set the hop length based on the shorter audio
        hop_length = min(len(audio1), len(audio2))

        # Compute the Short-Time Fourier Transforms (STFTs) of the audio signals
        stft1 = librosa.stft(audio1, hop_length=hop_length)
        stft2 = librosa.stft(audio2, hop_length=hop_length)

        # Calculate the phase difference between the two STFTs
        phase_diff = np.angle(stft2) - np.angle(stft1)

        # Reconstruct the audio using the magnitude of the second STFT and the aligned phase
        aligned_audio = librosa.istft(np.abs(stft2) * np.exp(1j * phase_diff))

        # Save the aligned audio to the output path using soundfile
        sf.write(self.output_audio_path1, aligned_audio, sr1)
        sf.write(self.output_audio_path2, aligned_audio, sr2)

class LevelBalancer:
    def __init__(self, audio_path1, audio_path2, output_path):
        self.audio_path1 = audio_path1
        self.audio_path2 = audio_path2
        self.output_path = output_path

    def balance_levels(self):
        audio1 = AudioSegment.from_wav(self.audio_path1)
        audio2 = AudioSegment.from_wav(self.audio_path2)

        audio1_adjusted = audio1 - 10
        audio2_adjusted = audio2 + 2

        combined_audio = audio1_adjusted.overlay(audio2_adjusted, position=0.5*len(audio1_adjusted))

        combined_audio.export(self.output_path, format='wav')

class Equalizer:
    def __init__(self, audio_path, output_path, cutoff_frequency=1900):
        self.audio_path = audio_path
        self.output_path = output_path
        self.cutoff_frequency = cutoff_frequency

    @staticmethod
    def lowpass_filter(cutoff, fs, order=5):
        nyquist = 0.5 * fs
        normal_cutoff = cutoff / nyquist
        b, a = butter(order, normal_cutoff, btype='high', analog=False)
        return b, a

    def apply_equalization(self):
        audio, sr = librosa.load(self.audio_path)

        # Apply the low-pass filter
        b, a = self.lowpass_filter(self.cutoff_frequency, sr)
        filtered_audio = lfilter(b, a, audio)

        sf.write(self.output_path, filtered_audio, sr)
class Reverb:
    def __init__(self, decay=0.5):
        self.decay = decay

    def apply_reverb(self, audio):
        num_samples = len(audio)
        reverb = audio.overlay(audio, loop=True)
        reverb = reverb - 10  # Adjust volume level to control reverb strength
        reverb = reverb.fade_out(int(num_samples * self.decay))
        return reverb
    
def plate_reverb(audio, sample_rate, decay=0.5, delay_range=(50, 100), num_reflections=4):
    num_samples = len(audio)
    output = np.zeros(num_samples, dtype=np.float32)

    for _ in range(num_reflections):
        delay = np.random.randint(delay_range[0], delay_range[1])
        feedback = np.random.uniform(0.4, 0.7)
        reflection = np.zeros(num_samples, dtype=np.float32)
        reflection[0] = 1.0

        for i in range(1, num_samples):
            if i - delay >= 0:
                reflection[i] = audio[i - delay] + reflection[i - 1] * feedback
            else:
                reflection[i] = reflection[i - 1] * feedback

        output += reflection

    # Normalize the output to prevent clipping
    max_amplitude = np.max(np.abs(output))
    if max_amplitude > 0:
        output /= max_amplitude

    return output

class SongCombiner:
    def __init__(self, song_paths):
        self.song_paths = song_paths

    def combine_songs(self, output_path):
        # Initialize an empty audio segment to store the combined audio
        combined_audio = AudioSegment.empty()

        # Load each song and append it to the combined audio
        for song_path in self.song_paths:
            song = AudioSegment.from_file(song_path)
            combined_audio += song

        # Export the combined audio to the specified output path
        combined_audio.export(output_path, format="wav")
        return output_path
class AudioProcessor:
    def __init__(self, input_paths, number):
        self.input_paths = input_paths
        self.number=number
    def process_audio(self):
        results=[]
        for j in range(number):
            random.shuffle(self.input_paths)
            arr=[]
            for i in range(0, len(self.input_paths)-1, 2):
                int_b1='C:\\Users\\sanja\\Desktop\\songs\\'+str(j)+'b1'+str(i)+'.wav'
                int_b2='C:\\Users\\sanja\\Desktop\\songs\\'+str(j)+'b2'+str(i+1)+'.wav'

                int_s1='C:\\Users\\sanja\\Desktop\\songs\\'+str(j)+'s1'+str(i)+'.wav'
                int_s2='C:\\Users\\sanja\\Desktop\\songs\\'+str(j)+'s2'+str(i)+'.wav'

                int_p1='C:\\Users\\sanja\\Desktop\\songs\\'+str(j)+'p1'+str(i)+'.wav'
                int_p2='C:\\Users\\sanja\\Desktop\\songs\\'+str(j)+'p2'+str(i)+'.wav'

                int_lb='C:\\Users\\sanja\\Desktop\\songs\\'+str(j)+'lb'+str(i)+'.wav'
                
                out_eq='C:\\Users\\sanja\\Desktop\\songs\\'+str(j)+'eq'+str(i)+'.wav'
                
                out_rev='C:\\Users\\sanja\\Desktop\\songs\\'+str(j)+'rev'+str(i)+'.wav'
                
                beat_matcher = BeatMatcher(self.input_paths[i], self.input_paths[i+1], int_b1, int_b2)
                beat_matcher.match_beats()

                scale_matcher = ScaleMatcher(int_b1, int_b2, int_s1, int_s2)
                scale_matcher.match_scale()
    
                phase_aligner = PhaseAlignment(int_s1, int_s2, int_p1, int_p2) # PHASE ALIGNMENT IS NOT WORKING
                phase_aligner.align_phases()

                level_balancer = LevelBalancer(int_s1, int_s2, int_lb)
                level_balancer.balance_levels()

                equalizer = Equalizer(int_lb, out_eq)
                equalizer.apply_equalization()
                
                
                '''revaudio = AudioSegment.from_file(out_eq)
        
                # Create a Reverb object with a decay factor
                reverb_effect = Reverb(decay=0.5)
        
                # Apply reverb to the audio
                reverb_audio = reverb_effect.apply_reverb(revaudio)
            
                # Export the reverb-affected audio to the output file
                reverb_audio.export(out_rev, format="wav")'''

                audio, sample_rate = sf.read(out_eq)
        
                # Apply Plate Reverb effect
                reverb_audio = plate_reverb(audio, sample_rate, decay=0.5, delay_range=(50, 100), num_reflections=4)
        
                # Save the reverb-affected audio to the output file
                sf.write(out_rev, reverb_audio, sample_rate)
                
                audioadj=AudioManipulator(out_rev)
                audioadj.increase_volume(20)
                audioadj.save(out_rev)
                arr.append(out_rev)
                
                #Removing intermediate files
                os.remove(int_b1)
                os.remove(int_b2)
                os.remove(int_s1)
                os.remove(int_s2)
                os.remove(int_p1)
                os.remove(int_p2)
                os.remove(int_lb)
                os.remove(out_eq)
                
            random.shuffle(arr)
            song_combiner = SongCombiner(arr)
            output_path='C:\\Users\\sanja\\Desktop\\songs\\output'+str(j)+'.wav'
            combined_path = song_combiner.combine_songs(output_path)
            #print("Combined Song Path:", combined_path)
            results.append(output_path)
            #Removing intermediate files
            for i in arr:
                os.remove(i)
                
        print(results)
if __name__ == "__main__":
    input_paths = [
        "C:\\Users\\sanja\\Desktop\\songs\\Firework.wav",
        "C:\\Users\\sanja\\Desktop\\songs\\The Lazy Song.wav",
        "C:\\Users\\sanja\\Desktop\\songs\\Naa Ready.wav",
        "C:\\Users\\sanja\\Desktop\\songs\\No Lie.wav"
    ]
    number=1
    audio_processor = AudioProcessor(input_paths,number)
    audio_processor.process_audio()
