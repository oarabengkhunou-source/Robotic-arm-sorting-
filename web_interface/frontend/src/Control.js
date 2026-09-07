import React, { useState } from "react";

const Control = () => {
  const [detectedCubes, setDetectedCubes] = useState([]);
  const [isDetecting, setIsDetecting] = useState(false);

  // Handle AI-powered cube pickup
  const handleAiPickupCube = async (color) => {
    try {
      setIsDetecting(true);

      // Get current detections from the AI backend
      const response = await fetch("http://localhost:5000/detect");
      const data = await response.json();

      // Find cubes of the requested colour
      const targetCubes = data.detections.filter(
        (cube) => cube.color === color && cube.confidence > 0.7
      );

      if (targetCubes.length === 0) {
        throw new Error(
          `No ${color} cubes detected with high confidence`
        );
      }

      // Select the most confident detection
      const bestCube = targetCubes.reduce((best, cube) =>
        cube.confidence > best.confidence ? cube : best
      );

      // Send pickup command to the robotic arm
      await fetch(
        "http://localhost:5001/pickup_cube_at_coordinates",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            x: bestCube.robot_coordinates.x,
            y: bestCube.robot_coordinates.y,
            z: bestCube.robot_coordinates.z,
            color: color,
          }),
        }
      );
    } catch (error) {
      console.error("Pickup failed:", error);
    } finally {
      setIsDetecting(false);
    }
  };

  return (
    <div>
      <h2>Robotic Arm Control</h2>

      <button
        onClick={() => handleAiPickupCube("red")}
        disabled={isDetecting}
      >
        Pick Red Cube
      </button>

      <button
        onClick={() => handleAiPickupCube("blue")}
        disabled={isDetecting}
      >
        Pick Blue Cube
      </button>

      <button
        onClick={() => handleAiPickupCube("white")}
        disabled={isDetecting}
      >
        Pick White Cube
      </button>
    </div>
  );
};

export default Control;