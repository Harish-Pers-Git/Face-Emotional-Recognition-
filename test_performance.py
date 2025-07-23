import time
import cv2
import numpy as np
from MAIN import OptimizedFacialExpressionDetector

def test_performance():
    """
    Test the performance of the optimized facial expression detector
    """
    print("=== Performance Test ===")
    
    try:
        # Initialize detector
        print("Initializing detector...")
        detector = OptimizedFacialExpressionDetector()
        
        # Test camera capture speed
        print("Testing camera performance...")
        start_time = time.time()
        frame_count = 0
        
        # Run for 5 seconds to measure performance
        while time.time() - start_time < 5:
            ret, frame = detector.cap.read()
            if ret:
                frame_count += 1
            time.sleep(0.01)  # Small delay
        
        fps = frame_count / 5
        print(f"✅ Camera FPS: {fps:.1f}")
        
        # Test face detection speed
        print("Testing face detection...")
        ret, frame = detector.cap.read()
        if ret:
            start_time = time.time()
            faces = detector.detect_faces_optimized(frame)
            detection_time = time.time() - start_time
            print(f"✅ Face detection time: {detection_time*1000:.1f}ms")
            print(f"✅ Faces detected: {len(faces)}")
        
        print("✅ Performance test completed successfully!")
        detector.cleanup()
        
    except Exception as e:
        print(f"❌ Performance test failed: {e}")

if __name__ == "__main__":
    test_performance() 