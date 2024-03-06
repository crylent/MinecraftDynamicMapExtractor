# Minecraft Dynamic Map Extractor
Script for saving [Minecraft Dynamic Map](https://www.spigotmc.org/resources/dynmap%C2%AE.274/) as high-res image.

### Parameters
| Parameter  | Description | Example or possible values |
| - | - | - |
| `host`  | Website address (where Minecraft Dynamic Map is up) with port  | `http://yourserverip:8123` |
| `world_name`  | Switch between worlds  | `world`, `world_nether`, `world_the_end` |
| `map_name` | Switch between flat and surface maps | `flat`, `t`, `ct`, `nt` for nether, `st` for the end |
| `zooom` | Quality | from `0` (most detailed) to `5` (least detailed)  |
| `x1`, `y1`, `x2`, `y2` | Left, bottom, right, top edges | Multiples of 2^`zooom` |
| `delay` | Delay in seconds between requests to prevent DDoS protection from triggering | `0.5` should be fine if not sure, but it will be pretty slow (34 minutes for high-res map in examples) |
| `filename` | Output file name | `map.jpg` |

### Examples
```
x1 = -64
y1 = -64
x2 = 64
y2 = 64
```

#### High-res map (zoom=1)
![highres](https://github.com/crylent/MinecraftDynamicMapExtractor/assets/35966912/9f538b11-7afa-4ff5-b641-8982a6a42854)

#### Low-res map (zoom=5)
![lowres](https://github.com/crylent/MinecraftDynamicMapExtractor/assets/35966912/33462aaa-7ad4-4b0c-bfbb-a45c475a11b4)
