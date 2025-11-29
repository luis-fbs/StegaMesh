# StegaMesh
Invisible data. Visible 3D. Steganography for Wavefront OBJ

## Usage
### Hidding text
```bash
python3 main.py source.obj "text to hide" destination
```
or
```bash
python3 main.py source.obj "text to hide"
```
> This will create the file source_hidden.obj

### Extracting hidden text
```bash
python3 main.py -d source.obj
```
