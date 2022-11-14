import json
import sys
from random import randrange


def main():
    config = sys.argv[1]

    new_config = {"weight":{}}
    lucky = ""
    with open("./config/" + config + ".json", 'r') as f:
        obj = json.load(f);
        total = 0
        for name in obj["weight"]:
            total += obj["weight"][name]
        weight = randrange(total)

        select = 0
        for name in obj["weight"]:
            select += obj["weight"][name]
            if lucky=="" and select > weight:
                lucky = name
                new_config["weight"][name] = 0
            else:
                new_config["weight"][name] = obj["weight"][name]==0 and 1 or obj["weight"][name]*2


    with open("./config/" + str(int(config)+1) + ".json", "x") as f:
        f.write(json.dumps(new_config, indent=4))

    print("恭喜 " + lucky + " 同学中奖!!!")
if __name__ == '__main__':
    main()