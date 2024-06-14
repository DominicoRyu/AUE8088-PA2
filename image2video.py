import os
import cv2
import argparse
from pathlib import Path

# python image2video.py --image_folder runs/detect/adamw --output_video yolo5n_adamw_output.mp4 --fps 30 --img_format jpg


def images_to_video(image_folder, output_video, fps=30, img_format='jpg'):
    images = [img for img in os.listdir(image_folder) if img.endswith(f".{img_format}")]
    images.sort()  # Ensure images are sorted in the correct order
    
    if len(images) == 0:
        raise ValueError("No images found in the specified folder")

    # Read the first image to get the dimensions
    first_image_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_image_path)
    height, width, layers = frame.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for mp4
    video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    for image in images:
        image_path = os.path.join(image_folder, image)
        frame = cv2.imread(image_path)
        video.write(frame)

    video.release()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert images to video")
    parser.add_argument('--image_folder', type=str, required=True, help="Folder containing the images")
    parser.add_argument('--output_video', type=str, required=True, help="Output video file path")
    parser.add_argument('--fps', type=int, default=30, help="Frames per second for the video")
    parser.add_argument('--img_format', type=str, default='jpg', help="Image format (e.g., jpg, png)")

    args = parser.parse_args()
    images_to_video(args.image_folder, args.output_video, args.fps, args.img_format)
