		
# gns3theme

gns3theme is a shell script that will apply a custom stylesheet to gns3-gui, all the ui files has been themed with stylesheet usingQT Designer. This script will provide a way to change any color of the gns3-gui. Here is some features:
- Change gns3 theme from a predefined schemes 
- Change ethernet/serial link width and color
- Change grid size and color (Smoother snap to grid)
- Apply transparency to gns3-gui
- Create a custom theme.


### Install solarized-dark theme
```
cd /path/to/gns3-gui-2.1.4
./gns3theme.sh --scheme solarized-dark
./gns3theme.sh --scheme solarized-dark --sbg d32f2f      (optional: change scheme selection color)
./gns3theme.sh --scheme solarized-dark --opacity 0.95    (optional: apply transparency)
```
See `./gns3theme.sh --help` for more options.
![solarized-dark1](https://user-images.githubusercontent.com/10103340/37628258-ed97732a-2b95-11e8-8a7b-886921c33070.png)
![solarized-dark2](https://user-images.githubusercontent.com/10103340/37628262-f1475a08-2b95-11e8-8b58-b98a233f6e58.png)
![solarized-dark3](https://user-images.githubusercontent.com/10103340/37628264-f375f3de-2b95-11e8-858f-58debc8e4e59.png)

### Install solarized-light theme
```
cd /path/to/gns3-gui-2.1.4
gns3theme --scheme solarized-light
gns3theme --scheme solarized-light --opacity 0.96    (optional: apply transparency)
```
![solarized-light1](https://user-images.githubusercontent.com/10103340/37628614-67402176-2b97-11e8-9201-5911edc6e39f.png)
![preferences_1](https://user-images.githubusercontent.com/10103340/37628619-69e24e4a-2b97-11e8-97bc-f2d96f5cb070.png)
![preferences_2](https://user-images.githubusercontent.com/10103340/37628622-6bb91b7c-2b97-11e8-8ca4-bb62d7a8b153.png)
### Install Other themes
```
You basically can theme gns3 of any theme of your choice.
see `gns3theme --help` for more information
```


