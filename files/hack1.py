#D:\\Python\\tutorials\\pygame\\video\\troll\\You've been trolled.mp4
import pygame
import moviepy.editor as mp
import cv2

pygame.init()

class Hack1(object):

    def __init__(self,vid_path):
        self.vid_path=vid_path
        self.icon_img=r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\game logo\\hacking(1).PNG'
        self.icon=pygame.image.load(self.icon_img)
        self.icon_surface = pygame.Surface((32, 32))
        self.icon_surface.blit(self.icon, (0, 0))

    def main(self):
        pygame.display.set_caption("initiating hack")
        pygame.display.set_icon(self.icon_surface)
        # load the video file
        clip = mp.VideoFileClip(self.vid_path)
        video = cv2.VideoCapture(self.vid_path)
        # extract audio from the video
        audio = clip.audio

        # FPS
        clock = pygame.time.Clock()
        FPS= video.get(cv2.CAP_PROP_FPS)

        # save audio to a temporary file
        temp_audio_file = "temp_audio.wav"
        audio.write_audiofile(temp_audio_file)

        # initialize Pygame audio mixer
        pygame.mixer.init()

        # load audio file into Pygame mixer
        pygame.mixer.music.load(temp_audio_file)

        # play audio
        pygame.mixer.music.play()

        # create a Pygame window
        window = pygame.display.set_mode((clip.w, clip.h))

        # play video frames
        for frame in clip.iter_frames():
            # convert frame to Pygame surface
            surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))

            # draw surface onto the window
            window.blit(surface, (0, 0))

            # update the display
            pygame.display.update()

            # check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            clock.tick(FPS)

        # clean up
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.display.quit()
        clip.close()


