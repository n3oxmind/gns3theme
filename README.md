		
# gns3theme

gns3theme is a shell script that will apply a custom stylesheet to gns3-gui, all the ui files has been themed with stylesheet using QT Designer. This script will provide a way to change any color of the gns3-gui. Here is some features:
- Change gns3 theme from a predefined schemes 
- Change ethernet/serial link width and color
- Change grid size and color (Smoother snap to grid) [this been adopted by gns3-gui-2.1.5 and above]
- Apply full transparency to gns3-gui
- Create a custom gns3-gui theme.

### List all supported themes
```
./gns3theme.sh -l
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

### Install n30x-light theme
```
./gns3theme.sh --scheme tomorrow --opacity 0.91    # --opacity is optional 
```
![n30x-light](https://user-images.githubusercontent.com/10103340/40444984-abe11d10-5e7f-11e8-842d-e5a8d3e05966.png)

### Install tomorrow  theme
```
./gns3theme.sh --scheme tomorrow 
./gns3theme.sh --scheme tomorrow --opacity 0.95    # --opacity is optional
```
![tomorrow](https://user-images.githubusercontent.com/10103340/40444837-4de4e99e-5e7f-11e8-8f3e-2122f0ec2813.png)

### Install solarized-light theme
```
gns3theme --scheme solarized-light
gns3theme --scheme solarized-light --opacity 0.96    # --opacity is optional
```
![solarized-light](https://user-images.githubusercontent.com/10103340/40444850-596c16ca-5e7f-11e8-94dc-b0f72a3e3dde.png)

### Install n30x-dark3 theme
```
./gns3theme.sh --scheme n30x-dark3
./gns3theme.sh --scheme n30x-dark3 --opacity 0.95    # --opacity is optional
```
![n30x-dark3](https://user-images.githubusercontent.com/10103340/40444874-68f21964-5e7f-11e8-829d-2075f5d18fc6.png)

### Install Other themes
**Note**: You can add your own schemes to `schemes` file, just follow the given format inside the file.
You basically can theme gns3 of any theme of your choice.
see `gns3theme --help` for more information


