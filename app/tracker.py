from deep_sort_realtime.deepsort_tracker import DeepSort


class Tracker:
    def __init__(self):
        self.tracker = DeepSort(max_age=30)

    def update(self, detections, frame):
        tracks = self.tracker.update_tracks(detections, frame=frame)

        results = []

        for t in tracks:
            if not t.is_confirmed():
                continue

            x1, y1, x2, y2 = map(int, t.to_ltrb())

            results.append((x1, y1, x2, y2))

        return results