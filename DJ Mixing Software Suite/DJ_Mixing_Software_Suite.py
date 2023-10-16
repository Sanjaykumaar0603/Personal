import customtkinter as ctk
from tkinter import font as tkfont
from tkinter import *
from PIL import Image, ImageTk
from customtkinter import CTkImage
import pygame
import soundfile as sf
import librosa
from pydub import AudioSegment
import numpy as np
from scipy.signal import correlate
from scipy.signal import butter, lfilter
import random
import os
from pydub.playback import play
#import pygame as pyg

output_mixes = []
impsongs = [] #available songs
songs=[]
input_tracks = [] #input for mix
mix_count = 0
app=0
second=0

class App(ctk.CTk):
    def __init__(self):
        input_tracks.clear()
        
        mix_count=0
        ctk.CTk.__init__(self)
        ctk.set_default_color_theme("dark-blue")
        self.title("DJ Mixing Suite")
        self.geometry("730x600")
        self.configure(bg="#262626")
        self.main_font = tkfont.Font(family="Helvetica", size=12)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


        container = ctk.CTkFrame(self)
        container.grid_rowconfigure(0, weight=1)

        container.grid_columnconfigure(0, weight=1)
        container.grid(row=0, column=0, sticky="nsew")
        self.frames = {}

        for F in (SelectPage, CountPage):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(SelectPage)

    def show_frame(self, pageName):
        frame = self.frames[pageName]
        frame.tkraise()


class SelectPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.grid_rowconfigure(2,weight=1)

        self.grid_columnconfigure(0, weight=1)

        selectLabel = ctk.CTkLabel(self, text="Select Songs",)
        selectLabel.main_font= tkfont.Font(family="Helvetica", size=16)
        selectLabel.grid(row= 0,column=0,pady=10, padx=10, sticky="news")
        self.songlist_frame = SongList(self, songs)
        self.songlist_frame.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nsew")




        button = ctk.CTkButton(self, text="GO!",command=lambda: controller.show_frame(CountPage))
        button.grid(row=2, column=0, sticky="n")


# scrollable song list class

class SongList(ctk.CTkScrollableFrame):
    def __init__(self, master, values):
        super().__init__(master, label_text="Location = C:\\Users\\sanja\\Desktop\\songs\\")

        self.values = values
        self.songframes = []
      
        for i, value in enumerate(self.values):
            
            songframe = InputSongFrame(self, path=value)
            songframe.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.songframes.append(songframe)
   
        button = ctk.CTkButton(self, text="OK",command=self.getselection)
        button.grid(row=5, column=6, sticky="n")
    def getselection(self):
        
        for songframe in self.songframes:
            if songframe.checkbox.get() == 1:
                input_tracks.append(songframe.path)
        print("INPUT TRACKS:",input_tracks)


class InputSongFrame(ctk.CTkFrame):
    def __init__(self, master, path, **kwargs):
        super().__init__(master, **kwargs)
        for i in impsongs:
            if path in i:
                self.path = impsongs[impsongs.index(i)]
                break
        
        self.songTitle = ctk.CTkLabel(self, text=path[:-4])
        self.songTitle.grid(row=0, sticky="nsew")
        # play/pause buttons
        #self.pauseImg = PhotoImage(file="C:\\Users\\sanja\\AppData\\Local\\Programs\\Python\\Python310\\pause.png")
        #self.pauseButton = ctk.CTkButton(self, image=self.pauseImg, text="", command=self.pause_song)
        self.pauseButton = ctk.CTkButton(self, text="Pause", command=self.pause_song)
        self.pauseButton.grid(row=1, column=1, sticky="ns")
        #self.playImg =PhotoImage(file="C:\\Users\\sanja\\AppData\\Local\\Programs\\Python\\Python310\\play.png")
        #self.playButton = ctk.CTkButton(self, image=self.playImg, text="", command=self.play_song)
        self.playButton = ctk.CTkButton(self, text="Play", command=self.play_song)
        self.playButton.grid(row=1, column=0, sticky="ns")

        self.loadButton = ctk.CTkButton(self, text="Load", command=self.load)
        self.loadButton.grid(row=1, column=6, sticky="ns")

        
        self.selected_string = ctk.StringVar(value="select?")
        
        self.checkbox = ctk.CTkCheckBox(master=self, textvariable=self.selected_string)
        self.checkbox.grid(row=1, column=2, sticky="nsew")
        pygame.mixer.init()
        #self.sound = pygame.mixer.Sound(self.path)
        #self.sound.play()
        #pygame.mixer.pause()
    def play_song(self):
        pygame.mixer.unpause()
        

    def pause_song(self):
        pygame.mixer.pause()
        
    def load(self):
        pygame.mixer.quit()
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(self.path)
        self.sound.play()
        pygame.mixer.pause()
 

class CountPage(ctk.CTkFrame):
    global mix_count
    def __init__(self,parent, controller, **kwargs):
        super().__init__(parent, **kwargs)
        self.grid(sticky="news")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.controller=controller
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.mixes_label = ctk.CTkLabel(self, text="Enter number of mixes")
        self.mixes_label.grid(row=0, sticky="news")
        self.no_mixes = ctk.StringVar(self)
        self.no_mixes_entry = ctk.CTkEntry(master=self, textvariable=self.no_mixes)
        self.no_mixes_entry.grid(row=1, sticky="n")

        self.nextpage_button = ctk.CTkButton(self, text="Generate mixes", command=self.output_trigger)
        self.nextpage_button.grid(row=2, sticky="n")

    def output_trigger(self):
        nn = self.no_mixes.get()
        if(nn=="" or "0" in nn):
            mix_count=1
        else:
            mix_count=int(nn)
        print(mix_count)
        input_tracks.append(mix_count)
        self.next_page_operator()

    def next_page_operator(self):
        app.destroy()
        pass


class OutputPage(ctk.CTk):

    def __init__(self):
        ctk.CTk.__init__(self)
        ctk.set_default_color_theme("dark-blue")
        self.title("DJ Mixing Suite")
        self.geometry("600x700")
        self.configure(bg="#262626")
        self.main_font = tkfont.Font(family="Helvetica", size=12)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


        container = ctk.CTkFrame(self)
        container.grid_rowconfigure(0, weight=1)

        container.grid_columnconfigure(0, weight=1)
        container.grid(row=0, column=0, sticky="nsew")

        self.frames = {}

        frame = ShowPage(container, self)

        self.frames[ShowPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(ShowPage)

    def show_frame(self, pageName):
        frame = self.frames[pageName]
        frame.tkraise()
        
class ShowPage(ctk.CTkFrame):
    global output_mixes
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.grid_rowconfigure(2,weight=1)

        self.grid_columnconfigure(0, weight=1)

        selectLabel = ctk.CTkLabel(self, text="Mixes",)
        selectLabel.main_font= tkfont.Font(family="Helvetica", size=16)
        selectLabel.grid(row= 0,column=0,pady=10, padx=10, sticky="news")
        self.songlist_frame = MixList(self,output_mixes)
        self.songlist_frame.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nsew")




        button = ctk.CTkButton(self, text="BACK",command=start)
        button.grid(row=2, column=0, sticky="n")
class MixList(ctk.CTkScrollableFrame):
    def __init__(self, master, values):
        super().__init__(master, label_text="Location = C:\\Users\\sanja\\Desktop\\songs\\")

        self.values = values
        self.songframes = []

        for i, value in enumerate(self.values):
            songframe = MixFrame(self, path=value)
            songframe.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.songframes.append(songframe)
            
class MixFrame(ctk.CTkFrame):
    def __init__(self, master, path, **kwargs):
        super().__init__(master, **kwargs)
        self.path = path
        self.songTitle = ctk.CTkLabel(self, text=path[:-4])
        self.songTitle.grid(row=0, sticky="nsew")
        # play/pause buttons
        #self.pauseImg1 = PhotoImage(file="C:\\Users\\sanja\\AppData\\Local\\Programs\\Python\\Python310\\pause.png")
        self.pauseButton1 = ctk.CTkButton(self, text="Pause", command=self.pause_song)
        self.pauseButton1.grid(row=1, column=1, sticky="ns")
        #self.playImg1 =PhotoImage(file="C:\\Users\\sanja\\AppData\\Local\\Programs\\Python\\Python310\\play.png")
        self.playButton1 = ctk.CTkButton(self, text="Play", command=self.play_song)
        self.playButton1.grid(row=1, column=0, sticky="ns")
        self.loadButton = ctk.CTkButton(self, text="Load", command=self.load)
        self.loadButton.grid(row=1, column=5, sticky="ns")
        pygame.mixer.init()

    def play_song(self):
        pygame.mixer.unpause()
        

    def pause_song(self):
        pygame.mixer.pause()
        
    def load(self):
        pygame.mixer.quit()
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(self.path)
        self.sound.play()
        pygame.mixer.pause()

def start():
    global app
    global second
    global songs
    global impsongs
    global input_tracks
    global mix_count
    global output_mixes
    songs.clear()
    output_mixes.clear()
    for i in impsongs:
        songs.append(i[i.rindex("\\")+1:])
    second.destroy()
    app = App()
    app.mainloop()
    try:
        mix_count=input_tracks.pop()
    except:
        pass
    print(mix_count)
    if(len(input_tracks)>1):
        audio_processor = AudioProcessor(input_tracks,mix_count)
        audio_processor.process_audio()
    else:
        output_mixes=input_tracks
    second = OutputPage()
    second.mainloop()


##############################################################################GUI########################################^################GUI##########################################################GUI###################################
"""--------------------------------------------------------------------------------------------------------------------^GUI^-------------------------vCODEv--------------------------------------------------------------------------------------"""


class Matcher:
    def __init__(self, audio_path1, audio_path2, output_path1, output_path2):
        self.audio_path1 = audio_path1
        self.audio_path2 = audio_path2
        self.output_path1 = output_path1
        self.output_path2 = output_path2

class BeatMatcher(Matcher):
    def __init__(self, audio_path1, audio_path2, output_path1, output_path2):
        super().__init__(audio_path1, audio_path2, output_path1, output_path2)

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
class ScaleMatcher(Matcher):
    def __init__(self, audio_path1, audio_path2, output_path1, output_path2, pitch_shift_amount=10):
        super().__init__(audio_path1, audio_path2, output_path1, output_path2)
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

class LevelBalancer:
    def __init__(self, audio_path1, audio_path2, output_path):
        self.audio_path1 = audio_path1
        self.audio_path2 = audio_path2
        self.output_path = output_path

    def balance_levels(self):
        audio1 = AudioSegment.from_wav(self.audio_path1)
        audio2 = AudioSegment.from_wav(self.audio_path2)

        audio1_adjusted = audio1 - 15
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
    global output_mixes
    global mix_count
    def __init__(self, input_paths, number):
        self.input_paths = input_paths
        self.number=number
    def process_audio(self):
        for j in range(self.number):
            random.shuffle(self.input_paths)
            arr=[]
            for i in range(0, len(self.input_paths)-1, 2):
                int_b1='C:\\Users\\sanja\\Desktop\\songs\\'+str(j)+'b1'+str(i)+'.wav'
                int_b2='C:\\Users\\sanja\\Desktop\\songs\\'+str(j)+'b2'+str(i+1)+'.wav'

                int_s1='C:\\Users\\sanja\\Desktop\\songs\\'+str(j)+'s1'+str(i)+'.wav'
                int_s2='C:\\Users\\sanja\\Desktop\\songs\\'+str(j)+'s2'+str(i)+'.wav'

                int_lb='C:\\Users\\sanja\\Desktop\\songs\\'+str(j)+'lb'+str(i)+'.wav'
                
                out_eq='C:\\Users\\sanja\\Desktop\\songs\\'+str(j)+'eq'+str(i)+'.wav'
                
                out_rev='C:\\Users\\sanja\\Desktop\\songs\\'+str(j)+'rev'+str(i)+'.wav'
                
                beat_matcher = BeatMatcher(self.input_paths[i], self.input_paths[i+1], int_b1, int_b2)
                beat_matcher.match_beats()

                scale_matcher = ScaleMatcher(int_b1, int_b2, int_s1, int_s2)
                scale_matcher.match_scale()
    

                level_balancer = LevelBalancer(int_s1, int_s2, int_lb)
                level_balancer.balance_levels()

                equalizer = Equalizer(int_lb, out_eq)
                equalizer.apply_equalization()
                
                
                revaudio = AudioSegment.from_file(out_eq)
        
                # Create a Reverb object with a decay factor
                reverb_effect = Reverb(decay=0.5)
        
                # Apply reverb to the audio
                reverb_audio = reverb_effect.apply_reverb(revaudio)
            
                # Export the reverb-affected audio to the output file
                reverb_audio.export(out_rev, format="wav")

                '''audio, sample_rate = sf.read(out_eq)
        
                # Apply Plate Reverb effect
                reverb_audio = plate_reverb(audio, sample_rate, decay=0.5, delay_range=(50, 100), num_reflections=4)
        
                # Save the reverb-affected audio to the output file
                sf.write(out_rev, reverb_audio, sample_rate)'''
                
                audioadj=AudioManipulator(out_rev)
                audioadj.increase_volume(20)
                audioadj.save(out_rev)
                arr.append(out_rev)
                
                #Removing intermediate files
                os.remove(int_b1)
                os.remove(int_b2)
                os.remove(int_s1)
                os.remove(int_s2)
                os.remove(int_lb)
                os.remove(out_eq)
                
            random.shuffle(arr)
            song_combiner = SongCombiner(arr)
            output_path='C:\\Users\\sanja\\Desktop\\songs\\output'+str(j)+'.wav'
            combined_path = song_combiner.combine_songs(output_path)
            #print("Combined Song Path:", combined_path)
            output_mixes.append(output_path)
            #Removing intermediate files
            for i in arr:
                os.remove(i)
                
        print(output_mixes)
if __name__ == "__main__":
    ml=os.listdir('C:\\Users\\sanja\\Desktop\\songs\\')
    for i in ml:
        if(i[:6]=="output"):
            continue
        else:
            impsongs.append('C:\\Users\\sanja\\Desktop\\songs\\'+i)

    second=ctk.CTk() # this is done so that when going back from outputpage to first page , the outputpage gets deleted
    start()
    second.mainloop()
    #print(len(input_paths))
    #print(input_paths)
    
























