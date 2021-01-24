with open("input.txt") as file:
    lines = file.read().splitlines()

def parse_tiles():
    tiles = {}

    tile_id = -1
    current_tile = []

    for line in lines:
        if line.startswith("Tile"):
            tile_id = int(line.split(" ")[1][:-1])
        elif line == "":
            tiles[tile_id] = current_tile
            current_tile = []
        else:
            current_tile.append(line)

    tiles[tile_id] = current_tile
    return tiles

def get_edges(tile):
    return [
        tile[0],
        tile[9],
        "".join(tile[n][0] for n in range(10)),
        "".join(tile[n][9] for n in range(10))
    ]

def has_matching_edge(tile_1, tile_2):
    for edge_1 in get_edges(tile_1):
        for edge_2 in get_edges(tile_2):
            if edge_1 == edge_2 or edge_1 == edge_2[::-1]:
                return True
            
    return False

def find_corner_tiles():
    corner_ids = []

    for (tile_id, tile) in tiles.items():
        matching = 0

        for (other_tile_id, other_tile) in tiles.items():
            if tile_id != other_tile_id and has_matching_edge(tile, other_tile):
                matching += 1

        if matching == 2:
            corner_ids.append(tile_id)

    print(corner_ids[0] * corner_ids[1] * corner_ids[2] * corner_ids[3])

tiles = parse_tiles()
find_corner_tiles()
