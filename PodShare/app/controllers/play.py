from flask import Response


class PlayController:
    def stream(self, audio_id):
        def generate():
            with open(f"audio/{audio_id}.mp3", "rb") as f:
                data = f.read(1024)
                while data:
                    yield data
                    data = f.read(1024)

        return Response(generate(), mimetype="audio/mp3")
