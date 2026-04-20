import os
import pygame


class MusicPlayer:
    def __init__(self, width, height, music_folder):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Music Player")

        self.font_title = pygame.font.SysFont("arial", 32, bold=True)
        self.font_text = pygame.font.SysFont("arial", 24)
        self.font_small = pygame.font.SysFont("arial", 20)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.music_folder = os.path.join(base_dir, music_folder)

        self.playlist = self.load_playlist()
        self.current_index = 0

        self.is_playing = False
        self.track_start_ticks = 0
        self.paused_position = 0

        self.bg_color = (30, 30, 40)
        self.text_color = (240, 240, 240)
        self.accent_color = (100, 180, 255)
        self.line_color = (80, 80, 100)

        if self.playlist:
            self.load_track(self.current_index)

    def load_playlist(self):
        if not os.path.exists(self.music_folder):
            return []

        files = []
        for file_name in os.listdir(self.music_folder):
            if file_name.lower().endswith((".mp3", ".wav")):
                files.append(file_name)

        files.sort()
        return files

    def load_track(self, index):
        if not self.playlist:
            return

        track_path = os.path.join(self.music_folder, self.playlist[index])
        pygame.mixer.music.load(track_path)

    def play(self):
        if not self.playlist:
            return

        pygame.mixer.music.play()
        self.is_playing = True
        self.track_start_ticks = pygame.time.get_ticks() - self.paused_position

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.paused_position = 0

    def next_track(self):
        if not self.playlist:
            return

        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.load_track(self.current_index)
        self.paused_position = 0
        self.play()

    def previous_track(self):
        if not self.playlist:
            return

        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.load_track(self.current_index)
        self.paused_position = 0
        self.play()

    def get_current_track_name(self):
        if not self.playlist:
            return "No tracks found"
        return self.playlist[self.current_index]

    def get_track_length(self):
        if not self.playlist:
            return 0

        track_path = os.path.join(self.music_folder, self.playlist[self.current_index])
        try:
            sound = pygame.mixer.Sound(track_path)
            return sound.get_length()
        except pygame.error:
            return 0

    def get_current_position(self):
        if not self.is_playing:
            return self.paused_position / 1000

        elapsed_ms = pygame.time.get_ticks() - self.track_start_ticks
        return elapsed_ms / 1000

    def format_time(self, seconds):
        seconds = max(0, int(seconds))
        minutes = seconds // 60
        sec = seconds % 60
        return f"{minutes:02d}:{sec:02d}"

    def update(self):
        if self.is_playing:
            if not pygame.mixer.music.get_busy():
                self.next_track()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return False
                elif event.key == pygame.K_p:
                    self.play()
                elif event.key == pygame.K_s:
                    self.stop()
                elif event.key == pygame.K_n:
                    self.next_track()
                elif event.key == pygame.K_b:
                    self.previous_track()

        return True

    def draw_progress_bar(self, x, y, w, h):
        pygame.draw.rect(self.screen, self.line_color, (x, y, w, h), border_radius=6)

        total_length = self.get_track_length()
        current_pos = self.get_current_position()

        if total_length > 0:
            progress = min(current_pos / total_length, 1)
            fill_width = int(w * progress)
            pygame.draw.rect(
                self.screen,
                self.accent_color,
                (x, y, fill_width, h),
                border_radius=6
            )

    def draw(self):
        self.screen.fill(self.bg_color)

        title = self.font_title.render("Music Player", True, self.text_color)
        self.screen.blit(title, (30, 25))

        track_label = self.font_text.render("Current track:", True, self.text_color)
        self.screen.blit(track_label, (30, 90))

        track_name = self.font_text.render(self.get_current_track_name(), True, self.accent_color)
        self.screen.blit(track_name, (30, 125))

        status_text = "Playing" if self.is_playing else "Stopped"
        status = self.font_text.render(f"Status: {status_text}", True, self.text_color)
        self.screen.blit(status, (30, 175))

        self.draw_progress_bar(30, 230, 740, 22)

        current_time = self.format_time(self.get_current_position())
        total_time = self.format_time(self.get_track_length())
        time_text = self.font_small.render(f"{current_time} / {total_time}", True, self.text_color)
        self.screen.blit(time_text, (30, 265))

        controls_1 = self.font_small.render("P = Play    S = Stop    N = Next    B = Previous    Q = Quit", True, self.text_color)
        self.screen.blit(controls_1, (30, 320))

        playlist_title = self.font_small.render("Playlist:", True, self.text_color)
        self.screen.blit(playlist_title, (550, 90))

        start_y = 120
        for i, track in enumerate(self.playlist):
            color = self.accent_color if i == self.current_index else self.text_color
            item = self.font_small.render(track, True, color)
            self.screen.blit(item, (550, start_y + i * 28))

        pygame.display.flip()