import cv2
import time


def process_video_stream(source=0):
    """
    Reads frames from a video source (webcam or video file), resizes them,
    and logs frame metadata to verify stable processing.

    source: 0 for default webcam, or a file path like "sample_video.mp4"
    """
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print(f"ERROR: Could not open video source: {source}")
        return

    print(f"Successfully opened video source: {source}")

    frame_count = 0
    start_time = time.time()

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Stream ended or frame could not be read.")
            break

        frame_count += 1

        # Resize frame to a standard width (helps consistent processing later)
        resized_frame = cv2.resize(frame, (640, 480))

        # Log frame metadata every 30 frames (roughly once a second at 30fps)
        if frame_count % 30 == 0:
            elapsed = round(time.time() - start_time, 2)
            print(f"Frame #{frame_count} | Elapsed: {elapsed}s | Shape: {resized_frame.shape}")

        # Display the frame in a window
        cv2.imshow("Consumer Attention Mapping - Stream Verification", resized_frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Stream stopped by user (pressed 'q').")
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"Total frames processed: {frame_count}")


if __name__ == "__main__":
    # source=0 uses your webcam. Replace with a file path to test a video instead,
    # e.g. process_video_stream("sample_video.mp4")
    process_video_stream(source=0)