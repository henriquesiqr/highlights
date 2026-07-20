from moviepy import VideoFileClip

class VideoEditor:

    def export(
        self,
        input_video: str,
        output_video: str,
        start: float,
        end: float,
    ):

        clip = VideoFileClip(input_video)

        highlight = clip.subclipped(start, end)

        highlight.write_videofile(
            output_video,
            codec="libx264",
            audio=False,
            logger=None,
        )

        clip.close()
        highlight.close()