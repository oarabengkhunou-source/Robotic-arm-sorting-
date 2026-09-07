import cv2
import numpy as np


class CubeDetector:
    """
    Detects and classifies coloured waste cubes
    using computer vision and HSV colour detection.
    """

    def __init__(self):
        # HSV colour ranges for different waste types
        self.color_ranges = {
            "red": {
                "lower": np.array([0, 120, 120]),
                "upper": np.array([10, 255, 255]),
                "category": "organic"
            },
            "blue": {
                "lower": np.array([100, 150, 150]),
                "upper": np.array([130, 255, 255]),
                "category": "plastic"
            },
            "white": {
                "lower": np.array([0, 0, 180]),
                "upper": np.array([180, 50, 255]),
                "category": "paper"
            }
        }

    def detect_cubes(self, frame):
        """
        Detect coloured cubes in a camera frame.
        """
        # Convert BGR image to HSV colour space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        detected_cubes = []

        # Process each configured waste colour
        for color_name, color_info in self.color_ranges.items():
            cubes = self._detect_color_cubes(
                hsv,
                frame,
                color_name,
                color_info
            )
            detected_cubes.extend(cubes)

        return detected_cubes

    def _detect_color_cubes(self, hsv, frame, color_name, color_info):
        """
        Detect objects matching a specific HSV colour range.
        """
        mask = cv2.inRange(
            hsv,
            color_info["lower"],
            color_info["upper"]
        )

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        cubes = []

        for contour in contours:
            area = cv2.contourArea(contour)

            # Ignore very small objects/noise
            if area < 500:
                continue

            x, y, w, h = cv2.boundingRect(contour)

            cubes.append({
                "color": color_name,
                "category": color_info["category"],
                "confidence": 1.0,
                "coordinates": {
                    "x": x + w // 2,
                    "y": y + h // 2
                },
                "bounding_box": {
                    "x": x,
                    "y": y,
                    "width": w,
                    "height": h
                }
            })

        return cubes