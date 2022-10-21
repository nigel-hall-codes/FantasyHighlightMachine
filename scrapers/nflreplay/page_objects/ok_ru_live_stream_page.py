from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import requests
import cv2

class LiveStream:
    def __init__(self, driver):
        self.driver = driver


    def process_browser_log_entry(self, entry):
        response = json.loads(entry['message'])['message']
        return response


    def log_live_stream(self):
        while True:
            browser_log = self.driver.get_log('performance')
            events = [self.process_browser_log_entry(entry) for entry in browser_log]
            events = [event for event in events if 'Network.response' in event['method']]

            for e in events:
                try:
                    print(e['params']['response']['url'])
                    if e['params']['response']['url'].endswith('.ts'):
                        url = e['params']['response']['url']
                        r1 = requests.get(url, stream=True)
                        if (r1.status_code == 200):
                            with open('testvod.mpeg', 'ab') as f:
                                for chunk in r1.iter_content(chunk_size=1024):
                                    f.write(chunk)
                        else:
                            print("Received unexpected status code {}".format(r1.status_code))

                except:
                    print("No Response")

    def play_saved_footage(self):
        cap = cv2.VideoCapture('testvod.mpeg')

        # Check if camera opened successfully
        if (cap.isOpened() == False):
            print("Error opening video  file")

        # Read until video is completed
        while (cap.isOpened()):

            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:

                # Display the resulting frame
                cv2.imshow('Frame', frame)

                # Press Q on keyboard to  exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            # Break the loop
            else:
                break

        # When everything done, release
        # the video capture object
        cap.release()

        # Closes all the frames
        cv2.destroyAllWindows()

