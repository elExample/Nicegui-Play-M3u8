# -*- coding: utf-8 -*-
# by: lyon
from nicegui import ui

'''

ez play m3u8 video

'''

@ui.page("/")
async def main():
    ui.add_body_html('<script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>')
    ui.add_body_html("""
    <script>
        function playHls(className, source) {
        var videos = document.getElementsByClassName(className);
        for (var i = 0; i < videos.length; i++) {
            var video = videos[i];
            if (Hls.isSupported()) {
                var hls = new Hls();
                hls.loadSource(source);
                hls.attachMedia(video);
                hls.on(Hls.Events.MANIFEST_PARSED, function() {
                    video.play();
                });
            } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
                video.src = source;
                video.addEventListener('loadedmetadata', function() {
                    video.play();
                });
            }
        }
    }
    </script>
    """)

    with ui.card().classes("w-full h-full"):
        video = ui.video(src="", autoplay=True, muted=True).classes("w-full").classes('video_label')

    def play_video():
        ui.run_javascript(
            f'playHls("video_label", "video/test.m3u8");')

    ui.button('Play', on_click=play_video)

ui.run()

