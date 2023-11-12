folder_names = [
    "0hh1", "0hn0", "2048", "30dollarwebsite", "alienhominid", "amidstthesky", "among-us", "animatorvsanimation",
    "asteroids", "astray", "ballistic-chickens", "banjo-kazooie", "basketandball", "basketbros", "blue", "btd",
    "btd2", "btd3", "btd5", "bunker", "burnout-drift-3", "cat-ninja", "champion-island", "chess", "chessai",
    "chill-radio", "chrome-dino", "circus", "clicker-heroes", "cookieclicker", "csgo-clicker", "cubefield",
    "custom-tetris", "dbzdevolution", "deepest-sword", "doodle-jump", "doom", "drift-boss", "drift-hunters",
    "eaglercraft", "eaglerx", "edgesurf", "eggy-car", "eggycar", "ejs", "elastic-man", "fancypants", "flagracer",
    "flappybird", "fluid-simulation", "fnaf", "fnaw", "fnf-week7", "funnyshooter2", "galaga", "gba",
    "getaway-shootout", "google-snake", "grindcraft", "hackertyper", "hexgl", "hextris", "html-editor",
    "impossible-quiz", "incremancer", "jacksmith", "ltf", "ltf2", "madalin-cars-2", "madalin-cars-3", "mc-classic",
    "mcjs", "mctd", "mctd2", "mineblocks", "minesweeper", "moonlander", "motox3m", "msflight", "n-gon", "n64",
    "olicryptor", "pac-man", "pacman-3d", "paperio2", "piclient", "pico-8", "poom", "powder-game", "retro-bowl",
    "riddleschool", "riddleschool2", "riddleschool3", "riddleschool4", "riddleschool5", "riddletransfer",
    "riddletransfer2", "rocket-soccer", "ruffle", "ruffle-demo", "run2", "run3", "sandboxels", "sandspiel", "sfh",
    "sfh2", "sfh3", "slope", "sm64", "space-cadet-pinball", "spelunky", "spinningrat", "ssf", "subway-surfers",
    "tab-hidder", "tank-trouble-2", "tanuki-sunset", "temple-run-2", "tetris", "thumby-ide", "tinyfishing",
    "tosstheturtle", "typewriter", "unfair-mario", "verynormalshooter", "vex3", "vex4", "vex5", "vex6", "vmlinux",
    "wallsmash", "waterworks", "wbwwb", "weavesilk", "webretro", "webxash", "wordle", "worlds-hardest-game"
]

# Add ".png" after each name
folder_names_with_png = [name + ".png" for name in folder_names]

# Write names to a file
output_file_path = "pngoutput.txt"
with open(output_file_path, 'w') as file:
    for name in folder_names_with_png:
        file.write(name + '\n')

print(f"Modified names written to '{output_file_path}'.")
