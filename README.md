# gns3theme

gns3theme is python tool that will adds a custom theme to gns3. Support both Linux and MacOS.
- Change gns3 theme from a predefined schemes 
- Change ethernet/serial link width and color 
- Apply full transparency to gns3-gui (not implemented yet)
- Create a custom gns3-gui theme.

### Installation
1. Download latest ![gns3theme](https://github.com/n3oxmind/gns3theme/tree/master)
1. Downlad latest ![gns3-gui](https://github.com/GNS3/gns3-gui/releases)
4. Extract both repors
3. cd to gns3theme directory
4. Install gns3_gui `sudo ./gns3theme.py --install </path/to/gns3-gui_dir> -u <username> -s <colorscheme>`. Run only once
5. Add custom theme `./gns3theme.py -s <colorscheme>`. Check `./gns3theme.py --ls` for supported colorschemes.
6. Start gns3 and choose Edit->Preferences->General->Interface Style->Custom

### List default colorschemes
```sh
$ ./gns3theme.py --ls
solarized-light
solarized-dark
n30x-dark
n30x-darker
n30x-darkblue

Add your colorscheme in 'colorschemes.py' file
```

### Install n30x-dark
```sh
$ ./gns3theme.sh -s n30x-dark
```
![n30x-dark3](https://user-images.githubusercontent.com/10103340/44069564-3681323a-9f34-11e8-9f6c-7d458b0298bf.png)


### Install solarized-light theme
```sh
$ gns3theme -s solarized-light
```
![solarized-light](https://user-images.githubusercontent.com/10103340/44070067-9d04544a-9f36-11e8-9793-e73522e9002b.png)


### Install tomorrow theme
```sh
$ gns3theme -s tomorrow
```
![tomorrow](https://user-images.githubusercontent.com/10103340/44069498-f4c867aa-9f33-11e8-8ca1-82a26cca134e.png)


### Install n30x-light
```sh
$ gns3theme -s n30x-light
```
![n30x-light](https://user-images.githubusercontent.com/10103340/44069475-d54f28be-9f33-11e8-8a0e-f1fc3bf889c1.png)


### Tips
`./gns3theme.py --install <gns3_gui_dir>` is only required on first installation and if you want to make/apply changes to grid color.

Changing colorscheme is as simple as `./gns3theme.py -s n30x-darker`. To further customize specific colorscheme use --bg, bg2, --fg, --fg2 ..., etc options to target specific ui element. For example, if you like **n30x-dark** theme and you want to change the selection background color, you can achieve this as below:
```sh
$ ./gns3theme.py -s n30x-dark --sbg ffffff
```
custom colorscheme file is stored in `~/.config/gns3theme/custom_style.css`. You can change any color manually with your fav text editor. 

To add more colorschemes follow the format in `colorschmes.py` and add as many colorschmes as you want.

If you like the icons that i'm using in the screenshots. Copy the **symbols** folder to your GNS3 directory. They will appear under the custom_symbols when you right-click on any appliance. you can change individual devices manually or make them as default icons from gns3 preferences.

### gns3theme usage
```sh
usage: gns3theme --install <path/to/gns3_gui_dir> --scheme <colorscheme>
       gns3theme --scheme <colorscheme> [options]

manditory arguments:
  -i, --install PATH            path to gns3-gui source directory
  -s, --scheme NAME             choose color scheme to apply for gns3-gui
  -u, --user USER               Specify username for installation. only used with --install option

optional arguments:
  --bg COLOR                    change primary background color
  --bg2 COLOR                   change secondary background color
  --fg COLOR                    change primary foreground color
  --fg2 COLOR                   change secondary foreground color
  --tbg COLOR                   change toolbar background color
  --sbg COLOR                   change selection background color
  --sfg COLOR                   change selection foreground color
  --bbg COLOR                   change button background color
  --lc COLOR                    change ethernet link color. Reinstall gns3-gui as root is required
  --lw NUM                      change ethernet and serial links width. Reinstall gns3-gui as root is required
  --gc COLOR                    change grid color. Reinstall gns3-gui as root is required

optional flags:
  --help                        show this help
  --ls                          list predefined color schemes
```
