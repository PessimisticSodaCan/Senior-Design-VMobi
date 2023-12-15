# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
# Import libraries
import os
import concurrent.futures
from GoogleImageScraper import GoogleImageScraper
from patch import webdriver_executable


def worker_thread(search_key):
    image_scraper = GoogleImageScraper(
        webdriver_path,
        image_path,
        search_key,
        number_of_images,
        headless,
        min_resolution,
        max_resolution,
        max_missed)
    image_urls = image_scraper.find_image_urls()
    #image_scraper.save_images(image_urls, keep_filenames)

    # Release resources
    del image_scraper


if __name__ == "__main__":
    # Define file path
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))
    search_keys = ["person", "elephant", "wine glass", "dining table", "bicycle", "bear", "cup", "toilet", "car",
                   "fork", "tv monitor", "motor bike", "knife", "laptop", "airplane", "backpack", "spoon", "mouse",
                   "bus", "umbrella", "bowl", "remote", "train", "handbag", "banana", "keyboard", "truck", "tie",
                   "apple", "cell phone", "boat", "suitcase", "sandwich", "microwave", "traffic light", "orange",
                   "oven", "fire hydrant", "broccoli", "toaster", "stop sign", "carrot", "sink", "parking meter",
                   "sports ball", "hot dog", "refrigerator", "bench", "pizza", "book", "bird", "baseball", "bat",
                   "donut", "clock", "cat", "baseball glove", "cake", "vase", "dog", "skateboard", "chair", "scissors",
                   "horse", "surfboard", "sofa", "sheep", "tennis racket", "potted plant", "cow", "bottle", "bed",
                   "tooth brush"]
    size = len(search_keys)
    # Parameters
    number_of_images = 10  # Desired number of images
    headless = True  # True = No Chrome GUI
    min_resolution = (0, 0)  # Minimum desired image resolution
    max_resolution = (9999, 9999)  # Maximum desired image resolution
    max_missed = 10  # Max number of failed images before exit
    number_of_workers = size  # Number of "workers" used
    keep_filenames = False  # Keep original URL image filenames

    for search_key in search_keys[25:]:
        image_scraper = GoogleImageScraper(webdriver_path, image_path, search_key, number_of_images, headless,
                                           min_resolution, max_resolution)
        image_urls = image_scraper.find_image_urls()
        # image_scraper.save_images(image_urls)

    # Run each search_key in a separate thread
    # Automatically waits for all threads to finish
    # Removes duplicate strings from search_keys
#    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_workers) as executor:
 #       executor.map(worker_thread, search_keys)
