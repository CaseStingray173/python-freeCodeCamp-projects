import cv2 as cv
import mediapipe as mp
import math
import time


class hand_detector:
    def __init__(self, mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.mode = mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode, self.max_num_hands, self.min_detection_confidence,
                                         self.min_tracking_confidence)
        self.mp_draw = mp.solutions.drawing_utils

        self.fing_tip_ids = [4, 8, 12, 16, 20]

    def find_hands(self, img, draw=True):
        img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)

        # # Prints None if no hand is detected, prints the coordinates both hands are detected
        # print(result.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for hand_lms in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, hand_lms, self.mp_hands.HAND_CONNECTIONS)
        return img

    def find_position(self, img, hand_num=0, draw=True):
        self.lms_list = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_num]
            for id, lms in enumerate(my_hand.landmark):
                h, w, c = img.shape
                # Position of the center
                cx, cy = int(lms.x * w), int(lms.y * h)
                self.lms_list.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 7, (255, 0, 0), cv.FILLED)

        return self.lms_list

    def find_pos_bbox(self, img, hand_num=0, draw=True):
        x_list = []
        y_list = []
        bbox = []
        self.lms_list = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_num]
            for id, lms in enumerate(my_hand.landmark):
                h, w, c = img.shape
                # Position of the center
                cx, cy = int(lms.x * w), int(lms.y * h)
                x_list.append(cx)
                y_list.append(cy)
                self.lms_list.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 7, (255, 0, 0), cv.FILLED)

            x_min, x_max = min(x_list), max(x_list)
            y_min, y_max = min(y_list), max(y_list)
            bbox = x_min, y_min, x_max, y_max

            if draw:
                cv.rectangle(img, (x_min - 20, y_min - 20), (x_max + 20, y_max + 20), (0, 255, 0), 2)

        return self.lms_list, bbox

    def fingers_up(self):
        fingers = []

        # Thumb
        # NOTE: To detect the thumb on right hand use ">". To detect thumb on left hand
        #       use "<"
        if self.lms_list[self.fing_tip_ids[0]][1] > self.lms_list[self.fing_tip_ids[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 Fingers
        for id in range(1, 5):
            if self.lms_list[self.fing_tip_ids[id]][2] < self.lms_list[self.fing_tip_ids[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers

    def find_distance(self, p1, p2, img, draw=True, r = 10, t = 3):
        x_1, y_1 = self.lms_list[p1][1:]
        x_2, y_2 = self.lms_list[p2][1:]
        cx, cy = (x_1 + x_2) // 2, (y_1 + y_2) // 2

        if draw:
            cv.line(img, (x_1, y_1), (x_2, y_2), (255, 0, 0), t)
            cv.circle(img, (x_1, y_1), r, (255, 0, 0), cv.FILLED)
            cv.circle(img, (x_2, y_2), r, (255, 0, 0), cv.FILLED)
            cv.circle(img, (cx, cy), r, (0, 0, 255), cv.FILLED)
        length = math.hypot(x_2 - x_1, y_2 - y_1)

        return length, img, [x_1, y_1, x_2, y_2, cx, cy]


def main():
    prev_time = 0
    cur_time = 0
    cap = cv.VideoCapture(0)
    detector = hand_detector()
    while True:
        success, img = cap.read()
        img = detector.find_hands(img)
        lms_list = detector.find_position(img)
        if len(lms_list) != 0:
            print(lms_list[4])
        cur_time = time.time()
        fps = 1 / (cur_time - prev_time)
        prev_time = cur_time

        cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv.imshow("Image", img)
        cv.waitKey(1)


if __name__ == "__main__":
    main()
