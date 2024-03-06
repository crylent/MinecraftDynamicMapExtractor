import time
import requests
from PIL import Image
from io import BytesIO
from datetime import datetime, timedelta


def get_tile(x, y):
    r = requests.get(url + x.__str__() + "_" + y.__str__() + ".jpg", stream=True)
    if r.status_code == 200:
        return r.content
    return None


##############
# PARAMETERS #
##############
host = "http://example.com:1234"  # website address with port
world_name = "world"  # world, world_nether or world_the_end
map_name = "flat"  # flat, t (world surface), ct (world caves), nt (nether surface), st (the end surface)
zoom = 5  # 0 = most detailed, 5 = least detailed
x1 = -64  # left edge, multiple of 2^zoom
y1 = -64  # bottom edge, multiple of 2^zoom
x2 = 64  # right edge, multiple of 2^zoom
y2 = 64  # top edge, multiple of 2^zoom
delay = 0.5  # delay in seconds between requests to prevent DDoS protection from triggering
filename = "map.jpg"  # output file name

tile_width = 128
tile_height = 128

url = host + "/tiles/" + world_name + "/" + map_name + "/0_0/"
if zoom > 0:
    for i in range(zoom):
        url += "z"
    url += "_"
zoom_k = int(pow(2, zoom))

total_width = tile_width * (x2 - x1 + 1) // zoom_k
total_height = tile_height * (y2 - y1 + 1) // zoom_k

expected_duration = (x2 - x1) * (y2 - y1) // pow(zoom_k, 2) * delay
expected_end = datetime.fromtimestamp(time.time() + expected_duration).strftime("%H:%M:%S")
print("Expected duration: " + str(timedelta(seconds=expected_duration)) + " (until " + expected_end + ")")

image = Image.new('RGB', (total_width, total_height))
for X in range(x1, x2 + 1, zoom_k):
    print(str((X - x1) // zoom_k + 1) + "/" + str((x2 - x1) // zoom_k + 1))
    for Y in range(y1, y2 + 1, zoom_k):
        success = False
        while not success:
            try:
                t = time.time()
                tile = Image.open(BytesIO(get_tile(X, Y)))
                image.paste(tile, ((X - x1) * tile_width // zoom_k, (y2 - Y) * tile_height // zoom_k))
                sleep_time = delay - (time.time() - t)
                if sleep_time > 0:
                    time.sleep(sleep_time)
                success = True
            except BaseException as error:
                print(error)
                input("Connection was aborted or timed out. Press Enter to try again.")
    image.save(filename)
