# colors in BGR color space by OpenCV
bgr_blue  =          np.array([255, 0, 0], dtype=np.uint8)
bgr_green  =         np.array([0, 255, 0], dtype=np.uint8)
bgr_red  =           np.array([0, 0, 255], dtype=np.uint8)
bgr_cyan  =          np.array([255, 255, 0], dtype=np.uint8)
bgr_yellow  =        np.array([0, 255, 255], dtype=np.uint8)
bgr_purple  =        np.array([255, 0, 255], dtype=np.uint8)

'''
Popular CSS color trend by year
2020 - Classic Blue
rgb(52, 86, 139)

2019 - Living Coral
rgb(255, 111, 97)

2018 - Ultra Violet
rgb(107, 91, 149)

2017 Greenery
RGB(136, 176, 75)

2016 Rose Quartz
RGB(247, 202, 201)
'''

popular_colors = [
  np.array([139, 86, 52], dtype=np.uint8),
  np.array([97, 111, 255], dtype=np.uint8),
  np.array([149, 91, 107], dtype=np.uint8),
  np.array([75, 176, 136], dtype=np.uint8),
  np.array([201, 202, 247], dtype=np.uint8),
]
