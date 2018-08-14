		
# gns3theme

gns3theme is a shell script that will apply a custom stylesheet to gns3-gui, all the ui files has been themed with stylesheet using QT Designer. This script will provide a way to change any color of the gns3-gui. Here is some features:
- Change gns3 theme from a predefined schemes 
- Change ethernet/serial link width and color
- Apply full transparency to gns3-gui
- Create a custom gns3-gui theme.

### List all supported themes
```sh
$ ./gns3theme.sh -l
scheme-template:  bg      bg2     fg      fg2     tbg     sbg     sfg     bbg     bfg     color
solarized-light:  #fdf6e3 #eee8d5 #657b83 #0087ff #eee8d5 #0087ff #e4e4e4 #d70000 #1d2021 light
solarized-dark:   #002b36 #073642 #839496 #0087ff #073642 #d75f00 #1c1c1c #8a8a8a #1d2021 dark
gruvbox-light:    #fbf1c7 #ebdbb2 #282828 #458588 #d5c4a1 #076678 #f9f5d7 #cc241d #3c3836 light
gruvbox-dark:     #282828 #3c3836 #ebdbb2 #fe8019 #3c3836 #fb4934 #32302f #458588 #1d2021 dark
tomorrow:         #ffffff #f2f2f2 #4d4d4d #0087ff #cccccc #d6d6d6 #4271ae #3e999f #ffffff light
tomorrow-night:   #2d2d2d #404040 #cccccc #b7855f #404040 #515151 #f2777a #f2777a #303030 dark
n30x-light:       #fafafa #eeeeee #424242 #03a9f4 #eeeeee #03a9f4 #ffffff #e91e63 #1a1a1a light
n30x-dark3:       #252525 #2a2a2a #939393 #b7855f #2d2d2d #323232 #b7855f #c2185b #1a1a1a dark
```
### Install n30x-dark3
```sh
$ ./gns3theme.sh --scheme n30x-dark3 --opacity 0.91    # --opacity is optional 
```
![n30x-dark3](https://user-images.githubusercontent.com/10103340/44069564-3681323a-9f34-11e8-9f6c-7d458b0298bf.png)

### Install solarized-light theme
```sh
$ gns3theme --scheme solarized-light
$ gns3theme --scheme solarized-light --opacity 0.96    # --opacity is optional
```
![solarized-light](https://user-images.githubusercontent.com/10103340/44070067-9d04544a-9f36-11e8-9793-e73522e9002b.png)

### Install gruvbox-light theme
```sh
$ gns3theme --scheme gruvbox-light
$ gns3theme --scheme gruvbox-light --opacity 0.96    # --opacity is optional
```
![gruvbox-light](https://user-images.githubusercontent.com/10103340/44069710-e9138df8-9f34-11e8-889b-f33b81c9c180.png)

### Install tomorrow  theme
```sh
$ ./gns3theme.sh --scheme tomorrow 
$ ./gns3theme.sh --scheme tomorrow --opacity 0.95    # --opacity is optional
```
![tomorrow-light](https://user-images.githubusercontent.com/10103340/44069498-f4c867aa-9f33-11e8-8ca1-82a26cca134e.png)

### Install n30x-light theme (transparent version)
```sh
$ ./gns3theme.sh --scheme tomorrow --opacity 0.91    # --opacity is optional 
```
![n30x-light](https://user-images.githubusercontent.com/10103340/44069475-d54f28be-9f33-11e8-8a0e-f1fc3bf889c1.png)

### Install Other themes
**Note**: You can add your own schemes to `schemes` file, just follow the given format inside the file.
You basically can theme gns3 of any theme of your choice.
see `gns3theme --help` for more information

