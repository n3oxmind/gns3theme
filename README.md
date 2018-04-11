		
# gns3theme

gns3theme is a shell script that will apply a custom stylesheet to gns3-gui, all the ui files has been themed with stylesheet using QT Designer. This script will provide a way to change any color of the gns3-gui. Here is some features:
- Change gns3 theme from a predefined schemes 
- Change ethernet/serial link width and color
- Change grid size and color (Smoother snap to grid)
- Apply transparency to gns3-gui
- Create a custom theme.

### List gns3 color schemes
```
./gns3theme.sh -l
scheme-template:  bg      bg2     fg      fg2     tbg     sbg     sfg     bbg     bfg     color
solarized-light:  #fdf6e3 #eee8d5 #657b83 #0087ff #eee8d5 #0087ff #e4e4e4 #d70000 #1d2021 light
solarized-dark:   #002b36 #073642 #839496 #0087ff #073642 #d75f00 #1c1c1c #8a8a8a #1d2021 dark
gruvbox-light:    #fbf1c7 #ebdbb2 #282828 #458588 #d5c4a1 #076678 #f9f5d7 #cc241d #3c3836 light
gruvbox-dark:     #282828 #3c3836 #ebdbb2 #fe8019 #3c3836 #fb4934 #32302f #458588 #1d2021 dark
tomorrow:         #ffffff #f2f2f2 #4d4d4d #0087ff #cccccc #d6d6d6 #4271ae #3e999f #ffffff light
tomorrow-night:   #ffffff #f2f2f2 #4d4d4d #0087ff #cccccc #d6d6d6 #4271ae #3e999f #ffffff dark
n30x-dark3:       #252525 #2a2a2a #939393 #b7855f #2d2d2d #323232 #b7855f #c2185b #1a1a1a dark
```

### Install tomorrow  theme
```
./gns3theme.sh --scheme tomorrow 
./gns3theme.sh --scheme tomorrow --opacity 0.95    # optional: apply transparency
```
![tomorrow](https://user-images.githubusercontent.com/10103340/38634778-6149a8e4-3d78-11e8-951d-ad65ccd43901.png)

### Install solarized-light theme
```
gns3theme --scheme solarized-light
gns3theme --scheme solarized-light --opacity 0.96    # optional: apply transparency
```
![solarized-light](https://user-images.githubusercontent.com/10103340/38635551-98d55090-3d7a-11e8-8552-68ee3891dc59.png)

### Install n30x-dark3 theme
```
./gns3theme.sh --scheme n30x-dark3
./gns3theme.sh --scheme n30x-dark3 --opacity 0.95    # optional: apply transparency
```
![n30x-dark3](https://user-images.githubusercontent.com/10103340/38636484-2955005a-3d7d-11e8-998e-08f1c5ebe95a.png)

### Install Other themes
```
Note: You can add your own schemes to schemes.txt files just follow the given format.
You basically can theme gns3 of any theme of your choice.
see `gns3theme --help` for more information
```


