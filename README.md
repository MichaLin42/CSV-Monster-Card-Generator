# Welcome to the CSV2MonsterCard project

The goal of this project is to develop a python script that will assist to create monster card data for [rpg-cards.vercel.app](https://rpg-cards.vercel.app). The moster cards will be compatible with the [Shadowdark RPG](https://www.thearcanelibrary.com/pages/shadowdark).
The script will read a CSV file which contains the monster stats and convert it to a JSON file which can be then imported into the [rpg-cards.vercel.app](https://rpg-cards.vercel.app) card generator.


Example card output from [rpg-cards.vercel.app](https://rpg-cards.vercel.app):

![Skeleton monster card](https://raw.githubusercontent.com/MichaLin42/CSV-Monster-Card-Generator/main/doc/card_example.png)


## Requirements
 - Python 3.6 or higher

## Usage
![enter image description here](https://raw.githubusercontent.com/MichaLin42/CSV-Monster-Card-Generator/main/doc/monster_card_generator.png)
 - Use the provided **monster_example.csv** file to fill in your monster data. You can also create your own CSV file as long as it has the same format (column names) as the provided example file.
 - Start the **create_cards.py** script and select your input CSV file (e.g. **monster_example.csv**) and output JSON file. The name of the JSON file does not matter.
 - Click Convert to create the JSON file
 - Open https://rpg-cards.vercel.app and select *"Load from file"* from the **File** menu to import your JSON file
 - From there you can print or edit the imported cards.
 
 ## Hints
 
 - The script can handle up to 3 talents per monster
 - Everything before the first "." in the talent text will be used for the talent name
 - The script expects the stats to be in the same format as in the Shadowdark Core Rulebook (e.g. S +1, D +0, C +2, I -2, W +0, Ch -1)
 - You can use any icon from https://game-icons.net. Just put the name of the icon you want to use into the **Icon** column (e.g. "imp-laugh" for https://game-icons.net/1x1/lorc/imp-laugh.html)
