import cv2
import numpy as np
import Cards
#import time
import os


### ---- INITIALIZATION ---- ###
# Define constants and initialize variables

## Camera settings
IM_WIDTH = 1280
IM_HEIGHT = 720 
FRAME_RATE = 10

path = os.path.dirname(os.path.abspath(__file__))
query_ranks = Cards.load_ranks(path + '/Card_Query/ranks/')
query_suits = Cards.load_suits(path + '/Card_Query/suits/')

## Initialize calculated frame rate because it's calculated AFTER the first time it's displayed
frame_rate_calc = 1
freq = cv2.getTickFrequency()

## Define font to use
font = cv2.FONT_HERSHEY_SIMPLEX

def testcam(cap):
    if cap is None or not cap.isOpened():
        return False
    else:
        return True


def init_cam():
    c = 4
    cap = cv2.VideoCapture(c)
    while not testcam(cap):
        c -= 1
        cap = cv2.VideoCapture(c)
        print(c)
    return c


def rescale_frame(frame, percent=75):
    scale_percent = 75
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


def run():

    cap = cv2.VideoCapture(init_cam())

    while True:

        #########Camera###########
        ret, frame = cap.read()

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        frame_blur = cv2.medianBlur(frame_gray, 5)

        frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        white = np.array([127, 127, 127])
        black = np.array([255, 255, 155])

        frame_thres = cv2.inRange(frame_gray, 127, 255)
        #frame_thres = Cards.preprocess_image(frame)


        ###################

        ######Poker Logic#######

        # Find and sort the contours of all cards in the image (query cards)
        cnts_sort, cnt_is_card = Cards.find_cards(frame_thres)

        # If there are no contours, do nothing
        if len(cnts_sort) != 0:

            # Initialize a new "cards" list to assign the card objects.
            # k indexes the newly made array of cards.
            cards = []
            k = 0

            # For each contour detected:
            for i in range(len(cnts_sort)):
                if cnt_is_card[i] == 1:

                    # Create a card object from the contour and append it to the list of cards.
                    # preprocess_card function takes the card contour and contour and
                    # determines the cards properties (corner points, etc). It generates a
                    # flattened 200x300 image of the card, and isolates the card's
                    # suit and rank from the image.
                    cards.append(Cards.preprocess_card(cnts_sort[i], frame))

                    # Find the best rank and suit match for the card.
                    (
                        cards[k].best_rank_match,
                        cards[k].best_suit_match,
                        cards[k].rank_diff,
                        cards[k].suit_diff,
                    ) = Cards.match_card(cards[k], query_ranks, query_suits)

                    # Draw center point and match result on the image.
                    frame = Cards.draw_results(frame, cards[k])
                    k = k + 1

            # Draw card contours on image (have to do contours all at once or
            # they do not show up properly for some reason)
            if len(cards) != 0:
                temp_cnts = []
                for i in range(len(cards)):
                    temp_cnts.append(cards[i].contour)
                cv2.drawContours(frame, temp_cnts, -1, (255, 0, 0), 2)

        # Draw framerate in the corner of the image. Framerate is calculated at the end of the main loop,
        # so the first time this runs, framerate will be shown as 0.
        cv2.putText(
            frame,
            "FPS: " + str(int(frame_rate_calc)),
            (10, 26),
            font,
            0.7,
            (255, 0, 255),
            2,
            cv2.LINE_AA,
        )

        # Finally, display the image with the identified cards!
        cv2.imshow("Card Detector", frame)

        ################

        #######End#######
        cv2.imshow("frame", frame)
        cv2.imshow("frame_thres ", frame_thres)

        if cv2.waitKey(20) & 0xFF == ord("q"):
            break
        ################

    cap.release()
    cv2.destroyAllWindows()


run()