levle_map = [
    '                            ', # 0 
    '                            ', # 1
    '                            ', # 2
    ' XX    XXX            XX    ', # 3
    ' XX P                       ', # 4
    ' XXXX         XX         XX ', # 5
    ' XXXX       XX              ', # 6
    ' XX    X  XXXX    XX  XX    ', # 7
    '       X  XXXX    XX  XXX   ', # 8
    '    XXXX  XXXXXX  XX  XXXX  ', # 9
    'XXXXXXXX  XXXXXX  XX  XXXX  ', # 10
    ]

tile_size = 64
screen_width = 1200
# Screen heigt is relative to tile size and map.
screen_heigt = len(levle_map) * tile_size