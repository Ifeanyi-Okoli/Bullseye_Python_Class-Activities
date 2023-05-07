from helper.sms import SMS as sms, SMS_API_KEY
from helper.video import StreamVideo as video


class Main:
    def __init__(self, video, sms, customer) -> None:
        self.sms = sms
        self.video = video
        self.customer = customer

    def run(self):
        self.video.start()
        self.sms.send_sms("Video started")        
        
    def stream(self):
       if self.video.isComplete:
            print(self.sms.send())                                       
        
    def start(self):
        self.stream()
        return "streaming started"

if __name__ == "__main__":
    main = Main(video, sms, None)
    main.start()