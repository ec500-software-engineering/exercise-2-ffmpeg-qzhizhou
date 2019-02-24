import unittest
import main


class test_ffmpeg(unittest.TestCase):
    def setUp(self):
        self.input = "video.mp4"
        self.out_480 = "480p_video.mp4"
        self.out_720 = "720p_video.mp4"

        self.ff = main.ffmpegs(3)
        self.ff.create_tasks()
        self.ff.work()

        return super().setUp()

    def test_duration(self):

        meta_in = self.ff.ffprobe(self.input)
        meta_480 = self.ff.ffprobe(self.out_480)
        meta_720 = self.ff.ffprobe(self.out_720)

        in_duration = (int)(meta_in['format']['duration'].split('.')[0])
        out_480_duaration = (int)(meta_480['format']['duration'].split('.')[0])
        out_720_duaration = (int)(meta_720['format']['duration'].split('.')[0])

        assert in_duration == out_480_duaration
        assert in_duration == out_720_duaration


if __name__ == "__main__":
    unittest.main()
