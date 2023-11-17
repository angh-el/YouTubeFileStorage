from moviepy.editor import VideoFileClip
import numpy as np
import cv2
import YouTubeDownloader


class VideoReverter:
    def __init__(self, video_path):
        self.video_path = video_path
        self.char_to_color_map = {
            ' ': (255, 255, 255),
            '0': (255, 0, 0),
            '1': (255, 15, 0),
            '2': (255, 30, 0),
            '3': (255, 45, 0),
            '4': (255, 61, 0),
            '5': (255, 76, 0),
            '6': (255, 91, 0),
            '7': (255, 107, 0),
            '8': (255, 122, 0),
            '9': (255, 137, 0),
            'a': (255, 153, 0),
            'b': (255, 168, 0),
            'c': (255, 183, 0),
            'd': (255, 198, 0),
            'e': (255, 214, 0),
            'f': (255, 229, 0),
            'g': (255, 244, 0),
            'h': (249, 255, 0),
            'i': (234, 255, 0),
            'j': (219, 255, 0),
            'k': (203, 255, 0),
            'l': (188, 255, 0),
            'm': (173, 255, 0),
            'n': (158, 255, 0),
            'o': (142, 255, 0),
            'p': (127, 255, 0),
            'q': (112, 255, 0),
            'r': (96, 255, 0),
            's': (81, 255, 0),
            't': (66, 255, 0),
            'u': (50, 255, 0),
            'v': (35, 255, 0),
            'w': (20, 255, 0),
            'x': (5, 255, 0),
            'y': (0, 255, 10),
            'z': (0, 255, 25),
            'A': (0, 255, 40),
            'B': (0, 255, 56),
            'C': (0, 255, 71),
            'D': (0, 255, 86),
            'E': (0, 255, 102),
            'F': (0, 255, 117),
            'G': (0, 255, 132),
            'H': (0, 255, 147),
            'I': (0, 255, 163),
            'J': (0, 255, 178),
            'K': (0, 255, 193),
            'L': (0, 255, 209),
            'M': (0, 255, 224),
            'N': (0, 255, 239),
            'O': (0, 254, 255),
            'P': (0, 239, 255),
            'Q': (0, 224, 255),
            'R': (0, 209, 255),
            'S': (0, 193, 255),
            'T': (0, 178, 255),
            'U': (0, 163, 255),
            'V': (0, 147, 255),
            'W': (0, 132, 255),
            'X': (0, 117, 255),
            'Y': (0, 101, 255),
            'Z': (0, 86, 255),
            '!': (0, 71, 255),
            '"': (0, 56, 255),
            '#': (0, 40, 255),
            '$': (0, 25, 255),
            '%': (0, 10, 255),
            '&': (5, 0, 255),
            "'": (20, 0, 255),
            '(': (35, 0, 255),
            ')': (50, 0, 255),
            '*': (66, 0, 255),
            '+': (81, 0, 255),
            ',': (96, 0, 255),
            '-': (112, 0, 255),
            '.': (127, 0, 255),
            '/': (142, 0, 255),
            ':': (158, 0, 255),
            ';': (173, 0, 255),
            '<': (188, 0, 255),
            '=': (203, 0, 255),
            '>': (219, 0, 255),
            '?': (234, 0, 255),
            '@': (249, 0, 255),
            '[': (255, 0, 244),
            '\\': (255, 0, 229),
            ']': (255, 0, 214),
            '^': (255, 0, 198),
            '_': (255, 0, 183),
            '`': (255, 0, 168),
            '{': (255, 0, 152),
            '|': (255, 0, 137),
            '}': (255, 0, 122),
            '~': (255, 0, 107),
            
        }


        self.color_matching_range = 25



    def detect_colors_in_video(self):
        cap = cv2.VideoCapture(self.video_path)
        frame_time = 0.07  
        detected_characters_string = "" 

        while True:
            cap.set(cv2.CAP_PROP_POS_MSEC, frame_time * 1000)

            ret, frame = cap.read()

            if not ret:
                break

            detected_colors = self.detect_colors_in_strips(frame)


            detected_characters = self.convert_colors_to_characters(detected_colors)


            detected_characters_string += "".join(detected_characters)


            frame_time += 0.1


        cap.release()

        # print(f"Before Sterilisation: Detected characters: {detected_characters_string}")

        updated_characters_string = self.text_sterilisation(detected_characters_string)

        # print(f"After Sterilisation: {updated_characters_string}")

        self.add_to_file(updated_characters_string)


    def text_sterilisation(self, input_string):
        chars = list(input_string)


        if chars and chars[0] == "'":
            chars.pop(0)


        if chars and chars[-1] == "'":
            chars.pop()


        i = 0
        while i < len(chars):
            if chars[i] == '0' and (i == 0 or not chars[i - 1].isdigit()):
                chars[i] = ' '

            elif chars[i] == '\\' and chars[i+1] =='n' :
                chars[i] = '\n'
                chars.pop(i+1)

            elif chars[i] == '\\' and chars[i+1] == 't':
                chars[i] = '\t'
                chars.pop(i+1)

            i += 1

        updated_string = ''.join(chars)

        return updated_string



    def add_to_file(self, updated_string):
    
        with open("ReverterVideo.txt", "w", encoding="utf-8") as file:
            file.write(updated_string)
        # print("Updated New.txt")





    def detect_colors_in_strips(self, frame):
        frame_width = frame.shape[1]
        strip_width = frame_width // 10
        strip_percentage = 0.99

        detected_colors = []

        for i in range(10):
            start_x = int(i * strip_width + (strip_width * (1 - strip_percentage) / 2))
            end_x = int((i + 1) * strip_width - (strip_width * (1 - strip_percentage) / 2))

            strip = frame[:, start_x:end_x]

            strip_hsv = cv2.cvtColor(strip, cv2.COLOR_BGR2HSV)

            hist = cv2.calcHist([strip_hsv], [0], None, [256], [0, 256])

            dominant_color_index = np.argmax(hist)
            dominant_color = np.array([dominant_color_index, 255, 255], dtype=np.uint8)
            dominant_color_rgb = cv2.cvtColor(np.array([[dominant_color]], dtype=np.uint8), cv2.COLOR_HSV2RGB)[0][0]

            detected_colors.append(tuple(dominant_color_rgb))

        return detected_colors



    def closest_color(self, color):
        color = np.array(color)

        if np.array_equal(color, np.array([255, 255, 255])):
            return ' '

        closest_color = min(self.char_to_color_map.items(), key=lambda x: np.linalg.norm(np.array(x[1]) - color) if np.linalg.norm(np.array(x[1]) - color) <= self.color_matching_range else float('inf'))

        return closest_color[0]



    ## USED TO WORK
    def convert_colors_to_characters(self, colors):
        characters = []

        for color in colors:
            closest_color = self.closest_color(color)

            character = closest_color

            # print(f"Detected Color: {color}, Mapped Character: {character}")

            characters.append(character)

        return characters






# video_path = "test.mp4"
# video_path = "Muffin Recipe Colour Encoded.mp4"

# video_reverter = VideoReverter(video_path)
# video_reverter.detect_colors_in_video()



