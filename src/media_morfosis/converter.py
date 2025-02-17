import os
import ffmpeg
from pathlib import Path

class Converter:
    def __init__(self, file):
        if os.path.isfile(file):
            self.file = file

    def output_file(self, extension):
        p = Path(self.file)
        return str(p.with_suffix(extension))

    def run(self, output_extension, **args):
        stream = ffmpeg.input(self.file).output(self.output_file(output_extension), **args)
        return ffmpeg.run(stream)

    def wav_to_mp3(self):
        return self.run('.mp3', acodec='mp3', y=None, vn=None, ar='44100', ac=2, id3v2_version=3, map_metadata=0, **{ 'b:a': '320k'})

    def wma_to_mp3(self):
        return self.run('.mp3', acodec='mp3', y=None, vn=None, ar='44100', ac=2, id3v2_version=3, map_metadata=0, **{ 'b:a': '320k'})

    def mp4_to_mp3(self):
        return self.run('.mp3', acodec='mp3', y=None, vn=None, ar='44100', ac=2, id3v2_version=3, map_metadata=0, **{ 'b:a': '320k'})

    def flac_to_mp3(self):
        return self.run('.mp3', acodec='mp3', y=None, vn=None, ar='44100', ac=2, id3v2_version=3, map_metadata=0, **{ 'b:a': '320k'})

    def mpeg_to_mp3(self):
        return self.run('.mp3', acodec='mp3', y=None, vn=None, ar='44100', ac=2, id3v2_version=3, map_metadata=0, **{ 'b:a': '320k'})

    def mpeg_to_avi(self):
        return self.run('.avi', vcodec='mpeg4', vtag='XVID', acodec='mp3', y=None, ar='44100', ac=2, **{ 'b:a': '128k', 'b:v': '4000k' })

    def m4a_to_mp3(self):
        return self.run('.mp3', acodec='mp3', y=None, vn=None, ar='44100', ac=2, id3v2_version=3, map_metadata=0, **{ 'b:a': '320k'})

    def flv_to_mp3(self):
        return self.run('.mp3', acodec='mp3', y=None, vn=None, ar='44100', ac=2, id3v2_version=3, map_metadata=0, **{ 'b:a': '320k'})

    def mp4_to_avi(self):
        return self.run('.avi', vcodec='mpeg4', vtag='XVID', acodec='mp3', y=None, ar='44100', ac=2, **{ 'b:a': '128k', 'b:v': '4000k' })

    def mov_to_avi(self):
        return self.run('.avi', vcodec='msmpeg4v2', acodec='pcm_u8', y=None, ac=2, **{ 'b:a': '128k', 'b:v': '4000k' })

    def mkv_to_avi(self):
        return self.run('.avi', vcodec='mpeg4', vtag='XVID', acodec='mp3', y=None, ac=2, **{ 'b:a': '128k', 'b:v': '4000k' })

    def avi_to_flv(self):
        return self.run('.flv', r='30', acodec='copy', y=None, ac=2, **{ 'b:a': '128k', 'b:v': '4000k' })

    def flv_to_mp4(self):
        return self.run('.mp4', vcodec='libx264', crf=19, strict='experimental', y=None)

