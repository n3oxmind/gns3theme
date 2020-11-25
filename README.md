		
# gns3theme

gns3theme is a shell and  python script that will add custom theme feature to gns3-gui. 
- Change gns3 theme from a predefined schemes 
- Change ethernet/serial link width and color
- Apply full transparency to gns3-gui
- Create a custom gns3-gui theme.

### List all supported themes (you can add your own)
```sh
$ ./gns3theme.sh -l
scheme-template:  bg      bg2     fg      fg2     tbg     sbg     sfg     bbg     bfg     lc      lw  gc        color
solarized-light:  #fdf6e3 #eee8d5 #657b83 #0087ff #eee8d5 #0087ff #e4e4e4 #d70000 #1d2021 #657b83 1.2 #e6e6e6   light
solarized-dark:   #002b36 #073642 #839496 #0087ff #073642 #d75f00 #1c1c1c #8a8a8a #1d2021 #839496 1.2 #003d4d   dark
gruvbox-light:    #fbf1c7 #ebdbb2 #282828 #458588 #d5c4a1 #076678 #f9f5d7 #cc241d #3c3836 #282828 1.2 #d9d9d9   light
gruvbox-dark:     #282828 #3c3836 #ebdbb2 #fe8019 #3c3836 #fb4934 #32302f #458588 #1d2021 #ebdbb2 1.2 #404040   dark
tomorrow:         #ffffff #f2f2f2 #4d4d4d #0087ff #cccccc #d6d6d6 #4271ae #3e999f #ffffff #4d4d4d 1.2 #e6e6e6   light
tomorrow-night:   #2d2d2d #404040 #cccccc #b7855f #404040 #515151 #f2777a #f2777a #303030 #cccccc 1.2 #404040   dark
n30x-light:       #fafafa #eeeeee #424242 #03a9f4 #eeeeee #03a9f4 #ffffff #e91e63 #1a1a1a #424242 1.2 #e6e6e6   light
n30x-grey:        #e0e0e0 #d9d9d9 #424242 #0288d1 #bfbfbf #0288d1 #ffffff #c4c4c4 #000000 #424242 1.2 #cccccc   light
n30x-darkw:       #252525 #2a2a2a #00997a #b7855f #404040 #323232 #9575cd #c2185b #1a1a1a #939393 1.2 #323232   dark
n30x-darker:      #0d0d0d #141414 #008066 #2979FF #181818 #000000 #BA4551 #161616 #b3b3b3 #008066 1.2 #181818   dark
n30x-darkblue:    #28283e #26263e #00997a #934806 #20203a #22223e #c46008 #24243e #00997a #939393 1.2 #32324e   dark
```
### Installation
1. Download/Clone ![gns3theme](https://github.com/n3oxmind/gns3theme/tree/master)
2. Extract gns3theme
3. cd to gns3theme directory
4. Run as root `./gns3theme.sh  --install --src /path/to/gns3-gui-version`. For transparent theme add -o option.
5. Change colorscheme as many as you want as a regular user. See below for more details on how to change colorscheme.
6. Make sure to choose the following from `Preferences->General->Interface Style`:
	* Choose `CustomLight` for light themes (this only effect toolbar icons visibility)
	* Choose `CustomDark` for dark themes	(this only effect toolbar icons visibility)


### Install n30x-dark3
```sh
$ ./gns3theme.sh --scheme n30x-dark3
```
![n30x-dark3](https://user-images.githubusercontent.com/10103340/44069564-3681323a-9f34-11e8-9f6c-7d458b0298bf.png)

### Install solarized-light theme
```sh
$ gns3theme --scheme solarized-light
```
![solarized-light](https://user-images.githubusercontent.com/10103340/44070067-9d04544a-9f36-11e8-9793-e73522e9002b.png)

### Install gruvbox-light theme
```sh
$ gns3theme --scheme gruvbox-light
```
![gruvbox-light](https://user-images.githubusercontent.com/10103340/44069710-e9138df8-9f34-11e8-889b-f33b81c9c180.png)

### Install tomorrow  theme
```sh
$ ./gns3theme.sh --scheme tomorrow 
```
![tomorrow-light](https://user-images.githubusercontent.com/10103340/44069498-f4c867aa-9f33-11e8-8ca1-82a26cca134e.png)


### Install n30x-light theme (transparent version)
```sh
$ ./gns3theme.sh --scheme tomorrow 
```
![n30x-light](https://user-images.githubusercontent.com/10103340/44069475-d54f28be-9f33-11e8-8a0e-f1fc3bf889c1.png)


### Change colorshceme manually
custom colorscheme file is stored in `~/.config/gns3theme/custom.css`. You can change any color manually and see the changes by selecting any of `Preferences->General->Interface Style->{CustomDark, CustomLight}`.

### Install Other themes
**Note**: You can add your own schemes to `colorschemes` file, just follow the given format inside the file.
see `gns3theme --help` for more information

